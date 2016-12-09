with open('./input.txt') as f:
	instr = f.read()
instr = instr.split('\n')[:-1]

# for inst in instr:
# 	print(inst)

# width, height = 50, 6
width, height = 7, 3
screen = [[[0] for x in range(width)]\
		 	   for y in range(height)]

def rect(A,B):
	for r in range(B):
		for c in range(A):
			screen[r][c] = 1

def rotate_row(A,B):
	new_row = [screen[A][(c - B) % width] for c in range(width)]
	screen[A] = new_row

def rotate_col(A,B):
	new_col = [screen[(r-B)%height][A] for r in range(height)]
	for r in range(height):
		screen[r][A] = new_col[r]

def print_screen():
	for r in range(height):
		print(''.join(['.' if screen[r][c]==[0] else '#' for c in range(width)]))
	print()

def total_lit():
	return sum(0 if screen[r][c]==[0] else 1 for c in range(width) for r in range(height))

# rect(3,2)
# print_screen()

# rotate_col(1,1)
# print_screen()

# rotate_row(0,4)
# print_screen()

# rotate_col(1,1)
# print_screen()

# print(total_lit())

inst = instr[0]
print(inst)
inst_list = inst.split(" ")
'rect': lambda l: 