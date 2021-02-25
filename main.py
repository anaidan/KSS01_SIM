from tkinter import *
import time
import math
from HUB import hub
# from FLO_HINGE import flo_hinge


def calc_rod_int(x1, y1, x2 , y2, r1, r2):
    R = math.sqrt((x1-x2)**2+(y1-y2)**2)

    xa = .5*(x1+x2) + (r1**2-r2**2)/(2*R**2) * (x2-x1) + .5*math.sqrt(2*(r1**2+r2**2)/(R**2) - (r1**2-r2**2)**2/(R**4) - 1)*(y2-y1)
    xb = .5*(x1+x2) + (r1**2-r2**2)/(2*R**2) * (x2-x1) - .5*math.sqrt(2*(r1**2+r2**2)/(R**2) - (r1**2-r2**2)**2/(R**4) - 1)*(y2-y1)

    ya = .5*(y1+y2) + (r1**2-r2**2)/(2*R**2) * (y2-y1) + .5*math.sqrt(2*(r1**2+r2**2)/(R**2) - (r1**2-r2**2)**2/(R**4) - 1)*(x1-x2)
    yb = .5*(y1+y2) + (r1**2-r2**2)/(2*R**2) * (y2-y1) - .5*math.sqrt(2*(r1**2+r2**2)/(R**2) - (r1**2-r2**2)**2/(R**4) - 1)*(x1-x2)

    return xa, ya

WIDTH = 600.0
HEIGHT = 600.0
UPD_TIME = 0.01


window = Tk()
window.tk.call('tk', 'scaling', .50)

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

hub_1 = hub(60.0, HEIGHT - 60.0, 50.0, 10.0, 153.0, 0.0, canvas)
hub_2 = hub(250, HEIGHT - 100, 45, hub_1.rpm * hub_1.radius / 45, 143.0, 0.0, canvas)
hub_3 = hub(350, HEIGHT - 200, 30, hub_2.rpm * hub_2.radius / 30, 190.0, 0.0, canvas)


hub_1.create_shapes()
hub_2.create_shapes()
hub_3.create_shapes()

l2 = canvas.create_line(0, 0, 0, 0, fill="gray")
l3 = canvas.create_line(0, 0, 0, 0, fill="gray")

p2 = canvas.create_oval(- 1, - 1,  1,  1, outline="black", fill="black", width=1)

int1 = canvas.create_oval(-1, -1, 1, 1, outline="black", fill="black", width=1)

while True:
    hub_1.upd_rod_joint()
    hub_2.upd_rod_joint()
    hub_3.upd_rod_joint()

    xt, yt = hub_1.calc_rod_intersect(hub_2)
    xf, yf = hub_1.rod_joint_pos
    xf2, yf2 = hub_2.rod_joint_pos
    canvas.coords(int1, xt - 1, yt - 1, xt + 1, yt + 1)
    hub_1.draw_rod(xf, yf, xt, yt)
    hub_2.draw_rod(xf2, yf2, xt, yt)

    xp, yp = hub_3.rod_joint_pos
    xq, yq = calc_rod_int(xt, yt, xp, yp, 140, hub_3.rod_len)
    canvas.coords(p2, xq-1, yq-1, xq+1, yq+1)

    canvas.coords(l3, xp, yp, xq, yq)
    canvas.coords(l2, xt, yt, xq, yq)


    # print(xt)
    # print(yt)

    window.update()
    time.sleep(UPD_TIME)

window.mainloop()
