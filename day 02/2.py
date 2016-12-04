with open('./input.txt') as f:
	dirs = f.read()

# testing

# dirs = """ULL
# RRDDD
# LURDL
# UUUUD
# """

dirs = dirs.split('\n')[:-1]
# print(dirs)

keypad = [[1,2,3],[4,5,6],[7,8,9]]
# print(keypad[1][2])

move_dict = {
	'U':( -1,  0 ),
	'D':(  1,  0 ),
	'L':(  0, -1 ),
	'R':(  0,  1 )
}

def perform_move(char,r,c):
	this_move = move_dict[char]
	r = max(0,min(2,r+this_move[0]))
	c = max(0,min(2,c+this_move[1]))
	return r,c

r,c = 1,1
tor = []
for d in dirs:
	for char in d:
		r,c = perform_move(char,r,c)
	tor.append(keypad[r][c])

print('part 1:', ''.join([str(t) for t in tor]))

zzz = None
true_keypad = [[zzz, zzz, '1', zzz, zzz],
			   [zzz, '2', '3', '4', zzz],
			   ['5', '6', '7', '8', '9'],
			   [zzz, 'A', 'B', 'C', zzz],
			   [zzz, zzz, 'D', zzz, zzz]]

def true_move(char,r,c):
	this_move = move_dict[char]
	# lazy soln would be to just check if new move is none
	# in which case don't actually update..
	r = max(abs(2-c),min(4-abs(2-c),r+this_move[0]))
	c = max(abs(2-r),min(4-abs(2-r),c+this_move[1]))
	return r,c

r,c = 2,0
tor = []
for d in dirs:
	for char in d:
		r,c = true_move(char,r,c)	
	tor.append(true_keypad[r][c])
print('part 2:', ''.join(tor))
# r,c = 2,0
# for char in 'RRDDD':
# 	r,c = true_move(char,r,c)
# 	print(true_keypad[r][c])