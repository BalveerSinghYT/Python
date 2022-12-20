import tkinter as tk
import time
import math

class Clock(tk.Canvas):

    def __init__(self, parent, width=500, height=500):
        super().__init__(parent, width=width, height=height)

        self.width = width
        self.height = height

        self.center_x = width / 2
        self.center_y = height / 2

        self.radius = min(width, height) / 2

        self.create_oval(0, 0, width, height, fill="black", outline="white")
        self.create_oval(10, 10, width-10, height-10, fill="black", outline="white")

        self.create_text(self.center_x, self.center_y-225, text="12", fill="white")
        self.create_text(self.center_x, height-20, text="6", fill="white")
        self.create_text(20, self.center_y, text="9", fill="white")
        self.create_text(width-20, self.center_y, text="3", fill="white")

        self.hour_hand = self.create_line(0, 0, 0, 0, width=5, fill="white")
        self.minute_hand = self.create_line(0, 0, 0, 0, width=3, fill="white")
        self.second_hand = self.create_line(0, 0, 0, 0, width=1, fill="red")

        self.update_clock()

    def update_clock(self):
        now = time.localtime()

        seconds = now.tm_sec
        minutes = now.tm_min
        hours = now.tm_hour

        second_angle = (seconds / 60) * 360
        minute_angle = (minutes / 60) * 360
        hour_angle = (hours / 12) * 360

        self.coords(self.second_hand, self.center_x, self.center_y, self.center_x + math.sin(math.radians(second_angle)) * self.radius, self.center_y - math.cos(math.radians(second_angle)) * self.radius)
        self.coords(self.minute_hand, self.center_x, self.center_y, self.center_x + math.sin(math.radians(minute_angle)) * self.radius * 0.8, self.center_y - math.cos(math.radians(minute_angle)) * self.radius * 0.8)
        self.coords(self.hour_hand, self.center_x, self.center_y, self.center_x + math.sin(math.radians(hour_angle)) * self.radius * 0.5, self.center_y - math.cos(math.radians(hour_angle)) * self.radius * 0.5)

        self.after(1000, self.update_clock)
        
        # Digital Time
        show_time = time.strftime("%H:%M:%S")
        digital_clock = tk.Entry(root, width=10, font=("Arial", 20, "bold"), bg="black", fg="white", bd=0, justify="center")
        digital_clock.insert(tk.END, show_time)
        digital_clock.place(x=self.center_x-80, y=self.center_y-80)

        # Date
        self.create_text(self.center_x, self.center_y+100, text=time.strftime("%d/%m/%Y"), fill="white", font=("Arial", 15, "bold"))
        
        # Week Day
        self.create_text(self.center_x, self.center_y+120, text=time.strftime("%A"), fill="white", font=("Arial", 10))
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Analog-Digital Clock")
    root.resizable(False, False)

    clock = Clock(root)
    clock.pack()

    root.mainloop()
