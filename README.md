# Text to Image Tool

## Overview

This is a Tkinter application that allows users to create images from text and convert existing images. It includes features for selecting background and text colors, specifying dimensions, and choosing file formats.

## Features

- **Text to Image Tool**: Convert text to an image with customizable background and text colors, dimensions, and formats.
- **Image Converter**: Convert multiple existing images to specified dimensions and formats.

## Requirements

- Python 3.x
- Pillow
- Tkinter (usually included with Python)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DarkCelestialonly1/TextToImage.git

pip install -r requirements.txt

python TTI.py


Sure! Here's a comprehensive README.md file for your project, including a description, installation instructions, and usage details:

markdown
Copy code
# Text to Image Tool

## Overview

This Tkinter application allows users to create images from text and convert existing images. It includes features for selecting background and text colors, specifying dimensions, and choosing file formats.

## Features

- **Text to Image Tool**: Convert text to an image with customizable background and text colors, dimensions, and formats.
- **Image Converter**: Convert multiple existing images to specified dimensions and formats.

## Requirements

- Python 3.x
- Pillow
- Tkinter (usually included with Python)

## Installation

1. **Clone the repository**:

   git clone https://github.com/DarkCelestialonly1/TextToImage.git

   
Navigate to the project directory:


cd TextToImage

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required packages:


pip install -r requirements.txt


Usage
Run the application:

python TTI.py
Use the "Text to Image" tab to create images from text:

Enter the text you want to convert into an image in the "Text" field.
Optionally, choose a background color and text color using hex codes or the color picker.
Specify the desired width and height of the image.
Select the unit for dimensions (px, cm, mm).
Click the "Save Image" button to generate and save the image.
Use the "Image Converter" tab to convert existing images:

Click the "Browse" button to select one or multiple images.
Specify the desired width and height for the output images.
Select the unit for dimensions (px, cm, mm).
Choose the output file format (PNG, JPG, BMP) using the radio buttons.
Click the "Convert Images" button to resize and save the selected images.
Example
Here's a quick example of how to use the tool:

Text to Image:

Enter text: "Hello, World!"
Background color: #FFFFFF (default)
Text color: #000000 (default)
Width: 800
Height: 600
Unit: px
Click "Save Image" to save the generated image as a PNG file.
Image Converter:

Select images using the "Browse" button.
Width: 1000
Height: 800
Unit: px
Choose output format: PNG
Click "Convert Images" to resize and save the images.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Pillow for image processing.
Tkinter for the GUI framework.
