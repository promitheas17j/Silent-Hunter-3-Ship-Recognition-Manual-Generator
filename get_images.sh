#!/bin/sh
# Set the source directory
src_dir="YOUR /Silent Hunter 3/data/Sea/" # CHANGE THIS TO YOUR SILENT HUTNER 3 GAME DIRECTORY
# Set the destination directory
dest_dir="images"
mkdir -p "$dest_dir"

exclude_images=("ATug_sil.tga" "BuV_Dock1_sil.tga" "BuV_Dock2_sil.tga" "JunkM_sil.tga" "JunkS_sil.tga" "NDST_sil.tga" "NF_boat_1_sil.tga" "NF_boat_2_sil.tga" "NF_boat_3_sil.tga" "NF_boat_3L_sil.tga" "NF_boat_4_sil.tga" "NF_boat_5_sil.tga" "NF_boat_L_sil.tga" "NPTV_sil.tga" "SCHO__sil.tga" "Schute_M2_sil.tga" "Sloop__sil.tga")

# Find and copy the matching files
find "$src_dir" -type f -name "*_sil.tga" | while read file; do
	# Extract the filename
	filename=$(basename "$file")
    # Extract the subdirectory name
    subdir=$(basename "$(dirname "$file")")
    # Check if the file name matches the pattern
    # if [[ $(basename "$file") == "${subdir}_sil.tga" ]]; then
	if [[ ! " ${exclude_images[@]} " =~ " ${filename} " ]]; then
        # Copy the file to the destination
		if [[ ${filename} == "NKLs__sil.tga" ]]; then
			cp "$file" "$dest_dir"/NKLS__sil.tga
		else
			cp "$file" "$dest_dir"
		fi
		echo "Copied: $filename to $dest_dir"
	else
		echo "Excluded: $filename"
    fi
done

mogrify -format png "$dest_dir"/*.tga
rm "$dest_dir"/*.tga
