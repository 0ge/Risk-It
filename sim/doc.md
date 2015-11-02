# Source documentation

This page contains the source code documentation for the simulator.

## Versioning

This repo uses [GitFlow](http://nvie.com/posts/a-successful-git-branching-model/).
For a small project like this, it basically boils down to using two branches; `master` that holds the latest stable release and `develop` where all new (untested) commits are added.

## Simulator

The Simulator is the core. It first loads a WorldMap, then fetches moves from Players, validates Moves, executes Moves and summarizes the results.

## WorldMap

The WorldMap holds all Territories that builds up the game map. It provides function to read a map from an XML file and to validate the map.

## Territory

Holds information about a territory, such as owner, name, continent it belongs to, current troops residing in the territory, etc.

## Player

The Player class is the superclass of all AI implementations. The Simulator will set the Cards and Reinforcements variables and pass in a WorldMap. From this information the Player must figure out a valid Move and return this.

## Move

The Move is a superclass with Reinforcement, AttackMove and TacticalMove as subclasses. Quite self explanatory.

## MoveExecutor and MoveValidator

Helper classes that executes move on a map and that validates a move based on a map.
