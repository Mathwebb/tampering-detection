import cv2
import os
import numpy as np
import random

# Specify the folder path where your images are located
folder_path = '../data_sets/xrays/authentic'

# Get a list of all files in the folder
image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Loop through the image files and read and modify each one
for image_file in image_files:
    # Check if the file is an image (you can add more image extensions as needed)
    if image_file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        # Construct the full path to the image
        image_path = os.path.join(folder_path, image_file)
        
        # Read the image using OpenCV
        image = cv2.imread(image_path)
        
        # Get the dimensions of the image
        height, width, _ = image.shape

        # Generate random coordinates for the spot
        random_x = random.randint(500, width - 500)
        random_y = random.randint(200, height - 200)

        # Generate a random color for the spot (random BGR values)
        spot_color = (255,255,255)

        # Define the size of the spot (randomly between 5 and 20 pixels)
        spot_size = random.randint(30, 100)

        # Generate a random shape (0 for a circle, 1 for a square, 2 for a rectangle)
        shape_choice = random.choice([0, 1, 2])

        # Draw the selected shape on the image
        if shape_choice == 0:
            cv2.circle(image, (random_x, random_y), spot_size, spot_color, -1)
        elif shape_choice == 1:
            cv2.rectangle(image, (random_x, random_y), (random_x + spot_size, random_y + spot_size), spot_color, -1)
        else:
            random_width = random.randint(20, 50)
            random_height = random.randint(20, 50)
            cv2.rectangle(image, (random_x, random_y), (random_x + random_width, random_y + random_height), spot_color, -1)
        
        # Save the modified image (you can save it with a different name)
        modified_image_path = os.path.join(folder_path, '..', 'tampered', 'modified_' + image_file)
        cv2.imwrite(modified_image_path, image)

        # Optionally, display the modified image (you can uncomment these lines)
        # cv2.imshow('Modified Image', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()