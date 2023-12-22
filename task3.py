#
# Create a canvas object and use key bindings to be able to move a sprite around the canvas.
# * Make a sound effect for every time you move the sprite
# * Make a sound effect every time it tries to move off the screen and prevent it from moving off the screen

import tkinter as tk
import playsound

#simple class for the coordinates of the box and the box itself
class MoveCanvas(tk.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
        self.dx = 0
        self.dy = 0

        #change this a bit to make it bigger
        self.box = self.create_rectangle(0, 0, 10, 10, fill="black")

        #one tick is 25ms
        self.dt = 25
        self.tick()
    
    #move every tick
    def tick(self):
        self.move(self.box, self.dx, self.dy)
        self.after(self.dt, self.tick)
    
    def change_heading(self, dx, dy):
        print(self.dx, self.dy)

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