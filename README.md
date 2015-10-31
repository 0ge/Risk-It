# Risk-It
Risk game simulator to battle with AIs.

# Game logic

The game is turned based. It uses standard Risk rules, so anyone familiar with those rules should be familiar with these.
There are some additional constraints placed on the game to allow it to simulate smoothly. These are as follows.

1. If the game has not ended within a certain number of rounds, the game is finished and winning order is determined by the player controlling the most territories. Army size does not count.
2. If a player (AI) fails to make a valid move a certain number of times, the player's turn is finished.

A game consits of a number of *rounds*, in which each player has a *turn*.

## Start

The game is started by loading a map and randomizing the order of players and then their territories.
The territories are randomly assigned in player order, meaning if the number of territories are not evenly divided by the number of players, the players starting will start with more territories.
Each player then has a number of reinforcements to place and may place these to its will to its controlled territories. This is done hidden, i.e. no player knows another player's reinforcement beforehand.

## Player's turn

A player's turn consists of three phases; reinforcement, attacking and move. Attacking and moving are optional.

### Reinforce

Reinforcements are determined by the number of controlled territories and number of controlled areas. Additionally, cards may be traded to receive additional reinforcements. See table below.
The reinforcements may be placed in any distribution over the territories controlled by the player.

**Card values**

| Cards       | Troops |
| ----------- | ------ |
| 3 circles   | 4      |
| 3 squares   | 6      |
| 3 stars     | 8      |
| One of each | 10     |

### Attack and defense

A player may attack from one territory to an adjecent enemy territory. The attacker may choose to attack with 1-3 troops, but there must be at least one troop left in the territory attacking.
E.g. a territory with 3 troops may attack with 1 *or* 2 troops.
Similarily, the defender may defend with 1-2 troops. However, the defender may choose to defend with all available troops. E.g. a territory with 2 troops may defend with 1 *or* 2 troops.

The battle results are determined by dice rolls. The attack gets one dice per attacking troop (i.e. 1-3 dices) and the defender gets one dice per defending troop (i.e. 1-2 dices).
The highest attacking dice is then compared with the highest defending dice. If *both* players have 2 or more dices, the second highest attacking dice is compared with the second highest defending dice.
Whoever has the lowest value for each attacking-defending pair, loses one troop. If the dice pair are equal, the attacker loses.

A player may attack any number of times from any number of territories in any order, assuming the above rules are obeyed.

**Examples**

| Attacking dices | Defender dices | Attacker loss | Defender loss |
| --------------- | -------------- | ------------- | ------------- |
| 5,3,1           | 6,2            | 1             | 1             |
| 6               | 6              | 1             | 0             |
| 5               | 6,2            | 1             | 0             |
| 3,3             | 6,1            | 1             | 1             |

### Move

At the end of each turn, the player may move any number of troops from one territory to another *once*, but at least one troop must remain in the originating territory.
