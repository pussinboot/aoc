with open('./input.txt') as f:
	ip_addr = f.read()
# ip_addr = """abba[mnop]qrst
# abcd[bddb]xyyx
# aaaa[qwer]tyui
# ioxxoj[asdfgh]zxcvbn
# """
# ip_addr = """aba[bab]xyz
# xyx[xyx]xyx
# aaa[kek]eke
# zazbz[bzb]cdb
# """
ip_addr = ip_addr.split('\n')[:-1]

def find_all(s, ch):
	return [i for i, ltr in enumerate(s) if ltr == ch]

flatten = lambda l: [item for sublist in l for item in sublist]

def split_addr(ip):
	lb, rb = find_all(ip,'['), find_all(ip,']')
	# returns outside brackets, inside brackets
	return [ip[l+1:r] for l,r in zip([-1]+rb,lb+[len(ip)])],\
		   [ip[l+1:r] for l,r in zip(lb,rb)]

def check_abba(sub_ip):
	return any(a==d and b==c and a!=b for a,b,c,d in \
	 	 zip(sub_ip,sub_ip[1:],sub_ip[2:], sub_ip[3:]))

def check_aba(sub_ip):
	return [''.join([a,b,c]) for a,b,c in \
	 	   zip(sub_ip,sub_ip[1:],sub_ip[2:])\
	 	   if a==c and a!=b]

def flip_aba(aba):
	return ''.join([aba[1],aba[0],aba[1]])

count_tls = 0
count_ssl = 0

for ip in ip_addr:
	outs, ins = split_addr(ip)
	if all(check_abba(inn) == False for inn in ins):
		if any(check_abba(out) for out in outs):
			count_tls += 1
	# part 2
	outer_abas = flatten([check_aba(out) for out in outs])
	inner_abas = flatten([check_aba(inn) for inn in ins])
	if any(flip_aba(inner) in outer_abas for inner in inner_abas):
		count_ssl += 1

print('part 1:',count_tls)
print('part 2:',count_ssl)
