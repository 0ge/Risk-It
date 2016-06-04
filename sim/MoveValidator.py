import WorldMap
import Move

class MoveValidator(object):
        
    def valid_move(self, game_map, move):
        
        self._map = game_map
        self._move = move
        
        # If there are reinforcements, these must be placed, or cards must be played
        if self._move.player.reinforcements > 0:
            if move.__class__ is not Move.Reinforce and move.__class__ is not Move.TradeCards:
                self.msg = "Player still has reinforcements and did not move or trade cards."
                return False
        
        if move.__class__ is Move.EndMove:
            return self.is_valid_end_move()
            
        if move.__class__ is Move.Reinforce:
            return self.is_valid_reinforce()
        
        if move.__class__ is Move.AttackMove:
            return self.is_valid_attack_move()
        
        if move.__class__ is Move.TacticalMove:
            return self.is_valid_tactical_move()
        
    def is_valid_end_move(self):
        
        # The player can end it's turn if it has reinforcements or more than 4 cards
        if self._move.player.reinforcements > 0:
            self.msg = "Player tried to end turn but has " + str(self._move.player.reinforcements) + " reinforcements left."
            return False
            
        if len(self._move.player.cards) > 4:
            self.msg = "Player tried to end turn but has " + str(len(self._move.player.cards)) + " cards."
            return False
            
        return True
        
    def is_valid_reinforce(self):
    
        # Reinforcements must satisfy the following:
        # - Territory must be owned by player
        # - Must not place more reinforcement than player has
        
        if self._move.target.owner is not self._move.player:
            self.msg = "Player tried to reinforce territory not under players control."
            return False
            
        if self._move.quantity > self._move.player.reinforcements:
            self.msg = "Player tried to reinforce with " + str(self.quantity) + " troops but has only " + str(self._move.player.reinforcements) + " troops available."
            return False
            
        return True
    
    def is_valid_attack_move(self):
        
        # AttackMove must satisfy the following:
        # - The attacker must not attack with more than 3 troops
        # - The attacker must leave at least 1 troop behind
        # - The origin must be owned by the player
        # - The target's owner must not be the attacker
        
        if  self._move.quantity >= self._move.origin.troops:
            self.msg = "Player tried to attack with " + str(self._move.quantity) + " troops with only " + str(self._move.origin.troops) + " troops in originating territory."
            return False
            
        if self._move.quantity > 3:
            self.msg = "Player tried to attack with more than 3 troops (" + str (self._move.quantity) + ")"
            return False
            
        if self._move.quantity < 1:
            self.msg = "Player tried to attack with less than 1 troop (" + str (self._move.quantity) + ")"
            return False
            
        if self._move.origin.owner is not self._move.player:
            self.msg = "Player tried to attack from territory " + self._move.origin.name + ", which is not under player's control."
            return False
            
        if self._move.target.owner is self._move.player:
            self.msg = "Player tried to attack itself from territory " + self._move.origin.name + " to " + self._move.target.name + "."
            return False
        
        return True
    
    def is_valid_tactical_move(self):
        
        # TacticalMove must satisfy the following:
        # - The target must be owned by the player
        # - At least one troop must be left behind
        
        if self._move.target.owner is not self._move.player:
            return False
            
        if self._move.quantity >= self._move.target.troops:
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