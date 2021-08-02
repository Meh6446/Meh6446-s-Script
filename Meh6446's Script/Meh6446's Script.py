from os import truncate
from pygame.version import PygameVersion


try:
    import os
    import sys
    import time
    import pyfiglet
    import dealer
    import copy
    import pygame
    from pygame.locals import *
    import random
except:
    if os.name == 'nt':
        os.system('python -m pip install -r requirements.txt')
    elif os.name == 'posix':
        pass

#Utilities
def banner():
    banner_figlet = pyfiglet.figlet_format("Meh6446\'s Script", font="small")
    print(banner_figlet + "Made By Meh6446")

def typing(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./10)

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

def intro():
    clear()
    banner()
    print('If you have any questions or suggestions contact me on Discord')
    print('My Discord: Meh6446#6446\n')
    input('Press Enter to continue\n')
    menu()

def menu():
    while True:
        clear()
        print(pyfiglet.figlet_format("Menu", font="small"))
        print("[1] PyPackage Installer")
        print("[2] Blackjack")
        print("[3] PyGame Tetris")
        print
        print("[4] Exit")
        choice = input("Choose by Entering option's Number\n> ")
        if choice == "1":
            downloader()

        elif choice == "2":
            blackjack()

        elif choice == "3":
            clear()
            print("### Controls ###")
            print("Arrow Keys - Move\nP - Pause")
            tetris()

        elif choice == "4":
            clear()
            while True:
                clear()
                c = input("Are you sure?\n[Y/N] > ").lower()
                if c == 'y':
                    typing("Thank You for using this program!!!")
                    sys.exit()
                elif c == 'n':
                    menu()
                else:
                   print('Please enter either y or n')        
        else:
           print("Please enter an option's number")
           input('')

#Program Functions
def downloader():
    clear()
    print(pyfiglet.figlet_format("PyPackage Intaller", font="small"))
    try:
        num = int(input("How many packages do you wanna install?\n> "))
        package = []
        for i in range(num):
            clear()
            name = input("Enter package name\n> ")
            package.append(name)
    except ValueError:
        print("Please Enter a Number")
        input('')
        downloader()

    order = 0    
    while len(package) > 0:
        clear()
        try:
            if os.name =='nt':
                os.system(f'pip install {package[order]}')
                typing("Loading...")
                input('Press Enter to continue')
            elif os.name == 'posix':
                os.system(f'pip3 install {package[order]}')
                typing("Loading...")
                input('Press Enter to continue')
            order = order + 1
        except IndexError:
            q = input('That\'s all, or do you want to install more packages?\n[Y/N] > ').lower()
            if q == 'y':
                downloader()
            elif q == 'n':
                typing("Loading Main Menu...")
                menu()

def blackjack():
    print(pyfiglet.figlet_format("Blackjack", font='small'))
    print("###DISCLAIMER###\nCredits will not be saved once you exit Blackjack\n")
    print("Would you like to turn on betting?")
    betting_on = input("[Y/N] > ").lower()
    print("")

    if betting_on == 'y':
        betting = True
        player_wallet = 100
    elif betting_on == 'n':
        betting = False

            # Meh6446 : Game setup
    keep_playing = True
    while keep_playing:
        clear()
        playing_deck = copy.copy(dealer.the_deck)
        player_hand = []
        player_score = 0
        dealer_hand = []
        dealer_score = 0

            #show players hand and total
        player_hand.append(dealer.draw_card(playing_deck))
        player_hand.append(dealer.draw_card(playing_deck))
        player_score = dealer.compute_score(player_hand)
        print("Starting hand: " + dealer.cards_in_hand(player_hand))
        print("Total: " + str(player_score))
        if betting == True:
            print("Player Credits: " + str(player_wallet))
        print("")
 
            #bet code
        player_bet = 0
        if betting == True:
            while player_bet == 0:
                try:
                    player_bet = int(input("How many credits would you like to bet?\n> "))
                    if player_bet > player_wallet:
                        print("\nYou don't have that many credits to bet\n")
                        player_bet = 0
                except:
                    print("\nPlease Enter a Number\n")
                    player_bet = 0
        print("")
  
            #game loop
        in_game = True
        player_wins = None
        while in_game == True:
            print("Would you like to draw a card?")
            keep_going = input("Hit or Stand\n[H/S] > ").lower()
            print('')
            #if player hit
            if keep_going == "h":
                clear()
                player_hand.append(dealer.draw_card(playing_deck))
                player_score = dealer.compute_score(player_hand)
                if player_score > 21:
                    print("Current hand: " + dealer.cards_in_hand(player_hand))
                    print("Current Total: " + str(player_score))
                    print('')
                    print("Oh no!  You went bust!")
                    player_wins = False
                    in_game = False
                elif player_score == 21:
                    print("Current hand: " + dealer.cards_in_hand(player_hand))
                    print("Current Total: " + str(player_score))
                    print('')
                    print("BLACKJACK!!! You Win!")
                    player_wins = True
                    in_game = False      
                elif len(player_hand) > 4:
                    print("Wow!  You got a 'Five Card Charlie'!  You Win!")
                    player_wins = True
                    in_game = False
                else:
                    print("Current hand: " + dealer.cards_in_hand(player_hand))
                    print("Current Total: " + str(player_score) + "\n")
            #when the player stands the dealer draws/code for dealer
            elif keep_going == "s":
                clear()
                print("Now the dealer will draw.")
                dealer_hand.append(dealer.draw_card(playing_deck))
                dealer_hand.append(dealer.draw_card(playing_deck))
                dealer_score = dealer.compute_score(dealer_hand)
                while dealer_score < 16:
                    dealer_hand.append(dealer.draw_card(playing_deck))
                    dealer_score = dealer.compute_score(dealer_hand)
                print("Dealer's hand: " + dealer.cards_in_hand(dealer_hand))
                print("Dealer's Total: " + str(dealer_score))
                print('')
                if dealer_score > 21:
                    print("The dealer went bust!  You win!")
                    player_wins = True
                    in_game = False
                elif len(dealer_hand) > 4:
                    print("The dealer got a 'Five Card Charlie'.  You lose!")
                    player_wins = False
                    in_game = False
                elif dealer_score == 21:
                    print("Dealer's hand: " + dealer.cards_in_hand(dealer_hand))
                    print("Dealer's Total: " + str(dealer_score))
                    print('')
                    print("Dealer's BLACKJACK!!! You Lose!")
                    player_wins = False
                    in_game = False
                elif dealer_score >= player_score:
                    print("The dealer beat you!  You lose!")
                    player_wins = False
                    in_game = False
                else:
                    print("You beat the dealer!  You win!")
                    player_wins = True
                    in_game = False
        #betting total/added to player's wallet if win
        if betting == True:
            if player_wins == True:
                print("\nYour hand: " + dealer.cards_in_hand(player_hand))
                input('')
                player_wallet = player_wallet + player_bet
            elif player_wins == False:
                print("\nYour hand: " + dealer.cards_in_hand(player_hand))
                input('')
                player_wallet = player_wallet - player_bet                
                if player_wallet < 1:
                    print("You've run out of credits!\nGame Over!")
                    typing("You can't continue if you turn on betting...\nReturning to Main Menu...")
                    break
                      
        check_continue = input("\nContinue Playing?\n[Y/N] > ").lower()
        if check_continue == "n":
            print("Thanks For Playing!!!")
            typing("Loading Main Menu")
            keep_playing = False
            menu() 
        elif check_continue == "y":
            print('\n##### NEW GAME #####\n')

def tetris():
    clear()
    print(pyfiglet.figlet_format("Tetris", font = "small"))
    print("### Controls ###")
    print("Arrow Keys - Move\nP - Pause")
    input("Press Enter To Continue\n")
    colors = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
    ]

    class Figure:
        figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],#I piece
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],#L piece
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],# reverse L piece 
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],#T piece
        [[1, 2, 5, 6]], #O piece
        [[0, 1, 5, 6], [1, 4, 5, 8]],#Z piece
        [[1, 2, 4, 5], [0, 4, 5, 9]]#S piece
    ]

        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.type = random.randint(0, len(self.figures) - 1)
            self.color = random.randint(1, len(colors) - 1)
            self.rotation = 0

        def image(self):
            return self.figures[self.type][self.rotation]

        def rotate(self):
            self.rotation = (self.rotation + 1) % len(self.figures[self.type])

    class Tetris:
        level = 2
        score = 0
        state = "start"
        field = []
        height = 0
        width = 0
        x = 100
        y = 60
        zoom = 20
        figure = None

        def __init__(self, heigtht, width):
            self.height = heigtht
            self.width = width
            self.field = []
            self.score = 0
            self.state = "start"
            for i in range(heigtht):
                new_line = []
                for j in range(width):
                    new_line.append(0)
                self.field.append(new_line)
        
        def new_figure(self):
            self.figure = Figure(3, 0)

        def intersects(self):
            intersection = False
            for i in range(4):
                for j in range(4):
                    if i * 4 + j in self.figure.image():
                        if i + self.figure.y > self.height - 1 or \
                                j + self.figure.x > self.width - 1 or \
                                j + self.figure.x < 0 or \
                                self.field[i + self.figure.y][j + self.figure.x] > 0:
                            intersection = True
            return intersection

        def break_lines(self):
            lines = 0
            for i in range(1, self.height):
                zeros = 0
                for j in range(self.width):
                    if self.field[i][j] == 0:
                        zeros += 1
                if zeros == 0:
                    lines += 1
                    for i1 in range(1, 2, -1):
                        for j in range(self.width):
                            self.field[i1][j] = self.field[i1 - 1][j]
            self.score += lines ** 2
        
        def go_space(self):
            while not self.intersects():
                self.figure.y += 1
            self.figure.y -= 1
            self.freeze()

        def go_down(self):
            self.figure.y += 1
            if self.intersects():
                self.figure.y -= 1
                self.freeze()

        def freeze(self):
            for i in range(4):
                for j in range(4):
                    if i * 4 + j in self.figure.image():
                        self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
            self.break_lines()
            self.new_figure()
            if self.intersects():
                self.state = "gameover"

        def go_side(self, dx):
            old_x = self.figure.x
            self.figure.x += dx
            if self.intersects():
                self.figure.x = old_x

        def rotate(self):
            old_rotation = self.figure.rotation
            self.figure.rotate()
            if self.intersects():
                self.figure.rotation = old_rotation


# Initialize the game engine
    pygame.init()

    #Pause Check
    pause = False
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)

    size = (400, 500)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Tetris")

    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()
    fps = 25
    game = Tetris(20, 10)
    counter = 0

    pressing_down = False

    while not done:
        if game.figure is None:
            game.new_figure()
        counter += 1
        if counter > 100000:
            counter = 0

        if counter % (fps // game.level // 2) == 0 or pressing_down:
            if game.state == "start":
                game.go_down()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.rotate()
                if event.key == pygame.K_DOWN:
                    pressing_down = True
                if event.key == pygame.K_LEFT:
                    game.go_side(-1)
                if event.key == pygame.K_RIGHT:
                    game.go_side(1)
                if event.key == pygame.K_SPACE:
                    game.go_space()
                if event.key == pygame.K_ESCAPE:
                    game.__init__(20, 10)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    if game.state == "gameover":
                        pause = False
                    else:
                        pause = True
                        paused(pause)
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pressing_down = False

        def paused(pause):
            font2 = pygame.font.SysFont('Calibri', 60, True, False)
            pause_text = font2.render('Paused', True, BLACK)
            screen.blit(pause_text, [200, 20])
            while pause == True:        
                for event in pygame.event.get():
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_p:
                            pause = False

        screen.fill(WHITE)

        for i in range(game.height):
            for j in range(game.width):
                pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                if game.field[i][j] > 0:
                    pygame.draw.rect(screen, colors[game.field[i][j]],
                                     [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

        if game.figure is not None:
            for i in range(4):
                for j in range(4):
                    p = i * 4 + j
                    if p in game.figure.image():
                        pygame.draw.rect(screen, colors[game.figure.color],
                                         [game.x + game.zoom * (j + game.figure.x) + 1,
                                          game.y + game.zoom * (i + game.figure.y) + 1,
                                          game.zoom - 2, game.zoom - 2])

        font = pygame.font.SysFont('Calibri', 25, True, False)
        font1 = pygame.font.SysFont('Calibri', 65, True, False)
        text = font.render("Score: " + str(game.score), True, BLACK)
        text_game_over = font1.render("Game Over", True, BLACK)
        text_game_over1 = font1.render("Press ESC", True, BLACK)

        screen.blit(text, [0, 0])
        if game.state == "gameover":
            screen.blit(text_game_over, [20, 200])
            screen.blit(text_game_over1, [25, 265])


        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
    menu()

def platformer():
    pygame.init()

    screen_width = 500
    screen_height = 500

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Platformer')

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

try:
    platformer()
except KeyboardInterrupt:
    typing('Exiting...')