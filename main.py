from tkinter import *
import time
import math
from HUB import hub
from FLO_HINGE import flo_hinge

WIDTH = 500.0
HEIGHT = 500.0
UPD_TIME = 0.01

window = Tk()
window.tk.call('tk', 'scaling', .50)
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

hubs = []
flo_hinges = []
un_rs = 100

hubs.append(hub(150.0, HEIGHT - 100.0, 35.0, 10.0, 150.0, 0.0, canvas))
hubs.append(hub(250, HEIGHT - 200, 45, hubs[0].rpm * hubs[0].radius / 45, 150, 0.0, canvas))
hubs.append(hub(350, HEIGHT - 300, 49, hubs[1].rpm * hubs[1].radius / 49, 220, 0.0, canvas))
# hubs.append(hub(450, HEIGHT - 400, 43, hubs[2].rpm * hubs[2].radius / 43, un_rs, 0.0, canvas))
# hubs.append(hub(550, HEIGHT - 500, 44, hubs[3].rpm * hubs[3].radius / 44, 140, 0.0, canvas))

flo_hinges.append(flo_hinge(150, canvas))
flo_hinges.append(flo_hinge(150, canvas))
# flo_hinges.append(flo_hinge(150, canvas))
# flo_hinges.append(flo_hinge(150, canvas))

for i in range(0, len(hubs)):
    hubs[i].create_shapes()

for i in range(0, len(flo_hinges)):
    flo_hinges[i].create_shapes()

while True:
    hubs[0].update(flo_hinges[0])
    for i in range(1, len(hubs)):
        hubs[i].update(flo_hinges[i-1])

    flo_hinges[0].calc_rod_intersect(True, hubs[0], hubs[1])
    for i in range(1, len(flo_hinges)):
        flo_hinges[i].calc_rod_intersect(False, flo_hinges[i-1], hubs[i+1])

    for i in range(0, len(flo_hinges)-1):
        flo_hinges[i].update(flo_hinges[i+1])
    flo_hinges[-1].update(None)

    window.update()
    time.sleep(UPD_TIME)

window.mainloop()
