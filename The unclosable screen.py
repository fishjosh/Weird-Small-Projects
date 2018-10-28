from graphics import *
def unclosable():
    x=0
    win = GraphWin("UNCLOSABLE SCREEN",400,400)
    pt = Point(-1,20)
    pt.draw(win)
    while x==0:
        win.getMouse()
    win.close()
unclosable()
    