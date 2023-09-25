import random
import string
from PIL import Image



def random_str(length: int):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))


def compress_img(
        image:bytearray, 
        ext:str = 'jpg', 
        new_size_ratio: int = 0.9, 
        quality: int = 90, 
        width: int = None, 
        height: int = None
    ) -> None:
    # img = Image.open(image_name)
    img: Image = Image.frombytes(image)
    if new_size_ratio < 1.0:
        img = img.resize((int(img.size[0] * new_size_ratio), int(img.size[1] * new_size_ratio)))
    elif width and height:
        img = img.resize((width, height), Image.ANTIALIAS)
    # new_filename = f"{filename}_compressed{ext}"
    return img
    # try:
    #     img.save(new_filename, quality=quality, optimize=False)
    # except OSError:
    #     img = img.convert("RGB")
    #     img.save(new_filename, quality=quality, optimize=False)