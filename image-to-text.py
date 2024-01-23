from PIL import Image

canvas = input("For what canvas to process your image? Enter 'light' or 'dark': ")
match canvas:
    case 'light':
        characters = "@#S%?*+;:,. "
    case 'dark':
        characters = "@#S%?*+;:,. "[::-1]
    case _:
        print(canvas, "is not an option.")
        quit()
# attempt to open image from user-input
path = input("Enter a valid pathname to an image: ").replace('"', "")
try:
    image = Image.open(path)
except FileNotFoundError:
    print(path, "is not a valid pathname to an image.")
    quit()
# name of the file in which the result will be saved
name = input("Enter a name for the file in which you want the result to be saved, followed by .txt: ")
if '.' in name:
    if name[name.find('.'):] != '.txt':
        print(name[name.find('.'):], "is an invalid file extension.")
        quit()
else:
    print("The file must have an extension.")
    quit()
file = open(name, "w")
# resize
width, height = image.size
ratio = height / width
new_width = int(input("Enter a new width of the image in pixels: "))
new_height = int(new_width * ratio)
resized_image = image.resize((new_width, new_height))
# convert to ASCII
grayscale_image = resized_image.convert("L")
pixels = list(grayscale_image.getdata())
char_image = ''.join(characters[pixel // 22] for pixel in pixels)
# format
pixel_count = len(char_image)
formatted_image = "\n".join(char_image[i:(i + new_width)] for i in range(0, pixel_count, new_width))
# print
file.seek(0)
file.write(formatted_image)
file.truncate()
file.close()
# work completion notification
print(f"Processed! The result's saved as {file.name}.")
