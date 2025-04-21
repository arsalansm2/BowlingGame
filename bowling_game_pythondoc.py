# bowling_game.py

class BowlingGame:
    """
    A class to simulate a standard 10-pin bowling game.

    Methods:
    --------
    roll(pins):
        Records the number of pins knocked down in a single roll.
    
    score():
        Calculates the total score of the game.

    is_strike(i):
        Returns True if the roll at index i is a strike.

    is_spare(i):
        Returns True if the rolls at index i and i+1 are a spare.

    strike_bonus(i):
        Calculates bonus score for a strike.

    spare_bonus(i):
        Calculates bonus score for a spare.

    sum_of_balls_in_frame(i):
        Calculates the score for a standard frame.

    safe_get(index):
        Safely returns the value at a given index or 0 if out of bounds.
    """

    def __init__(self):
        """Initializes a new bowling game with an empty roll list."""
        self.rolls = []

    def roll(self, pins):
        """
        Records the number of pins knocked down in a roll.

        Parameters:
        -----------
        pins : int
            Number of pins knocked down (0 to 10).
        """
        self.rolls.append(pins)

    def score(self):
        """
        Calculates the total score for the game.

        Returns:
        --------
        int
            Total score based on the standard bowling rules.
        """
        result = 0
        roll_index = 0
        for _ in range(10):
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
        """Returns True if the roll at index i is a strike."""
        return self.rolls[i] == 10

    def strike_bonus(self, i):
        """Returns the bonus points awarded for a strike."""
        return self.safe_get(i + 1) + self.safe_get(i + 2)

    def is_spare(self, i):
        """Returns True if the rolls at i and i+1 add up to a spare."""
        return self.rolls[i] + self.rolls[i+1] == 10

    def spare_bonus(self, i):
        """Returns the bonus points awarded for a spare."""
        return self.safe_get(i + 2)

    def sum_of_balls_in_frame(self, i):
        """Returns the total pins knocked down in a frame."""
        return self.rolls[i] + self.rolls[i+1]

    def safe_get(self, index):
        """
        Safely returns the roll value at index or 0 if out of bounds.

        Parameters:
        -----------
        index : int
            The index in the rolls list to access.

        Returns:
        --------
        int
            The value at the index or 0.
        """
        return self.rolls[index] if index < len(self.rolls) else 0
