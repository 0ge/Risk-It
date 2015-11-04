import xml.etree.ElementTree as ET
import Territory

class WorldMap(object):
    
    name = ""
    territories = []
    
    def is_valid(self):
        
        # Should check that each terroritories neighbours
        # are also has the territory as neighbour.
        
        return False
        
    def get_territory_for_name(self, name):
        
        for t in self.territories:
            if t.name == name:
                return t
            
    def get_territories_for_player(self, player):
        
        found_territories = []
        
        for territory in self.territories:
            if territory.owner is player:
                found_territories.append(territory)
                
        return found_territories
        
    def read_map_file(self, file):
        tree = ET.parse(file)
        root = tree.getroot()
        
        self.name = root.get('name')
        
        # Loop through all territories
        for territory in root:
            t = Territory.Territory()
            t.name = territory.get('name')
            t.troops = int(territory.find('Troops').text)
            t.continent = territory.find('Continent').text
            self.territories.append(t)
            
        # Loop again and set territories
        for territory in root:
            t = self.get_territory_for_name(territory.get('name'))
            for neighbour in territory.find('Neighbours'):
                n = self.get_territory_for_name(neighbour.get('name'))
                print 'Adding ' + n.name + ' to ' + t.name
                t.neighbours.append(n)
        
    def description(self):
        
        desc = 'Map: ' + self.name + '\n'
        
        for t in self.territories:
            desc += t.description() + '\n'
            
        return desc