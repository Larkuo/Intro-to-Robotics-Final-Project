import os
import natsort
import cv2

def resize_images(src_path, dst_path):
    files = os.listdir(src_path)
    sorted_files = natsort.natsorted(files, reverse=False)

    for f in sorted_files:
        f_path = src_path + f
        if f.find("png") != -1: # check if file is not an annotation
            if open(f_path) != None:
                img = cv2.imread(f_path)
                img_r = cv2.resize(img, (400, 400))
                name_r = dst_path + "\\resized_" + f
                cv2.imwrite(name_r, img_r)
                print(f"[{f}] resized to 400,400")

# ------------------MAIN------------------------------------
src = 'Sorted Scrape\\Unlabelled Testing Images\\'
dst = 'Unlabelled Resize\\'
resize_images(src, dst)