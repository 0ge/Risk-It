class MoveValidator(object):
        
    def valid_move(self, map, move):
        
        if move.__class__ is Reinforce:
            return is_valid_reinforce(move)
        
        if move.__class__ is AttackMove:
            return is_valid_attack_move(move)
        
        if move.__class__ is TacticalMove:
            return is_valid_tactical_move
        
    def is_valid_reinforce(self, move):
    
        return False
    
    def is_valid_attack_move(self,move):
    
        return False
    
    def is_valid_tactical_move(self, move):
    
        return False