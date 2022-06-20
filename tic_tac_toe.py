from random import choice


class Game:
    def __init__(self, name='', value=''):
        self.name = name
        self.value = value
        self._victory = False
        self.color()

    @property
    def victory(self):
        return self._victory
    @victory.setter
    def victory(self, new_victory):
        self._victory = new_victory


    def read_int(self, question):
        while True:
            try:
                num = int(input(question))
                if num < 1 or num > 2:
                    print(f'{self.red}\nOnly options 1 and 2 available{self.ends_color}')
                    continue
            except (ValueError, TypeError):
                print(f'{self.red}\nOnly whole numbers{self.ends_color}')
            else:
                return num


    def play_game(self):
        self.line_and_list()
        print(self.interface())
        print(f'{self.blue}Welcome to the Old Game\nChoose one of the options below{self.ends_color}\n')
        game_mode = self.read_int('[1] SinglePlayer\n[2] MultiPlayer\n: ')
        self.singleplayer() if game_mode == 1 else self.multiplayer()


    def color(self):
        self.ends_color = '\033[m'
        self.red = '\033[1;31m'
        self.yellow = '\033[1;33m'
        self.blue = '\033[1;34m'
        self.white = '\033[1;97m'


    def line_and_list(self):
        Game.lineA = [[' '],[' '],[' ']]
        Game.lineB = [[' '],[' '],[' ']]
        Game.lineC = [[' '],[' '],[' ']]
        Game.list_values = [
            'A0','A1','A2', 
            'B0','B1','B2',
            'C0','C1','C2',]
    
    def interface(self):
        return f'''{self.white}
        __|   0     1     2
        A | {Game.lineA[0]} {Game.lineA[1]} {Game.lineA[2]}
        B | {Game.lineB[0]} {Game.lineB[1]} {Game.lineB[2]}
        C | {Game.lineC[0]} {Game.lineC[1]} {Game.lineC[2]}
        
        {self.ends_color}'''


    def multiplayer(self):
        self.line_and_list()
        player1_name = str(input('Player1, what your name? '))
        player2_name = str(input('Player2, what your name? '))

        player1 = Player(player1_name, 'x')
        player2 = Player(player2_name, 'o')


        while True:
            player1.play()
            player1.check_victory()
            if self.victory:
                print(self.interface())
                break

            player2.play()
            player2.check_victory()
            if self.victory:
                print(self.interface())
                break

            if self.victory == 'Tied':
                print(self.interface())
                break


    def singleplayer(self):
        self.line_and_list()
        player_name = str(input('Player, what your name? '))
        enemy_name = str(input(f"{player_name}, what is your rival's name? "))

        player = Player(player_name, 'x')
        enemy = Enemy(enemy_name, 'o') 

        while True:
            player.play()
            player.check_victory()
            if self.victory:
                print(self.interface())
                break

            enemy.play()
            enemy.check_victory()
            if self.victory:
                print(self.interface())
                break

            if self.victory == 'Tied':
                print(self.interface())
                break



    def check_victory(self):
        value = self.value * 3
        
        # LineA = [[x],[],[]]
        # lineB = [[],[x],[]]
        # lineC = [[],[],[x]]

        victore1 = f'{Game.lineA[0][0]}' + f'{Game.lineB[1][0]}' + f'{Game.lineC[2][0]}'
        if victore1 == value:
            print(f'\n{self.yellow}Player {self.name}, YOU WON{self.ends_color}')
            Game.victory = True
            
        # LineA = [[],[],[x]]
        # lineB = [[],[x],[]]
        # lineC = [[x],[],[]]

        victore2 = f'{Game.lineA[2][0]}' + f'{Game.lineB[1][0]}' + f'{Game.lineC[0][0]}'
        if victore2 == value:
            print(f'\n{self.yellow}Player {self.name}, YOU WON{self.ends_color}')
            Game.victory = True

        # LineA = [[x],[x],[x]]
        # lineB = [[],[],[]]
        # lineC = [[],[],[]]

        victore3 = f'{Game.lineA[0][0]}' + f'{Game.lineA[1][0]}' + f'{Game.lineA[2][0]}'
        if victore3 == value:
            print(f'\n{self.yellow}Player {self.name}, YOU WON{self.ends_color}')
            Game.victory = True

        # LineA = [[],[],[]]
        # lineB = [[x],[x],[x]]
        # lineC = [[],[],[]]

        victore4 = f'{Game.lineB[0][0]}' + f'{Game.lineB[1][0]}' + f'{Game.lineB[2][0]}'
        if victore4 == value:
            print(f'\n{self.yellow}Player {self.name}, YOU WON{self.ends_color}')
            Game.victory = True

        # LineA = [[],[],[]]
        # lineB = [[],[],[]]
        # lineC = [[x],[x],[x]]

        victore5 = f'{Game.lineC[0][0]}' + f'{Game.lineC[1][0]}' + f'{Game.lineC[2][0]}'
        if victore5 == value:
            print(f'\n{self.yellow}Player {self.name}, YOU WON{self.ends_color}')
            Game.victory = True

        # LineA = [[x],[],[]]
        # lineB = [[x],[],[]]
        # lineC = [[x],[],[]]

        victore6 = f'{Game.lineA[0][0]}' + f'{Game.lineB[0][0]}' + f'{Game.lineC[0][0]}'
        if victore6 == value:
            print(f'\n{self.yellow}Player {self.name}, YOU WON{self.ends_color}')
            Game.victory = True

        # LineA = [[],[x],[]]
        # lineB = [[],[x],[]]
        # lineC = [[],[x],[]]

        victore7 = f'{Game.lineA[1][0]}' + f'{Game.lineB[1][0]}' + f'{Game.lineC[1][0]}'
        if victore7 == value:
            print(f'\n{self.yellow}Player {self.name}, YOU WON{self.ends_color}')
            Game.victory = True

        # LineA = [[],[],[x]]
        # lineB = [[],[],[x]]
        # lineC = [[],[],[x]]

        victore8 = f'{Game.lineA[2][0]}' + f'{Game.lineB[2][0]}' + f'{Game.lineC[2][0]}'
        if victore8 == value:
            print(f'\n{self.yellow}Player {self.name}, YOU WON{self.ends_color}')
            Game.victory = True

        if Game.list_values == []:
            print(f'\n{self.yellow}There was a tie{self.ends_color}')
            Game.victory = 'Tied'


    def marking(self):
        mark = str(input(f'''{self.white}
        ------- {self.name} Turn -------

        __|   0     1     2
        A | {Game.lineA[0]} {Game.lineA[1]} {Game.lineA[2]}
        B | {Game.lineB[0]} {Game.lineB[1]} {Game.lineB[2]}
        C | {Game.lineC[0]} {Game.lineC[1]} {Game.lineC[2]}
        : {self.ends_color}''')).upper()

        return mark


    def scoring(self, mark, index, value):
        if mark in Game.list_values:
            if 'A' in mark:
                if Game.lineA[index] == [' ']: 
                    Game.lineA[index].clear()
                    Game.lineA[index].append(value)
                    Game.list_values.remove(mark)

            elif 'B' in mark:
                if Game.lineB[index] == [' ']: 
                    Game.lineB[index].clear()
                    Game.lineB[index].append(value)
                    Game.list_values.remove(mark)


            elif 'C' in mark:
                if Game.lineC[index] == [' ']: 
                    Game.lineC[index].clear()
                    Game.lineC[index].append(value)
                    Game.list_values.remove(mark)

        else:
            print(f'{self.red}Option not available{self.ends_color}')
            self.play()
        

    def play_user(self):
        self.mark = self.marking()
        self.index = int(self.mark[1])
        self.scoring(self.mark, self.index, self.value)

class Player(Game):
    def __init__(self, name, value):
        super().__init__(name, value)

    def play(self):
        super().play_user()

    def check_victory(self):
        super().check_victory()
    


class Enemy(Game):
    def __init__(self, name, value):
        super().__init__(name, value)

    def play(self):
        mark = choice(self.list_values)
        index = int(mark[1])


        if 'A' in mark:
            if Game.lineA[index] == [' ']: 
                Game.lineA[index].clear()
                Game.lineA[index].append(self.value)
                Game.list_values.remove(mark)

        elif 'B' in mark:
            if Game.lineB[index] == [' ']: 
                Game.lineB[index].clear()
                Game.lineB[index].append(self.value)
                Game.list_values.remove(mark)
            
        elif 'C' in mark:
            if Game.lineC[index] == [' ']: 
                Game.lineC[index].clear()
                Game.lineC[index].append(self.value)
                Game.list_values.remove(mark)
