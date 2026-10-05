import unittest
from unittest.mock import patch

from app import Figure, count_symbols, count_vowels, divide, read_positive_number


class TestFigure(unittest.TestCase):
    def test_figure_properties(self) -> None:
        for figure_type in Figure.FIGURES:
            with self.subTest(figure_type=figure_type):
                figure = Figure(figure_type, 5)
                self.assertEqual(figure_type, figure.get_figure_type)
                self.assertEqual(5, figure.get_figure_length)

    def test_figure_angles(self) -> None:
        cases = (
            ("квадрат", [90, 90, 90, 90]),
            ("прямокутник", [90, 90, 90, 90]),
            ("трикутник", [60, 60, 60]),
        )
        for figure_type, expected_angles in cases:
            with self.subTest(figure_type=figure_type):
                self.assertEqual(expected_angles, Figure(figure_type, 5).get_angles())

    def test_zero_length(self) -> None:
        with self.assertRaises(AssertionError):
            Figure("квадрат", 0)

    def test_negative_length(self) -> None:
        with self.assertRaises(AssertionError):
            Figure("квадрат", -1)

    def test_unknown_figure_type(self) -> None:
        with self.assertRaises(AssertionError):
            Figure("коло", 1)


class TestStringFunctions(unittest.TestCase):
    def test_count_symbols(self) -> None:
        self.assertEqual(3, count_symbols("abc"))

    def test_count_symbols_empty_string(self) -> None:
        self.assertEqual(0, count_symbols(""))

    def test_count_symbols_one_character(self) -> None:
        self.assertEqual(1, count_symbols("я"))

    def test_divide_by_zero(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_divide(self) -> None:
        self.assertEqual(5, divide(10, 2))

    def test_count_vowels_in_word(self) -> None:
        self.assertEqual(3, count_vowels("молоко"))

    def test_count_vowels_empty_string(self) -> None:
        self.assertEqual(0, count_vowels(""))

    def test_count_vowels_digits(self) -> None:
        self.assertEqual(0, count_vowels("12345"))

    def test_count_vowels_ukrainian_letters(self) -> None:
        self.assertEqual(4, count_vowels("Україна"))

    @patch("builtins.input", return_value="7")
    def test_read_positive_number(self, mock_input) -> None:
        self.assertEqual(7, read_positive_number())
        mock_input.assert_called_once_with("Введіть додатне ціле число: ")

    @patch("builtins.input", return_value="текст")
    def test_read_non_integer(self, mock_input) -> None:
        with self.assertRaisesRegex(ValueError, "Потрібно ввести ціле число"):
            read_positive_number()
        mock_input.assert_called_once()

    @patch("builtins.input", return_value="0")
    def test_read_zero(self, mock_input) -> None:
        with self.assertRaisesRegex(AssertionError, "більшим за нуль"):
            read_positive_number()
        mock_input.assert_called_once()


if __name__ == "__main__":
    unittest.main(verbosity=2)
