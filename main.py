from tkinter import *
import time
import math
from HUB import hub
from FLO_HINGE import flo_hinge

WIDTH = 600.0
HEIGHT = 800.0
UPD_TIME = 0.01

window = Tk()
window.tk.call('tk', 'scaling', .50)
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

hub_1 = hub(60.0, HEIGHT - 60.0, 50.0, 15.0, 153.0, 0.0, canvas)
hub_2 = hub(250, HEIGHT - 100, 45, hub_1.rpm * hub_1.radius / 45, 143.0, 0.0, canvas)
hub_3 = hub(350, HEIGHT - 200, 30, hub_2.rpm * hub_2.radius / 30, 190.0, 0.0, canvas)
hub_4 = hub(450, HEIGHT - 300, 60, hub_3.rpm * hub_3.radius / 60, 220.0, 0.0, canvas)
hub_5 = hub(500, HEIGHT - 500, 40, hub_4.rpm * hub_4.radius / 40, 220.0, 0.0, canvas)

flo_hinge_1 = flo_hinge(140, canvas)
flo_hinge_2 = flo_hinge(190, canvas)
flo_hinge_3 = flo_hinge(140, canvas)
flo_hinge_4 = flo_hinge(5, canvas)

hub_1.create_shapes()
hub_2.create_shapes()
hub_3.create_shapes()
hub_4.create_shapes()
hub_5.create_shapes()

flo_hinge_1.create_shapes()
flo_hinge_2.create_shapes()
flo_hinge_3.create_shapes()
flo_hinge_4.create_shapes()



while True:
    hub_1.update(flo_hinge_1)
    hub_2.update(flo_hinge_1)
    hub_3.update(flo_hinge_2)
    hub_4.update(flo_hinge_3)
    hub_5.update(flo_hinge_4)

    flo_hinge_1.calc_rod_intersect(True, hub_1, hub_2)
    flo_hinge_2.calc_rod_intersect(False, flo_hinge_1, hub_3)
    flo_hinge_3.calc_rod_intersect(False, flo_hinge_2, hub_4)
    flo_hinge_4.calc_rod_intersect(False, flo_hinge_3, hub_5)

    flo_hinge_1.update(flo_hinge_2)
    flo_hinge_2.update(flo_hinge_3)
    flo_hinge_3.update(flo_hinge_4)
    flo_hinge_4.update(None)


    # hub_1.draw_rod()

    # xt, yt = hub_1.calc_rod_intersect(hub_2)
    # xf, yf = hub_1.rod_joint_pos
    # xf2, yf2 = hub_2.rod_joint_pos
    # canvas.coords(int1, xt - 1, yt - 1, xt + 1, yt + 1)
    # hub_1.draw_rod(xf, yf, xt, yt)
    # hub_2.draw_rod(xf2, yf2, xt, yt)
    #
    # xp, yp = hub_3.rod_joint_pos
    # xq, yq = calc_rod_int(xt, yt, xp, yp, 140, hub_3.rod_len)
    # canvas.coords(p2, xq-1, yq-1, xq+1, yq+1)
    #
    # canvas.coords(l3, xp, yp, xq, yq)
    # canvas.coords(l2, xt, yt, xq, yq)


    # print(xt)
    # print(yt)

    window.update()
    time.sleep(UPD_TIME)

window.mainloop()
