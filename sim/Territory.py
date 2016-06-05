class Territory(object):
    
    def __init__(self):
        self.name = ''
        self.neighbours = []
        self.troops = 1
        self.owner = None
    
    def is_neighbour_of(self, neighbour):
        
        #TODO: Implement
        return False
        
    def description(self):
        
        desc = self.name + ' (' + self.owner.name + ', ' + str(self.troops) + '):  <' + ','.join(x.name for x in self.neighbours) + '>'
        
        return desc