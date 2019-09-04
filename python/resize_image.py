from PIL import Image
img = Image.open('caffe.png')
resized_img = img.resize((100,100))
resized_img.save('caffe_small.png')