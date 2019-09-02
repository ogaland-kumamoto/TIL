import zipfile
with zipfile.ZipFile('mydir.zip','a') as zf:
  zf.write('mydir1/test3.txt')