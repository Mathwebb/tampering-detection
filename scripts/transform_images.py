
from PIL import Image
import os

# caminho para a pasta com as imagens .tif
tif_folder_path = "/c:/Repositories/projects/my-projects/tensor-flow-test/images/tif_images/"

# percorrer todas as imagens .tif na pasta
for filename in os.listdir(tif_folder_path):
    if filename.endswith(".tif"):
        # abrir a imagem .tif
        tif_path = os.path.join(tif_folder_path, filename)
        with Image.open(tif_path) as im:
            # criar o caminho para a imagem .jpg
            jpg_path = os.path.splitext(tif_path)[0] + ".jpg"
            # salvar a imagem .jpg
            im.save(jpg_path)
            # remover a imagem .tif
            os.remove(tif_path)
