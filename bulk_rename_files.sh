#!/bin/bash

# Usage: bulk_rename_files.sh <file_type> <num_files> <new_name>

file_type=$1
num_files=$2
new_name=$3

# Find files matching the specified file type
files=$(find . -maxdepth 1 -name "*.$file_type" | head -n $num_files)

# Check if any files were found
if [[ -z $files ]]; then
    echo "No files found with the specified file type: $file_type"
    exit 1
fi

# Rename the files
i=1
for file in $files; do
    dir=$(dirname "$file")
    extension="${file##*.}"
    new_file="$dir/$new_name$i.$extension"
    mv "$file" "$new_file"
    echo "Renamed: $file -> $new_file"
    ((i++))
done
