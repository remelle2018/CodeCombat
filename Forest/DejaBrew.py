#http://codecombat.com/play/level/deja-brew
# You can add strings together, and add numbers into strings.
# Sing along, using string concatenation:
# X potions of health on the wall!
# X potions of health!
# Take Y down, pass it around!
# X-Y potions of health on the wall.

potionsOnTheWall = 10
numToTakeDown = 1
while True:
    self.say(potionsOnTheWall + " potions of health on the wall!")
    # Sing the next line:
    self.say(potionsOnTheWall + " potions of health!")
    # Sing the next line:
    self.say("Take 1 down, pass it around!")
    potionsOnTheWall -= numToTakeDown
    # Sing the last line:
    self.say(potionsOnTheWall + " potions of health on the wall!")