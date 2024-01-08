"""Game tests module"""
import unittest
from main import User, Board


class Test(unittest.TestCase):
    """Test class"""
    def setUp(self):
        """Set up method"""
        self.player1 = User("Denis", "Crosses")
        self.player2 = User("Masha", "Circles")
        self.board = Board()

    def test_init(self):
        """Test function for initialization"""
        self.assertEqual(self.player1.name, "Denis")
        self.assertEqual(self.player2.name, "Masha")
        self.assertTrue(
            self.player1.role.lower() and self.player2.role.lower() in ("circles", "crosses"))

    def test_set_figure(self):
        """Testing setting figures"""
        self.board.set_value(0, 0, "Crosses")
        self.board.set_value(0, 1, "Circles")
        self.assertEqual(self.board.board[0][0], 1)
        self.assertEqual(self.board.board[0][1], 0)

    def test_setting_same_place_error(self):
        """Testing setting the figure in the same place"""
        self.board.set_value(0, 0, "Crosses")
        with self.assertRaises(ValueError):
            self.board.set_value(0, 0, "Circles")
            self.board.set_value(0, 0, "Crosses")

    def test_set_out_of_bounds(self):
        """Testing case of out of bounds"""
        with self.assertRaises(ValueError):
            self.board.set_value(3, 3, "Crosses")
            self.board.set_value(5, 5, "Circles")
