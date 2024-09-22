# Requirements
----
- Silent Hunter 3 with the GWX mod installed
- imagemagick package (for the mogrify tool)
- python 3
- LaTeX with pdflatex

# Usage
- Clone this repo onto your system. It will be your "working directory"
- Make the scripts executable if necessary
```
chmod +x get_images.sh
chmod +x get_ship_info.py
chmod +x generate_latex_file.py
```

- Change the directory in ```get_images.sh``` to wherever your game is installed:

```src_dir="YOUR /Silent Hunter 3/data/Sea/" # CHANGE THIS TO YOUR SILENT HUTNER 3 GAME DIRECTORY```

- Change the directory in ```get_ship_info.py``` to wherever your game is installed:


```sea_directory = "YOUR /Silent Hunter 3/data/Sea/" # CHANGE THIS TO YOUR SILENT HUTNER 3 GAME DIRECTORY```

- First run ```get_images.sh```
- Then run ```get_ship_info.py```
- Finally run ```generate_latex_file.py```

If you dont want to automatically generate the PDF file then set the following line in ```generate_latex_file.py``` to False:

```compile_pdf = True```
