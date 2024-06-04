from PIL import Image, ImageDraw
from PIL import Image

try:
    image = Image.new("RGB", (10, 10), "white")
    print("Pillow is installed correctly!")
except ImportError as e:
    print("Pillow is not installed. Please install it using 'pip install Pillow'.")

import os

class ImageGenerator:
    def __init__(self):
        # Initialize any necessary variables or resources
        pass  # Currently, there's nothing to initialize

    def generate_image(self, mood):
        '''
        Generate abstract image based on the given mood.
        Args:
            mood (str): The selected mood.
        Returns:
            image (PIL.Image.Image): The generated abstract image.
        '''
        image = Image.new("RGB", (1080, 1080), "white")
        draw = ImageDraw.Draw(image)
        
        # Add simple drawing based on mood
        if mood == 'happy':
            draw.ellipse((270, 270, 810, 810), fill='yellow', outline='black')
            draw.ellipse((380, 380, 460, 460), fill='black')  # Left eye
            draw.ellipse((620, 380, 700, 460), fill='black')  # Right eye
            draw.arc((450, 450, 630, 630), start=0, end=180, fill='black')  # Smile
        else:
            draw.rectangle((270, 270, 810, 810), fill='gray', outline='black')
            draw.line((380, 380, 700, 700), fill='black', width=5)  # Cross
            draw.line((700, 380, 380, 700), fill='black', width=5)  # Cross

        return image

    def save_image(self, image, filename):
        '''
        Save the generated image to a file with the given filename.
        Args:
            image (PIL.Image.Image): The image to be saved.
            filename (str): The desired filename.
        Returns:
            None
        '''
        # Ensure the filename has a valid extension
        if not os.path.splitext(filename)[1]:
            filename += '.png'  # Default to .png if no extension is provided
        try:
            image.save(filename)
            print(f"Image saved as {filename}")
        except Exception as e:
            print(f"Error saving image: {e}")

# Example usage
image_generator = ImageGenerator()
image = image_generator.generate_image('happy')  # Assuming 'happy' is a valid mood
image_generator.save_image(image, 'test_image')  # This will save as 'test_image.png'
