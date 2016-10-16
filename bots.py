import random

class Bot():

        def __init__(self, name, hp_max, hp, initiative, move_speed, melee_hit_percent, melee_dmg, ranged_hit_percent, ranged_dmg, evasion_percent):

                self.name = name
                self.hp_max = hp_max
                self.hp = hp
                self.initiative = initiative
                self.move_speed = move_speed
                self.melee_hit_percent = melee_hit_percent
                self.melee_dmg = melee_dmg
                self.ranged_hit_percent = ranged_hit_percent
                self.ranged_dmg = ranged_dmg
                self.evasion_percent = evasion_percent

        def print_stats(self):
                print(self.name+' HP: '+str(self.hp)+'/'+str(self.hp_max))

        def initiative_roll(self):
                initiative_roll = random.randint(0, self.initiative)
                return initiative_roll

        def melee_hit(self, other_bot, hit_mod = 0):

                chance_to_hit = random.randint(1, 100)
                chance_to_crit = random.randint(1, 100)
                
                if chance_to_crit >= 95:
                        print(self.name+' autohit '+other_bot.name)
                        return True
                elif chance_to_crit <= 5:
                        print(self.name+' autofail '+other_bot.name)
                        return False

                if chance_to_hit <= self.melee_hit_percent + hit_mod:
                        if random.randint(1, 100) > other_bot.evasion_percent:
                                print(self.name+' hit ('+str(chance_to_hit)+'/'+str(self.melee_hit_percent)+') '+other_bot.name)
                                return True
                        else:
                                print(other_bot.name+' evaded')
                                return False
                else:
                        print(self.name+' missed ('+str(chance_to_hit)+'/'+str(self.melee_hit_percent)+') '+other_bot.name)
                        return False

        def ranged_hit(self, other_bot):
                pass

        def take_damage(self, dmgAmount):
                self.hp = self.hp - dmgAmount
                if self.hp <= 0:
                        print(self.name + ' is dead!')
