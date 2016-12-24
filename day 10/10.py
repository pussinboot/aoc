with open('./input.txt') as f:
	instr = f.read()
instructions = instr.split('\n')[:-1]

bots = {}
outputs = {}

def check_bot_action_possible(bot_no):
	if bot_no in bots:
		if not None in bots[bot_no]:
			return True
	return False

def give_bot_val(bot_no,value):
	if bots[bot_no][0] is None:
		bots[bot_no][0] = value
	else:
		bots[bot_no][1] = value

def do_bot_instr(bot_instr):
	bb = bot_instr.split(' ')
	bot_nos = [bb[1],bb[6],bb[11]]
	# check that the bots exist.. make them if not
	for bn in bot_nos:
		if bn not in bots:
			bots[bn] = [None, None]
	if check_bot_action_possible(bot_nos[0]):
		low, high = min(bots[bot_nos[0]]),max(bots[bot_nos[0]])
		if bb[5] == 'bot':
			give_bot_val(bot_nos[1],low)
		else:
			outputs[bot_nos[1]] = low
		if bb[10] == 'bot':
			give_bot_val(bot_nos[2],high)
		else:
			outputs[bot_nos[2]] = high
		bots[bot_nos[0]] = [None, None]
	else:
		return bot_instr

def do_value_instr(val_instr):
	vv = val_instr.split(" ")
	if vv[-1] in bots:
		give_bot_val(vv[-1],int(vv[1]))
		return
	else:
		return val_instr

def do_instruction(inst):
	if inst[:3] == 'bot':
		return do_bot_instr(inst)
	else:
		return do_value_instr(inst)
	# returns inst if not possible
	return inst
found_p1 = False
while len(instructions) > 0:
	instruction = instructions.pop(0)
	# process instruction
	res = do_instruction(instruction)
	# if cant, put it back on end
	if res is not None:
		instructions.append(res)
	if not found_p1:
		for b in bots:
			if bots[b] == [61,17] or bots[b] == [17,61]:
				print('part 1:',b)
				found_p1 = True

print('part 2:', outputs['0'] * outputs['1'] * outputs['2'])