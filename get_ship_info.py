#!/bin/env python3
import os
import csv

# Define the directory containing the ship folders
sea_directory = "YOUR /Silent Hunter 3/data/Sea/" # CHANGE THIS TO YOUR SILENT HUTNER 3 GAME DIRECTORY
# Define the output CSV file
current_dir = os.getcwd()
output_csv = current_dir + "/ship_info.csv"

# Define the exclude list
exclude_list = [
        "Buoy_R1_FL",
        "NPTV",
        "NF_boat_L",
        "IcebergM1",
        "Buoy_G1_FL",
        "NF_boat_1",
        "IcebergM3",
        "BuV_Dock2",
        "NHA_Boat1",
        "NF_boat_3",
        "Schute_M2",
        "Buoy_D2_FL",
        "Buoy_O1_FL",
        "Sloop_",
        "Buoy_R2_FL",
        "NF_boat_5",
        "IcebergS1",
        "NF_boat_4",
        "JunkS",
        "NF_boat",
        "BuV_Dock1",
        "JunkM",
        "NF_boat_3L",
        "Iceberg",
        "IcebergS2",
        "PBTrawler",
        "NF_boat_2",
        "Buoy_G2_FL",
        "ATug",
        "NLTF",
        "NAMS",
        "IcebergS3",
        "NATF",
        "IcebergM2",
        "SCHO_",
        "NMSTR",
        "NDST",
]

# List to hold the extracted ship information
ship_data = []

# Traverse the Sea directory
for ship_name in os.listdir(sea_directory):
    ship_path = os.path.join(sea_directory, ship_name)
    
    # Check if it's a directory
    if (os.path.isdir(ship_path)) and (ship_name not in exclude_list):
        cfg_file = os.path.join(ship_path, f"{ship_name}.cfg")
        
        # Check if the config file exists
        if os.path.isfile(cfg_file):
            ship_info = {}
            
            # Read the config file
            with open(cfg_file, 'r') as file:
                section = None
                for line in file:
                    line = line.strip()
                    if line.startswith("[") and line.endswith("]"):
                        section = line[1:-1]  # Get the section name
                    elif "=" in line and section == "Unit":
                        key, value = line.split("=", 1)
                        ship_info[key.strip()] = value.strip()
            
            # Collect the required information
            if ship_info:
                ship_data.append({
                    "Ship Name": ship_name,
                    "ClassName": ship_info.get("ClassName", ""),
                    "MaxSpeed": ship_info.get("MaxSpeed", ""),
                    "Length": ship_info.get("Length", ""),
                    "Width": ship_info.get("Width", ""),
                    "Mast": ship_info.get("Mast", ""),
                    "Draft": ship_info.get("Draft", ""),
                    "RenownAwarded": ship_info.get("RenownAwarded", ""),
                })

# Write the collected data to the CSV file
with open(output_csv, 'w', newline='') as csvfile:
    fieldnames = ["Ship Name", "ClassName", "MaxSpeed", "Length", "Width", "Mast", "Draft", "RenownAwarded"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for ship in ship_data:
        writer.writerow(ship)

print(f"Data extracted and saved to {output_csv}.")
