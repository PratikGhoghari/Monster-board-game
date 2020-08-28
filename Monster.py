import random
import time
class Monster:

    monsters = []
    board_size = 10
    board = []                                          

    def __init__(self,name='',health=100,attack=30):
        self.name = name
        self.health = int(health)
        self.xPos = 0
        self.yPos = 0
        self.attack = attack  
        self.add_monsters_to_list()                  # Adds monster to list when the monster is created.
        
    def __str__(self):                     #Prints monster name instead of object location.
        return self.name

    def add_monsters_to_list(self):
        Monster.monsters.append(self)

    @classmethod
    def create_board(cls):                         # Generate the board.
        for k in range(cls.board_size):
            cls.board.append([])
        for i in range(cls.board_size):
            for j in range(cls.board_size):
                cls.board[i].append('-')

    @classmethod
    def draw_board(cls):                        # Print the board.
        for i in range(cls.board_size):
            for j in range(cls.board_size):
                print(cls.board[i][j],end=' ')
            print('')

    def get_attack(self):
        return self.attack

    def set_X_Y_position(self):                 # sets random position for monster and adds to board
        has_monster = True                                 
        x_Pos = self.xPos = random.randint(0,Monster.board_size-1)
        y_Pos = self.yPos = random.randint(0,Monster.board_size-1)

        if (Monster.board[x_Pos][y_Pos] == '-'):
            Monster.board[x_Pos][y_Pos] = self
        else:
            while (has_monster):   
                x_Pos = self.xPos = random.randint(0,Monster.board_size-1)
                y_Pos = self.yPos = random.randint(0,Monster.board_size-1)
                if Monster.board[x_Pos][y_Pos] == '-':
                    Monster.board[x_Pos][y_Pos] = self
                    has_monster = False     
             
    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_X_Y_position(self):                 # Returns tuple
        return self.xPos,self.yPos

    def set_health(self,health):
        self.health = health

    @classmethod
    def total_monsters(cls):
        monsters = cls.monsters
        return len(monsters)

    @staticmethod
    def is_monster_near(enemy,warrior):               # Takes tuple as argument and checks for monster nearby ie, (North, South, East, West)
        enemy_pos_X = enemy[0]
        enemy_pos_Y = enemy[1]
        warrior_pos_X = warrior[0]
        warrior_pos_Y = warrior[1]

        # The below if-statement might be optimized
        if (enemy_pos_X-1 == warrior_pos_X and enemy_pos_Y == warrior_pos_Y) or (enemy_pos_X == warrior_pos_X and warrior_pos_Y+1 == enemy_pos_Y) or (enemy_pos_X+1 == warrior_pos_X and enemy_pos_Y == warrior_pos_Y) or (enemy_pos_X == warrior_pos_X and enemy_pos_Y+1 == warrior_pos_Y):
            return True
        else:
            return False

    def attack_enemy(self,enemy):                       
        attack = self.get_attack()
        if not enemy.get_health() <= 0 and not self.get_health() <= 0:      # Both of them should be alive to fight.
            health = enemy.get_health()
            #print(f'Health of Monster {enemy.name} is :',health)
            #print(f'Health of Monster {self.name} is :',self.get_health())
            health-=attack
            enemy.set_health(health)
            #print(f'Monster {self.name} has attacked Monster {enemy.name} and health of Monster {enemy.name} is: ',enemy.get_health())
            #Monster.board_size-=2

        else:
            print(f'Monster {enemy.name} is dead')
            position = 0
            x_Pos = 0
            y_Pos = 0
            position = enemy.get_X_Y_position()
            x_Pos = position[0]
            y_Pos = position[1]
            Monster.board[x_Pos][y_Pos] = '-'          
            Monster.monsters.remove(enemy)
            Monster.board_size-=2

    @classmethod 
    def attack_monsters(cls):                     # As of now Monsters jumps randomly but we can make it move in a particular direction.
        while(Monster.total_monsters()>1):      
            Monster.update_monster_position()
            Monster.draw_board()
            position_x=0                               
            position_y=0
            for enemy in cls.monsters:                
                enemy_position = enemy.get_X_Y_position()
                for warrior in cls.monsters:
                    warrior_position = warrior.get_X_Y_position()              
                    if enemy == warrior:                              # Cannot attack itself.
                        continue
                    elif Monster.is_monster_near(enemy_position,warrior_position):      # Returns true if monster is near.
                        warrior.attack_enemy(enemy)  
            print('##################################')
            time.sleep(1.5)    
        print(f'MONSTER {Monster.monsters[0]} WON')

    @classmethod
    def update_monster_position(cls):            
        for monster in cls.monsters:
            position = 0
            x_Pos = 0
            y_Pos = 0
            position = monster.get_X_Y_position()
            x_Pos = position[0]
            y_Pos = position[1]
            Monster.board[x_Pos][y_Pos] = '-'
            monster.set_X_Y_position()

s = Monster('S',73,attack=42)
k = Monster('K',80,attack=52)
z = Monster('Z',85,attack=48)
p = Monster('P',attack=30)
q = Monster('Q',90,attack=50)

Monster.create_board()
Monster.attack_monsters()
print('Game over')






'''
 warrior     enemy
(2,4) -->  (2,3),    (1,4),   (2,5),  (3,4)
      -->  (2,3+1), (2-1,4), (2,5-1),  (3-1,4)
'''


