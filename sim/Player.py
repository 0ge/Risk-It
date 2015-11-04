import Move
from random import randint

class Player(object):
    
    def __init__(self):
        self.cards = []
        self.reinforcements = 0
        self.name = "No name."
    
    def do_turn(self, world_map):
        
        #TODO: Implement standard behaviour
        # Simple logic:
        # If reinforcements: reinforce random territory
        # Else: End move
        
        if self.reinforcements > 0:
            available_territories = world_map.get_territories_for_player(self)
            random_territory = available_territories[randint(0, len(available_territories)-1)]
            return Move.Reinforce(self, random_territory, self.reinforcements)
        else:
            return Move.EndMove(self)