import cv2 as cv
import numpy as np
import os


def separate_casia_by_image_types(authentic_dir, tampered_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    authentic_images = os.listdir(authentic_dir)
    tampered_images = os.listdir(tampered_dir)
    for image in authentic_images:
        image_name, image_ext = image.split('.')
        if image_ext not in ['jpg', 'jpeg', 'png', 'bmp', 'tiff', 'tif']:
            continue
        image_class, image_type, image_id = image_name.split('_')
        image_path = os.path.join(authentic_dir, image)
        out_type_dir = os.path.join(output_dir, 'authentic', image_type)
        if not os.path.exists(out_type_dir):
            os.makedirs(out_type_dir)
        img = cv.imread(image_path)
        cv.imwrite(os.path.join(out_type_dir, image), img)

    for image in tampered_images:
        image_name, image_ext = image.split('.')
        if image_ext not in ['jpg', 'jpeg', 'png', 'bmp', 'tiff', 'tif']:
            continue
        image_info = image_name.split('_')
        image_1_type, image_2_type = image_info[-3][:3], image_info[-2][:3]
        image_type = image_1_type + '_' + image_2_type
        image_path = os.path.join(tampered_dir, image)
        out_type_dir = os.path.join(output_dir, 'tampered', image_type)
        if not os.path.exists(out_type_dir):
            os.makedirs(out_type_dir)
        img = cv.imread(image_path)
        cv.imwrite(os.path.join(out_type_dir, image), img)


if __name__ == '__main__':
    # D:\data_sets\general_image_tampering\CASIA\CASIA2
    casia2_dir = os.path.join(
        'D:\\', 'data_sets', 'general_image_tampering', 'CASIA', 'CASIA2')
    authentic_dir = os.path.join(casia2_dir, 'authentic')
    tampered_dir = os.path.join(casia2_dir, 'tampered')
    output_dir = os.path.join(casia2_dir, '..', 'CASIA2_separated')
    separate_casia_by_image_types(authentic_dir, tampered_dir, output_dir)
