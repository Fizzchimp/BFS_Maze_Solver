from Lqueue import *
from turtle import position
from settings import *
from window import *
import time

class PositionNode():
    def __init__(self, x, y, p):
        self.position = (x, y)
        self.parent = p
    
    def compareNode(self, node):
        if self.position == node.position:
            return True
        return False
    

class World:
    def __init__(self):
        self.window = Window(WIDTH, HEIGHT)
        self.player = None
        self.end = None


    def buildMaze(self):
        x = y =0
        for row in range(len(GRID)):
            for col in range( len(GRID[row])):
                grid_mark = GRID[row][col]
                x = LEFT + ( col * 25)
                y = TOP - (row * 25)
                

                
                if grid_mark == "#":
                    self.window.DrawWall(x + IMAGE_OFFSET, y - IMAGE_OFFSET)
                
                    
                if grid_mark == "E":
                    self.end = (x,y)
                    self.window.DrawEnd(x + IMAGE_OFFSET, y - IMAGE_OFFSET)
                
                if grid_mark == "S":
                    self.player = (x,y)
                    self.window.DrawPlayer(x + IMAGE_OFFSET,y - IMAGE_OFFSET)
                    self.stack.push(PositionNode(row, col))


    def findPath(self):
        o_nodes = LQueue(999)
        v_nodes = []
        nodePath = []
        
        node = PositionNode(self.player[0], self.player[1])
        
        o_nodes.enqueue(node)
        
        while not o_nodes.isemtpy():
            current = o_nodes.dequeue()
            v_nodes.append(current)
            x, y = current.position
            
            if current.position == self.end:
                nodePath = []
                
                while current.position != self.player:
                    x, y = current.position
                    nodePath.append(current)
                    current = current.parent
                    
                nodePath.reverse()
                return nodePath
            
            neighbours = [PositionNode(x - 1, y, current),
                          PositionNode(x, y - 1, current),
                          PositionNode(x + 1, y, current),
                          PositionNode(x, y + 1, current)]
            
            for z in neighbours:
                x, y = z.position
                
                if MAP[x][y] != "#" and z not in v_nodes and not o_nodes.search(z):
                    o_nodes.enqueue(z)
        return False

    def runWorld(self):
        self.buildMaze
        steps = self.findPath
