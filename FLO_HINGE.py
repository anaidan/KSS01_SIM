import math

UPD_TIME = 0.01

class flo_HINGE:
    def __init__(self, axel_x, axel_y, rod_len, canvas):
        self.axel_x = axel_x
        self.axel_y = axel_y
        self.rod_len = rod_len  # in pixels
        self.canvas = canvas

    def create_shapes(self):
        x = self.axel_x
        y = self.axel_y
        self.canvas.create_oval(self.axel_x - self.radius, self.axel_y - self.radius,
                           self.axel_x + self.radius, self.axel_y + self.radius,
                           outline="gray", fill="white", width=1)
        self.rod = self.canvas.create_line(0, 0, 0, 0, fill="gray")


