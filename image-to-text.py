from PIL import Image, ExifTags

charset = "@#S%?*+;:,. "

canvas = input("For what background to process your image? Enter 'light' or 'dark': ")
match canvas:
    case 'light':
        characters = charset
    case 'dark':
        characters = charset[::-1]
    case _:
        print(canvas, "is not a valid background type.")
        quit()

# Load image and handle orientation
path = input("Enter a valid pathname to an image: ").replace('"', "")
try:
    image = Image.open(path)
    for orientation in ExifTags.TAGS:
        if ExifTags.TAGS[orientation] == 'Orientation':
            break
    exif = image._getexif()
    if exif is not None:
        orientation_value = exif.get(orientation)
        if orientation_value == 3:
            image = image.rotate(180, expand=True)
        elif orientation_value == 6:
            image = image.rotate(270, expand=True)
        elif orientation_value == 8:
            image = image.rotate(90, expand=True)
except FileNotFoundError:
    print(path, "is not a valid pathname to an image.")
    quit()

# Ask for file name
name = input("Enter a name for the file in which you want the result to be saved, followed by .txt: ")
if '.' in name:
    if not name.endswith(".txt"):
        print("The file must have a '.txt' extension.")
        quit()
else:
    print("The file must have an extension.")
    quit()

# Resize while keeping the aspect ratio
width, height = image.size
ratio = height / width
try:
    new_width = int(input("Enter a new width of the image in pixels: "))
except ValueError:
    print("Width must be an integer.")
    quit()
new_height = int(new_width * ratio)
resized_image = image.resize((new_width, new_height))

# Convert to ASCII
grayscale_image = resized_image.convert("L")
pixels = list(grayscale_image.getdata())
char_image = ''.join(characters[pixel * len(characters) // 256] for pixel in pixels)

# Format into lines based on image width
pixel_count = len(char_image)
formatted_image = "\n".join(char_image[i:(i + new_width)] for i in range(0, pixel_count, new_width))

# Write to file
with open(name, 'w') as file:
    file.write(formatted_image)

# Work completion notification
print(f"Processed! The result has been saved as {name}.")
