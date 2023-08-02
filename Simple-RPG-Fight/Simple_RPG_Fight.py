#John-Phillip Sims

import json

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
    def __init__(name, pClass, hp, sp, attack, defense, magic, speed, luck, dSkills, pSSkills, eSSkills, buffs):
        self.name = name
        self.pClass = pClass
        self.hp = hp
        self.sp = sp
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.speed = speed
        self.luch = luck
        self.dSkills = dSkills
        self.pSSkills = pSSkills
        self.eSSkills = eSSkills
        self.buffs = buffs

#class for damaging skills
#name is the name
#description is a description of the skill
#cost is how much SP it takes to use the skill
#damage is how much damage the skill does
class dSkill:
    def __init__(name, description, cost, damage):
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
    def __init__(name, description, cost, affectedStat, statChange):
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
    def __init__(name, description, cost, affectedStat, statChange):
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
    def __init__(affectedStat, statChange, turnsLeft):
        self.affectedStat = affectedStat
        self.statChange = statChange
        turnsLeft = 3

if __name__=='__main__':
    print('Welcome to my simple turn-based RPG battle system!')
    pName = input('Please enter your name:')



