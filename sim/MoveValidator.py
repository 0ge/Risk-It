import WorldMap
import Move

class MoveValidator(object):
        
    def valid_move(self, map, move, player):
        
        self._map = map
        self._move = move
        self._player = player
        
        # If there are reinforcements, these must be placed, or cards must be played
        if player.reinforcements > 0:
            if move.__class__ is not Reinforce and move.__class__ is not TradeCards:
                return False
        
        if move.__class__ is Reinforce:
            return is_valid_reinforce()
        
        if move.__class__ is AttackMove:
            return is_valid_attack_move()
        
        if move.__class__ is TacticalMove:
            return is_valid_tactical_move()
        
    def is_valid_reinforce(self):
    
        # Reinforcements must satisfy the following:
        # - Territory must be owned by player
        # - Must not place more reinforcement than player has
        
        if self._move.origin.owner is not self._player:
            return False
            
        if self._move.quantity > self._player.reinforcements:
            return False
            
        return True
    
    def is_valid_attack_move(self):
        
        # AttackMove must satisfy the following:
        # - The attacker must not attack with more than 3 troops
        # - The attacker must leave at least 1 troop behind
        # - The origin must be owned by the player
        # - The target's owner must not be the attacker
        
        if  self._move.quantity >= self._move.origin.troops:
            return False
            
        if self._move.quantity > 3:
            return False
            
        if self._move.origin.owner is not self._player:
            return False
            
        if self._move.target.owner is self._player:
            return False
        
        return True
    
    def is_valid_tactical_move(self):
        
        # TacticalMove must satisfy the following:
        # - The target must be owned by the player
        # - At least one troop must be left behind
        
        if self._move.target.owner is not self._player:
            return False
            
        if self._move.quantity >= self._move.origin.troops:
            return False
    
        return False
        
    def is_valid_trade_cards(self):
        
        # TradeCards must satisfy the following:
        # - Three cards
        # - Each unique or all the same
        
        if len(self._move.cards) != 3:
            return False
            
        unique = set(self._move.cards)
        if len(unique) != 3 and len(unique) != 1:
            return False
            
        return True