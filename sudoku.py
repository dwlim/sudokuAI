from __future__ import print_function

#grid = [0] * 81
size = 9
grid = [[0 for x in range(size)] for y in range(size)]
grid[0] = [0,7,6,1,0,0,0,9,0]
grid[1] = [4,1,8,0,9,0,0,0,0]
grid[2] = [0,3,0,5,0,4,0,0,1]
grid[3] = [0,6,1,2,0,0,0,0,4]
grid[4] = [3,0,0,0,0,0,0,0,2]
grid[5] = [2,0,0,0,0,6,8,3,0]
grid[6] = [1,0,0,3,0,8,0,4,0]
grid[7] = [0,0,0,0,6,0,2,5,8]
grid[8] = [0,8,0,0,0,7,3,1,0]

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
			loc = grid[row][index] - 1
			if (loc != -1):
				valid[loc] = False
		for index in range(len(grid)):
			loc = grid[index][col] - 1
			if (loc != -1):
				valid[loc] = False
		for i in range(3):
			for j in range(3):
				loc = grid[(row/3)*3+i][(col/3)*3+j] - 1
				if (loc != -1):
					valid[loc] = False
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

def filled():
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if (grid[i][j] == 0):
				return False
	return True
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
print("---------------------", end="\n")
print(" Generating answer...", end="\n")

while(not filled()):
	fillNumbers()

print("---------------------", end="\n")
printGrid()

# v = getValidNumbers(2,0)
# print(v, end="\n")
# print(getAnswer(2,0), end="\n")