import os

dataset_path = os.path.join(
    'D:\\', 'data_sets', 'general_image_tampering', 'IMD2020')

for folder in os.listdir(dataset_path):
    images_path = os.listdir(os.path.join(dataset_path, folder))
    for image_path in images_path:
        image_name = image_path.split('.')[0]
        image_type = image_path.split('.')[1]
        if image_name.endswith('_orig'):
            os.rename(
                os.path.join(dataset_path, folder, image_path),
                os.path.join(dataset_path, 'authentic', image_name + '.' + image_type))
        elif image_name.endswith('_mask'):
            os.rename(
                os.path.join(dataset_path, folder, image_path),
                os.path.join(dataset_path, 'mask', image_name + '.' + image_type))
        else:
            os.rename(
                os.path.join(dataset_path, folder, image_path),
                os.path.join(dataset_path, 'tampered', image_name + '.' + image_type))
