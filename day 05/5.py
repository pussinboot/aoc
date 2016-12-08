from hashlib import md5

puz_in = 'wtnhxymk'
# puz_in = 'abc'

count = 0
output = []
output_ordered = ['_']*8

while '_' in output_ordered:
	to_hash = '{}{}'.format(puz_in,count)
	
	ret_hash = md5(to_hash.encode()).hexdigest()
	if ret_hash[:5] == '00000':
		output.append(ret_hash[5])
		try:
			ind = int(ret_hash[5])
			if output_ordered[ind] == '_':
				output_ordered[ind] = ret_hash[6]
				print(''.join(output_ordered))
		except:
			pass
	count += 1
	
print('part 1:',''.join(output[:8]))	
print('part 2:',''.join(output_ordered))
