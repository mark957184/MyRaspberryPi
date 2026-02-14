# THIS CODE IS MADE ON A DEBIAN ENVIROMENT

import tkinter as tk
import platform
import psutil

class TempMonitorApp:
    def __init__(self, root):
        self.root = root

        self.root.title("TempMonitor 1.0") # Learned from some documentations to setup the app, this decides the title of the app

        self.root.attributes("-topmost", True) # In this way the app is always-on-top

        self.root.overrideredirect(True) # Makes it a cool border-less UI

        # Aesthetics of the app
        self.root.geometry("200x80")
        self.root.configure(bg='black')

        # Unpacks and loads the text
        self.label = tk.Label(root, text="Inizializzazione...", 
                              fg="white", bg="black", 
                              font=("Helvetica", 14, "bold"))
        self.label.pack(expand=True)

        self.update_stats()

    def get_temp(self):
        try:
            with open("/sys/class/thermal/thermal_zone0/temp", "r") as t: # This folder is present only on the Raspberry, not in the WSL Debian environment
                return f"{int(t.read()) / 1000:.1f}°C"
        except:
            return "N/A"
        
    def update_stats(self):
        temp = self.get_temp()
        cpu = psutil.cpu_percent()
        
        self.label.config(text=f"CPU: {cpu}%\nTemp: {temp}") # Updates infos
        self.root.attributes("-topmost", True) # Makes it always-on-top after every update
        self.root.update()
        self.root.after(1000, self.update_stats) # Executes every second
    
root = tk.Tk()
app = TempMonitorApp(root)
root.mainloop()


# unfortunately the always-on-top functionality is not considered in subsystems like Debian in WSL, but in the raspberry it will work gracefully