import zipfile
with zipfile.ZipFile('mydir.zip','w') as zf:
  zf.write('mydir1/test1.txt')
  zf.write('mydir1/test2.txt')