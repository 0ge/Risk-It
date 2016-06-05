import Move
from random import randint

class MoveExecutor(object):
    
    def execute_move(self, map, move):
        # TODO: Implement
        
        self.move = move
        if isinstance(move, Move.Reinforce):
            self.execute_reinforce()
            
        if isinstance(self.move, Move.AttackMove):
            self.execute_attack()
            
        print(move)
        
    def execute_reinforce(self):
        
        print("Executing reinforcement.")
        self.move.target.troops += self.move.quantity
        self.move.player.reinforcements -= self.move.quantity
        
        
    def execute_attack(self):
        
        print("Executing attack.")
        attacker_dices = []
        
        for i in range(0, self.move.quantity):
            attacker_dices.append(randint(1,6))
            
        defender_dices = []
        
        for i in range(0, self.move.target.troops):
            defender_dices.append(randint(1,6))
            
        if len(defender_dices) > 2:
            defender_dices = defender_dices[0:1]
            
        dices = min(len(defender_dices), len(attacker_dices))
        attacker_dices.sort(reverse = True)
        defender_dices.sort(reverse = True)
        
        attacker_losses = 0
        defender_losses = 0
        
        print(str(len(attacker_dices)) + " vs. " + str(len(defender_dices)))
        
        for i in range(0,dices):
            attacker_wins = attacker_dices[i] > defender_dices[i]
            
            if attacker_wins:
                attacker_losses += 1
            else:
                defender_losses += 1
                
        self.move.origin.troops -= attacker_losses
        self.move.target.troops -= defender_losses

        print("Attacker lost " + str(attacker_losses) + " troops. Defender lost " + str(defender_losses) + " troops. Dices: " + ','.join(str(x) for x in attacker_dices) + " vs " + ','.join(str(x) for x in defender_dices))
        
        # Take control
        if self.move.target.troops < 1:
            print(self.move.player.name + " took control over " + self.move.target.name + ".")
            self.move.target.owner = self.move.player