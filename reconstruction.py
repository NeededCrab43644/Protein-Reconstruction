unscrambled = ""
transition = ""
finished = False
size = 0
scrambled = open("puzzle2.txt").read()
x=scrambled.replace(",", "").replace("\n", " ").split(" ")
unscrambled += x[0]
while not(finished):
	finished = True
	for i in range(14, 1, -1):
		for fragment in x:
			key = unscrambled[-i:]
			if key in fragment:
				if not(fragment in unscrambled):
					size = 15 - i
					unscrambled += fragment[-size:]
					finished = False
					break
		if not(finished):
			break
print("Test")
finished = False
while not(finished):
	finished = True
	for i in range(14, 1, -1):
		for fragment in x:
			key = unscrambled[0:i]
			if key in fragment:
				if not(fragment in unscrambled):
					transition = fragment
					size = len(unscrambled) - i
					transition += unscrambled[-size:]
					unscrambled = transition
					finished = False
					break
		if not(finished):
			break
print(unscrambled)
