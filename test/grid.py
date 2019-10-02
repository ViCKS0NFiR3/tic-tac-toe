import pygame

img_O = pygame.image.load('C:\\Users\\apollo\\Documents\\Alpha and Omega\\pygame\\tic-tac-toe-master\\O.png')
img_O = pygame.transform.scale(img_O,(200,200))
img_X = pygame.image.load('C:\\Users\\apollo\\Documents\\Alpha and Omega\\pygame\\tic-tac-toe-master\\X.png')
img_X = pygame.transform.scale(img_X,(200,200))
class Grid:
    def __init__(self):
        self.grid_lines = [((0,200), (600,200)), ((0,400), (600,400)), ((200,0), (200,600)), ((400,0), (400,600))]
        self.grid = [[0 for x in range(3)] for y in range(3)]
        self.switch_player = True
        # search directions     N      NW       W      SW    S    SE     E    NE
        self.search_dirs = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
        self.game_over = False

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
            self.check_grid(x,y,player)
        else:
            self.switch_player = False

    def print_grid(self):
        for row in self.grid:
            print(row)
    
    def is_within_bounds(self,x,y):
        return x >= 0 and x < 3 and y >= 0 and y < 3

    def check_grid(self,x,y,player):
        count = 1
        for index, (dirx, diry) in enumerate(self.search_dirs):
            if self.is_within_bounds(x+dirx, y+diry) and self.get_cell_value(x+dirx,y+diry) == player:
                count += 1
                print(count)
                xx = x + dirx
                yy = y + diry
                if self.is_within_bounds(xx+dirx,yy+diry) and self.get_cell_value(xx+dirx,yy+diry) == player:
                    count += 1
                    if count == 3:
                        break
                if count < 3:
                    new_dir = 0 
                    # mapping the indeces to opposite direction: 0-4 1-5 2-6 3-7 4-0 5-1 6-2 7-3
                    if index == 0:
                        new_dir = self.search_dirs[4]
                    elif index == 1:
                        new_dir = self.search_dirs[5]
                    elif index == 2:
                        new_dir = self.search_dirs[6]
                    elif index == 3:
                        new_dir = self.search_dirs[7]
                    elif index == 4:
                        new_dir = self.search_dirs[0]
                    elif index == 5:
                        new_dir = self.search_dirs[1]
                    elif index == 6:
                        new_dir = self.search_dirs[2]
                    elif index == 7:
                        new_dir = self.search_dirs[3]

                    if self.is_within_bounds(x + new_dir[0], y + new_dir[1]) and self.get_cell_value(x + new_dir[0], y + new_dir[1]) == player:
                        count += 1
                        if count == 3:
                            break

                    else:
                        count = 1
        if count == 3:
            print(player, 'wins!')
            self.game_over = True

        else:
            self.game_over = self.is_grid_full()


    def is_grid_full(self):
        for row in self.grid:
            for value in row:
                if value == 0:
                    return False
                else:
                    return True

    def clear_grid(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                self.set_cell_value(x,y,0)