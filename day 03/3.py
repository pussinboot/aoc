with open('./input.txt') as f:
	triangles = f.read()
triangles = triangles.split('\n')[:-1]

def possible(lens):
	m = max(lens)
	return sum(lens) - m > m

total_count = 0
store_lens = [0]*len(triangles)
for i,t in enumerate(triangles):
	lens = [int(l) for l in t.split(" ") if len(l) > 0]
	store_lens[i] = lens
	total_count += possible(lens)

print('part 1:',total_count)

total_count = 0
for i in range(0,len(triangles),3):
	cols = [[row[j] for row in store_lens[i:i+3]] for j in range(3)]
	total_count += sum([possible(col) for col in cols])

print('part 2:',total_count)
