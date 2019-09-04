import zipfile
with zipfile.ZipFile('mydir.zip','r') as zf:
  zf.extractall('extract_dir')