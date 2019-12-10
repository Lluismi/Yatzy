class Yatzy:

    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = d5

    @staticmethod
    def total_score(*dice):
        total = 0
        for dices in dice:
            total += dices
        return total

    @staticmethod
    def yatzy(dice):
        if dice.count(dice[0]) != 5:
            return 0
        return 50

    @staticmethod
    def ones(*dice):
        ONE = 1
        return dice.count(ONE) * ONE

    @staticmethod
    def twos(*dice):
        TWO = 2
        return dice.count(TWO) * TWO

    @staticmethod
    def threes(*dice):
        THREE = 3
        return dice.count(THREE) * THREE

    def fours(self):
        four = 4
        return self.dice.count(four) * four

    def fives(self):
        five = 5
        return self.dice.count(five) * five

    def sixes(self):
        six = 6
        return self.dice.count(six) * six

    @staticmethod
    def one_pair(*dice):
        for dado in range(6):
            if dice.count(dado) == 2:
                return 2 * dado
        return 0

    @staticmethod
    def two_pair(*dice):
        two_pairs = 0
        num = 1
        score = 0
        while two_pairs < 2 and num <= 6:
            if dice.count(num) >= 2:
                two_pairs += 1
                score += 2 * num
            num += 1
        if two_pairs == 2:
            return score
        else:
            return 0

    @staticmethod
    def three_pair(*dice):
        for dado in range(6):
            if dice.count(dado) >= 3:
                return 3 * dado
        return 0

    @staticmethod
    def four_pair(*dice):
        for dado in range(6):
            if dice.count(dado) >= 4:
                return 4 * dado
        return 0

    @staticmethod
    def smallStraight(*dice):
        for dados in range(1, 6):
             if dice.count(dados) != 1:
                return 0
        return Yatzy.total_score(*dice)

    @staticmethod
    def largeStraight(*dice):
        for dados in range(2, 6):
             if dice.count(dados) != 1:
                return 0
        return Yatzy.total_score(*dice)    

    @staticmethod
    def fullHouse(*dice):
            if Yatzy.one_pair(*dice) and Yatzy.three_pair(*dice):
                return Yatzy.one_pair(*dice) + Yatzy.three_pair(*dice)
            return 0
