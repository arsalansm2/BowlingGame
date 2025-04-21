# test_bowling_game.py

import unittest
from bowling_game import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame()

    def roll_many(self, pins, times):
        for _ in range(times):
            self.game.roll(pins)

    def roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)

    def roll_strike(self):
        self.game.roll(10)

    def test_gutter_game(self):
        self.roll_many(0, 20)
        self.assertEqual(self.game.score(), 0)

    def test_all_ones(self):
        self.roll_many(1, 20)
        self.assertEqual(self.game.score(), 20)

    def test_one_spare(self):
        self.roll_spare()
        self.game.roll(3)
        self.roll_many(0, 17)
        self.assertEqual(self.game.score(), 16)

    def test_one_strike(self):
        self.roll_strike()
        self.game.roll(3)
        self.game.roll(4)
        self.roll_many(0, 16)
        self.assertEqual(self.game.score(), 24)

    def test_perfect_game(self):
        self.roll_many(10, 12)
        self.assertEqual(self.game.score(), 300)

    def test_all_spares(self):
        for _ in range(10):
            self.roll_spare()
        self.game.roll(5)
        self.assertEqual(self.game.score(), 150)

    def test_random_game(self):
        rolls = [1, 2, 3, 4, 5, 4, 3, 2, 10, 0, 1, 10, 10, 6, 2, 0, 1]
        for r in rolls:
            self.game.roll(r)
        self.assertTrue(isinstance(self.game.score(), int))

    def test_strike_in_last_frame(self):
        self.roll_many(0, 18)
        self.roll_strike()
        self.game.roll(10)
        self.game.roll(10)
        self.assertEqual(self.game.score(), 30)

    def test_spare_in_last_frame(self):
        self.roll_many(0, 18)
        self.roll_spare()
        self.game.roll(5)
        self.assertEqual(self.game.score(), 15)

if __name__ == '__main__':
    unittest.main()
