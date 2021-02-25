import math

UPD_TIME = 0.01

class flo_hinge:
    def __init__(self, rod_len, canvas):
        self.axel_x = 0
        self.axel_y = 0
        self.rod_len = rod_len  # in pixels
        self.canvas = canvas

    def create_shapes(self):
        x = self.axel_x
        y = self.axel_y
        self. axel = self.canvas.create_oval(self.axel_x - 1, self.axel_y - 1,
                           self.axel_x + 1, self.axel_y + 1,
                           outline="black", fill="white", width=1)
        self.rod = self.canvas.create_line(0, 0, 0, 0, fill="gray")

    def calc_rod_intersect(self, h2f, joint1, joint2):

        if h2f is True:
            x1, y1 = joint1.calc_rod_joint_pos()
            x2, y2 = joint2.calc_rod_joint_pos()
        else:
            x1 = joint1.axel_x
            y1 = joint1.axel_y
            x2, y2 =joint2.calc_rod_joint_pos()

        r1 = joint1.rod_len
        r2 = joint2.rod_len
        R = math.sqrt((x1-x2)**2+(y1-y2)**2)

        xa = .5*(x1+x2) + (r1**2-r2**2)/(2*R**2) * (x2-x1) + .5*math.sqrt(2*(r1**2+r2**2)/(R**2) - (r1**2-r2**2)**2/(R**4) - 1)*(y2-y1)
        # xb = .5*(x1+x2) + (r1**2-r2**2)/(2*R**2) * (x2-x1) - .5*math.sqrt(2*(r1**2+r2**2)/(R**2) - (r1**2-r2**2)**2/(R**4) - 1)*(y2-y1)

        ya = .5*(y1+y2) + (r1**2-r2**2)/(2*R**2) * (y2-y1) + .5*math.sqrt(2*(r1**2+r2**2)/(R**2) - (r1**2-r2**2)**2/(R**4) - 1)*(x1-x2)
        # yb = .5*(y1+y2) + (r1**2-r2**2)/(2*R**2) * (y2-y1) - .5*math.sqrt(2*(r1**2+r2**2)/(R**2) - (r1**2-r2**2)**2/(R**4) - 1)*(x1-x2)

        self.axel_x = xa
        self.axel_y = ya

    def update(self, next_joint):
        self.canvas.coords(self.axel, self.axel_x - 1, self.axel_y - 1, self.axel_x + 1, self.axel_y + 1)
        if next_joint is not None:
            self.canvas.coords(self.rod, self.axel_x, self.axel_y, next_joint.axel_x, next_joint.axel_y)
