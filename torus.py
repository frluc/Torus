#Torus

import random
from bots import Bot
from group import Group

#creating 6 bots

bot1 = Bot('Bob', 20, 20, 10, 2, 60, 5, 40, 3, 25)
bot2 = Bot('Bill', 20, 20, 10, 2, 60, 5, 40, 3, 25)
bot3 = Bot('Raoul', 20, 20, 10, 2, 60, 5, 40, 3, 25) 
bot4 = Bot('Dan', 20, 20, 10, 2, 60, 5, 40, 3, 25)
bot5 = Bot('Ray', 20, 20, 10, 2, 60, 5, 40, 3, 25)
bot6 = Bot('Moh', 20, 20, 10, 2, 60, 5, 40, 3, 25)

#creating 2 groups

group1 = Group("Alpha")
group2 = Group("Omega")

print()
group1.addbot(bot1)
group1.addbot(bot2)
group1.addbot(bot3)

print()
group2.addbot(bot4)
group2.addbot(bot5)
group2.addbot(bot6)

print()
group1.groupdisplay()

print()
group2.groupdisplay()

print()

#group initiative

group1_ini = 0
for x in group1.bot_list:
        group1_ini += x.initiative_roll()
print(group1.group_name+"initiative:"+str(group1_ini))

group2_ini = 0
for y in group2.bot_list:
        group2_ini += x.initiative_roll()
print(group2.group_name+"initiative:"+str(group2_ini))

print()

'''
#let's fight melee!

while True:
	
        bot1_ini = bot1.initiative_roll()
	bot2_ini = bot2.initiative_roll()

	if bot1_ini > bot2_ini:
		print(bot1.name+' act first')
		if bot1.melee_hit(bot2):
			bot2.take_damage(bot1.melee_dmg)
			if bot2.hp <= 0:
				break
		if bot2.melee_hit(bot1):
			bot1.take_damage(bot2.melee_dmg)
			if bot1.hp <= 0:
				break
	elif bot2_ini > bot1_ini:
		print(bot2.name+' act first')
		if bot2.melee_hit(bot1):
			bot1.take_damage(bot2.melee_dmg)
			if bot1.hp <= 0:
				break
		if bot1.melee_hit(bot2):
			bot2.take_damage(bot1.melee_dmg)
			if bot2.hp <= 0:
				break
	else:
                print('double hit!')
                if bot2.melee_hit(bot1):
                        bot1.take_damage(bot2.melee_dmg)
                if bot1.melee_hit(bot2):
                        bot2.take_damage(bot1.melee_dmg)
                if bot1.hp <= 0 or bot2.hp <= 0:
                        break

	bot1.print_stats()
	bot2.print_stats()
	print('')
'''
