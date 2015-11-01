class Territory:
    
    def __init__(self):
        self.name = ''
        self.neighbours = []
        self.troops = 1
        self.continent = ''
    
    def is_neighbour_of(self, neighbour):
        
        return False
        
    def description(self):
        
        desc = self.name + ' (' + self.troops + '): ' + self.continent + ' <' + ','.join(x.name for x in self.neighbours) + '>'
        
        return desc