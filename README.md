## Command & Conjure: Rise of the Guilds — Battle Card Simulator

A modular card battle simulator built in Python, featuring a JSON-based database and simple AI.

# About

*Command & Conjure* is a tactical fantasy card battle game with deep deck-building mechanics, inspired by the iconic Job System from Final Fantasy. Players build decks using a variety of races, jobs, and character levels to engage in strategic duels across a dynamic battlefield.

## Core Gameplay
# Deck Building
Players construct decks featuring character/monster cards, energy cards, and powerful tool cards.
# Job System
Cards represent different jobs (e.g., Warrior, Mage), with multiple levels (e.g., Warrior Lv3 vs Warrior Lv4). Higher-level cards offer stronger abilities.
# Special Jobs
Lv5 cards represent elite roles and are played in a separate slot. Each player may only have one Lv5 card active at a time.

## Energy System
The game features a layered energy mechanic with three distinct types:
Mana: Each card starts with a set amount of mana used for basic abilities.
Energy Cards: These are attached to specific cards on the field to unlock abilities.
Job Energy: A rare resource available on specific turns, required to activate powerful abilities

## Game Phases (In Development)
The turn structure is expected to follow four main phases:

*Start Phase*
*Battle Phase*
*Idle Phase*
*End Phase*

Each character/monster card can perform one action per turn, such as a basic attack. Some abilities may be used without consuming this action.

## Field Mechanics
The battlefield consists of 8 slots per player (4 front-row and 4 back-row); Cards in the back-row take halved damage and deal halved damage.
Only one card per column is allowed.
Cards can move between rows, but moving a card from front to back causes all attached cards to be discarded.

## Card Lifecycle
Each card has starting HP and Mana; When a card’s HP reaches 0, it is destroyed and sent to the discard pile.
