# bowling_game.py

class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        """Record a roll."""
        self.rolls.append(pins)

    def score(self):
    result = 0
    roll_index = 0
    for _ in range(10):  # 10 frames
        if self.is_strike(roll_index):
            result += 10 + self.strike_bonus(roll_index)
            roll_index += 1
        elif self.is_spare(roll_index):
            result += 10 + self.spare_bonus(roll_index)
            roll_index += 2
        else:
            result += self.sum_of_balls_in_frame(roll_index)
            roll_index += 2
    return result

    def is_strike(self, i):
        return self.rolls[i] == 10

    def strike_bonus(self, i):
        return self.rolls[i+1] + self.rolls[i+2]

    def is_spare(self, i):
        return self.rolls[i] + self.rolls[i+1] == 10

    def spare_bonus(self, i):
        return self.rolls[i+2]

    def sum_of_balls_in_frame(self, i):
        return self.rolls[i] + self.rolls[i+1]
