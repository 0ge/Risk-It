class Move(object):
    
    # A move is either a reinforcement, an attack or a tactical move.
    # These are all subclasses of Move.
    
    def __init__(self):
        self.origin = None
        self.quantity = 0
        self.target = None
    
class Reinforce(Move):
    
    def __init__(self, origin, quantity):
        super.__init__()
        self.origin = origin
        self.quantity = quantity
    
class AttackMove(Move):
    
    def __init__(self, origin, target, quantity):
        super.__init__()
        self.origin = origin
        self.target = target
        self.quanity = quantity
    
class TacticalMove(Move):
    
    def __init__(self, origin, target, quantity):
        super.__init__()
        self.origin = origin
        self.target = target
        self.quantity = quantity