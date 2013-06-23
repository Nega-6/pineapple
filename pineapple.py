import sys

class StoryPiece:
    def __init__(self, text):
        self.text = text
        self.choices = []

    def add_choice(self, choice):
        self.choices.append(choice)

    def run(self):
        print self.text

        while True:
            data = sys.stdin.readline().rstrip()
            for choice in self.choices:
                if data == choice.command:
                    return choice.destination
            print "Nothing happened."
            

class Choice:
    def __init__(self, command, destination):
        self.command = command
        self.destination = destination

door = StoryPiece("""You awake in a dungeon, your wrists are tied over your
head. You can tell you've been hanging there for hours, your fingers are numb
and your wrists are bleeding.  Your feet dangle inches from the floor, directly
infront of you is a table with a lantern on it. Next to the lanter, the rope
suspending you from the ceiling is tied to a nail on the wall. What do you
do?""")

rope = StoryPiece("""You kick the lantern over, knockin it into the rope. The
lantern breaks and burns a hole in the rope. You drop to the floor and your
hands are freed.""")

door.add_choice(Choice("Kick lantern", rope))

part = door

while True:
    part = part.run()
