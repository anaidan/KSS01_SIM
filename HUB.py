import math

UPD_TIME = 0.01

class hub:
    def __init__(self, axel_x, axel_y, radius, rpm, rod_len, ang, canvas):
        self.axel_x = axel_x
        self.axel_y = axel_y
        self.radius = radius  # in pixels
        self.rpm = rpm
        self.rod_len = rod_len  # in pixels
        self.ang = ang  # in radians
        self.RPU = self.rpm / 60.0 * UPD_TIME * 2.0 * math.pi
        self.rod_joint_pos = self.calc_rod_joint_pos()
        self.canvas = canvas

    def create_shapes(self):
        x, y = self.calc_rod_joint_pos()
        self.canvas.create_oval(self.axel_x - self.radius, self.axel_y - self.radius,
                           self.axel_x + self.radius, self.axel_y + self.radius,
                           outline="gray", fill="white", width=1)
        self.rj = self.canvas.create_oval(x - 1, y - 1, x + 1, y + 1,
                                     outline="black", fill="black", width=1)
        self.rod = self.canvas.create_line(0, 0, 0, 0, fill="gray")


    def calc_rod_joint_pos(self):
        x = self.axel_x + self.radius * math.cos(self.ang)
        y = self.axel_y - self.radius * math.sin(self.ang)
        self.rod_joint_pos = x, y
        return x, y

    def update(self, _flo_hinge):
        x, y = self.calc_rod_joint_pos()
        self.canvas.coords(self.rj, x - 1, y - 1, x + 1, y + 1)
        self.ang = (self.ang + self.RPU) % (2 * math.pi)
        self.canvas.coords(self.rod, x, y, _flo_hinge.axel_x, _flo_hinge.axel_y)



