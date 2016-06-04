class Continent(object):

    def __init__(self):
        self.name = ''
        self.territories = []
        self.bonusTroops = 0

    def description(self):

        desc = self.name + ' <' + ','.join(x.name for x in self.territories) + '>'

        return desc