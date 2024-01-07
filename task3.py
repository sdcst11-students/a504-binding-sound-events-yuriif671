#
# Create a canvas object and use key bindings to be able to move a sprite around the canvas.
# * Make a sound effect for every time you move the sprite
# * Make a sound effect every time it tries to move off the screen and prevent it from moving off the screen

import tkinter as tk
import playsound

#simple class for coordinates of the box and the box itself
class MoveCanvas(tk.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
        self.dx = 0
        self.dy = 0

        self.sound_played = False

        #it stores the coords in a strange way -- x1, x2 are top-left corner and the bottom-right corner is x2 and y2
        self.box = self.create_rectangle(140, 120, 150, 130, fill="black")

        #one tick is 25ms
        self.dt = 25
        self.tick()
    
    #move every tick and check the position
    def tick(self):
        #coords is a built-in method to get the current coordinates of an object (handy!)
        x1, y1, x2, y2 = self.coords(self.box)

        # Check if next tick will place the object out of boundary
        if x1 + self.dx <= 0 or x2 + self.dx >= 300:
            self.dx = 0
            playsound.playsound('sounds/dog-bark.mp3', block=False)

        elif y1 + self.dy <= 0 or y2 + self.dy >= 300:
            self.dy = 0
            playsound.playsound('sounds/dog-bark.mp3', block=False)

        self.move(self.box, self.dx, self.dy)
        self.after(self.dt, self.tick)
    
    #the actual change of direction!
    def change_heading(self, dx, dy):
        self.dx = dx
        self.dy = dy
 
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")
    
    #canvas
    cvs = MoveCanvas(root)
    cvs.pack(fill="both", expand=True)
    
    #speed of the cube
    ds = 3
  
    root.bind("<KeyPress-Left>", lambda _: [cvs.change_heading(-ds, 0), playsound.playsound('sounds/rizz-sound.mp3', block = False)])
    root.bind("<KeyPress-Right>", lambda _: [cvs.change_heading(ds, 0), playsound.playsound('sounds/rizz-sound.mp3', block = False)])
    root.bind("<KeyPress-Up>", lambda _: [cvs.change_heading(0, -ds), playsound.playsound('sounds/rizz-sound.mp3', block = False)])
    root.bind("<KeyPress-Down>", lambda _: [cvs.change_heading(0, ds), playsound.playsound('sounds/rizz-sound.mp3', block = False)])    
      
    root.mainloop()