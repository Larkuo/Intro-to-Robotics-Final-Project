import os
from PIL import Image

def rename_images(folder="folder"):
    for count, filename in enumerate(os.listdir(folder)):
        newname = f"img-{str(count)}.png"
        img_path = f"{folder}/{filename}"
        newname = f"{folder}/{newname}"

        os.rename(img_path, newname)
        print(f"file[{str(count)}] renamed from {filename} to {newname}")

def get_image_sizes(folder):
    for filename in os.listdir(folder):
        img = Image.open(f"{folder}/{filename}")
        size = img.size
        print(f"[{filename}].size = ({size})")
    
# -----------------------MAIN---------------------------

# rename_images("Sorted Scrape")

get_image_sizes("Sorted Scrape")