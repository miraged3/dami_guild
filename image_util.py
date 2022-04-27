import numpy as np
from PIL import Image


def stitch_image(file1, file2, is_horizontal=True):
    image1 = Image.open(file1)
    image2 = Image.open(file2)

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    if is_horizontal:
        result_width = width1 + width2
        result_height = max(height1, height2)
    else:
        result_width = max(width1, width2)
        result_height = height1 + height2

    result = Image.new('RGB', (result_width, result_height))
    if is_horizontal:
        result.paste(im=image1, box=(0, 0))
        result.paste(im=image2, box=(width1, 0))
    else:
        result.paste(im=image1, box=(0, 0))
        result.paste(im=image2, box=(0, height1))
    return result
