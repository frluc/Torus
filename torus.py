#Torus

import random
from bots import Bot

#creating 2 bots

bot1 = Bot('Bob', 20, 20, 10, 1, 80, 5, 40, 3, 20)
bot2 = Bot('Bill', 20, 20, 8, 2, 70, 6, 40, 3, 30)

bot1.print_stats()
bot2.print_stats()

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

	bot1.print_stats()
	bot2.print_stats()
	print('')
