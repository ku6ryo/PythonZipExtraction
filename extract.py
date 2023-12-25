import os
import zipfile
from constants import ZIP_FILE_PATH

# extract 5.txt in a numbers.zip file

found = False
with zipfile.ZipFile(ZIP_FILE_PATH, 'r') as zip_ref:
    # List all files and directories in the ZIP
    for file_path in zip_ref.namelist():
        print(file_path)
        file_name = os.path.basename(file_path)
        if file_name == '5.txt':
            found = True
            with zip_ref.open(file_path, 'r') as file:
                print("Extracted " + file_name + " to resources directory")
                print("Contents of " + file_name + ":")
                for line in file:
                    print(line.decode('utf-8').rstrip())
                break

if not found:
    print("5.txt not found in zip file")
