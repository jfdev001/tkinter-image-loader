"""A simple image loader for set size images.
Best practices with classes below:
https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
https://stackoverflow.com/questions/16115378/tkinter-example-code-for-multiple-windows-why-wont-buttons-load-correctly
"""

import tkinter as tk
from PIL import Image, ImageTk
import os


class ImageLoader:
    """A GUI that can cycle through images in a directory."""
    def __init__(self, master=None):
        """Construct master frame and pack the window to the screen."""
        self.master = master
        self.frame = tk.Frame(self.master)  # Parent frame
        self.master.title("Image Loader")
        self.frame.pack()

        # Create the rest of the GUI 
        self.create_photoimage_list()
        self.create_label()
        self.create_buttons()


    def create_photoimage_list(self):
        """List of PhotoImage objects made from files in image dir."""
        self.path = r"C:\Users\jared\Pictures\images"
        self.files_in_dir = os.listdir(self.path)
        self.cur_file_index = [0]  # Initial file position is 0 in list
        self.photoimage_list = []
        for img in self.files_in_dir:
            self.photoimage_list.append(ImageTk.PhotoImage(
                Image.open(self.path + "/" + img).resize((400,400))))


    def create_label(self):
        """Define and display Label for image.
        Why is self.master an invalid argument?
        """
        self.img = tk.Label(self.frame,
                    image=self.photoimage_list[self.cur_file_index[0]])
        self.img.grid(row=0, column=0, columnspan=3)


    def create_buttons(self):
        """Create a back, forward, and exit button for the program."""
        self.bck = tk.Button(master=self.frame, text="previous", 
                        command=self.backward)
        self.fwd = tk.Button(master=self.frame, text="next", 
                        command=self.forward)
        self.exit = tk.Button(master=self.frame, text="EXIT", 
                        command=self.frame.quit)
        self.bck.grid(row=1, column=0)                 
        self.exit.grid(row=1, column=1)
        self.fwd.grid(row=1, column=2)


    def forward(self):
        """Advance position in PhotoImage list by one."""
        if (self.cur_file_index[0] + 1 < len(self.files_in_dir)):
            self.cur_file_index[0] = self.cur_file_index[0] + 1
            self.img.configure(image=self.photoimage_list[
                self.cur_file_index[0]])
            self.img.image = self.photoimage_list[self.cur_file_index[0]]

    
    def backward(self):
        """Decrement position in PhotoImage list by one."""
        if (self.cur_file_index[0] - 1 > -1):
            self.cur_file_index[0] = self.cur_file_index[0] - 1
            self.img.configure(image=self.photoimage_list[
                self.cur_file_index[0]])
            self.img.image = self.photoimage_list[self.cur_file_index[0]]


def main():
    root = tk.Tk()
    app = ImageLoader(root)
    root.mainloop()


if __name__ == "__main__":
    main()