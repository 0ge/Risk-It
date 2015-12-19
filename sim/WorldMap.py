import xml.etree.ElementTree as ET
import Territory
import Continent
import sys

class WorldMap(object):
    
    name = ""
    territories = []
    continents = []
    
    def is_valid_territories(self):

        names = []
        for t in self.territories:
            names.append(t.name)
            for n in t.neighbours:
                correct = False
                for nn in n.neighbours:
                    if nn.name == t.name:
                        correct = True

                if not correct:
                    print 'Map error: ' + n.name + ' does not list '\
                          + t.name + ' as a neighbour!'
                    sys.exit(1)

    def is_valid_continents(self):

        territories = []
        territories_in_continents = []
        for t in self.territories:
            territories.append(t.name)

        for c in self.continents:
            for t in c.territories:
                territories_in_continents.append(t.name)

        a = set(territories) - set(territories_in_continents)
        if a:
            print ", ".join(str(e) for e in a) + ' is not assigned to a continent'
            sys.exit(1)

        a = set(territories_in_continents) - set(territories)
        if a:
            print ", ".join(str(e) for e in a) + ' is listed in a continent but is not a territory'
            sys.exit(1)

        for t in territories_in_continents:
            if territories_in_continents.count(t) > 1:
                print t + ' occurs in several continents'
                sys.exit(1)



    def get_territory_for_name(self, name):
        
        for t in self.territories:
            if t.name == name:
                return t

    def get_continent_for_name(self, name):

        for c in self.continents:
            if c.name == name:
                return c
            
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
        
        # Loop through all territories/continents
        for entry in root:
            if entry.tag == 'Territory':
                t = Territory.Territory()
                t.name = entry.get('name')
                t.troops = int(entry.find('Troops').text)
                self.territories.append(t)

            if entry.tag == 'Continent':
                c = Continent.Continent()
                c.name = entry.get('name')
                c.bonusTroops = int(entry.find('BonusTroops').text)
                self.continents.append(c)
            
        # Loop again and set territories
        for entry in root:
            if entry.tag == 'Territory':
                t = self.get_territory_for_name(entry.get('name'))
                for neighbour in entry.find('Neighbours'):
                    n = self.get_territory_for_name(neighbour.get('name'))
                    print 'Adding ' + n.name + ' to ' + t.name
                    t.neighbours.append(n)

            if entry.tag == 'Continent':
                c = self.get_continent_for_name(entry.get('name'))
                for territory in entry.find('Territories'):
                    t = self.get_territory_for_name(territory.get('name'))
                    print 'Adding ' + t.name + ' to ' + c.name
                    c.territories.append(t)


        self.is_valid_territories()
        self.is_valid_continents()
        
    def description(self):
        
        desc = 'Map: ' + self.name + '\n'
        
        for t in self.territories:
            desc += t.description() + '\n'
            
        return desc