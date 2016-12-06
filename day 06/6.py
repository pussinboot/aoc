with open('./input.txt') as f:
	message = f.read()
# message = """eedadn
# drvtee
# eandsr
# raavrd
# atevrs
# tsrnev
# sdttsa
# rasrtv
# nssdts
# ntnada
# svetve
# tesnvt
# vntsnd
# vrdear
# dvrsen
# enarar
# """
messages = message.split('\n')[:-1]
decoder = [{} for _ in range(len(messages[0]))]

for message in messages:
	for i,c in enumerate(message):
		if c in decoder[i]:
			decoder[i][c] += 1
		else:
			decoder[i][c] = 1

d_sorted = [list(d.items()) for d in decoder]

for i in range(len(d_sorted)):
	d_sorted[i].sort(key=lambda x: x[1],reverse=True)

p1_ans = [d[0][0] for d in d_sorted]
p2_ans = [d[-1][0] for d in d_sorted]
print('part 1:',''.join(p1_ans))
print('part 2:',''.join(p2_ans))