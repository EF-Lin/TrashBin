from PIL import Image

name = str(input())
img = Image.open(f'{name}.png')
img.save(f'{name}.ico', sizes=[(64, 64)])
