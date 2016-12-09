with open('./input.txt') as f:
	instr = f.read()
# instr = """rect 3x2
# rotate column x=1 by 1
# rotate row y=0 by 4 
# rotate column x=1 by 1
# """

instr = instr.split('\n')[:-1]

width, height = 50, 6
# width, height = 7, 3
screen = [[[0] for x in range(width)]\
		 	   for y in range(height)]

def rect(A,B):
	for r in range(B):
		for c in range(A):
			screen[r][c] = 1

def rect_handler(rest_inst):
	nos = rest_inst[0].split("x")
	nos = [int(n) for n in nos]
	rect(*nos)

def rotate_row(A,B):
	new_row = [screen[A][(c - B) % width] for c in range(width)]
	screen[A] = new_row

def rotate_col(A,B):
	new_col = [screen[(r-B)%height][A] for r in range(height)]
	for r in range(height):
		screen[r][A] = new_col[r]

row_col = {'row':rotate_row, 'column':rotate_col}

def rotate_handler(rest_inst):
	rc = int(rest_inst[1].split('=')[1]) # row/col no
	by = int(rest_inst[3]) # how much
	#rest_inst[0] # row or col
	row_col[rest_inst[0]](rc,by)

instr_passer = {'rect':rect_handler, 'rotate':rotate_handler}

def print_screen():
	for r in range(height):
		print(''.join(['.' if screen[r][c]==[0] else '#' for c in range(width)]))
	print()

def total_lit():
	return sum(0 if screen[r][c]==[0] else 1 for c in range(width) for r in range(height))


for inst in instr:
	inst.strip()
	inst_list = inst.split(" ")
	instr_passer[inst_list[0]](inst_list[1:])
	# print_screen()

print('part 1:',total_lit())


