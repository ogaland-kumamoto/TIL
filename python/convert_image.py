from PIL import Image
img = Image.open('caffe.jpg')
print(f'ファイル名：{img.filename}, フォーマット：{img.format}, サイズ： {img.size}')