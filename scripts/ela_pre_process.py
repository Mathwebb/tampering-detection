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


def prepare_image(image_path, image_size):
    return np.array(convert_to_ela_image(image_path, 90).resize(image_size))


def ela_pre_process(original_dir, tampered_dir, dataset_dir, image_size):

    original_images = os.listdir(original_dir)

    for image in original_images:
        ela_image = prepare_image(os.path.join(
            original_dir, image), image_size)
        Image.fromarray(ela_image).save(os.path.join(
            dataset_dir, '..', 'ELA_CASIA1', 'authentic', image))

    tampered_images = os.listdir(tampered_dir)

    for image in tampered_images:
        ela_image = prepare_image(os.path.join(
            tampered_dir, image), image_size)
        Image.fromarray(ela_image).save(os.path.join(
            dataset_dir, '..', 'ELA_CASIA1', 'tampered', image))
