import playsound
import tkinter as tk
from tkinter.ttk import *

window = tk.Tk()
window.geometry("600x250")


#labels
titleLable = tk.Label(window, text = "Soundboard!")

#buttons
dogButton = tk.Button(window, text = "Dog\nBark", height = 2, width = 9, command = lambda: playsound.playsound('sounds/dog-bark.mp3', block = False))
metalPipeButton = tk.Button(window, text = "Metal\nPipe", height = 2, width = 9, command = lambda: playsound.playsound('sounds/metal-pipe.mp3', block = False))
rizzButton = tk.Button(window, text = "Rizz\nSound", height = 2, width = 9, command = lambda: playsound.playsound('sounds/rizz-sound.mp3', block = False))

#grid
titleLable.grid(row = 1, column = 2)

dogButton.grid(row = 2, column = 1)
metalPipeButton.grid(row = 2, column = 2)
rizzButton.grid(row = 2, column = 3)

window.mainloop()