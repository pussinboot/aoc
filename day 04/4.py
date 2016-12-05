with open('./input.txt') as f:
	room_names = f.read()
room_names = room_names.split('\n')[:-1]

# room_names = ['aaaaa-bbb-z-y-x-123[abxyz]','a-b-c-d-e-f-g-h-987[abcde]','not-a-real-room-404[oarel]','totally-real-room-200[decoy]']

def parse_room_name(name):
	# split into letters, sector id, and checksum
	bracket = name.find('[')
	ls, checksum = name[:bracket], name[bracket+1:-1]
	last_dash = len(ls) - ls[::-1].find('-')
	letters, sector_id = ls[:last_dash], int(ls[last_dash:])
	return letters, sector_id, checksum
	# print(letters, sector_id, checksum)

def check_checksum(letters,sector_id,checksum):
	# now to check the checksum
	letter_dict = {}
	for c in letters:
		if c != '-':
			if c in letter_dict:
				letter_dict[c] += 1
			else:
				letter_dict[c] = 1

	d = list(letter_dict.items())
	d.sort(key=lambda x: x[0])
	d.sort(key=lambda x: x[1], reverse = True)

	check = ''.join([d[i][0] for i in range(5)])
	return sector_id * (check==checksum)

def parse_and_check(name):
	l,s,c = parse_room_name(name)
	return check_checksum(l,s,c)

print('part 1:',sum(map(parse_and_check,room_names)))