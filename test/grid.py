import pygame

img_O = pygame.image.load('C:\\Users\\51^7\\Pictures\\pygame\\O.png')
img_O = pygame.transform.scale(img_O,(200,200))
img_X = pygame.image.load('C:\\Users\\51^7\\Pictures\\pygame\\X.png')
img_X = pygame.transform.scale(img_X,(200,200))
class Grid:
    def __init__(self):
        self.grid_lines = [((0,200), (600,200)), ((0,400), (600,400)), ((200,0), (200,600)), ((400,0), (400,600))]
        self.grid = [[0 for x in range(3)] for y in range(3)]
        self.switch_player = True

    def draw(self,surface):
        for line in self.grid_lines:
            pygame.draw.line(surface, (200,200,200), line[0], line[1], 2)

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell_value(x,y) == "X":
                    surface.blit(img_X,(x*200,y*200))
                if self.get_cell_value(x,y) == "O":
                    surface.blit(img_O,(x*200,y*200 ))

    def get_cell_value(self,x,y):
        return self.grid[y][x]
     
    def set_cell_value(self,x,y,value):
        self.grid[y][x] = value
    
    def get_mouse(self,x,y,player):
        if self.get_cell_value(x,y) == 0:
            self.switch_player = True
            if player == "X":
                self.set_cell_value(x,y,"X")
            elif player == "O":
                self.set_cell_value(x,y,"O")
        else:
            self.switch_player = False

    def print_grid(self):
        for row in self.grid:
            print(row)

