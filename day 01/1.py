with open('./input.txt') as f:
	dirs = f.read()
# dirs = 'R8, R4, R4, R8 '

dirs = dirs.split(', ')
dirs[-1] = dirs[-1][:-1] # get rid of newline
# print(dirs)

# n, e, s, w
face_directions = [(0, 1),(1, 0),(0, -1),(-1, 0)]

def parse_direction(direction):
	turn = direction[0]
	how_far = int(direction[1:])
	return turn, how_far

def change_dir(cur_dir, lr):
	# clockwise
	diff = 1
	# counterclockwise
	if lr == 'L': diff = -1
	return (cur_dir + diff) % 4

def add_step(last_loc, direction, step_size):
	e = last_loc[0] + direction[0] * step_size
	n = last_loc[1] + direction[1] * step_size
	return (e,n)

### part 2

def check_intersect(a,b,c,d):
	# checks if two line segments interesect
	# the lines are defined by points a&b, c&d
	denom = (a[0]-b[0])*(c[1]-d[1]) - (a[1]-b[1])*(c[0]-d[0])
	if denom == 0: return # parallel or collinear
	x_coord = ((a[0]*b[1] - a[1]*b[0])*(c[0]-d[0]) + \
	- (a[0]-b[0])*(c[0]*d[1] - c[1]*d[0]))/denom
	y_coord = ((a[0]*b[1] - a[1]*b[0])*(c[1]-d[1]) + \
	- (a[1]-b[1])*(c[0]*d[1] - c[1]*d[0]))/denom
	if (min(a[0],b[0]) <= x_coord <= max(a[0],b[0])) and \
	   (min(a[1],b[1]) <= y_coord <= max(a[1],b[1])) and \
	   (min(c[0],d[0]) <= x_coord <= max(c[0],d[0])) and \
	   (min(c[1],d[1]) <= y_coord <= max(c[1],d[1])):
		return (x_coord,y_coord)

facing = 0
visited = [(0,0)]
p2_sol = 0
for d in dirs:
	last_location = visited[-1]
	t, h = parse_direction(d)
	facing = change_dir(facing,t)
	new_location = add_step(last_location,face_directions[facing],h)
	visited.append(new_location)
	for a,b in zip(visited[:-2],visited[1:-2]):
		intersect = check_intersect(a,b,visited[-2],visited[-1])
		if intersect is not None:
			if p2_sol == 0:
				p2_sol = int(abs(intersect[0]) + abs(intersect[1]))

print('part 1:',abs(visited[-1][0])+abs(visited[-1][1])) #271...z
print('part 2:',p2_sol)