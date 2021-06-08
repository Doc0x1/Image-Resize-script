from PIL import Image
from tkinter import filedialog, Tk
import os

# main resize method
def image_resize(resize_vals):
    new_width, new_height = resize_vals
    file_list = list()
    # list files in source directory to iterate through
    with os.scandir(filedialog.askdirectory(title="Select folder with images to resize")) as path:
        for file in path:
            if file.is_file():
                file_list.append(file.path)
    dest_folder_path = filedialog.askdirectory(title="Select Destination Folder for resized images")
    # iterate over images and resize them
    for file in file_list:
        try:
            img = Image.open(file)
            old_width, old_height = img.size
            # anything less than 500x500 doesn't need to be resized
            if old_width > 500 or old_height > 500:
                img_name = os.path.basename(img.filename)
                split_name = img_name.split('.')
                # add new img size to save name
                resized_name = f"{split_name[0]}-{new_width}x{new_height}.{split_name[1]}"
                print(f"Original size of {img_name} is {old_width}x{old_height}\n")
                print(f"Resizing {img_name} to {resize_vals}\n")
                # resize image
                img.thumbnail((500,500))
                img.save(f"{dest_folder_path}/{resized_name}")
                print(f"Success! Saved resized image as {resized_name} in directory {dest_folder_path}\n")
            else:
                print(f"File {img.filename} size below 500x500, skipping it...\n")
        except OSError:
            print("OSError exception occurred!")

# set up tkinter for the dialogs
Tk().withdraw()
resize_values=[input("Enter width for resized image: \n"), input("Enter height for resized image: \n")]
image_resize(resize_values)
print("Operation finished.")