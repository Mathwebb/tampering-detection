
from PIL import Image
import os

tif_folder_path = "/c:/Repositories/projects/my-projects/tensor-flow-test/images/tif_images/"

for filename in os.listdir(tif_folder_path):
    if filename.endswith(".tif"):
        tif_path = os.path.join(tif_folder_path, filename)
        with Image.open(tif_path) as img:
            jpg_path = os.path.splitext(tif_path)[0] + ".jpg"
            img.save(jpg_path)
            os.remove(tif_path)
