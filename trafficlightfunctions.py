from graphics import*

win = GraphWin("Stoplights", 200, 200)

def draw_traffic_light(x, y):
    draw_light_body(50, 20, 155, 125)
    draw_lamp("red", 87, 45, 20)
    draw_lamp("yellow", 87, 87, 20)
    draw_lamp("green", 87, 129, 20)

def draw_lamp(color, x, y, radius):
    l = Circle(Point(x, y), radius)
    l.setOutline("black")
    l.setFill(color)
    l.draw(win)

def draw_light_body(x, y, length, width):
    b = Rectangle(Point(x,y), Point(width, length))
    b.setOutline("black")
    b.setFill("white")
    b.draw(win)

draw_traffic_light(100,100)
