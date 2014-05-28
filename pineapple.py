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
            print "You had one job. Type the right thing. Remember lower case."
            

class Choice:
    def __init__(self, command, destination):
        self.command = command
        self.destination = destination
        
Menu = StoryPiece("Welcome to Castle Destroyer! The Calculus AB/BC review game. All answers are multiple choice and lower case. Simply type 'a', 'b', 'c' etc to provide an answer. Type 'start' to begin.  When the game ends type 'return' to restart. Type 'start' to begin.") 

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

R16 = StoryPiece("You won the game. Big woop. Cool guys don't look at explosions, you did it. Bye bye now. Type 'return' to restart")

D1 = StoryPiece("You are as loud and obnoxious as possible when reaching for the keys so you manage to alert the guard who returns and picks up his keys. GAME OVER.")

D2 = StoryPiece("As you move forward to choke out the guard, you trip in to him. When you do this, he turns around and bonks you over the head with his club.  You pass out and wake up chained to the wall in your cell. GAME OVER.")

D3 = StoryPiece("You being the clumbsy person that you are, you trip and tumble down the stairs. It was a pretty long fall, you broke everything on the way down. GAME OVER.")

D4 = StoryPiece("Your stench is overwhelming. A group of cooks turn to you and in a disgusted rage start beating you with pots and pans. GAME OVER.")

D5 = StoryPiece("You begin moving through the maze of traps, and things seem fine at first. In overwhelming joy for being so quick and nimble, you jump forward. As a result, you land in a spike trap. GAME OVER.")

D6 = StoryPiece("You take way too long getting where you need to go, and an archer spots you from his post. An arrow swiftly zooms through the air and goes in one ear and out the other. GAME OVER.")

D7 = StoryPiece("You feel along the wall and stumble upon a switch. You decide that flipping it can't hurt and it fills the hallway with flames. At least you could see for a second before death. GAME OVER.")

D8 = StoryPiece("You stumble and fumble through the armmor, being extremely obnoxious you alert the guards in the next room. The storm the room and start beating you, and slashing you up with their swords. GAME OVER.")

D9 = StoryPiece("You feel along the wall and stumble upon a switch. You decide that flipping it can't hurt and it fills the hallway with flames. At least you could see for a second before death. GAME OVER.")

D10 = StoryPiece("You stare at the guard in a daze. You make the decision of indecision, and you are ended in a single blow.")

D11 = StoryPiece("As you move towards the two guards to fight back, you slip and fall on to their swords. WAY TO GO, THEY DIDNT EVEN HAVE TO DO ANYTHING. GAME OVER.")

D12 = StoryPiece("You rush towards the gate and try to slide under, but you dont make it through in time and are immediately crushed. GAME OVER.")

D13 = StoryPiece("You stand around and get captured. You are returned to your cell after a stern whipping. GAME OVER.")

D14 = StoryPiece("This plan wasn't as smart as you thought, and you blow yourself up. Good job...GAME OVER.")

D15 = StoryPiece("You look at the explosion...cool guys dont look at explosions. GAME OVER.")

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

Q1.add_choice(Choice("a",D1))

Q1.add_choice(Choice("b",R2))

Q1.add_choice(Choice("c",D1))

Q1.add_choice(Choice("d",D1))

Q2.add_choice(Choice("a",R3))

Q2.add_choice(Choice("b",D2))

Q2.add_choice(Choice("c",D2))

Q2.add_choice(Choice("d",D2))

Q3.add_choice(Choice("a",R4))

Q3.add_choice(Choice("b",D3))

Q4.add_choice(Choice("a",D4))

Q4.add_choice(Choice("b",R5))

Q5.add_choice(Choice("a",D5))

Q5.add_choice(Choice("b",R6))

Q5.add_choice(Choice("c",D5))

Q6.add_choice(Choice("a",R7))

Q6.add_choice(Choice("b",D6))

Q6.add_choice(Choice("c",D6))

Q7.add_choice(Choice("a",D7))

Q7.add_choice(Choice("b",D7))

Q7.add_choice(Choice("c",D7))

Q7.add_choice(Choice("d",R8))

Q8.add_choice(Choice("a",R9))

Q8.add_choice(Choice("b",D8))

Q8.add_choice(Choice("c",D8))

Q8.add_choice(Choice("d",D8))

Q9.add_choice(Choice("a",D9))

Q9.add_choice(Choice("b",D9))

Q9.add_choice(Choice("c",R10))

Q10.add_choice(Choice("a",D10))

Q10.add_choice(Choice("b",D10))

Q10.add_choice(Choice("c",R11))

Q10.add_choice(Choice("d",D10))

Q11.add_choice(Choice("a",D11))

Q11.add_choice(Choice("b",D11))

Q11.add_choice(Choice("c",D11))

Q11.add_choice(Choice("d",R12))

Q12.add_choice(Choice("a",R13))

Q12.add_choice(Choice("b",D12))

Q13.add_choice(Choice("a",D13))

Q13.add_choice(Choice("b",D13))

Q13.add_choice(Choice("c",R14))

Q13.add_choice(Choice("d",D13))

Q14.add_choice(Choice("a",D14))

Q14.add_choice(Choice("b",R15))

Q15.add_choice(Choice("a",D15))

Q15.add_choice(Choice("b",R16))

Q15.add_choice(Choice("c",D15))

Menu.add_choice(Choice("start",R1))

D1.add_choice((Choice("restart"Menu))

D2.add_choice((Choice("restart"Menu))

D3.add_choice((Choice("restart"Menu))

D4.add_choice((Choice("restart"Menu))

D5.add_choice((Choice("restart"Menu))

D6.add_choice((Choice("restart"Menu))

D7.add_choice((Choice("restart"Menu))

D8.add_choice((Choice("restart"Menu))

D9.add_choice((Choice("restart"Menu))

D10.add_choice((Choice("restart"Menu))

D11.add_choice((Choice("restart"Menu))

D12.add_choice((Choice("restart"Menu))

D13.add_choice((Choice("restart"Menu))

D14.add_choice((Choice("restart"Menu))

D15.add_choice((Choice("restart"Menu))

R16.add_choice((Choice("restart"Menu))

part = Menu

while True:
    part = part.run()
