#John-Phillip Sims

import json
from random import randint
import os
import time

#Both the player and enemies will have the same stat setup
#HP - health points
#SP - special points.  spent on special skills
#attack - power of physical attacks
#defense - how resistant the entity is to damage
#magic - power of magical attacks and abilities
#speed - determines turn order
#luck - dermines crit rate and other stuff
#all stats will start somewhere between 1 and 10 but can be upgrade as fights are won
#dSkills will be a list of skills the entity can use to do damage
#pSSkills will be a list of skills the entity can use to buff themselves
#eSSkills will be a list of skills the entity can use to debuff enemies
#buffs will be a list of currently applied buffs and debuffs

class playerProfile:
    def __init__(self, name, pClass, hpMax, spMax, attack, defense, magic, speed, luck, dSkills, pSSkills, eSSkills):
        self.name = name
        self.pClass = pClass
        self.hpMax = hpMax
        self.hp = hpMax
        self.spMax = spMax
        self.sp = spMax
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.speed = speed
        self.luck = luck
        self.dSkills = dSkills
        self.pSSkills = pSSkills
        self.eSSkills = eSSkills

    buffs = []

class enemyProfile:
    def __init__(self, name, hpMax, spMax, attack, defense, magic, speed, luck, dSkills, pSSkills, eSSkills):
        self.name = name
        self.hpMax = hpMax
        self.hp = hpMax
        self.spMax = spMax
        self.sp = spMax
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.speed = speed
        self.luck = luck
        self.dSkills = dSkills
        self.pSSkills = pSSkills
        self.eSSkills = eSSkills

    buffs = []

#class for damaging skills
#name is the name
#description is a description of the skill
#cost is how much SP it takes to use the skill
#damage is how much damage the skill does
class dSkill:
    def __init__(self, name, description, cost, damage):
        self.name = name
        self.description = description
        self.cost = cost
        self.damage = damage

#class for self buffing skills
#name is the name
#description is a description of the skill
#cost is how much SP it takes to use the skill
#affectedStat tells what stat is affected 
#statChange tells how much that stat changes
class pSSkill:
    def __init__(self, name, description, cost, affectedStat, statChange):
        self.name = name
        self.description = description
        self.cost = cost
        self.affectedStat = affectedStat
        self.statChange = statChange

#class for enemy debuffing skills
#name is the name
#description is a description of the skill
#cost is how much SP it takes to use the skill
#affectedStat tells what stat is affected 
#statChange tells how much that stat changes
class eSSkill:
    def __init__(self, name, description, cost, affectedStat, statChange):
        self.name = name
        self.description = description
        self.cost = cost
        self.affectedStat = affectedStat
        self.statChange = statChange

#class for buffs and debuffs
#affectedStat tells what stat is affected 
#statChange tells how much that stat changes
#turnLeft tells how many turns the buff is active
class buff:
    def __init__(self, affectedStat, statChange):
        self.affectedStat = affectedStat
        self.statChange = statChange
        self.turnsLeft = 3

def clearScreen():
    if os.name == 'nt':
        clear = os.system('cls')
    else:
        clear = os.system('clear')

def playerTurn(Player, Enemy, skillsData):
    

    while True:
        print('Menu')
        print('\tattack')
        print('\tguard')
        print('\tskill')
        print('\tdie')
        pInput = input('what do you want to do?')

        if pInput.lower() == 'attack':
            print('attacking!')
            time.sleep(1)
            buffDmg = 0
            for i in Player.buffs:
                if i.affectedStat == 'attack':
                    buffDmg += i.statChange
            damage = Player.attack + buffDmg - Enemy.defense
            if(damage > 0):
                Enemy.hp = Enemy.hp - damage
                print('Your attack does ' + str(damage) + ' damage!')
                time.sleep(1)
                print('' + Enemy.name + ' is now at ' + str(Enemy.hp) + ' HP!')
            else:
                print("Your attack does no damage!")
            
            time.sleep(3)
            input('Press enter to continue')
            break
        elif pInput.lower() == 'guard':
            print('guarding!')
            break
        elif pInput.lower() == 'skill':
            print('skills list')
            break
        elif pInput.lower() == 'die':
            print('If you really want that')
            Player.hp = 0
            break
        else:
            print('Please enter a valid input')

    print('\n\nplayer turn done')

def printFightData(Player, Enemy):
    print('' + Enemy.name + '\n\tHP: ' + str(Enemy.hp))
    print('' + Player.name + '\n\tHP: ' + str(Player.hp) + ' / ' + str(Player.hpMax) + '\n\tSP: ' + str(Player.sp) + ' / ' + str(Player.spMax))

def fightingLoop(Player, enemyData, skillsData):
    while True:

        print('Lets get a random enemy')

        #Pulls a random enemy from the json data
        randomIndex = randint(0, len(enemyData['enemies'])-1)
        reTemp = enemyData['enemies'][randomIndex]
        randomEnemy = enemyProfile(reTemp['enemyName'], reTemp['hpMax'], reTemp['spMax'], reTemp['attack'], reTemp['defense'], reTemp['magic'], reTemp['speed'], reTemp['luck'], reTemp['dSkills'], reTemp['pSSkills'], reTemp['eSSkills'])

        print('A ' + randomEnemy.name + ' approaches!')

        #Start the fight

        while Player.hp > 0 and randomEnemy.hp > 0:
            clearScreen()
            printFightData(Player, randomEnemy)
            if Player.speed > randomEnemy.speed:
                print('player turn')
                playerTurn(Player, randomEnemy, skillsData)
                if(randomEnemy.hp > 0):
                    print('enemy turn')

            else:
                print('enemy turn')

                if Player.hp > 0:
                    print('player turn')

        print('fight done')


        if Player.hp <= 0:
            print('You have died.  Too bad :(')
            break

        #ask the player if they want to fight again
        pInput = input('Do you want to fight again? (Y/N)')
        if pInput == 'N' or pInput == 'n':
            break

    print('Fighting is done!')


if __name__=='__main__':
    print('Welcome to my simple turn-based RPG battle system!')
    pName = input('Please enter your name:')

    #open the json file with the player classes
    f = open('playerClasses.json')
    playerClasses = json.load(f)
    f.close()

    #open the file with the enemies
    f = open('enemies.json')
    enemyData = json.load(f)
    f.close()

    #open the file with the skills
    f = open('skills.json')
    skillsData = json.load(f)
    f.close()


    pClass = ""
    found = False

    while not found:
        print('Here is a list of available classes')
        for i in playerClasses['classes']:
            print(i['className'])
        pCtemp = input('\nWhich class do you want to play? ')
        for i in playerClasses['classes']:
            if pCtemp == i['className']:
                pClass = i
                found = True
                break
        if not found:
            print('Please enter a valid input')

    print('You have chosen the ' + pClass['className'] + ' class')

    Player = playerProfile(pName, pClass['className'], pClass['hpMax'], pClass['spMax'], pClass['attack'], pClass['defense'], pClass['magic'], pClass['speed'], pClass['luck'], pClass['dSkills'], pClass['pSSkills'], pClass['eSSkills'])

    print(Player.name)
    print('Stats:')
    print('Max HP: ' + str(Player.hpMax))
    print('Max SP: ' + str(Player.spMax))
    print('Attack: ' + str(Player.attack))
    print('Defense: ' + str(Player.defense))
    print('Magic: ' + str(Player.magic))
    print('Speed: ' + str(Player.speed))
    print('Luck: ' + str(Player.luck))

    print('Offensive Skills:')
    for i in Player.dSkills:
        print(i)

    print('Support Skills')
    for i in Player.pSSkills:
        print(i)
    for i in Player.eSSkills:
        print(i)

    pInput = input('Are you ready to start a fight? (Y/N)')

    if pInput.lower() == 'y':
        print('Start the Game!')
        fightingLoop(Player, enemyData, skillsData)
    else:
        print('Then get out of here!')