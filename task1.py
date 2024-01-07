import playsound
import tkinter as tk
from tkinter import PhotoImage
from tkinter.ttk import *

root = tk.Tk()

root.geometry("600x250")
root.title("Soundboard")

#labels
titleLable = tk.Label(root, text = "Soundboard!", font = ('Impact', 16))

dogLabel = tk.Label(root, text = "Dog Bark", font = ('Comic Sans MS', 14))
metalPipeLabel = tk.Label(root, text = "Metal Pipe", font = ('Comic Sans MS', 14))
rizzLabel = tk.Label(root, text = "Rizz", font = ('Comic Sans MS', 14))

#fun fact: this only works with pngs!
dogImage = PhotoImage(file="images/dog.png").subsample(3, 3)
metalPipeImage = PhotoImage(file="images/metal-pipe.png").subsample(5, 5)
rizzImage = PhotoImage(file="images/rizz.png").subsample(4, 4)

#buttons
dogButton = tk.Button(root, image = dogImage, height = 100, width = 100, command = lambda: playsound.playsound('sounds/dog-bark.mp3', block = False))
metalPipeButton = tk.Button(root, image = metalPipeImage, height = 100, width = 100, command = lambda: playsound.playsound('sounds/metal-pipe.mp3', block = False))
rizzButton = tk.Button(root, image = rizzImage, height = 100, width = 100, command = lambda: playsound.playsound('sounds/rizz-sound.mp3', block = False))

#grid
titleLable.grid(row = 1, column = 2)

dogLabel.grid(row = 2, column = 1)
metalPipeLabel.grid(row = 2, column = 2)
rizzLabel.grid(row = 2, column = 3)

dogButton.grid(row = 3, column = 1)
metalPipeButton.grid(row = 3, column = 2)
rizzButton.grid(row = 3, column = 3)

root.mainloop() 