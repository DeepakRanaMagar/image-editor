# pillow module -> Digital image processing
# built on top of the PIL(Python Image Library)




from PIL import Image, ImageEnhance, ImageFilter
import os 

path = './unedited'
pathOut ='./edited'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.j')
