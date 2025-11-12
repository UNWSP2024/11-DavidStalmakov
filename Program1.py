# David Stalmakov, 11/12/2025
# Favorite saying

import tkinter

# create main window
window = tkinter.Tk()
window.title("Favorite Saying")
window.geometry("500x500")

saying = "\"He who guards his mouth and his tongue, Guards his soul from troubles.\" (Proverbs 21:23)"
label = tkinter.Label(window, text=saying)
label.pack()

window.mainloop()