
# creates a zip file which contains 10 text files with 1 - 0 as its name.
# each text file contains 100 random numbers between 1 - 1000

import os
import zipfile
import tempfile as tmp
from constants import ZIP_FILE_PATH

# create a zip file
zip_file = zipfile.ZipFile(ZIP_FILE_PATH, 'w')

with tmp.TemporaryDirectory() as tmpdir:
    print("Created temporary directory: " + tmpdir)
    for i in range(10):
        file_name = str(i) + '.txt'
        tmp_file_path = os.path.join(tmpdir, file_name)
        file = open(tmp_file_path, 'w')
        for j in range(i):
            file.write(str(j) + '\n')
        file.close()
        zip_file.write(tmp_file_path, compress_type=zipfile.ZIP_DEFLATED)
        os.remove(tmp_file_path)
    
zip_file.close()

print("Created zip file: " + ZIP_FILE_PATH)