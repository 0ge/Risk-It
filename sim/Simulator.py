import Player
import Move
import MoveValidator
import MoveExecutor
import WorldMap
import copy
import math
import random

class Simulator(object):
    
    ERROR = 0
    WARNING = 1
    INFO = 2
    VERBOSE = 3
    DEBUG = 4
    
    def __init__(self, world_map):
    
        self.max_turns = 10
        self.max_player_tries = 3
        self.world_map = world_map
        self.players = []
        self.history = []
        self.number_of_turns = 0
        self.winner = None
        
        p1 = Player.Player()
        p1.name = "Player 1"
        p2 = Player.Player()
        p2.name = "Player 2"
        
        self.players.append(p1)
        self.players.append(p2)
        random.shuffle(self.players)
        
        self.validator = MoveValidator.MoveValidator()
        self.executor = MoveExecutor.MoveExecutor()
        
        self.log_level = 255
        
        self.assign_territories_to_players()
        
    def assign_territories_to_players(self):
        
        random.shuffle(self.world_map.territories)
        number_of_territories = len(self.world_map.territories)
        number_of_players = len(self.players)
        
        for i in range(0, number_of_territories):
            self.world_map.territories[i].owner = self.players[i % number_of_players]
            print("Set owner of " + self.world_map.territories[i].name + " to " + self.players[i % number_of_players].name)
        
    def print_msg(self, level, msg):
        
        if level <= self.log_level:
            print(msg)
    
    def restore_player(self, old_player, new_player):
        
        new_player.cards = old_player.cards
        new_player.reinforcements = old_player.reinforcements
        
    def run(self):
        
        # Do moves until limit is reached
        self.number_of_turns = 0
        while self.number_of_turns < self.max_turns:


            self.print_msg(self.INFO, "===================")
            self.print_msg(self.INFO, "ROUND " + str(self.number_of_turns + 1));
            self.print_msg(self.INFO, "-------------------")

            if self.do_turn():
                break;
            self.number_of_turns += 1

            self.print_msg(self.VERBOSE, self.world_map.description());
        
    def do_turn(self):
        
        # Turns works in the following way.
        # Player's do_turn method is called. It returns a move.
        # If the move is None the Player is done.
        # Otherwise, the Simulator will validate the move. If it was
        # a valid move the Simulator will update the WorldMap
        # accordingly. If it was not a valid move the WorldMap will
        # not be updated, but the Player may try another move. After
        # n consecutive fails the Player is skipped.

        for player in self.players:
            self.do_player_turns(player)
            self.print_msg(self.INFO, "-------------------")

            if (self.game_has_ended()):
                return True


        
        # Return True if game is over
        return False
            
    def do_player_turns(self, player):
        
        # Note: To avoid tampering with the internals of the player,
        # the player's attributes are reset to its previous values
        # when the player has made its move. This preserves its custom
        # variables, but hinders the player from changing number of
        # cards, etc.

        player_tries = 0        
        self.reinforce_player(player)
        
        # Make moves until player is finished or failed to make valid move
        while player_tries < self.max_player_tries:

            # To avoid the player from modifying itself, we let the player
            # execute on a copy of itself and execute the move on the
            # orignal player.
            player_copy = copy.deepcopy(player)

            # We must catch all any exception a player could throw. If it does,
            # we end its turn.
            try:
                move = player.do_turn(self.world_map)
            except Exception as exception:
                print("Player throw exception. Ending turn.")
                move = Move.EndMove()

            self.print_msg(self.VERBOSE, "Player " + str(player) + ": " + str(move))

            self.restore_player(player_copy, player)
            
            if self.is_valid_move(move, player):
                self.execute_move(move)
            
                # If the move was a TacticalMove or None, the round is finished
                if isinstance(move, Move.TacticalMove) or isinstance(move, Move.EndMove):
                    print("Player turn ended.")
                    break

            else:
                player_tries += 1
                self.print_msg(self.WARNING, player.name + ' made invalid move. ' + self.validator.msg)
            
    def is_valid_move(self, move, player):
        
        return self.validator.valid_move(self.world_map, move)
                
    def execute_move(self, move):
        
        self.history.append(move)
        self.executor.execute_move(self.world_map, move)
        
    def reinforce_player(self, player):
        
        # Player gets one reinforcement per 3 territories (minimum 3)
        player.reinforcements = math.floor(len(self.world_map.get_territories_for_player(player))/3.0)
        if player.reinforcements < 3:
            player.reinforcements = 3
            
        self.print_msg(self.INFO, 'Reinforce player ' + player.name + ' with ' + str(player.reinforcements) + " troops.")
        
    def stats(self):
        
        # This will return a formatted table with some statistics about the game

        if self.winner is not None:
            winner_msg = "Winner: " + self.winner.name + "\n"
        else:
            winner_msg = "Draw!\n"
        rounds_played = "Rounds played: " + str(self.number_of_turns) + "/" + str(self.max_turns) + "\n"

        return winner_msg + rounds_played

    def game_has_ended(self):

        # Check for total world domination by one player
        for player in self.players:
            territories_controlled_by_player = len(self.world_map.get_territories_for_player(player))
            total_number_of_territories = len(self.world_map.territories)
            if  territories_controlled_by_player == total_number_of_territories:
                self.winner = player
                return True

        return False

    

board_map = WorldMap.WorldMap()
board_map.read_map_file('World.xml')
sim = Simulator(board_map)
sim.run()
print(sim.stats())
print(sim.world_map.description())
