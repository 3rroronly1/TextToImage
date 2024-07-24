import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser, ttk
from PIL import Image, ImageDraw, ImageFont
import random
import os

def sequential_filename(base_name, start_index, extension=".png"):
    return f"{base_name}_{start_index}{extension}"

def random_filename(extension=".png"):
    return f"image_{random.randint(1000, 9999)}{extension}"

def convert_units(value, unit):
    if unit == "cm":
        return int(value * 37.7952755906)  # cm to pixels (approx)
    elif unit == "mm":
        return int(value * 3.77952755906)  # mm to pixels (approx)
    return int(value)

class TextToImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Image Tool")

        self.bg_color = "#FFFFFF"  # default white background
        self.text_color = "#000000"  # default black text
        self.output_extension = ".png"  # default extension

        self.create_widgets()

    def create_widgets(self):
        self.tab_control = ttk.Notebook(self.root)
        
        self.text_to_image_tab = ttk.Frame(self.tab_control)
        self.image_converter_tab = ttk.Frame(self.tab_control)
        
        self.tab_control.add(self.text_to_image_tab, text="Text to Image")
        self.tab_control.add(self.image_converter_tab, text="Image Converter")
        self.tab_control.pack(expand=1, fill="both")

        # Text to Image Tab
        tk.Label(self.text_to_image_tab, text="Text:").grid(row=0, column=0, padx=10, pady=5)
        self.text_entry = tk.Text(self.text_to_image_tab, height=20, width=50)
        self.text_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.text_to_image_tab, text="Background Color (Hex):").grid(row=1, column=0, padx=10, pady=5)
        self.bg_color_entry = tk.Entry(self.text_to_image_tab)
        self.bg_color_entry.grid(row=1, column=1, padx=10, pady=5)
        self.bg_color_button = tk.Button(self.text_to_image_tab, text="Pick Color", command=self.pick_bg_color)
        self.bg_color_button.grid(row=1, column=2, padx=10, pady=5)

        tk.Label(self.text_to_image_tab, text="Text Color (Hex):").grid(row=2, column=0, padx=10, pady=5)
        self.text_color_entry = tk.Entry(self.text_to_image_tab)
        self.text_color_entry.grid(row=2, column=1, padx=10, pady=5)
        self.text_color_button = tk.Button(self.text_to_image_tab, text="Pick Color", command=self.pick_text_color)
        self.text_color_button.grid(row=2, column=2, padx=10, pady=5)

        tk.Label(self.text_to_image_tab, text="Width:").grid(row=3, column=0, padx=10, pady=5)
        self.width_entry = tk.Entry(self.text_to_image_tab)
        self.width_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.text_to_image_tab, text="Height:").grid(row=4, column=0, padx=10, pady=5)
        self.height_entry = tk.Entry(self.text_to_image_tab)
        self.height_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(self.text_to_image_tab, text="Unit (px, cm, mm):").grid(row=5, column=0, padx=10, pady=5)
        self.unit_entry = tk.Entry(self.text_to_image_tab)
        self.unit_entry.grid(row=5, column=1, padx=10, pady=5)

        self.save_button = tk.Button(self.text_to_image_tab, text="Save Image", command=self.save_image)
        self.save_button.grid(row=6, column=1, padx=10, pady=10)

        # Image Converter Tab
        tk.Label(self.image_converter_tab, text="Select Images:").grid(row=0, column=0, padx=10, pady=5)
        self.image_listbox = tk.Listbox(self.image_converter_tab, selectmode=tk.MULTIPLE, width=50, height=10)
        self.image_listbox.grid(row=0, column=1, padx=10, pady=5)

        self.browse_button = tk.Button(self.image_converter_tab, text="Browse", command=self.browse_images)
        self.browse_button.grid(row=0, column=2, padx=10, pady=5)

        self.select_all_button = tk.Button(self.image_converter_tab, text="Select All", command=self.select_all_images)
        self.select_all_button.grid(row=1, column=2, padx=10, pady=5)

        self.deselect_all_button = tk.Button(self.image_converter_tab, text="Deselect All", command=self.deselect_all_images)
        self.deselect_all_button.grid(row=2, column=2, padx=10, pady=5)

        tk.Label(self.image_converter_tab, text="Width:").grid(row=1, column=0, padx=10, pady=5)
        self.convert_width_entry = tk.Entry(self.image_converter_tab)
        self.convert_width_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.image_converter_tab, text="Height:").grid(row=2, column=0, padx=10, pady=5)
        self.convert_height_entry = tk.Entry(self.image_converter_tab)
        self.convert_height_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.image_converter_tab, text="Unit (px, cm, mm):").grid(row=3, column=0, padx=10, pady=5)
        self.convert_unit_entry = tk.Entry(self.image_converter_tab)
        self.convert_unit_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.image_converter_tab, text="File Extension:").grid(row=4, column=0, padx=10, pady=5)
        self.extension_var = tk.StringVar(value=".png")

        self.png_radio = tk.Radiobutton(self.image_converter_tab, text="PNG", variable=self.extension_var, value=".png")
        self.png_radio.grid(row=4, column=1, padx=10, pady=5)
        self.jpg_radio = tk.Radiobutton(self.image_converter_tab, text="JPG", variable=self.extension_var, value=".jpg")
        self.jpg_radio.grid(row=4, column=2, padx=10, pady=5)
        self.bmp_radio = tk.Radiobutton(self.image_converter_tab, text="BMP", variable=self.extension_var, value=".bmp")
        self.bmp_radio.grid(row=4, column=3, padx=10, pady=5)

        self.convert_button = tk.Button(self.image_converter_tab, text="Convert Images", command=self.convert_images)
        self.convert_button.grid(row=5, column=1, padx=10, pady=10)

    def pick_bg_color(self):
        color_code = colorchooser.askcolor(title="Choose Background Color")[1]
        if color_code:
            self.bg_color_entry.delete(0, tk.END)
            self.bg_color_entry.insert(0, color_code)
            self.bg_color = color_code

    def pick_text_color(self):
        color_code = colorchooser.askcolor(title="Choose Text Color")[1]
        if color_code:
            self.text_color_entry.delete(0, tk.END)
            self.text_color_entry.insert(0, color_code)
            self.text_color = color_code

    def save_image(self):
        text = self.text_entry.get("1.0", tk.END).strip()
        bg_color = self.bg_color_entry.get() or "#FFFFFF"
        text_color = self.text_color_entry.get() or "#000000"

        width = self.width_entry.get()
        height = self.height_entry.get()
        unit = self.unit_entry.get().strip().lower()

        try:
            if not width or not height:
                raise ValueError("Width and height are required")

            width = convert_units(float(width), unit)
            height = convert_units(float(height), unit)

            large_width = 3000
            large_height = 3000
            large_image = Image.new('RGBA', (large_width, large_height), bg_color)
            draw = ImageDraw.Draw(large_image)

            font_size = 100
            font_path = "arial.ttf"
            font = ImageFont.truetype(font_path, font_size)

            while True:
                text_bbox = draw.textbbox((0, 0), text, font=font)
                text_width = text_bbox[2] - text_bbox[0]
                text_height = text_bbox[3] - text_bbox[1]

                if text_width > large_width - 40 or text_height > large_height - 40:
                    if font_size <= 10:
                        break
                    font_size -= 10
                    font = ImageFont.truetype(font_path, font_size)
                else:
                    if text_width <= width and text_height <= height:
                        break
                    font_size -= 1
                    font = ImageFont.truetype(font_path, font_size)

            # Draw text
            text_bbox = draw.textbbox((0, 0), text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            text_x = (large_width - text_width) / 2
            text_y = (large_height - text_height) / 2
            draw.text((text_x, text_y), text, font=font, fill=text_color)

            # Resize to user-specified dimensions
            resized_image = large_image.resize((width, height), Image.LANCZOS)

            # Save image with random name
            file_name = random_filename()
            resized_image.save(file_name)
            messagebox.showinfo("Success", f"Image saved as {file_name}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def browse_images(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png;*.jpg;*.bmp")])
        if file_paths:
            self.image_listbox.delete(0, tk.END)
            for file_path in file_paths:
                self.image_listbox.insert(tk.END, file_path)
            self.select_all_images()

    def select_all_images(self):
        self.image_listbox.select_set(0, tk.END)

    def deselect_all_images(self):
        self.image_listbox.select_clear(0, tk.END)

    def convert_images(self):
        try:
            width = self.convert_width_entry.get()
            height = self.convert_height_entry.get()
            unit = self.convert_unit_entry.get().strip().lower()
            extension = self.extension_var.get()

            if not width or not height:
                raise ValueError("Width and height are required")

            width = convert_units(float(width), unit)
            height = convert_units(float(height), unit)

            selected_files = self.image_listbox.curselection()
            if not selected_files:
                raise ValueError("No images selected")

            saved_files_count = 0
            start_index = 1
            for index in selected_files:
                file_path = self.image_listbox.get(index)
                try:
                    with Image.open(file_path) as img:
                        img_resized = img.resize((width, height))
                        file_name = sequential_filename("converted_image", start_index, extension)
                        img_resized.save(file_name)
                        saved_files_count += 1
                        start_index += 1
                except Exception as e:
                    messagebox.showerror("Error", f"Error processing {file_path}: {str(e)}")

            if saved_files_count > 0:
                messagebox.showinfo("Success", f"Total number of images saved: {saved_files_count}")
            else:
                messagebox.showinfo("No Images", "No images were successfully saved.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToImageApp(root)
    root.mainloop()
