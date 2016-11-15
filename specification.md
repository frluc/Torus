#Specifications

##Combat organisation

**I pre-combat :**

1. organize groups
2. groups orders
3. groups placement
4. initial initiative

**II combat cycle :**

1. adjust orders and initiative
2. resolve move
3. range round
4. melee round
5. push resolution
6. check win

**III post-combat :**

1. loot generation
2. report

##General combat principles

###ORDERS
Each group has 3 seperate orders :

1. move order = back/stay/forward
2. melee stance = hold/through
3. range stance = hold fire/fire once/fire at will

Hold melee stance has 2 consequences :

* group will stay in place if they meet a foe even if move order is forward
* group will try to block foes from going through

Hold melee stance has 2 consequences :

* group will try to go through foes if move order is forward
* group won't try to block foes from going through

Fire once range stance will cause the group to do a range attack as soon as possible, order will then automatically change to hold fire.  
Fire at will range stance will cause the group to do a range attack whenever possible.  

>Groups, orders, and initiative are set before actual combat, without knowing what the foe will set up.  
They can be adjusted slightly at the beginning of every combat cycle.  

###RESOLVE MOVE
Each group will attempt one by one to move toward their destination.  
A group can move if destination meets the following conditions :

* move order is not stay
* (group size + allies already at destination) < destination size
* not currently engaged in melee

Groups trying to push must be flagged for push resolution phase :

* group is engaged in melee
* attempting to move
* has through melee stance

###RANGE ROUND
Each group by order of initiative is cycled through.

If group range stance is hold fire  
or group doesn't have range units  
or group is melee engaged  
then skip phase for the group  

For range units, check for every range unit if foe in range and attack if possible.
  
If 1+ units has attacked and range stance is fire once  
then range order becomes hold fire.  

###MELEE ROUND
Each group by order of initiative is cycled through.  
If group is melee engaged  
then group attacks.  


###PUSH RESOLUTION
Each group is cycled, no order required.  

If group is flagged for push resolution, do all necesarry tests :

* (group size + allies already at destination) < destination size 
* foes in cell with HOLD melee stance ?

Depending if there are holding foes or not,
compare sum group individual push stat VS sum HOLD foes block stat.

Success means the group moves to destination, fails mean it stays in place.  

###CHECK WIN
If one win condition is met, stop the cycle and go to post-combat phase
