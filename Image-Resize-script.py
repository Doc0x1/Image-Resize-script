from PIL import Image
from tkinter import filedialog, Tk
import os


#---withdraw Tkinter and setup choice variables---#
Tk().withdraw()
copy_below_size = None
valid_choices = ["y", "n"]

#---Start value checking phase---#
try:
    resize_vals=[int(input("Enter width for resized images: \n")), int(input("Enter height for resized images: \n"))]
except ValueError:
    print("Value Error!\nValues entered are not integers!\nStopping script...")
    os.exit()
if (type(resize_vals[0]) == int and resize_values[0] > 99) and (type(resize_vals[1]) == int and resize_vals[1] > 99):
    new_width, new_height = resize_vals
else:
    print("Error! Image resize values need to be integers greater than 99!\nStopping script...\n")
    os.exit()
#---End value checking phase---#

#---Start image resize options selection phase---#
# list  to iterate through files in source directory
with os.scandir(filedialog.askdirectory(title="Select folder with images to resize")) as path:
    dest_folder_path = filedialog.askdirectory(title="Select Destination Folder for resized images")
    if dest_folder_path == path:
        print("Error!\nDestination folder is same as source directory! Stopping script...\n")
        os.exit()
    while True:
        yes_no = str(input(f"Do you want to copy images in {path} below size 500x500 to {dest_folder_path}?\n(Y/N): ").lower())
        if valid_choices[0] in yes_no:
            copy_below_size = True
            break
        elif valid_choices[1] in yes_no:
            copy_below_size = False
            break
        else:
            print("Please enter a valid choice, this is just a yes or no question.\n")
            continue
    file_list = list()
    for file in path:    
        if file.is_file():
            file_list.append(file.path)
#---End image resize options selection phase---#

#---Start image resizing phase---#
if copy_below_size:
    for file in file_list:
        try:
            img = Image.open(file)
            old_width, old_height = img.size
            img_name = os.path.basename(img.filename)
            split_name = img_name.split('.')
            # add new img size to save name
            resized_name = f"{split_name[0]}-{new_width}x{new_height}.{split_name[1]}"
            print(f"Original size of {img_name} is {old_width}x{old_height}\n")
            print(f"Resizing {img_name} to {resize_vals}\n")
            # resize image
            img.thumbnail((new_width. new_height))
            img.save(f"{dest_folder_path}/{resized_name}")
            print(f"Success! Saved resized image as {resized_name} in directory {dest_folder_path}\n")
else:
    for file in file_list:
        try:
            img = Image.open(file)
            old_width, old_height = img.size
            # anything less than new_width x new_height doesn't need to be resized
            if old_width <= new_width or old_height <= new_height:
                img_name = os.path.basename(img.filename)
                split_name = img_name.split('.')
                # add new img size to save name
                resized_name = f"{split_name[0]}-{new_width}x{new_height}.{split_name[1]}"
                print(f"Original size of {img_name} is {old_width}x{old_height}\n")
                print(f"Resizing {img_name} to {resize_vals}\n")
                # resize image
                img.thumbnail((new_width, new_height))
                img.save(f"{dest_folder_path}/{resized_name}")
                print(f"Success! Saved resized image as {resized_name} in directory {dest_folder_path}\n")
            else:
                print(f"File {img.filename} size is below {new_width}x{new_height}, skipping it...\n")
        except OSError:
            print("OSError exception occurred!")

print("Operation completed successfully.")