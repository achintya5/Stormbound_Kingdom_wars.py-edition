#Title and description
print ('Welcome to Stormbound:Kingdom Wars .py Edition! \n A turn based card game for users playing against each other!' )
#Declaration of rules and instructions
print ('''Rules and instructions of the game! \n Be sure to read all of them to have a great gaming experience! \n 
1.Each Player starts off with an HP pool of 20 points and 3 random cards in their hand
2.At the start of each play, players will play cards from their hand onto the field
3.To play a card, simply type in the corresponding place of that card in your hand.
4.Players can only play a single card per turn. Choose wisely.
5.Damage and healing are applied at the end of the turn, in that order respectively.
6.At the end of the turn, all cards on the field are discarded.
7.If you play an invalid move, you will lose your turn as a penalty.
8.The game continues until one player loses all of their HP, i.e. HP=0.
''' )
#Deck:Add card name and effect to this dictionary to add whatever cards you want to your game and make it enjoyable to you! (no profanity please)
Deck={'Militia':'The basic soldier. Dmg: 1','Mage':'A basic support unit. Dmg: 2, Heal: 1','Swordsman':'Backbone of the kingdom army. Dmg: 3',
      'Cavalier':'The paragons of bravery. Dmg: 5','Kurestral Majin':'Secretive cult mages. Dmg: 4, Heal: 2','Griffin':'Gradiose creatures of valor. Dmg: 6',
      'Kurestral Knight':'Protectors of the kingdom. Dmg: 7','Fort of Ebonrock':'Heart of the kingdom. Heal: 3','Dragonic Roamers':'Dragons in their early days. Dmg: 2',
      'Sunbeam Serpents':'Snakes of dazzling beauty. Dmg: 1, Heal: 2','Basilisk':'Poisonous land based reptile. Dmg: 3','Trandoshan':'Pack hunters from a galaxy far far away. Dmg: 3, Heal: 1',
      'Broodmother Qordia':'Broodmother of dragons. Dmg: 4, Heal: 3','Lucid Matriarchs':"Qordia's guardians. Dmg: 4",'Xuri':'Dragon lord of the undead swarm. Dmg: 8',
      'Moonlit Aerie':'The home of ancient dragons. Heal: 4','Copperskin Ranger':'Scouts of the swamps. Dmg: 2','Amberhides':'Froglike warriors. Dmg: 3',
      'Azure Hatchers': 'Nomadic caretakers. Heal: 2','Heliotrooper':'Seething amphibians. Dmg: 4','Harpies of the hunt':'Feral hunters. Dmg: 5',
      'Blood Ministers':'Cunning and manipulative. Dmg: 4, Heal: 1','Brood Sages':'Untamed cultists. Dmg: 5','Klaxi':'High preistess of the swamps. Dmg: 5, Heal: 1','Rain of frogs':'Sacrificial summoning. Dmg: 4'}
Deck_starter_1=['Militia','Mage','Dragonic Roamers','Sunbeam Serpents','Copperskin Ranger','Azure Hatchers']
Deck_starter_2=['Swordsman','Cavalier','Kurestral Majin','Basilisk','Trandoshan','Broodmother Qordia','Lucid Matriarchs','Amberhides','Heliotrooper','Harpies of the hunt']
Deck_starter_3=['Fort of Ebonrock','Moonlit Aerie','Rain of frogs','Griffin','Kurestral Knight','Xuri']
Deck_dmg={'Militia':1,'Mage':2,'Swordsman':3,'Cavalier':5,'Kurestral Majin':4,'Griffin':6,'Kurestral Knight':7,'Fort of Ebonrock':0,'Dragonic Roamers':2,
          'Sunbeam Serpents':1,'Basilisk':3,'Trandoshan':3,'Broodmother Qordia':4,'Lucid Matriarchs':4,'Xuri':8,'Moonlit Aerie':0,'Copperskin Ranger':2,
          'Amberhides':3,'Azure Hatchers':0,'Heliotrooper':4,'Harpies of the hunt':5,'Blood Ministers':4,'Brood Sages':5,'Klaxi':5,'Rain of frogs':4}
Deck_heal={'Militia':0,'Mage':1,'Swordsman':0,'Cavalier':0,'Kurestral Majin':2,'Griffin':0,'Kurestral Knight':0,'Fort of Ebonrock':3,'Dragonic Roamers':0,
          'Sunbeam Serpents':2,'Basilisk':0,'Trandoshan':1,'Broodmother Qordia':3,'Lucid Matriarchs':0,'Xuri':0,'Moonlit Aerie':4,'Copperskin Ranger':0,
          'Amberhides':3,'Azure Hatchers':2,'Heliotrooper':0,'Harpies of the hunt':0,'Blood Ministers':1,'Brood Sages':5,'Klaxi':1,'Rain of frogs':0}
for i in Deck: #Print deck
    print(i,':',Deck[i])
print('''\n Controls:-
[Y/N] to respond to confirmations.
[0,1,2] to choose card to play.
Press [Enter] to end turn.''')      
Game_confirm=input("\n Would you like to begin a game?")
Game_status=''
if Game_confirm=='Y':
    P1_name=input("Enter Player 1's name: ")
    P2_name=input("Enter Player 2's name: ")
    P1_HP=20
    P2_HP=20
    Game_status='Start'
else:
    print("Thank you for playing Stormbound:Kingdom Wars .py Edition!")
    Game_status='end'
import random               # Game setup (increase range to increase number of starting cards)
P1_hand,P1_field,P2_hand,P2_field=[ ],[ ],[ ],[ ]
i=random.randint(0, len(Deck_starter_1)-1)
r=list(Deck_starter_1)[i]
P1_hand.append(str(r))
i=random.randint(0, len(Deck_starter_2)-1)
r=list(Deck_starter_2)[i]
P1_hand.append(str(r))
i=random.randint(0, len(Deck_starter_1)-1)
r=list(Deck_starter_1)[i]
P2_hand.append(str(r))
i=random.randint(0, len(Deck_starter_2)-1)
r=list(Deck_starter_2)[i]
P2_hand.append(str(r))
while Game_status=='Start':
    P1_field=[] #Reset field
    i = random.randint(0, len(Deck) - 1) #Draw card
    r1=list(Deck)[i]
    P1_hand.append(r1)
    print(P1_name,'\t HP: ',P1_HP,'\t Hand: ',P1_hand) #Show stats and hand
    P1_card_num=int(input('Player 1 plays: ')) #Play card
    P1_card=P1_hand[P1_card_num]
    P1_field.append(P1_card)
    P2_field=[] #Reset field
    i = random.randint(0, len(Deck) - 1) #Draw card
    r2=list(Deck)[i]
    P2_hand.append(r2)
    print(P2_name,'\t HP: ',P2_HP,'\t Hand: ',P2_hand) #Show stats and hand
    P2_card_num=int(input('Player 2 plays: ')) #Play card
    P2_card=P2_hand[P2_card_num]
    P2_field.append(P2_card)
    print(P1_name,'played',P1_card,'!') #Announce cards played
    print(P2_name,'played',P2_card,'!')
    P1_maxHP,P1_dmg,P1_heal=20,0,0
    if P1_card_num>=len(P1_hand):
        print('That is an invalid move. You do not have that card in your hand.')
    P1_dmg=Deck_dmg[P1_card] #calculate dmg from Deck_dmg
    P1_heal=Deck_heal[P1_card] #calculate heal from Deck_heal
    P1_hand.remove(P1_hand[P1_card_num]) #discard used cards
    P2_HP-=P1_dmg #To calculate damage and effects
    P2_maxHP,P2_dmg,P2_heal=20,0,0
    if P2_card_num>=len(P2_hand):
        print('That is an invalid move. You do not have that card in your hand.')
    P2_dmg=Deck_dmg[P2_card] #calculate dmg from Deck_dmg
    P2_heal=Deck_heal[P2_card] #calculate heal from Deck_heal
    P2_hand.remove(P2_hand[P2_card_num]) #discard used cards
    P1_HP-=P2_dmg #To calculate damage and effects
    if P1_HP<=0 and P2_HP<=0: #To check HP and declare winner if any
        print('Game is over! \n Neither player wins, it is a draw!, \n Thank you for playing Stormbound:Kingdom Wars .py Edition!')
        Game_status='end'
        break
    elif P1_HP<=0:
        print('Game is over! \n Winner is',P2_name,'! \n Thank you for playing Stormbound:Kingdom Wars .py Edition!')
        Game_status='end'
        break
    elif P2_HP<=0:
        print('Game is over! \n Winner is',P1_name,'! \n Thank you for playing Stormbound:Kingdom Wars .py Edition!')
        Game_status='end'
        break
    else: #To apply healing if game is not over    
        P1_HP+=P1_heal
        P2_HP+=P2_heal
        if P1_HP>=P1_maxHP:
            P1_HP=20
        if P2_HP>=P2_maxHP:
            P2_HP=20
    Game_status=='Start'
