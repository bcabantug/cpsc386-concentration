# cpsc386-concentration
386-p2_CGZL
CPSC386-01 
Project 2: Simple Mutated Classic VG in Pygame

Team Name: CGZL
Team Members:
-Brian Cabantug (bcabantug@csu.fullerton.edu) CWID: 
-Hancheng Zhou (jerryzhhch@csu.fullerton.edu) CWID:
-Mason Guzman-Sanchez (macegs1995@gmail.com) CWID:
-Alexandre Lee (al2012@csu.fullerton.edu) CWID:

Introduction: This program is a game that launches a 4x4 card game of concentration using Pygame. This game allows the player to play
either with another human player or a level 0 AI Opponent/

Description of the Game:
There are 16 cards face down on the board, each having a matching card to have a total of 8 pairs. Each player takes a turn flipping two cards
each, attempting to find a matching pair. If a player finds a matching pair, then they earn 1 point and the cards stay face up. Otherwise, the
cards are flipped back over to their hidden state, ending the turn. The game continues until all cards are flipped over. Whoever has the
most points at the end wins the game.

Contents:
-README.txt (aka this file)
-main.py (script to run the game)
-IMG Folder (Folder that contains the image assets for the game)

External Requirements: None

Setup and Installation:
Install Python3 on local computer to use
Install Pygame Module
Copy the script file and IMG folder to home directory
Navigate to home directory and run using python3 (command: python3 maze_complete.py)


Features: 
-Easter Setting with Bunnies
-PVP or PVAI Mode Selection

Bugs: (currently)
-LVL 0 AI does not pick the last card if it is the only one not flipped over
-After AI turn, player needs to click before indication of player turn is shown.
