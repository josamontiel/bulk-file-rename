# Bulk file creating and renaming tool

> A bash script to bulk rename files

## Utility

The main functionality for this tool is to mass rename files in a given directory.

an example to this would be as follows:

```bash
bulk_rename_files.sh <file_type> <num_files> <new_name>
```

## Breaking down the script

The script itself has a few key parts:

1. Finding the files
2. Checking to see if the files exist already
3. Renaming the files.

### Finding the files matching the specified file type

```bash
files=$(find . -maxdepth 1 -name "*.$file_type" | head -n $num_files)
```

What happens here with the 1st argument `<file_type>`, `find . -maxdepth 1` is going into the first level directory, looking for all files ending in ``"*$file_type"``(Here, ``$file_type ``is the first argument, which in this case is ``.txt``).

### Checking if files exist

After inputting the first argument the script will now check for the files to see if they even exist. If the files do not exist, the program will imediately spit out ``No files found with the specified file type: $file_type`` and the program will ``exit``.

### Renaming the files

Renaming of the files will begin with the 3rd argument ``<new_name>`` will allow the end user to input the end name for all the files.
