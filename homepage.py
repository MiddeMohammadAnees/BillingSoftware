import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def open_page(page_name):
    # Replace this function with code to open different pages based on page_name
    pass

# Create the main application window
root = tk.Tk()
root.title("Home Page")

# Load your background image and resize it to fit the screen dimensions
background_image = Image.open("Images/b1.jpg")
background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
background_image = ImageTk.PhotoImage(background_image)

# Create a Canvas widget for the background image, set its size to screen dimensions
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack()

# Place the background image on the canvas
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Create buttons with different colors on the canvas
button_styles = {
    "About": {"text": "About", "background": "green"},
    "Contact": {"text": "Login", "bg": "blue"},
    "Admin":{"text": "Admin", "bg": "blue"}
}

# Y-coordinate to position buttons

for page_name, style_info in button_styles.items():
    if page_name == "About":
        x_coordinate = 1270  # Move the "About" button to the left side
        y_coordinate = 60
    elif page_name == "Contact":
        x_coordinate = root.winfo_screenwidth() - 150  # Move the "Contact" button to the right side
        y_coordinate = 60
    elif page_name == "Admin":
        x_coordinate = root.winfo_screenwidth() - 945  # Move the "Contact" button to the right side        
        y_coordinate = 409
    else:
        x_coordinate = 20

    button = ttk.Button(root, text=style_info["text"], style="Content.TButton",
                        command=lambda name=page_name: open_page(name))
    canvas.create_window(x_coordinate, y_coordinate, anchor="nw", window=button, width=100, height=40)
    y_coordinate += 50  # Increase the y-coordinate for the next button

# Create a transparent label to display the text in 1 line and move it to the right-center
text_line = "Billing software simplifies product management by enabling users to add and remove items from their inventory effortlessly. It streamlines the billing process, automates invoicing, and manages product catalogs efficiently, making it essential for businesses."

# Create a transparent image (1x1 pixel)
transparent_image = Image.new("RGBA", (1, 1), (255, 255, 255, 0))
transparent_photo = ImageTk.PhotoImage(transparent_image)



# Use the transparent image as the label's background
text_label = tk.Label(canvas, text=text_line, font=("Helvetica", 16),fg="black", image=transparent_photo, compound="center", justify="left", wraplength=500)
text_label.place(relx=0.7, rely=0.4, anchor="center")

# Start the Tkinter main loop
root.mainloop()
