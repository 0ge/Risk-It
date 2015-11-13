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
            print "Set owner of " + self.world_map.territories[i].name + " to " + self.players[i % number_of_players].name
        
    def print_msg(self, level, msg):
        
        if level <= self.log_level:
            print msg
    
    def restore_player(self, old_player, new_player):
        
        new_player.cards = old_player.cards
        new_player.reinforcements = old_player.reinforcements
        
    def run(self):
        
        # Do moves until limit is reached
        number_of_turns = 0
        while number_of_turns < self.max_turns:
            if self.do_turn():
                break;
            number_of_turns += 1
        
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
        
            player_copy = copy.deepcopy(player)
            move = player.do_turn(self.world_map)
            self.restore_player(player_copy, player)
            
            if self.is_valid_move(move, player):
                self.execute_move(move)
            
                # If the move was a TacticalMove or None, the round is finished
                if isinstance(move, Move.TacticalMove) or isinstance(move, Move.EndMove):
                    break
            else:
                player_tries += 1
                self.print_msg(self.VERBOSE, player.name + ' made invalid move. ' + self.validator.msg)
            
            move = player.do_turn(self.world_map)
            
    def is_valid_move(self, move, player):
        
        return self.validator.valid_move(self.world_map, move)
                
    def execute_move(self, move):
        
        self.executor.execute_move(self.world_map, move)
        
    def reinforce_player(self, player):
        
        # Player gets one reinforcement per 3 territories (minimum 3)
        player.reinforcements = math.floor(len(self.world_map.get_territories_for_player(player))/3.0)
        if player.reinforcements < 3:
            player.reinforcements = 3
            
        self.print_msg(self.INFO, 'Reinforce player ' + player.name + ' with ' + str(player.reinforcements) + " troops.")
    

board_map = WorldMap.WorldMap()
board_map.read_map_file('LargeWorld.xml')
sim = Simulator(board_map)
sim.run()
print sim.world_map.description()