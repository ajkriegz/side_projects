# resources for creating and opening a simple path to a resource folder and opening images from that file
# https://www.geeksforgeeks.org/python-os-path-join-method/
# https://www.programcreek.com/python/example/1992/os.startfile
import os
path = os.path.join("resources", "maxed characters.png")
os.startfile(path)
print("Opening \"maxed characters.png\"")
while True:
    try: 
        map_name = input("Enter map name: ")
        image_path = os.path.join("resources", f"{map_name}.png")
        os.startfile(image_path)
        print(f"Opening png file for \"{map_name}\".")
        #break
    except: 
        print(f"No png on file for \"{map_name}.\"")
        #break