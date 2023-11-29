import os
import numpy as np
from PIL import Image, ImageChops, ImageEnhance


def convert_to_ela_image(path, quality):

    original_image = Image.open(path).convert('RGB')

    resaved_file_name = 'resaved_image.jpg'
    original_image.save(resaved_file_name, 'JPEG', quality=quality)
    resaved_image = Image.open(resaved_file_name)

    ela_image = ImageChops.difference(original_image, resaved_image)

    extrema = ela_image.getextrema()
    max_difference = max([pix[1] for pix in extrema])
    if max_difference == 0:
        max_difference = 1
    scale = 255 / max_difference

    ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)

    return ela_image


def prepare_image(image_path, quality=90, image_size=None):
    if image_size is None:
        return np.array(convert_to_ela_image(image_path, quality))
    else:
        return np.array(convert_to_ela_image(image_path, quality).resize(image_size))


def ela_pre_process(original_dir, ela_processed_dir, image_size):
    supported_formats = ['jpg', 'jpeg', 'png', 'bmp', 'tiff', 'tif']

    if not os.path.exists(ela_processed_dir):
        os.makedirs(ela_processed_dir)
    original_images = os.listdir(original_dir)

    for image in original_images:
        image_name, image_ext = os.path.splitext(image)
        if image_ext not in supported_formats:
            continue
        ela_image = prepare_image(os.path.join(
            original_dir, image), image_size)
        Image.fromarray(ela_image).save(os.path.join(
            ela_processed_dir, image))
