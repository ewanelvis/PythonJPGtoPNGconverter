# author Ewane Elvis lil python image converter.
import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exists if not create
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# loop through Pokedex
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    # converts images to png and and save to new folder
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')




# save to the new folder