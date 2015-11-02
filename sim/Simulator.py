import Player
import Move
import MoveValidator
import MoveExecutor
import copy

class Simulator(object):
    
    def __init__(self):
    
        self.max_turns = 100
        self.max_player_tries = 3
        self.world_map = None
        self.players = []
        self.players.append(Player.Player())
    
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
        
        player_copy = copy.deepcopy(player)
        move = player.do_turn(self.world_map)
        
        # Make moves until player is finished or failed to make valid move
        while move is not None and tries < max_player_tries:
            
            self.restore_player(player_copy, player)
            
            if self.is_valid_move(move):
                self.execute_move(move)
            else:
                player_tries += 1
            
            move = player.do_turn(world_map)
            
    def is_valid_move(self, move):
        
        return MoveValidator.MoveValidator.valid_move(self.map, move)
                
    def execute_move(self, move):
        
        MoveExecutor.MoveExecutor.execute_move(self.map, move)
    

sim = Simulator()
sim.run()   
