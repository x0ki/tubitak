from tkinter import *
# create the canvas, size in pixels
while True:
    canvas = Canvas(width = 300, height = 200, bg = 'yellow')
    canvas.pack(expand = YES, fill = BOTH)
    # put in your own gif file here, may need to add full path
    # like 'C:/WINDOWS/Help/Tours/WindowsMediaPlayer/Img/mplogo.gif'
    gif1 = PhotoImage(file = '1_hM-YgNbGjv_yK1ezYNdIaQ.gif')
    # put gif image on canvas
    # pic's upper left corner (NW) on the canvas is at x=50 y=10
    canvas.create_image(50, 10, image = gif1, anchor = NW)
# run it ...
mainloop()