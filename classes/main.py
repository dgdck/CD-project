# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line


def main():
    dennis.introduce()
    print(dennis.strength())
    print(ray.compare_players(dennis, wim, 'speed'))

# 1 Players


class Player():
    def __init__(self, name, speed, endurance, accuracy):
        self.name = name
        if speed > 0 and speed <= 1:
            self.speed = speed
        else:
            raise ValueError('Speed must be between 0 and 1')
        if endurance > 0 and endurance <= 1:
            self.endurance = endurance
        else:
            raise ValueError('Endurance must be between 0 and 1')
        if accuracy > 0 and accuracy <= 1:
            self.accuracy = accuracy
        else:
            raise ValueError('Accuracy must be between 0 and 1')

    def introduce(self):
        return f"Hello everyone, my name is {self.name}."

    def strength(self):
        attributes = (
            'speed', self.speed,
            'endurance', self.endurance,
            'accuracy', self.accuracy
            )
        if self.speed == self.endurance and self.speed == self.accuracy:
            return attributes
        elif self.speed == self.endurance and self.speed > self.accuracy:
            return attributes[:4]
        elif self.speed > self.endurance and self.speed == self.accuracy:
            return attributes[:2] + attributes[4:]
        elif self.speed > self.endurance and self.speed > self.accuracy:
            return attributes[:2]
        elif self.endurance > self.speed and self.endurance > self.accuracy:
            return attributes[2:4]
        elif self.endurance > self.speed and self.endurance == self.accuracy:
            return attributes[2:]
        elif self.accuracy > self.speed and self.accuracy > self.endurance:
            return attributes[4:]


wim = Player('Wim', 0.3, 0.4, 0.9)
dennis = Player('Dennis', .3, .9, .4)


# 2 Commentators


class Commentator():
    def __init__(self, name):
        self.name = name

    def sum_player(self, player):
        return player.speed + player.endurance + player.accuracy

    def compare_players(self, p1, p2, attribute):
        if getattr(p1, attribute) > getattr(p2, attribute):
            return p1.name
        elif getattr(p1, attribute) < getattr(p2, attribute):
            return p2.name
        elif getattr(p1, attribute) == getattr(p2, attribute):
            p1_strength = p1.strength()
            p2_strength = p2.strength()
            if p1_strength[1] > p2_strength[1]:
                return p1.name
            elif p1_strength[1] < p2_strength[1]:
                return p2.name
            elif p1_strength[1] == p2_strength[1]:
                if self.sum_player(p1) > self.sum_player(p2):
                    return p1.name
                elif self.sum_player(p1) < self.sum_player(p2):
                    return p2.name
                elif self.sum_player(p1) == self.sum_player(p2):
                    return 'These two players might as well be twins!'


ray = Commentator('Ray Hudson')

if __name__ == '__main__':
    main()
