import Player

class Simulator:
    
    max_turns = 100
    max_player_tries = 3
    world_map = None
    players = []
    
    def init(self):
        players.add(Player())
    
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
        
        player_copy = player.copy()
        move = player.do_turn(world_map)
        
        # Make moves until player is finished or failed to make valid move
        while move is not None and tries < max_player_tries:
            
            self.restore_player(player_copy, player)
            
            if self.is_valid_move(move):
                self.execute_move(move)
            else:
                player_tries += 1
            
            move = player.do_turn(world_map)
                
    def execute_move(self, move):
        
        print "Executing move..."
    

sim = Simulator()
sim.run()   
