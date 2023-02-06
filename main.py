from PIL import Image

img = Image.open('./unedited/img1.jpeg')

print(img.size)
print(img.format)
print(img.mode)
# img.show()