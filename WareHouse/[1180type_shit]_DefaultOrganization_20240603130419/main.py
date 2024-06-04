'''
Main module for the Mood Designer application.
'''
import tkinter as tk
from image_generator import ImageGenerator
class MoodDesignerApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Mood Designer")
        self.image_generator = ImageGenerator()
        # GUI elements and layout
        self.mood_dropdown = tk.OptionMenu(self.window, tk.StringVar(), "Happy", "Sad", "Excited", "Calm")
        self.mood_dropdown.pack()
        self.filename_entry = tk.Entry(self.window)
        self.filename_entry.pack()
        self.generate_button = tk.Button(self.window, text="Generate", command=self.generate_image)
        self.generate_button.pack()
        self.window.mainloop()
    def generate_image(self):
        mood = self.get_selected_mood()  # Get the selected mood from the GUI
        image = self.image_generator.generate_image(mood)
        filename = self.get_desired_filename()  # Get the desired filename from the GUI
        self.image_generator.save_image(image, filename)
    def get_selected_mood(self):
        selected_mood = self.mood_dropdown.cget("text")  # Get the selected mood from the dropdown
        return selected_mood
    def get_desired_filename(self):
        desired_filename = self.filename_entry.get()  # Get the desired filename from the entry field
        return desired_filename
if __name__ == "__main__":
    app = MoodDesignerApp()