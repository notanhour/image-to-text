# image-to-text
A short Python script that converts an image into ASCII art. Character set is reversed depending on background brightness, and EXIF orientation is respected for correct image rotation.

## Features
- Converts images to ASCII using grayscale
- Supports both light and dark backgrounds
- Handles image orientation using EXIF metadata
- Keeps aspect ratio during resizing
- Saves result as .txt file

## Requirements
- Python 3.7+
- [Pillow](https://pypi.org/project/pillow/)

## License
This project is released under [The Unlicense](./LICENSE).
