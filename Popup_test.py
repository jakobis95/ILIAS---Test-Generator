from tkinter import *

root = Tk()

l = Label(root, text="Right-click to display menu", width=40, height=20)
l.pack()

popup = Menu(root, tearoff=0)
popup.add_command(label="New")
popup.add_command(label="Save")
popup.add_separator()
popup.add_command(label="Quit")

def do_popup(event):
    # entweder
    try:
        popup.tk_popup(event.x_root, event.y_root, 0)
    finally:
        popup.grab_release()
    # oder
    #popup.post(event.x_root, event.y_root)

l.bind("<Button-3>", do_popup)

root.mainloop()
