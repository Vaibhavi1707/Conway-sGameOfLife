import copy

def add(l):
	i = 0
	for i in range(0, len(l)):
		l[i].append(0)
		l[i].insert(0, 0)

	l2 = []
	length = len(l[0])
	for i in range(0, length):
		l2.append(0)

	l.append(l2)
	l.insert(0, l2)


def remove(l):
	l.pop()
	l.pop(0)
	for i in range(0, len(l)):
		l[i].pop()
		l[i].pop(0)


def check_dead(l, l1, i, j):
	count = 0
# if ( l1[i][j] == 0 ):
	m = -1
	n = -1
	for m in range( -1, 2 ):
		for n in range( -1, 2 ):
			if ( l1[i+m][j+n] == 1):
				count = count + 1
	if ( count == 3 ):
		l[i][j] = 1


	if ( j < len(l[0])-2 ):
		check_dead(l, l1, i, j+1)
	elif ( j == len(l[0])-2 and i == len(l)-2 ):
		 return True
	elif ( j == len(l[0])-2 ):
		check_dead(l, l1, i+1, 1)
	return True


def check_alive(l, l1, i, j):
	count = 0
# if ( l1[i][j] == 1):
	m = -1
	n = -1
	for m in range( -1, 2 ):
		for n in range( -1, 2 ):
			if ( l1[i+m][j+n] == 1):
				count = count + 1
	if ( count != 3 and count != 4):
		l[i][j] = 0

	if ( j < len(l[0])-2 ):
		check_alive(l, l1, i, j+1)
	elif ( j == len(l[0])-2 and i == len(l)-2 ):
		 return True
	elif ( j == len(l[0])-2 ):
		check_alive(l, l1, i+1, 1)
	return True

def main(l):
	add(l)

	l1 = copy.deepcopy(l)

	for i in range(1, len(l1)-1):
		for j in range(1, len(l1[0])-1):
			if (l1[i][j] == 0):
				check_dead( l, l1, i, j)
			elif(l1[i][j] == 1):
				check_alive( l, l1, i, j)

	remove(l)
	

	return l
#l = [[0,1,0,1,0,0,0], [0,0,1,1,0,0,0], [0,0,1,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]
# list =[]
# l = []
# for j in range(5):
# 	for i in range(7):
# 		a = input()
# 		list.append(a)
# 	l.append(list)
# 	list = []


