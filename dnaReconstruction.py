unscrambled = ""
transition = ""
finished = False
size = 0
scrambled = open("dna.txt").read()
x=scrambled.replace("\n", " ").split(" ")
x=list(set(x))
unscrambled += x[0]
print("Test")
while not(finished):
        finished = True
        for i in range(20, 10, -1):
                for fragment in x:
                        key = unscrambled[-i:]
                        if key in fragment:
                                if not(fragment in unscrambled):
					print(len(x))
					size = 100 - i
                                        unscrambled += fragment[-size:]
                                        finished = False
					x.remove(fragment)
					break
                if not(finished):
                        break
print("Halfway there!")
finished = False
while not(finished):
        finished = True
        for i in range(20, 10, -1):
                for fragment in x:
                        key = unscrambled[0:i]
                        if key in fragment:
                                if not(fragment in unscrambled):
                                        size = 100 - i
                                        unscrambled = fragment[0:size] + unscrambled
                                        finished = False
        	                	x.remove(fragment)
					break
                if not(finished):
                        break
print("Test 2")
oppositeStrand = ""
for letter in unscrambled:
	if letter == "A":
		oppositeStrand += "T"
	elif letter == "C":
		oppositeStrand += "G"
	elif letter == "T":
		oppositeStrand += "A"
	elif letter == "G":
		oppositeStrand += "C"
print("-----RESULTS-----\n\nStrand 1:\n" + unscrambled + "\n\nStrand 2:\n" + oppositeStrand + "\n-----------------")
print(len(unscrambled))
