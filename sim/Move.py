class Move:
    
    # A move is either a reinforcement, an attack or a tactical move.
    # These are all subclasses of Move. Use introspection to determine
    # which.
    origin
    target
    quantity
    
class Reinforce(Move):
    
    def __init__(self, origin, quantity):
        
        self.origin = origin
        self.quantity = quantity
    
class AttackMove(Move):
    
    def __init__(self, origin, target, quantity):
        
        self.origin = origin
        self.target = target
        self.quanity = quantity
    
class TacticalMove(Move):
    
    def __init__(self, origin, target, quantity):
        
        self.origin = origin
        self.target = target
        self.quantity = quantity