from tkinter import *
from time import sleep
import random
from turtle import heading
 
class Field:
    def __init__(self, c, n, m, width, height):
        '''
       c - canvas instance
       n - number of rows
       m - number of columns
       width - width of game field in pixels
       height - width of game field in pixels'''
        self.c = c
        self.a = []
        self.n = n + 2
        self.m = m + 2
        self.width = width
        self.height = height
        self.count = 0
        for i in range(self.n):
            self.a.append([])
            for j in range(self.m):
                #creating borders
                if i == 0 or i == 1 or i == 2 or i == 3 or i == self.n - 2  or i == self.n - 3 or i == self.n - 4 or j == 0 or j == 1 or j == 2 or j == 3 or j == self.m - 2 or j == self.m - 3 or j == self.m - 4  or j == self.m or i == self.n:
                    self.a[i].append(2)
                # self.a[i].append(choice([0, 1]))
                elif i == self.n / 2 and j == self.m / 2:
                    self.a[i].append(3)
                elif  ((i == (self.n / 2 - 1) or i == (self.n / 2 + 1)) and (j == self.m / 2)) or ((i == self.n / 2) and (j == (self.m / 2 - 1) or j == (self.m / 2 + 1))):
                    self.a[i].append(4)
                else:
                    self.a[i].append(random.randrange(0,  2))
        
        self.draw()
   
    def step(self):
        b = []
        for i in range(self.n):
            b.append([])
            for j in range(self.m):
                    b[i].append(0)
       
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                neib_sum = self.a[i - 1][j - 1] + self.a[i - 1][j] + self.a[i - 1][j + 1] + self.a[i][j - 1] + self.a[i - 1][j + 1] + self.a[i + 1][j - 1] + self.a[i + 1][j] + self.a[i + 1][j + 1]
                if self.a[i][j] == 2:
                    b[i][j] = 2
                elif self.a[i][j] == 3:
                    b[i][j] = 3
                elif self.a[i][j] == 4:
                    b[i][j] = 4
                elif neib_sum < 2 or neib_sum > 3:
                    b[i][j] = 0
                elif neib_sum == 3 or neib_sum == 2:
                    b[i][j] = 1
                else:
                    b[i][j] = self.a[i][j]
       
        self.a = b
 
 
    def print_field(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.a[i][j], end="")
            print()
 
    def draw(self):
        '''
       draw each element of matrix as a rectangle with white background and wall rectangle should have dark grey background
       '''
        color = "grey"
        sizen = self.width // (self.n - 2)
        sizem = self.height // (self.m - 2)
        for i in range(self.n):
            for j in range(self.m):
                if (self.a[i][j] == 2):
                    color = "grey"
                elif (self.a[i][j] == 3):
                    color = 'yellow'
                elif (self.a[i][j] == 4):
                    color = 'red'
                elif (self.a[i][j] == 1):
                    color = "green"
                else:
                    color = "black"
                self.c.create_rectangle((i-1) * sizen, (j-1) * sizem, (i) * sizen, (j) * sizem, fill=color)
        self.step()
        self.c.after(500, self.draw)
 

 
try:
    root = Tk()
    root.geometry("700x700")
    c = Canvas(root, width=700, height=700)
    c.pack()
    f = Field(c, 40, 40, 700, 700)
    f.print_field()
 
except:
	print('''Your PC cannnot open the file !!!
     Use another''')
 

root.mainloop()
