class Move(object):
    
    # A move is either a reinforcement, an attack or a tactical move.
    # These are all subclasses of Move.
    
    def __init__(self, player):
        self.origin = None
        self.quantity = 0
        self.target = None
        self.player = player
        
class EndMove(Move):
    
    def __init__(self, player):
        super(EndMove, self).__init__(player)
        
    def __str__(self):
        return self.player.name + " ended its turn."
        
class TradeCards(Move):
    
    def __init__(self, player):
        super(TradeCards, self).__init__(player)
        self.cards = cards
        
    def __str__(self):
        return self.player.name + " traded cards."
    
class Reinforce(Move):
    
    def __init__(self, player, target, quantity):
        super(Reinforce, self).__init__(player)
        self.target = target
        self.quantity = quantity
        
    def __str__(self):
        return self.player.name + " reinforced with " + str(self.quantity) + " to " + self.target.name + "."
    
class AttackMove(Move):
    
    def __init__(self, player, origin, target, quantity):
        super(AttackMove, self).__init__(player)
        self.origin = origin
        self.target = target
        self.quantity = quantity
        
    def __str__(self):
        return self.player.name + " attacked " + self.target.name + " with " + str(self.quantity) + " troops."
    
class TacticalMove(Move):
    
    def __init__(self, player, origin, target, quantity):
        super(TacticalMove, self).__init__(player)
        self.origin = origin
        self.target = target
        self.quantity = quantity
        
    def __str__(self):
        return self.player.name + " moved " + str(self.quantity) + " troops from " + self.origin.name + " to " + self.target.name + "."