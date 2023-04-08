# PythonRPG

## Description
A WIP project of an RPG written in Python using the [python-tcod](https://python-tcod.readthedocs.io/en/latest/) library.

### Objectives
This project is mostly an excercise in learning more about OOP concepts and Python. It will be built upon in my free time.
I'll be referencing and using some code and concepts from this amazingly well made [Roguelike tutorial](https://rogueliketutorials.com/) made specifically around
Python and tcod, though I don't intend for this game to develop into a traditional Roguelike game.

I have a fascination for Roguelikes, games that look like they were made in the early days of computers, and games
that invest heavily in systems and features while using simple graphics.

### Current priorities
Here is a list of features I'll be prioritizing for the moment:
- Building up the Engine class to be able to read pre-made game maps, parse them, and draw them
	- Maps will likely by made using the very cool [RexPaint application](https://www.gridsagegames.com/rexpaint/index.html)

- Implementing NPCs that can move around and speak to the player.
	- Message box UI will be needed for this too.

### Overly-ambitious game design ideas/long-term goals
Some things I have in mind for what I think would be a cool game, and what I'll be building up to.
- An 'active-time' Roguelike.
	- The game should flow in real-time, not just when the player moves as in a traditional Roguelike.
	- The game should operate in 'ticks' - NPCs or the player can move a number of tiles per tick, and maybe one tick passes each second.
- Plot things:
	- The game takes place on an alien world far in the future. It was a destination for the last remnants of humanity who left Earth
	in search of a new home after some disaster made Earth unlivable.
	- This new planet happens to be home to a number of alien species and civilizations that your colony has to find a way to cooperate with,
	or destroy.
- The player should be in charge of managing this colony of humans and building a new civilization.