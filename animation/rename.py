import os

files = os.listdir("./images")
file_names = []
for file_name in files:
    new_file_name = file_name.replace(" ", "").replace("(", "").replace(")", "")
    os.rename(f"./images/{file_name}", f"./images/{new_file_name}")
    