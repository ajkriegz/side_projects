import os
os.startfile("maxed characters.png")
print("Opening \"maxed characters.png\"")
while True:
    try: 
        map_name = input("Enter map name: ")
        os.startfile(f"{map_name}.png")
        print(f"Opening png file for \"{map_name}\".")
    except: 
        print(f"No png on file for \"{map_name}.\"")