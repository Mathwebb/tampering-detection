import os

target_dir = 'D:\data_sets\dental_radiograph\DentalPanoramicXrays\Images'

image_files = os.listdir(target_dir)

for image_file in image_files:
    os.rename(os.path.join(target_dir, image_file),  os.path.join(target_dir, f'val_a_{image_file.split("_")[-1]}'))
