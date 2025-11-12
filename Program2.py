# David Stalmakov, 11/12/2025
# Display Info
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # create the main window
        self.main_window = tkinter.Tk()

        # Create a 'Show Info' button
        self.my_button = tkinter.Button(self.main_window, text="Show Info", command=self.do_something)
        self.my_button.pack()
        # Create a quit button
        self.quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)
        self.quit_button.pack()
        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo("Info", "David Stalmakov: 1976 Staghorn Dr. Shakopee MN 55379")


if __name__ == '__main__':
    my_gui = MyGUI()