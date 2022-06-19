#This program creates a window and request the link to an image using Tkinter lib. Then it uses RemBG library to remove background using IA. It stores the output in ~/Downloads

import tkinter as tk
import subprocess as sb
import os

def create_output():
	if input_text.get():
		text_response = input_text.get()
		sb.getoutput("rm -rf exe.sh")
		sb.getoutput("rm -rf output.png")
		#print(str(text_response))
        #problem with returned data here
		first_commands = ('echo "curl -s', str(text_response),'|', 'rembg i -a -ae 15 > output.png" > exe.sh');
		command = ' '.join(first_commands)
		sb.getoutput(str(command))
		sb.getoutput("chmod 777 exe.sh")
		sb.getoutput("sh exe.sh")
		text_widget = tk.Text()
		text_widget.insert(tk.END, "Background removed!")
		text_widget.grid(row=3, column=0)
		sb.getoutput("open .")
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
					text="Enter the link of your image\nDon't put any spaces between, before or after the link",
					font=("Lato", 15))

input_msg.grid(row=0, column=0, sticky="N", padx=20, pady=10)

input_text = tk.Entry()
input_text.grid(row=1, column=0, sticky="WE", padx=16)

download_btn = tk.Button(text="Download ouput in PNG", command=create_output)
download_btn.grid(row=2, column=0, sticky="WE", padx=10, pady=10)

if __name__ == '__main__':
	window.mainloop()
