386-p2_CGZL
CPSC386-01 
Project 2: Simple Mutated Classic VG in Pygame

Team Name: CGZL
Team Members:
-Brian Cabantug (bcabantug@csu.fullerton.edu) CWID: 891096281
-Hancheng Zhou (jerryzhhch@csu.fullerton.edu) CWID: 891971798
-Mason Guzman-Sanchez (macegs1995@gmail.com) CWID: 890919442
-Alexandre Lee (al2012@csu.fullerton.edu) CWID: 892172396

Introduction: This program is a game that launches a 4x4 card game of concentration using Pygame. This game allows the player to play
either with another human player or a level 0 AI Opponent

Description of the Game:
There are 16 cards face down on the board, each having a matching card to have a total of 8 pairs. Each player takes a turn flipping two cards
each, attempting to find a matching pair. If a player finds a matching pair, then they earn 1 point and the cards stay face up. Otherwise, the
cards are flipped back over to their hidden state, ending the turn. The game continues until all cards are flipped over. Whoever has the
most points at the end wins the game. If a bunny pair is selected, then the player that selects it gets an extra turn.

Contents:
-README.txt (aka this file)
-global_inst.py (file that holds the globals)
-find_area.py (file that indicates the card areas)
-main.py (script to run the game)
-player_ai.py (file that holds the function when player vs ai is selected)
-player_player (file that holds the function when player vs player is selected)
-img Folder (Folder that contains the image assets for the game)
-sounds folder (Folder that contains the sound assets for the game)

External Requirements: None

Setup and Installation:
Install Python3 on local computer to use. Install instructions for python3 can be found here: https://docs.python.org/3/using/index.html
Install Pygame Module. Install instructions for Pygame can be found here: https://www.pygame.org/wiki/GettingStarted
Extract the script files and the sounds+img folders to your home directory
Navigate to home directory and run the main.py using python3 (command: python3 main.py)

Features: 
-Easter Setting with Bunnies
-PVP or PVAI Mode Selection from Main Menu
