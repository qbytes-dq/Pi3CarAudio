# shrink_image.py
import sys
#from Tkinter import Tk, PhotoImage, Label

if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    from Tkinter import *
else:
    from tkinter import *

root = Tk()

# First command line arg is image path. PNG format
#if sys.argv[1]:
if len(sys.argv) > 1:
    base_img = PhotoImage(file=sys.argv[1])
else:
    base_img = PhotoImage(file = "MeterV270.png")
    

#if base_img is None :
#   base_img = "MeterV270.png"

# Take only every 3rd pixel from x and y resulting in an image of 1/3 size
img1 = base_img.subsample(3, 3) 

# Take every pixel from x but only every other from y. Shrinks y by half
img2 = base_img.subsample(1, 2) 

base_img_label = Label(root, image=base_img)
img1_label        = Label(root, image=img1)
img2_label        = Label(root, image=img2)

base_img_label.pack()
img1_label.pack()
img2_label.pack()

root.mainloop()


### http://stackoverflow.com/questions/7966119/display-fullscreen-mode-on-tkinter
