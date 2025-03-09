# import tkinter as tk

# def on_button_click():
#     label.config(text="Hello, " + entry.get())

# # Create the main window
# root = tk.Tk()
# root.title("Simple Tkinter Interface")

# # Create and pack widgets
# label = tk.Label(root, text="Enter your name:")
# label.pack(pady=10)

# ===================

# def open_link(event):
#     webbrowser.open("https://www.example.com")

# # Create the main window
# root = tk.Tk()
# root.title("Clickable Link Example")

# # Create and pack widgets
# label_text = "Click the link below:"
# label = tk.Label(root, text=label_text, cursor="hand2", fg="blue", underline=True)
# label.pack(pady=10)

# # Bind the label to the open_link function when clicked
# label.bind("<Button-1>", open_link)

# # Start the Tkinter event loop
# root.mainloop()




import tkinter as tk
import webbrowser

def on_button_click():
    label.config(text="Hello, " + entry.get())
    
def open_link(event):
    webbrowser.open("https://colab.research.google.com/drive/1DyY5xXfYlbyHApnP3W4qN0u15qdGqban")
    
# Create the main window
root = tk.Tk()
root.title("Clickable Link Example")

# Create and pack widgets
label_text = "TO VIEW ANALYSIS"
label = tk.Label(root, text=label_text, cursor="hand2", fg="blue", underline=True)
label.pack(pady=10)

# Bind the label to the open_link function when clicked
label.bind("<Button-1>", open_link)

# Start the Tkinter event loop
root.mainloop()

# ======================


# entry = tk.Entry(root)
# entry.pack(pady=10)

# button = tk.Button(root, text="Say Hello", command=on_button_click)
# button.pack(pady=10)

# # Start the Tkinter event loop
# root.mainloop()