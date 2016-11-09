from __future__ import print_function

#grid = [0] * 81
size = 9
grid = [[0 for x in range(size)] for y in range(size)]
grid[0] = [9,3,0,6,0,5,8,0,1]
grid[1] = [5,0,0,0,0,0,0,0,7]
grid[2] = [0,0,0,0,0,8,4,0,3]
grid[3] = [0,5,8,0,6,3,2,0,0]
grid[4] = [0,0,3,0,4,0,1,0,0]
grid[5] = [0,0,7,8,1,0,3,6,0]
grid[6] = [7,0,6,2,0,0,0,0,0]
grid[7] = [3,0,0,0,0,0,0,0,6]
grid[8] = [8,0,9,4,0,6,0,3,2]

#prints out the grid
def printGrid():
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			print ("%d " % grid[i][j], end="")
			if(j%3 == 2):
				print ("  ", end="")
		print ("", end="\n")
		if(i%3 == 2):
			print ("", end="\n")

#inserts a number at a certain row and column. Example insertNumber(1,1,1)
#will insert then number 1 in the top left
def insertNumber(num, row, col):
	grid[row][col] = num
	return

#will check if a certain row is valid (ie. does it contain 1-9)
def validRow(row):
	valid = [False] * 9
	for index in range(len(grid[0])):
		valid[grid[row][index]-1] = True
	for index in range(len(valid)):
		if valid[index] == False:
			return False
	return True

#will check if a certain column is valid (ie. does it contain 1-9)
def validCol(col):
	valid = [False] * 9
	for index in range(len(grid)):
		valid[grid[index][col]-1] = True
	for index in range(len(valid)):
		if valid[index] == False:
			return False
	return True

#will check if a certain box is valid (ie. does it contain 1-9)
#box is specified via coordinate. 1,1 is the top left box,
#1,2 is the top middle box etc...
def validBox(boxR, boxC):
	valid = [False] * 9
	for i in range(len(grid)/3):
		for j in range(len(grid[0])/3):
			valid[grid[boxR+i][boxC+j]-1] = True
	for index in range(len(valid)):
		if valid[index] == False:
			return False
	return True

def getValidNumbers(row, col):
	if(grid[row][col] == 0):
		valid = [True] * 9
		for index in range(len(grid[0])):
			valid[grid[row][index]-1] = False
		for index in range(len(grid)):
			valid[grid[index][col]-1] = False
		for i in range(len(grid)/3):
			for j in range(len(grid[0])/3):
				valid[grid[(row/3 - 1)+i][(col/3 - 1)+j]-1] = False
		return valid
	return None

def getAnswer(row, col):
	v = getValidNumbers(row, col)
	p = 0
	ans = 0
	if(v == None):
		return grid[row][col]
	for index in range(len(v)):
		if(v[index]):
			p += 1
			ans = index+1
	if (p==1):
		return ans
	return 0

def fillNumbers():
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			grid[i][j] = getAnswer(i,j) 

#just testing and adding some random numbers and printing grid
# insertNumber(1, 1, 1)
# insertNumber(2, 2, 1)
# insertNumber(3, 3, 1)
# insertNumber(4, 1, 2)
# insertNumber(5, 2, 2)
# insertNumber(6, 3, 2)
# insertNumber(7, 1, 3)
# insertNumber(8, 2, 3)
# insertNumber(9, 3, 3)

printGrid()
# v = getValidNumbers(0,2)
# print(v, end="\n")
# print(getAnswer(0,2), end="\n")
print("---------------------", end="\n\n")
fillNumbers()
printGrid()