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
            print "You had one job. Type the right thing."
            

class Choice:
    def __init__(self, command, destination):
        self.command = command
        self.destination = destination
        
Menu = StoryPiece("Welcome to Castle Destroyer! The Calculus AB/BC review game. All answers are multiple choice and lower case. Simply type 'a', 'b', 'c' etc to provide an answer. Type 'start' to begin.  When the game ends type 'return' to restart.") 

R1 = StoryPiece("You awake to find yourself in a dark, moldy cell. There is a shaded hallway on the other side of your cell door and there are no windows.  A guard walks by your cell and whispers some obscenities to you before continuing. As he steps away the ring containing his keys clatters to the floor just outside your door. Type 'next' to continue.")

R2 = StoryPiece("You delicately retrieve the keys from the floor outside of your cell. You quietly unlock the door and step out in to the hallway.  You look all around and the only exit is currently being blocked by that rude and unsavory guard who is moving towards it slowly. You manage to sneak up to be only a few feet behind him before taking any drastic action. Type 'next' to continue.")

R3 = StoryPiece("You wrap your arm around the guards neck from behind and subdue him.  You proceed to take the club that he was carrying and bonk him over the head for good measure.  You search for anything else that could be of use but find nothing but a squished carrot.  As you move through the door at the end of the corridor you find yourself at the top of a long spiraling set of stairs. Type 'next' to continue.")

R4 = StoryPiece("You finally make it to the bottom of the maddeningly long staircase to find a lone door at the bottom.  In your excitement you jump through the door to find yourself in a crowded kitchen.  In the craziness noone immediately notices you, but you have to get out quickly before someone wises up to the fact that you stink more than a horse in heat in the middle of summer. Type 'next' to continue.")

R5 = StoryPiece("You make it through the back door to the castle and end up in the small plain behind the castle, flooded with mood. A step to your right causes the ground to collapse revealing a spike pit.  You manage to pull back just in time in order to not fall in.  You have to move quickly, there are archers in the towers watching the yard. A moments hesitation can mean the end. Type 'next' to continue.")

R6 = StoryPiece("You carefully maneuver through the open field around to the side of the castle. A few more traps were activated and narrowly missed on the way, but you manage to avoid alerting any guards. Ahead of you, to the right, on the the side of the castle is the door your looking for. The door down to the armory! Type 'next' to continue.")

R7 = StoryPiece("You enter through the door to the armory.  It is so dark here that you can't see your hands in front of your face.  You take a step forward and there is a surprising drop.  Oh great...you're on a staircase. But you're almost to the motherload of weapons! It's too late to give up now. Type 'next' to continue.")

R8 = StoryPiece("As you enter the armory there is a door to your right, but there is quite the ruckus coming from the other side. It is best to be quiet to avoid being found. There are old discarded weapons and shields along the floor, but there is quite the collection of prisitne weapons hanging on the wall. Type 'next to continue.")

R9 = StoryPiece("You pick out a gorgeous shield with a golden eagle on it, as well as a shiny shortsword.  There were many options that looked more glamorous, but the weight of this particular shortsword was absolutely perfect.  The ruckus from the other room grows closer so you rush back to the staircase in order to avoid a disaster. Type 'next' to continue")

R10 = StoryPiece("You come out of the door to the armory, and just your luck there's the ugly mug of a passing soldier staring you right in the eyes. He raises his sword, screaming something that roughly resembles 'YOURE MINE NOW!'. He beigns to swing his sword directly towards your head. Type 'next' to continue.")

R11 = StoryPiece("You swiftly cut down the screaming guard and rush along the side of the castle towards the courtyard. There is no chance of remaining undiscovered now. As you enter the courtyard you see two guards directly infront of you. On the opposite side of the courtyard there is a third guard rushing towards the mechanism to lower the gate. The two guards in front of you draw their swords and begin charging in your direction. Type 'next' to continue.")

R12 = StoryPiece("You do some sweet ninja moves and swing your sword around in a full circle chopping both guards in half, they float there in slow motion before turning in to dust. Classic ninja stuff. Now you've got to keep the gate from being closed. You rush towards the guard manning the gate, raising your sword high into the air and letting out your most vigorous war cry. Type 'next' to continue.")

R13 = StoryPiece("You manage to strike down the guard before the gate completely closes. It is left hanging two or three feet off of the ground.  You go to move around towards the gate and are blocked off by a platoon of guards, no less than thirty.  The only open space left is behind you, your back being towards the blacksmith's. Type 'next' to continue.")

R14 = StoryPiece("You rush in to the blacksmith's and lock the door behind you. You step away and you can see the door bending as the guards outside ram in to it.  You take a look around the room and there is not much to see, there are twenty or so kegs littering the floor, and a tanning rack covered in fresh cloth. To the side of the rack is the smeltery, still lit. You peek in to one of the kegs to find it full of gunpowder. The same seems to be true of the rest. The door begins to crack under the strength of the guards slamming in to it. Type 'next' to continue.")

R15 = StoryPiece("You light a piece of cloth from the tanning rack and tuck it in to one of the powder kegs.  You find a ladder in the corner of the room and climb up it on to the roof. You wait until you feel the time is right, and you jump for the gate. Landing feet before it and sliding under it. Before any of the guards have time to react they are blown from this world by the awesome power of these powder kegs. The gate slams shut and you start to walk away.  As the rest of the castle starts the blow up behind you. Type 'next' to continue.")

Q1 = StoryPiece("d/dx CU = ? A:c'u  B:cu'  C:c'u'  D:du")

Q2 = StoryPiece("Integral of du = ? A:u+c B:du+dc C:du+c D:u")

Q3 = StoryPiece("d/dx cosx = ? A:-sinx B:sinx")

Q4 = StoryPiece("Integral from 1 to 3 of -x^2 + 4x -3dx = ? A:6/3 B: -4/3:)

Q5 = StoryPiece("Summation of 1/n^p if p = 1/3 A:Converges B:Diverges C:Cannot be determined")

Q6 = StoryPiece("Integral of e^x = ? A:e^x + c B:12 C:e^x^x")

Q7 = StoryPiece("Integral of x^2 = ? A:2x+c B:1/2x^2 +c C:2+c D: 1/3x^3 +c")

Q8 = StoryPiece("Integral from 1 to 2 of x^2 = ? A:1/3 B:2/3 C:7 D:3")

Q9 = StoryPiece("d/dx x^6 + 3x^5 + 7x +3 = ? A: 601231 B:6x^5 +15x^4 C:6x^5 + 15x^4 + 7")

Q10 = StoryPiece("d/dx 3x^2 A:5x B:1231 C:6x D:42")

Q11 = StoryPiece("If d/dx represents speed, what will taking the integral yield? A:Speed B:Acceleration C:Nothing D:Position")

Q12 = StoryPiece("What is another term for anti-derivative that may include bounds? A:Integral B:Summation")

Q13 = StoryPiece("Fluffy the kitty accelerates at 6m/s. How can you determine his speed at time x=t? A:Take the derivative B:Use summation C:Take the integral and plug in t for x D:Take the integral")

Q14 = StoryPiece("On a position time graph, what represents the velocity? A: Slope of the tangent line B: Slope")

Q15 = StoryPiece("The ratio test is useful for what type of problem? A:Derivative B:Summation C:Integral")

R1.add_choice(Choice("next", Q1))

R2.add_choice(Choice("next", Q2))

R3.add_choice(Choice("next", Q3))

R4.add_choice(Choice("next", Q4))

R5.add_choice(Choice("next", Q5))

R6.add_choice(Choice("next", Q6))

R7.add_choice(Choice("next", Q7))

R8.add_choice(Choice("next", Q8))

R9.add_choice(Choice("next", Q9))

R10.add_choice(Choice("next", Q10))

R11.add_choice(Choice("next", Q11))

R12.add_choice(Choice("next", Q12))

R13.add_choice(Choice("next", Q13))

R14.add_choice(Choice("next", Q14))

R15.add_choice(Choice("next", Q15))

part = Menu

while True:
    part = part.run()
