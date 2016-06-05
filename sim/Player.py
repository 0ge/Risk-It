import Move
from random import randint

class Player(object):
    
    def __init__(self):
        self.cards = []
        self.reinforcements = 0
        self.name = "No name."
        self.has_attacked_randomly = False

    def __str__(self):
        return self.name

    def random_controlled_territory(self, world_map):
        available_territories = world_map.get_territories_for_player(self)
        random_territory = available_territories[randint(0, len(available_territories)-1)]

        return random_territory

    def territories_with_enemy_neighbour(self, world_map):
        available_territories = world_map.get_territories_for_player(self)
        valid_territories = list()

        # Loop through territories and check if any of neighbour is not this player
        for territoriy in available_territories:
            enemy_borders = False
            for neighbour in territoriy.neighbours:
                if neighbour.owner is not self:
                    enemy_borders = True
                    break
            if enemy_borders:
                valid_territories.append(territoriy)

        # Select territory at random
        return valid_territories


    
    def do_turn(self, world_map):
        
        #TODO: Implement standard behaviour
        # Simple logic:
        # If reinforcements: reinforce random territory
        # Else: Attack random neighbour once
        
        if self.reinforcements > 0:
            return self.do_reinforce(world_map)
            
        else:
            move = self.do_attack(world_map);

            if (type(move) is Move.EndMove):
                self.has_attacked_randomly = False;

            return move;

    def do_reinforce(self, world_map):

        random_territory = self.random_controlled_territory(world_map)
        self.has_attacked_randomly = False
        return Move.Reinforce(self, random_territory, self.reinforcements)


    def do_attack(self, world_map):

        prospect_territories = self.territories_with_enemy_neighbour(world_map)
        selected_territory = None
        for territory in prospect_territories:
            if territory.troops > 1:
                selected_territory = territory
                break

        if self.has_attacked_randomly:
            print("Has already attacked randomly.")
            return Move.EndMove(self)

        if territory is None:
            print("Player can not attack (no troops in any territory with enemy neighbour).")
            return Move.EndMove(self)

        all_available_neighbours = selected_territory.neighbours

        available_neighbours = []
        for neighbour in all_available_neighbours:
            if not neighbour.owner.name == self.name:
                available_neighbours.append(neighbour)

        if len(available_neighbours) < 1:
            print("Did not find any neighbours.")
            return Move.EndMove(self)

        random_neighbour = available_neighbours[randint(0, len(available_neighbours)-1)]
        attackers = selected_territory.troops - 1

        if (attackers < 1):
            print("Less than 1 attacker in " + selected_territory.name + " - ending turn.")
            return Move.EndMove(self)

        if (attackers > 3):
            attackers = 3

        self.has_attacked_randomly = True

        return Move.AttackMove(self, selected_territory, random_neighbour, attackers)