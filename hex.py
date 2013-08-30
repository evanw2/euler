#!/usr/bin/env python

#Not a solution to any problem, but might be a starting point towards doing something
#  on problem 351 -- Hexagonal orchards

def print_hex(n):
   #print ascending
   space = n
   star = n-1
   for i in range(1, n+1):
      space -= 1
      star += 1
      print " "*space + "* "*star
   #descending
   for i in range(1, n):
      space += 1
      star -= 1
      print " "*space + "* "*star

def print_hex2(n):
   #print ascending
   space = n
   star = n
   for i in range(1, n+1):
      space += 1
      print " "*space + "* "*star


def hex_grid(n):
   void = "-"
   op = "*"
   rows = 2*n+1
   board = []
   for i in range(rows):
      row = []
      for i in range(rows):
         row.append(op)
      board.append(row)
   #clear edges
   for i in range(rows):
      board[0][i] = void
      board[rows-1][i] = void
      board[i][0] = void
      board[i][rows - 1] = void
   #trim top left corner
   r = 1
   c = 1
   cl = n-1
   for i in range(n-1):
      for i in range(cl):
         board[r][c] = void
         board[rows-1 - r][rows-1 - c] = void
         c += 1
      c = 1
      r += 1
      cl -= 1
   return board

def print_brd(brd):
   sp = ""
   for row in brd:
      print sp,
      for item in row:
         print str(item),
      print ""
      sp += " "

#def random_walk(brd):
   #x = len(brd) / 2
   #y = len(


   
print_brd(hex_grid(5))


