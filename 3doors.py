import random

def Door_generator():
	Doors = []
	for i in range(3):
		if i == 2 and not 1 in Doors:
			Doors.append(1)		
		elif not 1 in Doors:
			Doors.append(random.randrange(0,2))
		else:
			Doors.append(0)
	return Doors

def First_selection():
	selection = random.randrange(0,3)
	return selection

def Open_door():
	your_door = 0
	other_door = 0
	for i in range(10000):
		Doors = Door_generator()
		selection = First_selection()
		for x in range(100):
			i = random.randrange(0,3)
			if 2 in Doors:
				pass
			elif Doors[i] != 1 and i != selection:
				Doors[i] = 2
		winning_door = Doors.index(1)
		if winning_door == selection:
			your_door += 1
		else:
			other_door += 1
	x = float(other_door) / (float(your_door) + float(other_door))
	print "You win by changing your selection {:.2%} percent of the time".format(x)
