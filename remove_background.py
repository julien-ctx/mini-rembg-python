#This program creates a window and request the link to an image using Tkinter lib. Then it uses RemBG library to remove background using IA. It stores the output in ~/Downloads

import tkinter as tk
import subprocess

def download_output():
        if input_text.get():
                text_response = input_text.get()
        else:
                text_response = "Input cannot be empty!"
        text_widget = tk.Text()
        text_widget.insert(tk.END, text_response)
        text_widget.grid(row=3, column=0)

window = tk.Tk();
window.geometry("900x550")
window.title("RemBG | Remove background from images")
window.grid_columnconfigure(0, weight=1)

input_msg = tk.Label(window, 
                                        text="Enter the link of your image", 
                                        font=("Lato", 15))

input_msg.grid(row=0, column=0, sticky="N", padx=20, pady=10)

input_text = tk.Entry()
input_text.grid(row=1, column=0, sticky="WE", padx=16)

download_btn = tk.Button(text="Download ouput in PNG", command=download_output)
download_btn.grid(row=2, column=0, sticky="WE", padx=10, pady=10)

stream = os.popen("curl -s ", str(input_text), " | rembg i -a -ae 15 > ~/omg.png")
img_output = stream.read()

if __name__ == '__main__':
        window.mainloop()
