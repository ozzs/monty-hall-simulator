<p align="center">
  <img src="https://github.com/ozzs/monty-hall-simulator/blob/main/monty-hall-logo.png" alt="MusicPlayerLogo" width="300">
  <h4 align="center"> Monty Hall interactive algorithm simulator </h4>
</p>
<br />

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
</p>
<br />

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#key-features">Key Features</a> •
  <a href="#tech">Tech</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#resources">Resources</a>
</p>

Don't forget to star us — it motivates us a lot! ⭐

## Overview
You are participating in Monty Hall's game show in TV, Let’s Make a Deal. Monty shows you 3 closed doors. 🚪

Two of the doors hide goats, while the other one hides a car. The game - you choose a door, and you win what is behind it. You probably want to win a car. 🚗

You point to one of the three doors, and then comes the twist: Monty goes and opens **another** door, revealing a goat behind it. 🐐

Monty asks if you want to change your choice to the third door (the door you didn't choose and he didn't open).

**Will you change your mind?** 🤔

Fascinated with how the Monty Hall algorithm works, I built a system to demonstrate how changing your choice in the game show will affect the final result.
<br /> <br />

<p align="center">
  <img alt="main-screen" src="https://github.com/ozzs/monty-hall-simulator/blob/main/assets/media/MainScreen.png" width="500" />
</p>

## Key Features
* Convenient and easy-to-use UI
* Educational
* Accompanied by sounds
* Open-Source code
* Highly detailed documentation of code

## Tech
The GUI (Graphical User Interface) system for the problem was created using **Python** and the following libraries:
* _tkinter_ - The main library used to develop the system. Python's de-facto standard GUI package
* _pygame_ - A cross-platform set of Python modules. It includes computer graphics and sound libraries designed to be used with Python
* _black_ for formatting 🎗

## Installation
To start working, you need to be in Python virtual environment.

The ``requirements.txt`` file lists all the Python libraries that the simulator depends on, and they can be installed from your terminal using:
```
pip install -r requirements.txt
```

After the libraries have finished installing, use the following command in the terminal to start the system:
```
python main.py
```

## Usage
If you followed the installation instructions, you should reach the main screen relatively easily.

Now, you are given three different game options to choose from:
* **Human Run** - Play and experience by yourself 👨‍💻
* **Statistics** - Display statistics for multiple computer-run games 📃
* **PC One Game** - Viewing a demo of the game, as it is played by the computer 💻

### Human Run
At first, choose one of the 3 partitions in front of you.

After that, the system runs the Monty Hall algorithm, taking into account the partition you chose.

At the end of the algorithm run, a goat is shown behind one of the 2 partitions that you **did not** choose. Then, you need to decide whether you want to change your choice or not.

Finally, you will be presented with the result:
* Did you win or lose?
* The location of the 2 goats and the car behind the partitions

<p align="center">
  <img alt="humen-run" src="https://github.com/ozzs/monty-hall-simulator/blob/main/assets/media/HumanRunGIF.gif" width="500" />
</p>

### Statistics
Selecting the Statistics, will take you to a screen that will ask you how many times do you want the computer to run the game.

After you make a choice, the following details will be presented to you:
* The number of games played by the computer (according to your choice)
* The number of times the computer won
* The number of times the computer lost
* Wins / Losses ratio

<p align="center">
  <img alt="statistics-run" src="https://github.com/ozzs/monty-hall-simulator/blob/main/assets/media/StatisticsGIF.gif" width="500" />
</p>

### PC One Game
Unlike Human Run, the transition between the stages in this mode occurs after a number of seconds defined by you, after which the system does not wait for your input.

On the first screen, you will be prompted to choose how long you want to wait between each transition.

On the second screen, The computer displays a random pick of one of the partitions.

On the third screen, the computer displays a goat behind one of the partitions that he did not choose.

Finally, the following details will be presented to you:
* Did the computer win or lose?
* The location of the 2 goats and the car behind the partitions

<p align="center">
  <img alt="pc-run" src="https://github.com/ozzs/monty-hall-simulator/blob/main/assets/media/PCRunGIF.gif" width="500" />
</p>

## Resources
* <a href="https://github.com/ozzs/monty-hall-simulator">Source Code</a>
* <a href="https://docs.python.org/3/library/tkinter.html">python.org</a>
* <a href="https://realpython.com/documenting-python-code">realpython.com</a>
* <a href="https://www.tutorialspoint.com/python/python_gui_programming.htm">tutorialspoint.com</a>
