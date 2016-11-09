from __future__ import print_function

grid = [0] * 81

#prints out the grid
def printGrid():
	for index in range(len(grid)):
		print ("%d " % grid[index], end="")
		if(index%3 == 2):
			print ("  ", end="")
		if(index%9 == 8):
			print ("", end="\n")
		if(index%27 == 26):
			print ("", end="\n")

#inserts a number at a certain row and column. Example insertNumber(1,1,1)
#will insert then number 1 in the top left
def insertNumber(num, row, col):
	position = (row-1)*9 + (col-1)
	grid[position] = num
	return

#will check if a certain row is valid (ie. does it contain 1-9)
def validRow(row):
	valid = [False] * 9
	position = (row-1)*9
	for index in range(9):
		valid[grid[position + index]-1] = True
	for index in range(len(valid)):
		if valid[index] == False:
			return False
	return True

#will check if a certain column is valid (ie. does it contain 1-9)
def validCol(col):
	valid = [False] * 9
	position = col-1
	for index in range(9):
		valid[grid[position + (index-1)*9]-1] = True
	for index in range(len(valid)):
		if valid[index] == False:
			return False
	return True

#will check if a certain box is valid (ie. does it contain 1-9)
#box is specified via coordinate. 1,1 is the top left box,
#1,2 is the top middle box etc...
def validBox(boxR, boxC):
	valid = [False] * 9
	position = (boxR-1) * 27 + (boxC-1) * 3
	boxIter = [0, 1, 2, 9, 10, 11, 18, 19, 20]
	for index in range(len(boxIter)):
		valid[grid[position + boxIter[index]]-1] = True
	for index in range(len(valid)):
		if valid[index] == False:
			return False
	return True

#just testing and adding some random numbers and printing grid
insertNumber(1, 1, 1)
insertNumber(2, 2, 1)
insertNumber(3, 3, 1)
insertNumber(4, 1, 2)
insertNumber(5, 2, 2)
insertNumber(6, 3, 2)
insertNumber(7, 1, 3)
insertNumber(8, 2, 3)
insertNumber(9, 3, 3)

printGrid()
print (validBox(1, 1), end="\n")