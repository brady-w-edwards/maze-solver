from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(50, 50, 100, 100)

    c1 = Cell(win)
    c1.has_left_wall = False
    c1.draw(100, 50, 150, 100)
    c1.draw_move(c)

    c2 = Cell(win)
    c2.has_bottom_wall = False
    c2.draw(200, 200, 250, 250)

    c3 = Cell(win)
    c3.has_top_wall = False
    c3.draw(300, 300, 350, 350)

    win.wait_for_close()

main()