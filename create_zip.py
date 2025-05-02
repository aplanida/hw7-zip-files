import os
import zipfile
import pytest


@pytest.fixture
def create_archive():
    file_names = ['item1.xlsx',
                  'outpu1.csv',
                  'pdf_sample.pdf']
    dir_path = os.getcwd()
    file_path = os.path.join(dir_path, 'files')

    if not os.path.exists(os.path.join(dir_path, 'resources')):
        os.mkdir(os.path.join(dir_path, 'resources'))
    with zipfile.ZipFile(os.path.join(dir_path, 'resources', 'myzip.zip'), 'w') as zf:
        for file in file_names:
            add_files = os.path.join(file_path, file)
            zf.write(add_files, os.path.basename(add_files))

# myzip = ZipFile("myzip.zip", "w")
