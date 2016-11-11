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
group1.add_bot(bot1)
group1.add_bot(bot2)
group1.add_bot(bot3)

print()
group2.add_bot(bot4)
group2.add_bot(bot5)
group2.add_bot(bot6)

print()
group1.display_group()

print()
group2.display_group()

print()

#group fight

def group_fight(g1, g2):
        
        init_order = list()
        
        for bot in g1.bot_list:
                init_order.append([bot, bot.initiative_roll()])
        init_order.sort(key=lambda x: x[1])

        fight_order = list()

        for i in range(0, len(init_order)):
                fight_order.append(init_order[i][0])

        for bot in fight_order:
                print(bot.name+' acts')
                bot2 = g2.bot_list[random.randint(0, len(g2.bot_list) - 1)]
                if bot.melee_hit(bot2):
                        bot2.take_damage(bot.melee_dmg)

group_fight(group1, group2)
group_fight(group2, group1)

print()
group1.display_group()

print()
group2.display_group()
