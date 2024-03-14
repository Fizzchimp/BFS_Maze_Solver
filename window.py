import turtle

class Window:
    def __init__(self, width, height):
        self.screen = turtle.Screen()
        self.screen.title("Maze Solved using a Stack")
        self.screen.bgcolor("#008080")
        self.screen.setup(width, height)
        self.screen.tracer(0)
        
        self.line = turtle.Turtle()
        self.line.color("#000000")
        self.line.penup()
        self.line.hideturtle()
        
        # create a turtle for drawing static objects in our maze
        self.image = turtle.Turtle()
        self.image.shape("square")                       
        self.image.penup()                    
        self.image.speed(0)
        
        
        # create a turtle object for drawing the player (which will move)
        self.playerImage = turtle.Turtle()
        self.playerImage.penup()
        self.playerImage.color("#FFAAFF") 
        self.playerImage.shape("square")
        
    def DrawWall(self, x, y):
        self.image.color("white") 
        self.image.goto(x, y)
        self.image.stamp()
        
    def DrawEnd(self, x, y):
        self.image.color("#FF0000") 
        self.image.goto(x, y)
        self.image.stamp()    
        
    def DrawPlayer(self, x, y):
        self.playerImage.goto(x, y)
        
    def DrawLine(self, x, y):
        self.line.pendown()        
        self.line.goto(x, y)