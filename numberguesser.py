#Sen is the mother
#Moduel Stuff
import os, sys
import time
import random
from time import sleep
import getpass
import logging
import ctypes

#Debugging Stuff
DebuggingFile = True
debuggingmode = False
if debuggingmode == True:
    try:
        os.remove('PasswordGenDebugging.txt')
    except FileNotFoundError:
        DebuggingFile = False
    logging.basicConfig(filename='PasswordGenDebugging.txt', level = logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.debug('Starting program')
    if DebuggingFile == True:
        logging.debug('Cleared old debug file')

#Gradients that i stole
def blue(text):
    os.system(""); faded = ""
    for line in text.splitlines():
        green = 0
        for character in line:
            green += 3
            if green > 255:
                green = 255
            faded += (f"\033[38;2;0;{green};255m{character}\033[0m")
        faded += "\n"
    return faded

def red(text):
    os.system(""); faded = ""
    for line in text.splitlines():
        green = 250
        for character in line:
            green -= 5
            if green < 0:
                green = 0
            faded += (f"\033[38;2;255;{green};0m{character}\033[0m")
        faded += "\n"
    return faded

def water(text):
    os.system(""); faded = ""
    green = 10
    for line in text.splitlines():
        faded += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
        if not green == 255:
            green += 15
            if green > 255:
                green = 255
    return faded

def purple(text):
    os.system("")
    faded = ""
    down = False

    for line in text.splitlines():
        red = 40
        for character in line:
            if down:
                red -= 3
            else:
                red += 3
            if red > 254:
                red = 255
                down = True
            elif red < 1:
                red = 30
                down = False
            faded += (f"\033[38;2;{red};0;220m{character}\033[0m")
    return faded

#Things i use everywhere
# Coloring cause color is cute and uwu
Green = "\033[0;32m"
Orange = "\033[0;33m"
Cyan = "\033[0;36m"
White = "\033[0;37m" 
black = "\033[0;30m"
black = "\033[0;90m"         # <<<<<Thanks to BobTheTomatoPie for the color and scroling
green = "\033[0;92m"
yellow = "\033[0;93m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
white = "\033[0;97m"
cyan_back="\033[0;46m"
pink_back="\033[0;45m"

#Very StraightForward
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
#Error Stuff
def error(error):
    print(purple(f"        [!] Error : {error}"))
    
# Console Ttle on windows
def set_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)
set_title("Number Guesser | By Kars#1996")
    
    
#Banner and shit
banner = '''                 ::::::::  :::    ::: :::::::::: ::::::::   ::::::::  :::::::::: ::::::::: 
                :+:    :+: :+:    :+: :+:       :+:    :+: :+:    :+: :+:        :+:    :+: 
               +:+        +:+    +:+ +:+       +:+        +:+        +:+        +:+    +:+  
              :#:        +#+    +:+ +#++:++#  +#++:++#++ +#++:++#++ +#++:++#   +#++:++#:    
             +#+   +#+# +#+    +#+ +#+              +#+        +#+ +#+        +#+    +#+    
            #+#    #+# #+#    #+# #+#       #+#    #+# #+#    #+# #+#        #+#    #+#     
            ########   ########  ########## ########   ########  ########## ###    ###      '''
            
#bro idek at this point
def NumberGuesserInto():
    numberoffuckups = 0
    clear()
    print(blue(banner))
    print(red('        Heres how this shit works'))
    print(red('        The program will pick a number beetween 1 and 200'))
    print(water('        Your job is to guess it, the program will tell you if it is higher or lower'))
    gotit = input(str(purple('\n        Do you understand?')+ water(' [Y/N]'))).lower()
    while gotit not in ['y', 'n']:
        error('You dumfuck pick Y or N')
        gotit = input(str(purple('\n        Do you understand?')+ water(' [Y/N]'))).lower()
        
    if gotit == 'y':
        print(red('        Intitialising...'))
        time.sleep(random.randint(2,7))
        NumberGuesserThing()
    if gotit == 'n':
        print(water('        cool ig'))
        time.sleep(4)
        quit()
        

#main number guesser
def NumberGuesserThing():
    clear()
    attempts = 1
    print(blue(banner))
    randomnumber = random.randint(1, 200)
    print(water(
        '        [>] I am thinking of a number between 1 and 200. Have a go and try figure it out!'))
    if debuggingmode == True:
        print(water(f'        [$] Debugging, Number = {randomnumber}'))
    while True:
        NumberGuess = input(
        str(blue('        Please input a number between 1 and 200 > ')+'\033[38;2;148;0;230m'))
        if not NumberGuess.isdigit() or int(NumberGuess) not in range(1, 201):
            error('Please input a number between 1 and 200')
            continue
        NumberGuess = int(NumberGuess)
        if not NumberGuess:
            print(
                red('        [!] Your guess was too high! Try a lower number'))
            attempts += 1
            continue
        if NumberGuess > randomnumber:
            print(
                red('        [!] Your guess was too high! Try a lower number'))
            attempts += 1
            continue
        if NumberGuess < randomnumber:
            print(
                red('        [!] Your guess was too low! Try a Higher number'))
            attempts += 1
            continue
        if NumberGuess == randomnumber:
            print(green + '        [!] Congrtas! You got the correct number!')
            print(blue(f'        [!] It took you {attempts} attempts.'))
            getpass.getpass(prompt=purple(
                '        [+] Press Enter to continue '))
            time.sleep(random.randint(2, 7))
            break
    credits()

#Credditing people who have helped me
def credits():
    clear()
    print(blue(banner))
    print(blue(f"                                    [>] By Kars#1996"))
    print(white + '        Thank you to' + magenta + ' freezer#3008 ' + white + 'For helping me go through the code and proof read it')
    print('        Thank you to the pylexnodes discord and all the other people who saw the gui')
    print(purple('        Thank you to you for using this shit project :D'))
    updates = input(str(red('        Would you like to go through all the updates for this project? [Y/N]'))).lower()
    while updates not in ['y', 'n']:
        error('Dude, come on. its y or no its not that hard')
        updates = input(str(red('        Would you like to go through all the updates for this project? [Y/N]'))).lower()
    if updates == 'n':
        print(red('        Thank you for using my number gen'))
        time.sleep(2)
        print(water('        Have a nice day :D'))
        time.sleep(3)
        quit()
    if updates == 'y':
        updatehist()

#Simpler run down version of the project
def simple():
    clear()
    print(blue(banner))
    print(red('        [$] Clearing files'))
    time.sleep(2)
    print(red('        [!] Simplifying'))
    time.sleep(3)
    print(green + '        [!] Sucsess!')
    time.sleep(3)
    print(white + ' ')
    clear()
    import base64, codecs
    hub = 'aW1wb3J0IHJhbmRvbQpudW1iZXIgPSByYW5kb20ucmFuZGludCgxLDIwMCkKdHJpZXMgPSAwCnByaW50KCdJIGFtIHRoaW5raW5nIG9mIGEgbnVtYmVyIGJldHdlZW4gMSBhbmQgMjAwJykKcHJpbnQoJ1BsZWFzZSBpbnB1dCB5b3VyIGd1ZXNzJykKd2hpbGUgVHJ1ZToKICAgIGd1ZXNzID0gaW50KGlucHV0KCc+JykpCiAgICBpZiBndWVzcyBub3QgaW4gcmFuZ2UoMSwgMjAxKToKICAgICAgICBwcmludCgnUGxlYXNlIGlucHV0IGEgbnVtYmVyIGJldHdlZW4gMSBhbmQgMjAwJykKICAgICAgICBjb250aW51ZQogICAgaWYgZ3Vlc3MgPiBudW1iZXI6CiAgICAgICAgcHJpbnQoJ1lvdXIgZ3Vlc3Mgd2FzIHRvbyBoaWdoLCBwbGVhc2UgdHJ5IGFnYWluJykKICAgICAgICB0cmllcyArPSAxCiAgICAgICAgY29udGludWUKICAgIGlmIGd1ZXNzIDwgbnVtYmVyOgogICAgICAgIHByaW50KCdZb3VyIGd1ZXNzIHdhcyB0b28gbG93LCBwbGVhc2UgdHJ5IGFnYWluJykKICAgICAgICB0cmllcyArPSAxCiAgICAgICAgY29udGludWUKICAgIGlmIGd1ZXNzID09IG51bWJlcjoKICAgICAgICBwcmludCgnQ29uZ3JhdHMsIHlvdSBnb3QgaXQgcmlnaHQhJykKICAgICAgICBwcmludChmJ0l0IHRvb2sgeW91IHt0cmllc30gdHJpZXMnKQogICAgICAgIGJyZWFr=='
    run = eval(compile(base64.b64decode(eval('hub')), '<string>', 'exec'))

#Cool Astetic Loading Bar
def LoadingBar():
    clear()
    print(blue(banner))
    time.sleep(0.4)
    print('Restarting:')
    time.sleep(0.3)
    toolbar_width = 40
    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
    i=0
    while i < toolbar_width:
        i=i+1
        time.sleep(0.1) # do real work here
    # update the bar
        sys.stdout.write("=")
        sys.stdout.flush()
    sys.stdout.write("]\n") # this ends the progress bar
    print(green + 'Sucsess!')
    time.sleep(2)
    Introduction()

#Simple debugging things (Will add more soon)
def debugging():
    global debuggingmode
    debuggingmode = False
    clear()
    print(blue(banner))
    print(blue(f"                                    [>] Debugging Mode Enabled"))
    debuggingmode = True
    print(water('        [$] Logging will be added soon'))
    print(red('        [!] Starting program in 5 seconds'))
    time.sleep(5)
    print(red('        [?] Would you like to restart the program? [Y/N]'))
    Restart = input(str('        >')).lower()
    if Restart == 'y':
        print(red('        [!] Restarting'))
        time.sleep(3)
        LoadingBar()
    if Restart == 'n':
        print(red('        [!] Continuing with the program'))
        NumberGuesserInto()


#History of all past updates
def updatehist():
    clear()
    print(blue(banner))
    print(blue(f"                                    [>] Update Lists"))
    print(blue('        [+] 1.3.5 - Fixxed logging'))
    print(blue('        [+] 1.3.4 - Fixed bug'))
    print(blue('        [+] 1.3.4 - Fixed an error caused by adding a debugging mode'))
    print(blue('        [+] 1.3.3 - Fixed a dumb oversight'))
    print(blue('        [+] 1.3.2 - Implemented some easter eggs'))
    print(blue('        [+] 1.3.1 - Implemented a debugging mode'))
    print(blue('        [+] 1.2.7 - Fixed another while true loop'))
    print(blue('        [+] 1.2.6 - Finally fixed the password gen bugs (ty freezer)'))
    print(blue('        [+] 1.2.5 - Fixed smol bugs + gui changes'))
    print(blue('        [+] 1.2.4 - Fixed Some typoes and bugs (My code sucks)'))
    print(blue('        [+] 1.2.3 - Fixed Some typoes'))
    print(blue('        [+] 1.2.3 - Fixed While True loop :skull:'))
    print(blue('        [+] 1.2.1 - Finished the number Generator'))
    print(blue('        [+] 1.2.0 - Added Guesser'))
    print(blue('        [+] 1.1.3 - Small Optimisations and stuff'))
    print(blue('        [-] 1.1.2 - Removed Redundant Code'))
    print(blue('        [+] 1.1.1 - Idr'))
    print(blue('        [+] 1.1.0 - Reworked Introduction and stuff'))
    print(red('        [+] 0.0.1 - Started Work on the number guesser'))
    getpass.getpass(prompt=red(
                '        [+] Press Enter to exit the program'))
    quit
    
    
    
#introduction ig
def Introduction():
    global debuggingmode
    debuggingmode = False
    clear()
    print(blue(banner))
    print(blue(f"                                    [>] Running version 1.3.6"))
    print(purple('\n\n        Welcome to my shit number guesser. I was bored and i had mothing better to do'))
    secretdebugging = getpass.getpass(prompt=purple('        [+] Press Enter to continue ')).lower()
    if secretdebugging == 'debug':
        print(red('        [$] Enabling Debugging Mode'))
        time.sleep(3)
        debugging()
    if secretdebugging == 'simple':
        print(red('        [$] Enabling simple code'))
        time.sleep(3)
        simple()
    else:
        NumberGuesserInto()
    
#Runs the program
Introduction()