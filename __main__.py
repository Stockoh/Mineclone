import tkinter
import ctypes
user32 = ctypes.windll.user32
user32.GetSystemMetrics(0)


Mineclone = tkinter.Tk()  # The window of the game
Mineclone.title = "Mineclone"

# Set the window to full screen
Mineclone.attributes("-fullscreen", True)

# Create the Scene
Scene = tkinter.Canvas(Mineclone, bg="white", width=user32.GetSystemMetrics(0),
                       height=user32.GetSystemMetrics(1))
Scene.grid()

# Start the game
Mineclone.mainloop()
