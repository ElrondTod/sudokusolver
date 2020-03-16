def printTable(t):
	a = ""
	for l in t:
		for n in l:
			a = a + str(n) + " "
		a = a + "\n"
	print(a)

def check(t, x, y, num):
	result = True
	for i in range(9):
		if i != x:
			result = result and t[i][y] != num
	if not result:
		return result
	for i in range(9):
		if i != y:
			result = result and t[x][i] != num
	if not result:
		return result
	i = x / 3
	j = y / 3
	for n in range(3):
		for m in range(3):
			if (i * 3 + n) != x and (j * 3 + m) != y:
				result = result and t[i * 3 + n][j * 3 + m] != num
	return result

def getPossibleNums(t, x, y):
	l = []
	for i in range(1, 10):
		if check(t, x, y, i):
			l.append(i)
	return l
	
def findNextEmptyPlace(t):
	for i in range(0, 9):
		for j in range(0, 9):
			if t[i][j] == 0:
				return (i, j)
	return (9, 9)

def solve(t, x, y):
	for k in getPossibleNums(t, x, y):
		t[x][y] = k
		a = findNextEmptyPlace(table)
		if a == (9, 9):
			return True
		if solve(t, a[0], a[1]):
			return True
	t[x][y] = 0
	return False

with open("sudoku.txt", 'r') as file:
	f = file.readlines()

table = []

for l in f:
	line = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	i = 0
	for c in l:
		if c == " " or c == "\n":
			continue
		else:
			line[i] = int(c)
			i = i + 1 
	table.append(line)
	
a = findNextEmptyPlace(table)

printTable(table)

if a == (9, 9):
	print("A sudoku meg van oldva")
else:
	if solve(table, a[0], a[1]):
		printTable(table)
	else:
		print("Nincs megoldas")