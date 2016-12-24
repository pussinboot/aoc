with open('./input.txt') as f:
	instr = f.read()
	instr = instr.strip()

test_inp = ['ADVENT',
'A(1x5)BC',
'(3x3)XYZ',
'A(2x2)BCD(2x2)EFG',
'(6x1)(1x3)A',
'X(8x2)(3x3)ABCY',]

test_outp = [
'ADVENT',
'ABBBBBC',
'XYZXYZXYZ',
'ABCBCDEFEFG',
'(1x3)A',
'X(3x3)ABC(3x3)ABCY',
]

def parse_instr(s):
	i = s.find('x')
	return int(s[:i]), int(s[i+1:])

def decompress(s):
	i = 0
	fin_len = len(s)
	tor = ['']*fin_len
	while i < fin_len:
		if s[i] == '(':
			end = s[i:].find(')')
			next_i, dup_count = parse_instr(s[i+1:end+i])
			# perform duplication
			tor[i] = s[end+i+1:end+i+1+next_i]*(dup_count)
			# continue
			i = i + end + next_i + 1
		else:
			tor[i] = s[i]
			i += 1
	return ''.join(tor).strip()

def len_sub(s):
	# print(s)
	if '(' in s and ')' in s:
		a = s.find('(')
		b = s.find(')')
		next_i, dup_count = parse_instr(s[a+1:b])
		return a + dup_count * len_sub(s[b+1:b+1+next_i]) + len_sub(s[b+1+next_i:])
	else:
		return len(s)


# for i in range(len(test_inp)):
# 	t = decompress(test_inp[i])
# 	print(t, t==test_outp[i])

print('part 1:',len(decompress(instr)))

# print(len_sub('X(8x2)(3x3)ABCY'))
# print(len_sub('(27x12)(20x12)(13x14)(7x10)(1x12)A'))
print('part 2:',len_sub(instr))