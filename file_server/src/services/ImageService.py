import os
from time import perf_counter
from PIL import Image

def compress_img(image_name, new_size_ratio=0.9, quality=90, width=None, height=None, to_jpg=True):
    img = Image.open(image_name)
    if new_size_ratio < 1.0:
        img = img.resize((int(img.size[0] * new_size_ratio), int(img.size[1] * new_size_ratio)))
    elif width and height:
        img = img.resize((width, height), Image.ANTIALIAS)
    filename, ext = os.path.splitext(image_name)
    if to_jpg:
        new_filename = f"{filename}_compressed.jpg"
    else:
        new_filename = f"{filename}_compressed{ext}"
    try:
        img.save(new_filename, quality=quality, optimize=False)
    except OSError:
        img = img.convert("RGB")
        img.save(new_filename, quality=quality, optimize=False)

start = perf_counter()
for i in range(1):
    compress_img('C:/vscode/AnoCat/file_server/src/services/3mb.png', new_size_ratio=1,quality=50, to_jpg=True)
print((perf_counter()-start)/1)