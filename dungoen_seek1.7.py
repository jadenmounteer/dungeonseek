#imports
from random import randint

#CLASSES (Classes of objects in the game, character, zombie, etc.)
class Player_Character:
    """ This is the character class. It contains all of the methods and attributes of the player's character. """
    def __init__(self, hit_points, max_hit_points, sword_skill, archery_skill, magic_skill, armor_skill, speed, stealth, strength, experience_points, barter_skill, player_level, player_class,
     player_name, points_to_allocate, room_location, dungeon_location, player_battle_cry, inventory, gold, player_in_combat, base_amount_of_damage, attacking_with):
        '''This function configures the player's attributes.'''
        self.hit_points = 0
        self.max_hit_points = 0 #These will increase as you level up. Your current hitpoints can never surpass your max hit points.
        self.sword_skill = 0
        self.archery_skill = 0
        self.magic_skill = 0
        self.armor_skill = 0
        self.speed = 0
        self.stealth = 0
        self.strength = 0
        self.experience_points = 0
        self.barter_skill = 0
        self.player_level = 1
        self.player_class = "Not chosen."
        self.player_name = "Not chosen."
        self.points_to_allocate = 0 #You can allocate these points when you level up.
        self.room_location = 0
        self.dungeon_location = ""
        self.player_battle_cry = "For Narnia!"
        self.inventory = []
        self.gold = 0
        self.player_in_combat = False
        self.base_amount_of_damage = 0 #This is the base amount of damage caused by the player while attacking an enemy using a sword, spell, or bow.
        self.attacking_with = "" #This attribute is updated when the player is attacking with a certain spell or weapon. It is used to see what kind of influence it has on the enemy.
    def battle_cry(self):
        return self.player_name + ": " + self.player_battle_cry + "!"
    def player_turn(self):
        """
        This function is called when it is the player's turn in combat.
        Shows that it is the player's turn. Asks what you would like to do.
        Displays the available options and the chance of success based on the enemy's attributes.
        Returns how the player would like to proceed. 
        """
        print()
        print("It is " + self.player_name + "'s turn!")
        print()

        #Asks the player to take action and creates a variable to store the player's action.
        print("What would you like to do?")
        player_action = ""
        print()

        #shows the actions available. Maybe put this in a while loop so you can periodically see your stats.
        action_taken = False 
        while action_taken == False:
            print("1 Attack with sword.")
            print("2 Attack with magic.")
            print("3 Attack with bow.")
            print("4 Use item.")
            print("5 Sneak away.")
            print("6 Run away.")
            print("7 View character stats.")
            player_action = input("Type the number of your action: ")
            
            #depending on the player's action, do something: 
            if player_action == "1":
                print("You attack with your sword.")
                action_taken = True
                break
            elif player_action == "2":
                self.use_spell()
                action_taken = True
                break
            elif player_action == "3":
                print("You attack with your bow.")
                action_taken = True
                break
            elif player_action == "4":
                print("You use an item.")
                action_taken = True
                break
            elif player_action == "5":
                print("You sneak away.")
                action_taken = True
            elif player_action == "6":
                print("You run away.")
                action_taken = True
                break 
            elif player_action == "7":
                view_character_stats()
            else:
                print("Please type a number from 1 to 7.")

            print()
            input("Press ENTER to continue.")
        return player_action
    def player_turn_non_combat(self):
        """
        This function is called when the player enters an empty room or after combat.
        Asks what you would like to do.
        Displays the available options: Look around, use spell, go left, go right, view stats, etc.
        Returns how the player would like to proceed. 
        """
    def use_spell(self):
        """ 
        This function is called by the  player_turn or the player_turn_non_combat functions.
        The player will now be able to choose which spell to use. If the player is in combat, his combat spells to combat things. If not, his spells do different things.
        The function first checks the player's magic level and determins the spells he can use from there.
        Then the function checks if the player is in combat and calls the correct function from the spell object.
        
         """
        print()
        print("Choose a spell to use...")

        #Gives the player a list of spells to use depending on the player's magic skill.

        spell_chosen = False

        # 1st tier spells
        if self.magic_skill >= 25 and self.magic_skill < 35:
            print()
            print("1 " + sparks_spell.description)
            print()
            spell_to_use = input("Type the number of the spell you wish to use: ")      
            #Depending on the spell the player chooses, call the function of that spell from the spell object.
            while spell_chosen != True:
                if spell_to_use == "1":
                    #If the player is in combat, call the use_spell_in_combat() function. If the player is outside of combat, call the non-combat function.
                    if self.player_in_combat == True:
                        print(sparks_spell.use_spell_in_combat())
                    elif self.player_in_combat == False:
                        print(sparks_spell.use_spell_outside_of_combat())
                    spell_chosen = False
                    break
        
        # 2nd tier spells
        elif self.magic_skill >= 35 and self.magic_skill < 45:
            print()
            print("1 " + sparks_spell.description)
            print("2 " + healing_spell.description)
            spell_to_use = input("Type the number of the spell you wish to use: ")
            #Depending on the spell the player chooses, call the function of that spell from the spell object.
            while spell_chosen != True:
                #Sparks spell
                if spell_to_use == "1":
                    #If the player is in combat, call the use_spell_in_combat() function. If the player is outside of combat, call the non-combat function.
                    if self.player_in_combat == True:
                        print(sparks_spell.use_spell_in_combat())
                    elif self.player_in_combat == False:
                        print(sparks_spell.use_spell_outside_of_combat())
                    spell_chosen = True
                    break
                #Healing spell
                elif spell_to_use == "2":
                    if self.player_in_combat == True:
                        print(healing_spell.use_spell_in_combat())
                    elif self.player_in_combat == False:
                        print(healing_spell.use_spell_outside_of_combat())
                    spell_chosen = True
                    break
                        
        # 3rd tier spells
        elif self.magic_skill >= 45 and self.magic_skill < 55:
            print("1 " + sparks_spell.description)
            print("2 " + healing_spell.description)
            print("3 " + fire_ball_spell.description)
            spell_to_use = input("Type the number of the spell you wish to use: ")
            #Depending on the spell the player chooses, call the function of that spell from the spell object.
            while spell_chosen != True:
                #Sparks spell
                if spell_to_use == "1":
                    #If the player is in combat, call the use_spell_in_combat() function. If the player is outside of combat, call the non-combat function.
                    if self.player_in_combat == True:
                        print(sparks_spell.use_spell_in_combat())
                    elif self.player_in_combat == False:
                        print(sparks_spell.use_spell_outside_of_combat())
                    spell_chosen = True
                    break
                #Healing spell
                elif spell_to_use == "2":
                    if self.player_in_combat == True:
                        print(healing_spell.use_spell_in_combat())
                    elif self.player_in_combat == False:
                        print(healing_spell.use_spell_outside_of_combat())
                    spell_chosen = True
                    break
                #Fireball spell
                elif spell_to_use == "3":
                    if self.player_in_combat == True:
                        print(fire_ball_spell.use_spell_in_combat())
                    elif self.player_in_combat == False:
                        print(fire_ball_spell.use_spell_outside_of_combat())
                    spell_chosen = True
                    break

        # 4th tier spells
        elif self.magic_skill >= 55 and self.magic_skill < 65:
            print()
            print("1 " + sparks_spell.description)
            print("2 " + healing_spell.description)
            print("3 " + fire_ball_spell.description)
            print("4 " + telekinesis_spell.description)
            spell_to_use = input("Type the number of the spell you wish to use: ")
            #Depending on the spell the player chooses, call the function of that spell from the spell object.
            while spell_chosen != True:
                #Sparks spell
                if spell_to_use == "1":
                    #If the player is in combat, call the use_spell_in_combat() function. If the player is outside of combat, call the non-combat function.
                    if self.player_in_combat == True:
                        print(sparks_spell.use_spell_in_combat())
                    elif self.player_in_combat == False:
                        print(sparks_spell.use_spell_outside_of_combat())
                    spell_chosen = True
                    break
                #Healing spell
                elif spell_to_use == "2":
                    if self.player_in_combat == True:
                        print(healing_spell.use_spell_in_combat())
                    elif self.player_in_combat == False:
                        print(healing_spell.use_spell_outside_of_combat())
                    spell_chosen = True
                    break
                #Fireball spell
                elif spell_to_use == "3":
                    if self.player_in_combat == True:
                        print(fire_ball_spell.use_spell_in_combat())
                    elif self.player_in_combat == False:
                        print(fire_ball_spell.use_spell_outside_of_combat())
                    spell_chosen = True
                    break
                #Telekinesis spell
                elif spell_to_use == "4":
                    if self.player_in_combat == True:
                        print(telekinesis_spell.use_spell_in_combat())
                    elif self.player_in_combat == False:
                        print(telekinesis_spell.use_spell_outside_of_combat())
                    spell_chosen = True
                    break
            return ""
#Create a Trader class here. He can have methods of introducing the player to each dungeon, trading, etc. Maybe he can be the final boss.

#Enemy classes
class Zombie:
    def __init__(self, name, hit_points, strength, status, speed, armor, weakness, base_amount_of_damage):
        self.name = name
        self.hit_points = hit_points
        self.strength = strength
        self.status = status
        self.speed = speed
        self.armor = armor
        self.weakness = weakness
        self.base_amount_of_damage = base_amount_of_damage
    def battle_cry(self):
        '''This function makes the zombie moan.'''
        print(self.name + ": " + "Uuuhhh")
        return ""
    def appear(self):
        '''This function describes the zombie appearing to the player. Using the randint function, it chooses from multiple descriptions.'''
        random_number = randint(1, 2)
        print()
        if random_number == 1:
            print("A figure limps towards you from the distance. As it draws closer you can see that it is a living corpse.")
            print("Its loose jaw falls open and a manacing moan leaves its mouth. It is coming straight for you.")
        elif random_number == 2:
            print('''Jeff the zombie approaches... 
                    ''')
        
    def turn(self):
        '''
        This function is called when it is the zombie's turn in combat.
        The zombie will attack and, using a random number as well as the enemy's attack attribute, it will calculate the
        base amount of damage. 
        '''
        print(self.name + " attacks!")
        print()
        input("Press ENTER to continue.")
    def death(self, cause_of_death):
        """ 
        This function takes the cause of death as a parameter. (player.attacking_with). Using an if statement, it outputs a description of the death.
        Causes of death include: Electricity, Psychic, Steel, Fire.
         """
        if cause_of_death == "Electricity":
            return self.name + " goes stiff as the electricity runs it's course through its body. Smoke rises from its head and it topples over defeated."
        elif cause_of_death == "Fire":
            return self.name + " catches fire. It doesn't seem to notice as it stumbles toward you. With its next step, it looses its footing and topples forward in a burning heap."
        else:
            return "Cause of death unknown."
class Fire_zombie(Zombie):
    def __init__(self, name, hit_points, strength, status, type, speed, armor, weakness, base_amount_of_damage):
        Zombie.__init__(self, name, hit_points, strength, status, speed, armor, weakness, base_amount_of_damage)
        self.type = "Fire"
class Poltergiest:
    def __init__(self, name, hit_points, archery, anger, armor):
        self.name = name
        self.hit_points = hit_points
        self.archery = archery
        self.anger = anger
        self.armor = armor
    def battle_cry(self):
        '''This function is the Poltergiest's battle cry.'''
        print(self.name + ": " + "oooooh!")
        return ""
    def turn(self):
        '''This function is called when it is the Poltergiest's turn in combat.'''
        print(self.name + " attacks!")
        print()
        input("Press ENTER to continue.")
class Quiz_Poltergiest(Poltergiest):
    def __init__(self, name, hit_points, archery, anger, armor, weakness):
        self.name = name
        self.hit_points = hit_points
        self.archery = archery
        self.anger = anger
        self.armor = armor
        self.weakness = weakness
    def quiz(self):
        '''This asks the player questions'''
     #input(self.name + ": " + "What month of the year has twenty eight days?")
        num = randint(1, 3)
        ghostRiddle1 = "What has to be broken before you can use it?"
        ghostRiddle2 = "What month has 28 days in it?"
        ghostRiddle3 = "I shave everyday, but my beard stays the same, what am I?"
        print(self.name + ": " + "I have a riddle for you, answer incorrectly and you die...")
        print("")

        if num == 1:
            print(self.name + ": " + ghostRiddle1)    
        elif num == 2:
            print(self.name + ": " + ghostRiddle2)
        elif num == 3:
            print(self.name+ ": " + ghostRiddle3)

#Boss classes
class Vampire:
    def __init__(self, name, hit_points, strength, status, speed):
        self.name = name
        self.hit_points = hit_points
        self.strength = strength
        self.status = status
        self.speed = speed

#Weapon classes. Maybe have these act just like spells. Each weapon has unique attributes.
class Sword:
    def __init__(self, name, hit_points, strength, status, speed):
        self.name = name
        self.hit_points = hit_points
        self.strength = strength
        self.status = status
        self.speed = speed
class Bow:
    def __init__(self, name, hit_points, strength, status, speed):
        self.name = name
        self.hit_points = hit_points
        self.strength = strength
        self.status = status
        self.speed = speed

#Spell classes
class Healing_spell:
    def __init__(self, description, attack_type):
        self.description = description
        self.attack_type = attack_type
    def use_spell_in_combat(self):
        """ This function calls the healing spell if the player is in combat. The spell will heal the player and then end his turn.
         Use a random int and the player's magic skill to determine how many hp it restores. """

        #Sets the player's base amount of damage done to 0.
        player.base_amount_of_damage = 0
        #sets the player attacking with to healing
        player.attacking_with = self.attack_type
        #Determins the amount to heal the player caused by dividing the player's magic skill by 10 to get the modifier, and then adding that to a random number between 1 and 20.
        hit_points_healed = (player.magic_skill / 10) + randint(1, 20)
        #Determins whether or not the spell will heal the player for more than his max hit points. If it will, it subtracts 1 from the hit points healed until it is equal to the max hit points.
        while (player.hit_points + hit_points_healed) > player.max_hit_points:
            hit_points_healed -= 1

        #Adds the hit_points_healed to the player's hit points.
        player.hit_points += hit_points_healed

        #determins the description of what happens based on the hp points restored. Returns how much hp was restored.
        return "You use the healing spell in combat to heal you " + str(hit_points_healed) + " hit points. You now have " + str(player.hit_points) + " hit points."
    def use_spell_outside_of_combat(self):
        """ This function calls the healing spell if the player is not in combat. """

        

        return "You use the healing spell outside of combat."
class Fireball_spell:
    def __init__(self, description, attack_type):
        self.description = description
        self.attack_type = attack_type
    def use_spell_in_combat(self):
        """ 
        This function calls the fireball spell if the player is in combat.
        Changes the attacking_with variable to be the fireball attack type.
        Calculates the base mount of damage.

        """
        print()
        #Changes the variable attacking_with to be fireball attack type (Fire).
        player.attacking_with = fire_ball_spell.attack_type
        #Determines the base amount of damage caused by dividing the player's magic skill by 10 to get the modifier, and then adding that to a random number between 1 and 20.
        player.base_amount_of_damage = (player.magic_skill / 10) + randint(1, 20)
        #Returns the base amount of damage caused by the spell and the description based on the number. Uses an if statement.
        if player.base_amount_of_damage >= 20:
            return "A ball of blue fire erupts from your outstretched arms and spins through the air."
        else:
            return player.player_name + " attacks with fireball spell."
    def use_spell_outside_of_combat(self):
        """ 
        This function calls the fireball spell if the player is not in combat.
        
        """

        return player.player_name + " uses the fireball spell."
class Telekinesis_spell:
    def __init__(self, description, attack_type):
        self.description = description
        self.attack_type = attack_type
    def use_spell_in_combat(self):
        """ 
        This function calls the telekinesis spell if the player is in combat.
        Changes the attacking_with variable to be the telekinesis attack type.
        Calculates the base mount of damage.

        """
        print()
        #Changes the variable attacking_with to be telekinesis attack type (Psychic).
        player.attacking_with = telekinesis_spell.attack_type
        #Determines the base amount of damage caused by dividing the player's magic skill by 10 to get the modifier, and then adding that to a random number between 1 and 20.
        player.base_amount_of_damage = (player.magic_skill / 10) + randint(1, 20)
        #Returns the base amount of damage caused by the spell and the description based on the number. Uses an if statement.
    
        return player.player_name + " attacks with telekinesis."
    def use_spell_outside_of_combat(self):
        """ 
        This function calls the telekinesis spell if the player is not in combat.
        
        """
        return "You use the telekinesis spell outside of combat."
class Sparks_spell:
    def __init__(self, description, attack_type):
        self.description = description
        self.attack_type = attack_type
    def use_spell_in_combat(self):
        """ 
        This function calls the sparks spell if the player is in combat.
        This spell will shock an enemy with electricity. Changes the variable attacking_with to the spark spell attack type.
        Using the player's magic skill and a random number, determines the base amount of damage it will cause.

        """
        print()
        #Changes the variable attacking_with to be sparks_spell attack type (Electricity) in the player object.
        player.attacking_with = sparks_spell.attack_type
        #Determines the base amount of damage caused by dividing the player's magic skill by 10 to get the modifier, and then adding that to a random number between 1 and 20.
        player.base_amount_of_damage = (player.magic_skill / 10) + randint(1, 20)
        #Returns the base amount of damage caused by the spell and the description based on the number. Uses an if statement.
        if player.base_amount_of_damage >= 20:
            return "Streaks of blue lightning flash from your outstretched hands."
        elif player.base_amount_of_damage >= 10:
            return "Bright sparks erupt from your fingertips."
        else:
            return player.player_name + " attacks with Sparks spell."
    def use_spell_outside_of_combat(self):
        """ 
        This function calls the sparks spell if the player is not in combat.
        This spell will produce light for the player to see. Maybe we can have the player operate machinery or something in certain areas.
        
        """
        print()
        return "You use the sparks speel while not in combat."
   
#OBJECTS (Objects of classes in the game.) Put these in the dungeon spawner functions, except for the player.
player = Player_Character(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, "Not chosen", "Not chosen", 0, 0, "", "For Narnia!", [], 0, False, 0, "")

#Spell Objects. Can I put this code in the Level_up() function? That way these are called into existence when the player learns the spell?
healing_spell = Healing_spell("Healing Spell - Healing light that pours from your fingertips.", "Healing")
fire_ball_spell = Fireball_spell("Fireball - A ball of fire that envelopes your enemies in flames.", "Fire")
telekinesis_spell = Telekinesis_spell("Telekinesis - You can levitate objects with your mere thought.", "Psychic")
sparks_spell = Sparks_spell("Sparks - Electricity races from your fingertips, sending a shock to your enemies.", "Electricity")

#FUNCTIONS (Spawn enemies)
def spawn_dungeon1_enemy(random_number):
    '''This function will spawn an enemy in the Tomb of the Undead dungeon. Using an if statement and a random number, an object is created for a monster. 
    This function is called in every room of the dungeon_level_1() function. Have 5-10 enemies for the first dungeon.'''

    if random_number == 1:
        #Spawn Jeff the zombie and give a short description using the appear() function.
        zombie1 = Zombie("Jeff the zombie", 20, 15, "alive", 10, 20, "Fire", 0)
        zombie1.appear()
        print()
        #Jeff moans by calling the battle_cry() function from the Zombie class.
        zombie1.battle_cry() 

        #Triggers combat between Jeff the zombie and the player.
        combat_1v1(player, zombie1)

    elif random_number == 2:
        print("A knife weilding zombie appears.")
        zombie2 = Zombie("Knife weilding Zombie", 10, 40, "alive", 15, 20, "Fire", 0)
        print()
        
        combat_1v1(player, zombie2)
    elif random_number == 3:
        print("A quiz ghost appears.")
        QUizghost = Quiz_Poltergiest("quiz ghost", 30, 20, 50, 30, "Psychic")
        print()
        combat_1v1(player, QUizghost)
def spawn_dungeon1_boss(random_number):
    '''This function will spawn a boss in the Tomb of the Undead dungeon. Using an if statement and a random number, an object is created for a boss. 
    This function is called in every room of the dungeon_level_1() function. With each room, the chances that the boss will spawn increases.'''

    if random_number == 1:
        #Spawn Blade the Vampire
        blade = Vampire("Blade", 20, 15, "alive", 10)
        #blade.appear()
        print()
        #Jeff moans by calling the battle_cry() function from the Zombie class.
        #blade.battle_cry() 


#FUNCTIONS (Rooms and locations and their descriptions.)
def dungeon_level_1_description_generator(random_number):
    '''This function generates a random description of a room based on the random_number parameter. Add maybe 10-15 different descriptions.'''
    if random_number == 1:
        return "You enter a dark and foreboding room."
    elif random_number == 2:
        return "You enter a cavern lined with coffins on the walls."
    elif random_number == 3:
        return "You traverse a dark and stoney passageway until emerging in a cold and dark stoney room."
    elif random_number == 4:
        return """You make your way down a series of stoney stone steps. After a while you see torchlight coming from below.
 You continue until you emerge in a dimly lit tomb."""
    elif random_number == 5:
        return "You emerge into a dark cathedral. Moonlight seeps in from the stainglass windows and illuminates a series of pews."
    elif random_number == 6:
        return """You emerge into the open night. Looking around, you see damp grass littered with broken tombstones and open graves.
 A full and foreboding moon shines overhead."""
    elif random_number == 7:
        return """Soon you begin to feel damp soil with every step. The air turns cold and you enter a cavern. Stalagtites dot the ceiling.
 As you near a chamber, you begin to make out dim torchlite. As it grows closer, it illuminates a table littered with ancient bones."""
    elif random_number == 8:
        return """Suddenly, you free fall and hit the ground hard snapping bones as you hit. Dazed, you get your bearings and realize 
 that you didn't break your bones, but you landed on a pile of them. You seem to be in a pit. Someone had laid a trap."""

def dungeon_level_1():
    '''This is the first dungeon (series of rooms) the player enters in the game. He will be introduced to the object of the game and will encounter a level 1 monster which will be randomly 
    picked from the level 1 monsters list.'''

    #If player.location = 0, the player talks with the trader and the trader introduces the player to the object of the game. For later
    #levels, the player can barter with the trader. Maybe make a trader() function.
    print()
    print("Hello stranger. I am the trader. I'll have more to say later on, but for now, move into that room.")
    print()
    input("Press ENTER to enter the Tomb of the Undead.")


    #Changes the location of the player to the first room and dungeon.
    player.room_location += 1
    player.dungeon_location = "Tomb of the Undead."
    #combat_1v1(player, zombie1)

    #Loop: The player battles through a series of 5 rooms. When he has battled through them, the loop breaks.
    while player.room_location <= 5:
        print()
        print("You enter room " + str(player.room_location) + " of " + player.dungeon_location)
        print()

        #uses a random function and an if statement to randomly generate a description of the room using the dungeon_room_description() function.
        random_number = randint(1, 8)
        print(dungeon_level_1_description_generator(random_number))

        #Generates a random number and calls the spawn_dungeon1_enemy() function to spawn an enemy for the player to face.
        #random_number = randint(1, 3)
        random_number = 1 #spawns a zombie for testing purposes.
        spawn_dungeon1_enemy(random_number)

        #Randomly generates loot inside of the room.

        #calls the refresh() function to see if you are dead or need to level up.
        refresh()

        #Increments the room location number to make the player move onto the next room.
        player.room_location += 1

        #As you enter more rooms, increases the chance of spawing the boss.

    
    print("You made it through " + player.dungeon_location)
    #Sets the room location to 0 again in preparation for the next dungeon.
    player.room_location = 0

    #The room is set back to zero and the player moves onto the next dungeon where he meets with the trader again.

#FUNCTIONS (Flow of the game)
def combat_1v1(player, e):
    '''
    This function simulates 1v1 combat. The x parameter is the player and the e parameter is the enemy.
    The function first checks to see who wil attack first. Then, based on who goes first, it calls the turn function. These functions return...
    
    '''
    print(player.player_name + " and " + e.name + " enter combat.")
    #changes the player_in_combat function to True
    player.player_in_combat = True
    print()
    print(player.battle_cry())
    print()
    print(e.battle_cry())
    print()
    input("Press ENTER to continue.")

    #Generates a random number to decide who goes first.
    who_attacks_first = randint(1, 2)
    player_attacks_first = False
    enemy_attacks_first = False
    if who_attacks_first == 1:
        player_attacks_first = True  
    elif who_attacks_first == 2:
        enemy_attacks_first = True

    #Calls the attack functions specific to each class for whoever goes first. Maybe make this a while loop.

    # if the player attacks first:
    if player_attacks_first == True:
        while player.hit_points > 0 or e.hit_points > 0:
            #player.player_turn()
            print()
            player.player_turn()
            # Determines the base amount of damage caused by the attack.
            #This determines if the player is attacking with the enemy's weakness. If he is, it does 5 extra damage.
            if player.attacking_with == e.weakness:
                player.base_amount_of_damage += 5
                print(player.attacking_with + " is " + e.name + "'s weakness!")
                print()
            #Determines whether or not you miss. Your base amount of damage should be greater than the enemy's armor / 2. If not, your amount of damage is set to 0. This won't happen if the player is healing himself.
            if player.base_amount_of_damage < e.armor / 2 and player.attacking_with != "Healing":
                print("You miss!")
                player.base_amount_of_damage = 0
            print("You do " + str(player.base_amount_of_damage) + " points of damage!")
            print()
            e.hit_points = e.hit_points - player.base_amount_of_damage
            print(e.name + " hit points = " + str(e.hit_points))
            #if the enemy dies...
            if e.hit_points <= 0:
                #Calls a function taking what the player was attacking with as a parameter. The function outputs the description of the enemy's death.
                print(e.death(player.attacking_with))
                print(e.name + " defeated.")
                print()
                input("Press ENTER to continue.")
                break
            print()
            #Enemy's turn
            #calls the e.turn() function specific to the enemy.
            e.turn()
            print()
            #Determines the base amount of damage caused by the enemy's attack using the e.base_amount_of_damgage attribute.

            #Determines whether or not the enemy misses judging by the player's armor class.
            print(e.name + " misses!")
            print()
            input("Press ENTER to continue.")
            print()
            if player.hit_points <= 0:
                print("You died.")
                return

    #if the enemy attacks first
    elif enemy_attacks_first == True:
        while e.hit_points > 0 or player.hit_points > 0:
            e.turn()
            print()
            print(e.name + " misses!")
            print()
            input("Press ENTER to continue.")
            print()
            if player.hit_points <= 0:
                print("You died.")
                return
            #player's turn
            player.player_turn()
            # Determines the base amount of damage caused by the attack.
            #This determines if the player is attacking with the enemy's weakness. If he is, it does 5 extra damage.
            if player.attacking_with == e.weakness:
                player.base_amount_of_damage += 5
                print(player.attacking_with + " is " + e.name + "'s weakness!")
                print()
            #Determines whether or not you miss. Your base amount of damage should be greater than the enemy's armor / 2. This won't happen if the player is healing himself.
            if player.base_amount_of_damage < e.armor / 2 and player.attacking_with != "Healing":
                print("You miss!")
                player.base_amount_of_damage = 0
            print("You do " + str(player.base_amount_of_damage) + " points of damage!")
            print()
            e.hit_points = e.hit_points - player.base_amount_of_damage
            print(e.name + " hit points = " + str(e.hit_points))
            print()
            if e.hit_points <= 0:
                #Calls a function taking what the player was attacking with as a parameter. The function outputs the description of the enemy's death.
                print(e.death(player.attacking_with))
                print(e.name + " defeated.")
                print()
                input("Press ENTER to continue.")
                break
    #Changes the player_in_combat variable to False
    player.player_in_combat = False
        
def player_dead():
    '''This function checks to see if the player is still alive. If so, the game goes on, if not, it is game over. Each enemy class will have a specific death that they will cause the player to experience.
    The function will account for the enemy the player is engaging and use the following code to get the death: enemy.death(). This function could also check to see if you've won the game.'''
def level_up():
    '''
    This function checks to see if the player has enough points to level up. If he does, he is given 5 points to allocate to whichever skills he chooses.
    The function also notifies you of new attacks and spells that you can use when you increase in level with each attribute.

    '''
    #right now, the player levels up at every 10 experience points gained. He is also given 5 points to allocate to skills. We can change this later on.
    if player.experience_points == 10:
        player.points_to_allocate = 5
        player.player_level = player.player_level + 1
        print("______________")
        print()
        print("  LEVEL UP!")
        print("______________")
        print()
        print("You are now level: " + str(player.player_level))
        #lets the player allocate points to his skills.
        while player.points_to_allocate != 0:
            print()
            print("You have " + str(player.points_to_allocate) + " points to allocate.")
            print("Which skill would you like to allocate points to?")
            print()
            print("1  Hit Points: " + str(player.hit_points))
            print("2  Sword skill: " + str(player.sword_skill))
            print("3  Archery skill: " + str(player.archery_skill))
            print("4  Magic skill: " + str(player.magic_skill))
            print("5  Armor skill: " + str(player.armor_skill))
            print("6  Barter skill: " + str(player.barter_skill))
            print("7  Speed: " + str(player.speed))
            print("8  Stealth: " + str(player.stealth))
            print("9  Strength: " + str(player.strength))
            print()
            skill_to_allocate_points_to = input("Type the number of the skill you want to allocate points to: ")
            #Checks to see if the string entered was correct:
            while skill_to_allocate_points_to != "1":
                if skill_to_allocate_points_to == "2":
                    break
                elif skill_to_allocate_points_to == "3":
                    break
                elif skill_to_allocate_points_to == "4":
                    break
                elif skill_to_allocate_points_to == "5":
                    break
                elif skill_to_allocate_points_to == "6":
                    break
                elif skill_to_allocate_points_to == "7":
                    break
                elif skill_to_allocate_points_to == "8":
                    break
                elif skill_to_allocate_points_to == "9":
                    break
                skill_to_allocate_points_to = input("That number does not exist. Please type the number of the skill you want to allocate points to: ")
           
            #Using the skill the player chose, the user is now asked how many points he wants to allocate to that skill.

            #Hit Points
            if skill_to_allocate_points_to == "1":
                quantity_of_points_to_add = input("How many points would you like to add to your hit points? ")
                points_added = False
                while points_added == False:
                    if quantity_of_points_to_add == "1": 
                        player.max_hit_points = player.max_hit_points + 1
                        player.points_to_allocate = player.points_to_allocate - 1
                        num_of_points_added = 1
                        points_added = True
                    elif quantity_of_points_to_add == "2":
                        player.max_hit_points = player.max_hit_points + 2
                        player.points_to_allocate = player.points_to_allocate - 2
                        num_of_points_added = 2
                        points_added = True
                    elif quantity_of_points_to_add == "3":
                        player.max_hit_points = player.max_hit_points + 3
                        player.points_to_allocate = player.points_to_allocate - 3
                        num_of_points_added = 3
                        points_added = True
                    elif quantity_of_points_to_add == "4":
                        player.max_hit_points = player.max_hit_points + 4
                        player.points_to_allocate = player.points_to_allocate - 4
                        num_of_points_added = 4
                        points_added = True
                    elif quantity_of_points_to_add == "5":
                        player.max_hit_points = player.max_hit_points + 5
                        player.points_to_allocate = player.points_to_allocate - 5
                        num_of_points_added = 5
                        points_added = True
                    else:
                        quantity_of_points_to_add = input("Please enter a number from 1-5: ")
                #while loop that checks to see if you're trying to add too many points. If you added too many points, it fixes the issue.
                while num_of_points_added > (player.points_to_allocate + num_of_points_added): 
                    print("You cannot add more points than you have.")
                    player.max_hit_points = player.max_hit_points - num_of_points_added
                    player.points_to_allocate = player.points_to_allocate + num_of_points_added
                    break
                print("Your total hit points is now: " + str(player.max_hit_points))

            #Sword skill
            if skill_to_allocate_points_to == "2":
                quantity_of_points_to_add = input("How many points would you like to add to your sword skill? ")
                points_added = False
                while points_added == False:
                    if quantity_of_points_to_add == "1":
                        player.sword_skill = player.sword_skill + 1
                        player.points_to_allocate = player.points_to_allocate - 1
                        num_of_points_added = 1
                        points_added = True
                    elif quantity_of_points_to_add == "2":
                        player.sword_skill = player.sword_skill + 2
                        player.points_to_allocate = player.points_to_allocate - 2
                        num_of_points_added = 2
                        points_added = True
                    elif quantity_of_points_to_add == "3":
                        player.sword_skill = player.sword_skill + 3
                        player.points_to_allocate = player.points_to_allocate - 3
                        num_of_points_added = 3
                        points_added = True
                    elif quantity_of_points_to_add == "4":
                        player.sword_skill = player.sword_skill + 4
                        player.points_to_allocate = player.points_to_allocate - 4
                        num_of_points_added = 4
                        points_added = True
                    elif quantity_of_points_to_add == "5":
                        player.sword_skill = player.sword_skill + 5
                        player.points_to_allocate = player.points_to_allocate - 5
                        num_of_points_added = 5
                        points_added = True
                    else:
                        quantity_of_points_to_add = input("Please enter a number from 1-5: ")
                #while loop that checks to see if you're trying to add too many points. If you added too many points, it fixes the issue.
                while num_of_points_added > (player.points_to_allocate + num_of_points_added): 
                    print("You cannot add more points than you have.")
                    player.sword_skill = player.sword_skill - num_of_points_added
                    player.points_to_allocate = player.points_to_allocate + num_of_points_added
                    break
                print("Your sword skill is now: " + str(player.sword_skill))

            #Archery skill
            if skill_to_allocate_points_to == "3":
                quantity_of_points_to_add = input("How many points would you like to add to your archery skill? ")
                points_added = False
                while points_added == False:
                    if quantity_of_points_to_add == "1":
                        player.archery_skill = player.archery_skill + 1
                        player.points_to_allocate = player.points_to_allocate - 1
                        num_of_points_added = 1
                        points_added = True
                    elif quantity_of_points_to_add == "2":
                        player.archery_skill = player.archery_skill + 2
                        player.points_to_allocate = player.points_to_allocate - 2
                        num_of_points_added = 2
                        points_added = True
                    elif quantity_of_points_to_add == "3":
                        player.archery_skill = player.archery_skill + 3
                        player.points_to_allocate = player.points_to_allocate - 3
                        num_of_points_added = 3
                        points_added = True
                    elif quantity_of_points_to_add == "4":
                        player.archery_skill = player.archery_skill + 4
                        player.points_to_allocate = player.points_to_allocate - 4
                        num_of_points_added = 4
                        points_added = True
                    elif quantity_of_points_to_add == "5":
                        player.archery_skill = player.archery_skill + 5
                        player.points_to_allocate = player.points_to_allocate - 5
                        num_of_points_added = 5
                        points_added = True
                    else:
                        quantity_of_points_to_add = input("Please enter a number from 1-5: ")
                #while loop that checks to see if you're trying to add too many points. If you added too many points, it fixes the issue.
                while num_of_points_added > (player.points_to_allocate + num_of_points_added): 
                    print("You cannot add more points than you have.")
                    player.archery_skill = player.archery_skill - num_of_points_added
                    player.points_to_allocate = player.points_to_allocate + num_of_points_added
                    break
                print("Your archery skill is now: " + str(player.archery_skill))
            
            #Magic skill
            if skill_to_allocate_points_to == "4":
                quantity_of_points_to_add = input("How many points would you like to add to your magic skill? ")
                points_added = False
                while points_added == False:
                    if quantity_of_points_to_add == "1":
                        player.magic_skill = player.magic_skill + 1
                        player.points_to_allocate = player.points_to_allocate - 1
                        num_of_points_added = 1
                        points_added = True
                    elif quantity_of_points_to_add == "2":
                        player.magic_skill = player.magic_skill + 2
                        player.points_to_allocate = player.points_to_allocate - 2
                        num_of_points_added = 2
                        points_added = True
                    elif quantity_of_points_to_add == "3":
                        player.magic_skill = player.magic_skill + 3
                        player.points_to_allocate = player.points_to_allocate - 3
                        num_of_points_added = 3
                        points_added = True
                    elif quantity_of_points_to_add == "4":
                        player.magic_skill = player.magic_skill + 4
                        player.points_to_allocate = player.points_to_allocate - 4
                        num_of_points_added = 4
                        points_added = True
                    elif quantity_of_points_to_add == "5":
                        player.magic_skill = player.magic_skill + 5
                        player.points_to_allocate = player.points_to_allocate - 5
                        num_of_points_added = 5
                        points_added = True
                    else:
                        quantity_of_points_to_add = input("Please enter a number from 1-5: ")
                #while loop that checks to see if you're trying to add too many points. If you added too many points, it fixes the issue.
                while num_of_points_added > (player.points_to_allocate + num_of_points_added): 
                    print("You cannot add more points than you have.")
                    player.magic_skill = player.magic_skill - num_of_points_added
                    player.points_to_allocate = player.points_to_allocate + num_of_points_added
                    break
                print()
                print("Your magic skill is now: " + str(player.magic_skill))
                print()

                #Depending on the player's magic skill, the player is notified that they can now use certain spells:
                if player.magic_skill >= 25 and player.magic_skill < 35:
                    print("You are now a newbie magician. You learn the Sparks spell. ")
                    input("Press ENTER to continue.")
                    print()
                    print("You can now use the following list of spells:")
                    print(sparks_spell.description)
                    print()
                elif player.magic_skill >= 35 and player.magic_skill < 45:
                    print("You are now an experienced magician. You learn the Healing Spell.")
                    input("Press ENTER to continue.")
                    print()
                    print("You can now use the following list of spells:")
                    print(sparks_spell.description)
                    print(healing_spell.description)
                elif player.magic_skill >= 45 and player.magic_skill < 55:
                    print("You are now a Wizard's apprentice. You learn the fireball spell.")
                    input("Press ENTER to continue.")
                    print()
                    print("You can now use the following list of spells:")
                    print(sparks_spell.description)
                    print(healing_spell.description)
                    print(fire_ball_spell.description)
                elif player.magic_skill >= 55 and player.magic_skill < 65:
                    print("You are now a journeyman wizard. You learn the telekinesis spell.")
                    input("Press ENTER to continue.")
                    print()
                    print("You can now use the following list of spells:")
                    print(sparks_spell.description)
                    print(healing_spell.description)
                    print(fire_ball_spell.description)
                    print(telekinesis_spell.description)


            #Amor skill
            if skill_to_allocate_points_to == "5":
                quantity_of_points_to_add = input("How many points would you like to add to your armor skill? ")
                points_added = False
                while points_added == False:
                    if quantity_of_points_to_add == "1":
                        player.armor_skill = player.armor_skill + 1
                        player.points_to_allocate = player.points_to_allocate - 1
                        num_of_points_added = 1
                        points_added = True
                    elif quantity_of_points_to_add == "2":
                        player.armor_skill = player.armor_skill + 2
                        player.points_to_allocate = player.points_to_allocate - 2
                        num_of_points_added = 2
                        points_added = True
                    elif quantity_of_points_to_add == "3":
                        player.armor_skill = player.armor_skill + 3
                        player.points_to_allocate = player.points_to_allocate - 3
                        num_of_points_added = 3
                        points_added = True
                    elif quantity_of_points_to_add == "4":
                        player.armor_skill = player.armor_skill + 4
                        player.points_to_allocate = player.points_to_allocate - 4
                        num_of_points_added = 4
                        points_added = True
                    elif quantity_of_points_to_add == "5":
                        player.armor_skill = player.armor_skill + 5
                        player.points_to_allocate = player.points_to_allocate - 5
                        num_of_points_added = 5
                        points_added = True
                    else:
                        quantity_of_points_to_add = input("Please enter a number from 1-5: ")
                #while loop that checks to see if you're trying to add too many points. If you added too many points, it fixes the issue.
                while num_of_points_added > (player.points_to_allocate + num_of_points_added): 
                    print("You cannot add more points than you have.")
                    player.armor_skill = player.armor_skill - num_of_points_added
                    player.points_to_allocate = player.points_to_allocate + num_of_points_added
                    break
                print("Your armor skill is now: " + str(player.armor_skill))
            
            #Barter skill
            if skill_to_allocate_points_to == "6":
                quantity_of_points_to_add = input("How many points would you like to add to your barter skill? ")
                points_added = False
                while points_added == False:
                    if quantity_of_points_to_add == "1":
                        player.barter_skill = player.barter_skill + 1
                        player.points_to_allocate = player.points_to_allocate - 1
                        num_of_points_added = 1
                        points_added = True
                    elif quantity_of_points_to_add == "2":
                        player.barter_skill = player.barter_skill + 2
                        player.points_to_allocate = player.points_to_allocate - 2
                        num_of_points_added = 2
                        points_added = True
                    elif quantity_of_points_to_add == "3":
                        player.barter_skill = player.barter_skill + 3
                        player.points_to_allocate = player.points_to_allocate - 3
                        num_of_points_added = 3
                        points_added = True
                    elif quantity_of_points_to_add == "4":
                        player.barter_skill = player.barter_skill + 4
                        player.points_to_allocate = player.points_to_allocate - 4
                        num_of_points_added = 4
                        points_added = True
                    elif quantity_of_points_to_add == "5":
                        player.barter_skill = player.barter_skill + 5
                        player.points_to_allocate = player.points_to_allocate - 5
                        num_of_points_added = 5
                        points_added = True
                    else:
                        quantity_of_points_to_add = input("Please enter a number from 1-5: ")
                #while loop that checks to see if you're trying to add too many points. If you added too many points, it fixes the issue.
                while num_of_points_added > (player.points_to_allocate + num_of_points_added): 
                    print("You cannot add more points than you have.")
                    player.barter_skill = player.barter_skill - num_of_points_added
                    player.points_to_allocate = player.points_to_allocate + num_of_points_added
                    break
                print("Your barter skill is now: " + str(player.barter_skill))
            
            #Speed
            if skill_to_allocate_points_to == "7":
                quantity_of_points_to_add = input("How many points would you like to add to your speed? ")
                points_added = False
                while points_added == False:
                    if quantity_of_points_to_add == "1":
                        player.speed = player.speed + 1
                        player.points_to_allocate = player.points_to_allocate - 1
                        num_of_points_added = 1
                        points_added = True
                    elif quantity_of_points_to_add == "2":
                        player.speed = player.speed + 2
                        player.points_to_allocate = player.points_to_allocate - 2
                        num_of_points_added = 2
                        points_added = True
                    elif quantity_of_points_to_add == "3":
                        player.speed = player.speed + 3
                        player.points_to_allocate = player.points_to_allocate - 3
                        num_of_points_added = 3
                        points_added = True
                    elif quantity_of_points_to_add == "4":
                        player.speed = player.speed + 4
                        player.points_to_allocate = player.points_to_allocate - 4
                        num_of_points_added = 4
                        points_added = True
                    elif quantity_of_points_to_add == "5":
                        player.speed = player.speed + 5
                        player.points_to_allocate = player.points_to_allocate - 5
                        num_of_points_added = 5
                        points_added = True
                    else:
                        quantity_of_points_to_add = input("Please enter a number from 1-5: ")
                #while loop that checks to see if you're trying to add too many points. If you added too many points, it fixes the issue.
                while num_of_points_added > (player.points_to_allocate + num_of_points_added): 
                    print("You cannot add more points than you have.")
                    player.speed = player.speed - num_of_points_added
                    player.points_to_allocate = player.points_to_allocate + num_of_points_added
                    break
                print("Your speed is now: " + str(player.speed))

            #Stealth
            if skill_to_allocate_points_to == "8":
                quantity_of_points_to_add = input("How many points would you like to add to your stealth? ")
                points_added = False
                while points_added == False:
                    if quantity_of_points_to_add == "1":
                        player.stealth = player.stealth + 1
                        player.points_to_allocate = player.points_to_allocate - 1
                        num_of_points_added = 1
                        points_added = True
                    elif quantity_of_points_to_add == "2":
                        player.stealth = player.stealth + 2
                        player.points_to_allocate = player.points_to_allocate - 2
                        num_of_points_added = 2
                        points_added = True
                    elif quantity_of_points_to_add == "3":
                        player.stealth = player.stealth + 3
                        player.points_to_allocate = player.points_to_allocate - 3
                        num_of_points_added = 3
                        points_added = True
                    elif quantity_of_points_to_add == "4":
                        player.stealth = player.stealth + 4
                        player.points_to_allocate = player.points_to_allocate - 4
                        num_of_points_added = 4
                        points_added = True
                    elif quantity_of_points_to_add == "5":
                        player.stealth = player.stealth + 5
                        player.points_to_allocate = player.points_to_allocate - 5
                        num_of_points_added = 5
                        points_added = True
                    else:
                        quantity_of_points_to_add = input("Please enter a number from 1-5: ")
                #while loop that checks to see if you're trying to add too many points. If you added too many points, it fixes the issue.
                while num_of_points_added > (player.points_to_allocate + num_of_points_added): 
                    print("You cannot add more points than you have.")
                    player.stealth = player.stealth - num_of_points_added
                    player.points_to_allocate = player.points_to_allocate + num_of_points_added
                    break
                print("Your stealth is now: " + str(player.stealth))

            #Strength
            if skill_to_allocate_points_to == "9":
                quantity_of_points_to_add = input("How many points would you like to add to your strength? ")
                points_added = False
                while points_added == False:
                    if quantity_of_points_to_add == "1":
                        player.strength = player.strength + 1
                        player.points_to_allocate = player.points_to_allocate - 1
                        num_of_points_added = 1
                        points_added = True
                    elif quantity_of_points_to_add == "2":
                        player.strength = player.strength + 2
                        player.points_to_allocate = player.points_to_allocate - 2
                        num_of_points_added = 2
                        points_added = True
                    elif quantity_of_points_to_add == "3":
                        player.strength = player.strength + 3
                        player.points_to_allocate = player.points_to_allocate - 3
                        num_of_points_added = 3
                        points_added = True
                    elif quantity_of_points_to_add == "4":
                        player.strength = player.strength + 4
                        player.points_to_allocate = player.points_to_allocate - 4
                        num_of_points_added = 4
                        points_added = True
                    elif quantity_of_points_to_add == "5":
                        player.strength = player.strength + 5
                        player.points_to_allocate = player.points_to_allocate - 5
                        num_of_points_added = 5
                        points_added = True
                    else:
                        quantity_of_points_to_add = input("Please enter a number from 1-5: ")
                #while loop that checks to see if you're trying to add too many points. If you added too many points, it fixes the issue.
                while num_of_points_added > (player.points_to_allocate + num_of_points_added): 
                    print("You cannot add more points than you have.")
                    player.strength = player.strength - num_of_points_added
                    player.points_to_allocate = player.points_to_allocate + num_of_points_added
                    break
                print("Your strength is now: " + str(player.strength))

            #sets the experience points back to 0 so the player can start leveling up again.
            player.experience_points = 0
            input("Press ENTER to continue.")
def refresh():
    '''This function refreshes the game by checking to see if the player is dead, can level up, etc.'''
    level_up()
    player_dead()
def view_character_stats():
    '''This function allows the player to view their stats in the game. Add options for the character to see their available moves and spells.'''
    print("______________")
    print()
    print("CHARACTER STATS")
    print("______________")
    print()
    print("Name: " + player.player_name)
    print("Class: " + player.player_class)
    print("Battle cry: " + player.player_battle_cry)
    print("Level: " + str(player.player_level))
    print("Dungeon: " + player.dungeon_location)
    print("Location: Room " + str(player.room_location))
    print("Hit Points: " + str(player.hit_points) + "/" + str(player.max_hit_points))
    print("Sword skill: " + str(player.sword_skill))
    print("Archery skill: " + str(player.archery_skill))
    print("Magic skill: " + str(player.magic_skill))
    print("Armor skill: " + str(player.armor_skill))
    print("Barter skill: " + str(player.barter_skill))
    print("Speed: " + str(player.speed))
    print("Stealth: " + str(player.stealth))
    print("Strength: " + str(player.strength))
    print("Experience points: " + str(player.experience_points))
    print("Points to next level: " + str(10 - player.experience_points))
    print()
    print()
def knight_class():
    '''This function will change all of the attributes of the Player_Character class to match that of the Knight class. It is called by the character_creation() function.'''
    print()
    player.hit_points = 100
    player.max_hit_points = 100
    player.sword_skill = 50
    player.archery_skill = 30
    player.magic_skill = 20
    player.armor_skill = 50
    player.speed = 20
    player.stealth = 20
    player.strength = 50
    player.barter_skill = 20
    player.player_class = "Knight"
    return "You are now playing as a knight."
def wizard_class():
    '''This function will change all of the attributes of the Player_Character class to match that of the wizard class. It is called by the character_creation() function.'''
    print()
    player.hit_points = 60
    player.max_hit_points = 60
    player.sword_skill = 30
    player.archery_skill = 20
    player.magic_skill = 50
    player.armor_skill = 20
    player.speed = 30
    player.stealth = 30
    player.strength = 20
    player.barter_skill = 30
    player.player_class = "Wizard"
    return "You are now playing as a wizard."
def thief_class():
    '''This function will change all of the attributes of the Player_Character class to match that of the thief class. It is called by the character_creation() function.'''
    print()
    player.hit_points = 70
    player.max_hit_points = 70
    player.sword_skill = 30
    player.archery_skill = 50
    player.magic_skill = 20
    player.armor_skill = 30
    player.speed = 50
    player.stealth = 50
    player.strength = 30
    player.barter_skill = 20
    player.player_class = "Thief"
    return "You are now playing as an thief."
def character_creation():
    '''This function enables the player to create his character by typing the name and picking from a set of premade characters.'''

    print("______________")
    print()
    print("CHARACTER CREATION")
    print("______________")
    print()

    #Player chooses character name and program verifies if it is correct.
    name_correct = False
    while name_correct == False:
        player.player_name = input("What is your name? ")
        print()
        print("Hello " + player.player_name)
        print()
        print ("Is " + player.player_name + " the correct name?")
        yes_or_no = input("Type y for yes and n for no. ")
        if yes_or_no == "y":
            print()
            print("Excellent. Your name is now " + player.player_name + ".")
            name_correct = True
            break

    #Asks the player to choose from a set of premade characters.
    print()
    print("Choose your class... ")
    print()

    print("1. Knight")
    print("Starting Hit Points: 100")
    print("Sword skill: 50")
    print("Archery skill: 30")
    print("Magic skill: 20")
    print("Armor skill: 50")
    print("Speed: 20")
    print("Stealth: 20")
    print("Strength: 50")
    print("Barter skill: 20")
    print()

    print("2. Wizard")
    print("Starting Hit Points: 60")
    print("Sword skill: 30")
    print("Archery skill: 20")
    print("Magic skill: 50")
    print("Armor skill: 20")
    print("Speed: 30")
    print("Stealth: 30")
    print("Strength: 20")
    print("Barter skill: 30")
    print()

    print("3. Thief")
    print("Starting Hit Points: 70")
    print("Sword skill: 30")
    print("Archery skill: 50")
    print("Magic skill: 20")
    print("Armor skill: 30")
    print("Speed: 50")
    print("Stealth: 50")
    print("Strength: 30")
    print("Barter skill: 20")
    print()

    character_chosen = int(input("Press 1 for Knight, 2 for Wizard, or 3 for Thief: "))

    #verifies that the player selected the correct class. If so, it calls the class function to change the player's attributes.
    class_correct = False
    while class_correct == False:
        if character_chosen == 1:
            yes_or_no2 = input("Are you sure you want to play as a knight? y/n ")
            if yes_or_no2 == "y":
                knight_class()
                break
            else:
                print()
                character_chosen = int(input("Press 1 for knight, 2 for wizard, or 3 for thief: "))
        elif character_chosen == 2:
            yes_or_no2 = input("Are you sure you want to play as a wizard? y/n ")
            if yes_or_no2 == "y":
                wizard_class()
                break
            else:
                print()
                character_chosen = int(input("Press 1 for kight, 2 for wizard, or 3 for thief: "))
        elif character_chosen == 3:
            yes_or_no2 = input("Are you sure you want to play as a thief? y/n ")
            if yes_or_no2 == "y":
                thief_class()
                break
            else:
                print()
                character_chosen = int(input("Press 1 for kight, 2 for wizard, or 3 for thief: "))

    #Lets the player define their battle cry.
    battle_cry_correct = False
    while battle_cry_correct == False:
        player.player_battle_cry = input("Type your battle cry: ")
        yes_or_no3 = input("Is " + player.battle_cry() + " correct? y/n: ")
        if yes_or_no3 == "y":
            battle_cry_correct = True
            break

    #Lets the player view the class information with a view_character_stats() function.
    input("Press ENTER to view character stats.")
    view_character_stats()
    print()
    input("Press ENTER to continue.")


    print()
    return "Character creation complete..."
def start_menu():
    '''This is the start menu of the game. It is called by the main() function. It displays the title of the game and asks the user to either start the game or view the game instructions.'''
    print()
    #displays the title of the game.
    print("===============")
    print()
    print(" DUNGEON SEEK")
    print()
    print("===============")
    print()
    print("-  A game made by Jaden and Jorey Mounteer using python 3")
    print()

    #Asks the user to press ENTER to start the game. Stores the user input in a global variable called start_game. In the future, we can add the option for
    # the user to also press i and then ENTER to view the game instructions.
    global start_game
    start_game = input("Press ENTER to start the game. ")
    print()

    #checks to see if user input the correct characters.
    while start_game != "":
        start_game = input("Please press ENTER to start the game: ")

    #sets start_game to the boolean value of True.
    start_game = True

    #breaks out of the function and tells the user that the game is being launched.

    return "Game launched..."
def main():
    '''This is the first function called. It calls the start_menu function and then proceeds with the rest of the game.'''
    
    #calls the start_menu() function.
    print()
    start_menu()
    print()

    #Calls the character_creation() function.
    character_creation()

    #testing level up system.
    player.experience_points = 10
    refresh()

    #calls the room_level_1() function which throws the player into the first dungeon: Tomb of the Undead.
    dungeon_level_1()
    
    #Displays Game over when the game ends.
    print()
    return "Game over."

#calls the main() function which launches the game.
if __name__ == '__main__':
    main()