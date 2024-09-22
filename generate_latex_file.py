#!/usr/bin/env python3
import os
import csv
import subprocess

# Define directories
current_dir = os.getcwd()
images_dir = "images"  # Directory where images are stored
output_tex = "rec_manual.tex"
output_pdf = "rec_manual.pdf"
template_file = "template.tex"

# Ensure images directory exists
if not os.path.exists(images_dir):
    os.makedirs(images_dir)
    print(f"Note: {images_dir} did not exist so it was created.")

# Function to escape LaTeX special characters
def escape_latex(text):
    if not isinstance(text, str):
        text = str(text)
    replacements = {
        '\\': r'\textbackslash{}',
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
    }
    for char, escape_seq in replacements.items():
        text = text.replace(char, escape_seq)
    return text

# Read ship data from CSV
ship_data = []
csv_file = os.path.join(current_dir, "ship_info.csv")
if not os.path.isfile(csv_file):
    print(f"Error: CSV file '{csv_file}' not found. Please ensure it exists in the current directory.")
    exit(1)

with open(csv_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ship_data.append(row)

# Start writing the LaTeX file
with open(output_tex, 'w', encoding='utf-8') as texfile:
    if not os.path.isfile(template_file):
        print(f"Error: LaTeX template file '{template_file}' not found. Please ensure it exists.")
        exit(1)
    with open(template_file, 'r', encoding='utf-8') as tmpl:
        template_content = tmpl.read()
        
    # Insert placeholder for ship info
    ship_info_placeholders = []
    
    for ship in ship_data:
        raw_ship_name = ship["Ship Name"].strip()
        escaped_ship_name = escape_latex(raw_ship_name)
        class_name = escape_latex(ship["ClassName"])
        max_speed = escape_latex(ship["MaxSpeed"])
        length = escape_latex(ship["Length"])
        width = escape_latex(ship["Width"])
        mast = escape_latex(ship["Mast"])
        
        image_filename = f"{raw_ship_name}_sil.png"
        image_path = os.path.join(images_dir, image_filename)

        if not os.path.isfile(image_path):
            print(f"Warning: Image for {raw_ship_name} not found at {image_path}. Please make sure it exists and try again.")
            exit(1)

        # Prepare the LaTeX command for the ship info
        ship_info_latex = f"""
\\shipinfo{{{image_path}}}{{{escaped_ship_name}}}{{{class_name}}}{{{max_speed}}}{{{length}}}{{{width}}}{{{mast}}}
"""
        ship_info_placeholders.append(ship_info_latex)

    # Replace the placeholder in the template with actual ship info
    ship_info_content = "\n".join(ship_info_placeholders)
    template_content = template_content.replace("% INSERT SHIP INFO HERE", ship_info_content)

    # Write the final LaTeX content to the file
    texfile.write(template_content)
    
    # Close the LaTeX document
    texfile.write("\\end{document}")

print(f"LaTeX file '{output_tex}' generated successfully.")

# Optional: Compile the LaTeX file to PDF
compile_pdf = True  # Set to False if you don't want to compile automatically

if compile_pdf:
    try:
        subprocess.run(["pdflatex", output_tex], check=True)
        subprocess.run(["pdflatex", output_tex], check=True)
        print(f"PDF '{output_pdf}' compiled successfully.")
    except subprocess.CalledProcessError as e:
        print("Error during PDF compilation:", e)
