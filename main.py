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

hubs = []
flo_hinges = []

hubs.append(hub(60.0, HEIGHT - 60.0, 50.0, 15.0, 153.0, 0.0, canvas))
hubs.append(hub(250, HEIGHT - 100, 45, hubs[0].rpm * hubs[0].radius / 45, 143.0, 0.0, canvas))
hubs.append(hub(350, HEIGHT - 200, 30, hubs[1].rpm * hubs[1].radius / 30, 190.0, 0.0, canvas))
hubs.append(hub(450, HEIGHT - 300, 60, hubs[2].rpm * hubs[2].radius / 60, 220.0, 0.0, canvas))
hubs.append(hub(500, HEIGHT - 500, 40, hubs[3].rpm * hubs[3].radius / 40, 220.0, 0.0, canvas))

flo_hinges.append(flo_hinge(140, canvas))
flo_hinges.append(flo_hinge(190, canvas))
flo_hinges.append(flo_hinge(140, canvas))
flo_hinges.append(flo_hinge(190, canvas))

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
    flo_hinges[3].update(None)

    window.update()
    time.sleep(UPD_TIME)

window.mainloop()
