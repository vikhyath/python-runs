def process(op, num1, num2):
	if op == '+':
		return num1 + num2

	if op == '-':
		return num2 - num1

	if op == '*':
		return num1 * num2

	if op == '/':
		return num2/num1

def compute(string):
	opstack = []
	numstack = []
	numtobe = ''
	num = False
	op = False
	for idx, char in enumerate(string):
		if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '/', '*', '(', ')']:
			continue

		if char in list(map(lambda y: str(y), range(0, 10))):
			numtobe += char
			# check if next char is also a num, if yes continue processing
			if len(string) > idx + 1 and string[idx+1] in list(map(lambda y: str(y), range(0, 10))):
				continue

			num = True
			op = False

		elif char in ['+', '-', '/', '*']:
			# if last was op, then this must be a sign for the future #
			if op == True:
				numtobe += char
				continue

			else:
				numtobe = ''

			op = True
			num = False

		else:
			numtobe = ''
			op = False
			num = False

		if len(numtobe):
			number = numtobe if len(numtobe) else char
			numtobe = ''
			numstack.append(number)
			if opstack and opstack[len(opstack) - 1] in ['*', '/']:
				num1 = numstack.pop()
				op = opstack.pop()
				num2 = numstack.pop()
				numstack.append(process(op, int(num1), int(num2)))

		if char in ['+', '-', '/', '*']:
			if char == '+' or char == '-':
				if len(opstack) and (opstack[len(opstack) - 1] == '*' \
					or opstack[len(opstack) - 1] == '/'):
					num1 = numstack.pop()
					num2 = numstack.pop()
					op = opstack.pop()
					numstack.append(process(op, int(num1), int(num2)))

			opstack.append(char)

		if char == '(':
			opstack.append(char)

		if char == ')':
			substr = ''
			while (opstack[len(opstack) - 1] != '('):
				num1 = numstack.pop()
				op = opstack.pop()
				substr = op + str(num1) + substr

			lastnum = numstack.pop()
			substr = str(lastnum) + substr
			val = compute(substr)
			opstack.pop()
			numstack.append(val)

	while(len(opstack)):
		num1 = numstack.pop(0)
		num2 = numstack.pop(0)
		op = opstack.pop(0)
		numstack.insert(0, process(op, int(num2), int(num1)))

	return(numstack[0])

print(compute("2+3-1*(5+2*(6-3*(9*8+(2+3-1-6))))+2"))
# print(compute("1*8+(2+3-1-6)-12"))


