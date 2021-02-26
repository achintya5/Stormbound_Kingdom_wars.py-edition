import turtle
import random
win=turtle.Screen()
win.title("Digiwars .py Edition")
win.bgcolor("black")
win.setup(width=1200, height=600)
win.tracer(0)
from turtle import Screen, Turtle

#game status
Game_status = ''
#arena
arena=Turtle()
arena.speed(0)
arena.color("white")
arena.hideturtle()
arena.shape("square")
arena.shapesize(stretch_wid=1, stretch_len=100)
arena.penup()

#Deck:Add card name and effect to this dictionary to add whatever cards you want to your game and make it enjoyable to you! (no profanity please)

Deck=['Militia','Mage','Swordsman','Cavalier','Kurestral Majin','Griffin','Kurestral Knight','Fort of Ebonrock','Dragonic Roamers','Sunbeam Serpents','Basilisk','Trandoshan','Broodmother Qordia','Lucid Matriarchs','Xuri','Moonlit Aerie','Copperskin Ranger','Amberhides','Azure Hatchers','Heliotrooper','Harpies of the hunt','Blood Ministers','Brood Sages','Klaxi','Rain of frogs']
Deck1=['Militia','Mage','Dragonic Roamers','Sunbeam Serpents','Copperskin Ranger','Azure Hatchers']
Deck2=['Swordsman','Cavalier','Kurestral Majin','Basilisk','Trandoshan','Broodmother Qordia','Lucid Matriarchs','Amberhides','Heliotrooper','Harpies of the hunt']
Deck_dmg={'Militia':1,'Mage':2,'Swordsman':3,'Cavalier':5,'Kurestral Majin':4,'Griffin':6,'Kurestral Knight':7,'Fort of Ebonrock':0,'Dragonic Roamers':2,
          'Sunbeam Serpents':1,'Basilisk':3,'Trandoshan':3,'Broodmother Qordia':4,'Lucid Matriarchs':4,'Xuri':8,'Moonlit Aerie':0,'Copperskin Ranger':2,
          'Amberhides':3,'Azure Hatchers':0,'Heliotrooper':4,'Harpies of the hunt':5,'Blood Ministers':4,'Brood Sages':5,'Klaxi':5,'Rain of frogs':4}
Deck_heal={'Militia':0,'Mage':1,'Swordsman':0,'Cavalier':0,'Kurestral Majin':2,'Griffin':0,'Kurestral Knight':0,'Fort of Ebonrock':3,'Dragonic Roamers':0,
          'Sunbeam Serpents':2,'Basilisk':0,'Trandoshan':1,'Broodmother Qordia':3,'Lucid Matriarchs':0,'Xuri':0,'Moonlit Aerie':4,'Copperskin Ranger':0,
          'Amberhides':3,'Azure Hatchers':2,'Heliotrooper':0,'Harpies of the hunt':0,'Blood Ministers':1,'Brood Sages':5,'Klaxi':1,'Rain of frogs':0}

#instructions for moves
ipen=Turtle()
ipen.speed(0)
ipen.color("white")
ipen.penup()
ipen.hideturtle()


#Opening Pen
pen=Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,240)
pen.write("Welcome to DigiWars .py Edition! \n A turn based card game for users playing against each other!", align="center", font=("Courier",20, "normal"))

#Instructions Pen
p=Turtle()
p.speed(0)
p.color("white")
p.penup()
p.hideturtle()
p.goto(0,-80)
p.write("Rules and instructions of the game!\nBe sure to read all of them to have a great gaming experience!\n1.Each Player starts off with an HP pool of 20 points and 3 random cards in their hand\n2.At the start of each play, players will play cards from their hand onto the field\n3.To play a card, simply type in the corresponding place of that card in your hand.\n4.Players can only play a single card per turn. Choose wisely.\n5.Damage and healing are applied at the end of the turn, in that order respectively.\n6.At the end of each turn, the card is replaced by a similar card.\n7.If you play an invalid move, you will lose your turn as a penalty.\n8.The game continues until one player loses all of their HP, i.e. HP=0.\n\n\n\nPress R if you have read the rules.", align="center", font=("Courier",20, "normal"))

#scoring
score1= Turtle()
score1.speed(0)
score1.color("green")
score1.penup()
score1.hideturtle()
score1.goto(400, 220)

score2= Turtle()
score2.speed(0)
score2.color("green")
score2.penup()
score2.hideturtle()
score2.goto(400,-100)


#some terms used in the game
p1hp=20
p2hp=20

p1hand=[]
r=Deck1[random.randint(0,len(Deck1)-1)]
p1hand.append(r)
r=Deck2[random.randint(0,len(Deck2)-1)]
p1hand.append(r)
r=Deck[random.randint(0,len(Deck)-1)]
p1hand.append(r)

p2hand=[]
r2=Deck1[random.randint(0,len(Deck1)-1)]
p2hand.append(r2)
r2=Deck2[random.randint(0,len(Deck2)-1)]
p2hand.append(r2)
r2=Deck[random.randint(0,len(Deck)-1)]
p2hand.append(r2)

#Functions
def deck_show():
    win.onkeypress(none, "r")
    win.onkeypress(none, "n")
    pen.clear()
    p.clear()
    pen.goto(0, -280)
    pen.write("Militia:The basic soldier. Dmg: 1\nMage:A basic support unit. Dmg: 2, Heal: 1\nSwordsman:Backbone of the kingdom army. Dmg: 3\nCavalier:The paragons of bravery. Dmg: 5\nKurestral Majin:Secretive cult mages. Dmg: 4, Heal: 2\nGriffin:Gradiose creatures of valor. Dmg: 6\nKurestral Knight:Protectors of the kingdom. Dmg: 7\nFort of Ebonrock:Heart of the kingdom. Heal: 3\nDragonic Roamers:Dragons in their early days. Dmg: 2\nSunbeam Serpents:Snakes of dazzling beauty. Dmg: 1, Heal: 2\nBasilisk:Poisonous land based reptile. Dmg: 3\nTrandoshan:Pack hunters from a galaxy far far away. Dmg: 3, Heal: 1\nBroodmother Qordia:Broodmother of dragons. Dmg: 4, Heal: 3\nLucid Matriarchs:Qordia's guardians. Dmg: 4\nXuri:Dragon lord of the undead swarm. Dmg: 8\nMoonlit Aerie:The home of ancient dragons. Heal: 4\nCopperskin Ranger:Scouts of the swamps. Dmg: 2\nAmberhides:Froglike warriors. Dmg: 3\nAzure Hatchers:Nomadic caretakers. Dmg: 2, Heal: 1\nHeliotrooper:Seething amphibians. Dmg: 4\nHarpies of the hunt:Feral hunters. Dmg: 5\nBlood Ministers:Cunning and manipulative. Dmg: 4, Heal: 1\nBrood Sages:Untamed cultists. Dmg: 5\nKlaxi:High preistess of the swamps. Dmg: 5, Heal: 1\nRain of frogs:Sacrificial summoning. Dmg: 4\n\nPress D to clear deck", align="center", font=("Courier",20, "normal"))

def game_confirmer():
    win.onkeypress(none, "d")
    win.onkeypress(none, "n")
    pen.clear()
    pen.goto(0, 0)
    pen.write('''\n Controls:-
Press [Y/N] to respond to confirmations.
Press [0,1,2] to choose card to play(Player 1)
Press [4,5,6] to choose card to play(Player 2).\n\n
Press Enter''',align="center", font=("Courier",20, "normal"))

def game_status():
    win.onkeypress(none, "Return")
    pen.clear()
    pen.goto(0, 0)
    pen.write(" Would you like to begin a game?\n Press Y if you want to.",align="center", font=("Courier",20, "normal"))
def none():
    c=1
def check():
    win.onkeypress(none,"r")
    win.onkeypress(none, "d")
    win.onkeypress(none, "Return")
    win.onkeypress(none, "y")
    win.onkeypress(none,"n")
    pen.clear()
    score1.write("Player 1 HP = {}".format(p1hp),align="center", font=("Courier",20, "bold"))
    score2.write("Player 2 HP = {}".format(p2hp),align="center", font=("Courier",20, "bold"))
    pen.goto(-200,200)
    pen.write("Player 1 Hand:\n{}".format(p1hand),align="center", font=("Courier",20, "normal"))
    ipen.goto(-200,160)
    ipen.write("Press 1,2 or 3 for these cards",align="center", font=("Courier",20, "normal"))
    p.clear()
    p.goto(-200,-100)
    p.write("Player 2 Hand:\n{}".format(p2hand), align="center", font=("Courier",20, "normal"))
    ipen.goto(-200,-140)
    ipen.write("Press 4,5 or 6 for these cards",align="center", font=("Courier",20, "normal"))

    arena.goto(0,0)
    arena.showturtle()
    Game_status='Start'

move=[]

def moves1():
    move.clear()
    move.append(1)

def moves2():
    move.clear()
    move.append(2)

def moves3():
    move.clear()
    move.append(3)

def moves4():
    move.clear()
    move.append(4)

def moves5():
    move.clear()
    move.append(5)

def moves6():
    move.clear()
    move.append(6)


#keybord binding
win.listen()
win.onkeypress(deck_show,"r")
win.onkeypress(game_confirmer,"d")
win.onkeypress(game_status,"Return")
win.onkeypress(check,"y")
win.onkeypress(moves1,"1")
win.onkeypress(moves2,"2")
win.onkeypress(moves3,"3")
win.onkeypress(moves4,"4")
win.onkeypress(moves5,"5")
win.onkeypress(moves6,"6")

chance=1
#Main game loop
while True:
    win.update()
    if move==[1] and chance==1:
        damage_on_2=int(Deck_dmg[p1hand[0]])
        heal_on_1=int(Deck_heal[p1hand[0]])
        p1hp+=heal_on_1
        p2hp-=damage_on_2
        score2.clear()
        score2.write("Player 2 HP = {}".format(p2hp), align="center", font=("Courier", 20, "bold"))
        ipen.clear()
        ipen.goto(0, 20)
        ipen.write("Player 1 played: {}".format(p1hand[0]), align="center", font=("Courier", 20, "normal"))
        move.append(100)
        p1hand.pop(0)
        r=Deck[random.randint(0,len(Deck)-1)]
        p1hand.append(r)
        pen.clear()
        pen.goto(-200,200)
        pen.write("Player 1 Hand:\n{}".format(p1hand),align="center", font=("Courier",20, "normal"))
        chance=2
    if move==[2] and chance==1:
        damage_on_2=int(Deck_dmg[p1hand[1]])
        heal_on_1=int(Deck_heal[p1hand[1]])
        p1hp+=heal_on_1
        p2hp-=damage_on_2
        score2.clear()
        score2.write("Player 2 HP = {}".format(p2hp), align="center", font=("Courier", 20, "bold"))
        ipen.clear()
        ipen.goto(0, 20)
        ipen.write("Player 1 played: {}".format(p1hand[1]), align="center", font=("Courier", 20, "normal"))
        move.append(100)
        p1hand.pop(1)
        r=Deck[random.randint(0,len(Deck)-1)]
        p1hand.append(r)
        pen.clear()
        pen.goto(-200,200)
        pen.write("Player 1 Hand:\n{}".format(p1hand),align="center", font=("Courier",20, "normal"))
        chance = 2
    if move==[3] and chance==1:
        damage_on_2=int(Deck_dmg[p1hand[2]])
        heal_on_1=int(Deck_heal[p1hand[2]])
        p1hp+=heal_on_1
        p2hp-=damage_on_2
        score2.clear()
        score2.write("Player 2 HP = {}".format(p2hp), align="center", font=("Courier", 20, "bold"))
        ipen.clear()
        ipen.goto(0, 20)
        ipen.write("Player 1 played: {}".format(p1hand[2]), align="center", font=("Courier", 20, "normal"))
        move.append(100)
        p1hand.pop(2)
        r=Deck[random.randint(0,len(Deck)-1)]
        p1hand.append(r)
        pen.clear()
        pen.goto(-200,200)
        pen.write("Player 1 Hand:\n{}".format(p1hand),align="center", font=("Courier",20, "normal"))
        chance = 2
    if move==[4] and chance==2:
        damage_on_1=int(Deck_dmg[p2hand[0]])
        heal_on_2=int(Deck_heal[p2hand[0]])
        p2hp+=heal_on_2
        p1hp-=damage_on_1
        score1.clear()
        score1.write("Player 1 HP = {}".format(p1hp), align="center", font=("Courier", 20, "bold"))
        ipen.clear()
        ipen.goto(0, 20)
        ipen.write("Player 2 played: {}".format(p2hand[0]), align="center", font=("Courier", 20, "normal"))
        move.append(100)
        p2hand.pop(0)
        r=Deck[random.randint(0,len(Deck)-1)]
        p2hand.append(r)
        p.clear()
        p.goto(-200,-100)
        p.write("Player 2 Hand:\n{}".format(p2hand), align="center", font=("Courier",20, "normal"))
        chance = 1
    if move==[5] and chance==2:
        damage_on_1=int(Deck_dmg[p2hand[1]])
        heal_on_2=int(Deck_heal[p2hand[1]])
        p2hp+=heal_on_2
        p1hp-=damage_on_1
        score1.clear()
        score1.write("Player 1 HP = {}".format(p1hp), align="center", font=("Courier", 20, "bold"))
        ipen.clear()
        ipen.goto(0, 20)
        ipen.write("Player 2 played: {}".format(p2hand[1]), align="center", font=("Courier", 20, "normal"))
        move.append(100)
        p2hand.pop(1)
        r=Deck[random.randint(0,len(Deck)-1)]
        p2hand.append(r)
        p.clear()
        p.goto(-200,-100)
        p.write("Player 2 Hand:\n{}".format(p2hand), align="center", font=("Courier",20, "normal"))
        chance = 1
    if move==[6] and chance==2:
        damage_on_1=int(Deck_dmg[p2hand[2]])
        heal_on_2=int(Deck_heal[p2hand[2]])
        p2hp+=heal_on_2
        p1hp-=damage_on_1
        score1.clear()
        score1.write("Player 1 HP = {}".format(p1hp), align="center", font=("Courier", 20, "bold"))
        ipen.clear()
        ipen.goto(0, 20)
        ipen.write("Player 2 played: {}".format(p2hand[2]), align="center", font=("Courier", 20, "normal"))
        move.append(100)
        p2hand.pop(2)
        r=Deck[random.randint(0,len(Deck)-1)]
        p2hand.append(r)
        p.clear()
        p.goto(-200,-100)
        p.write("Player 2 Hand:\n{}".format(p2hand), align="center", font=("Courier",20, "normal"))
        chance = 1

    if p1hp<=0:
        pen.clear()
        score1.clear()
        ipen.clear()
        score2.clear()
        p.clear()
        arena.hideturtle()
        pen.goto(0,0)
        pen.write("Player 2 has won the match! \nThank you for playing DigiWars.py Edition!",align="center", font=("Courier", 40, "normal"))
    if p1hp>=20:
        p1hp=20
    if p2hp<=0:
        pen.clear()
        score1.clear()
        ipen.clear()
        score2.clear()
        p.clear()
        arena.hideturtle()
        pen.goto(0, 0)
        pen.write("Player 1 has won the match! \nThank you for playing DigiWars.py Edition!",align="center", font=("Courier", 40, "normal"))
    if p2hp>=20:
        p2hp=20
