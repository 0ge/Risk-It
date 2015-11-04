import Move

class MoveExecutor(object):
    
    def execute_move(self, map, move):
        # TODO: Implement
        
        self.move = move
        if move.__class__ is Move.Reinforce:
            self.execute_reinforce()
            
        print move
        
    def execute_reinforce(self):
            
        self.move.target.troops += self.move.quantity
        self.move.player.reinforcements -= self.move.quantity