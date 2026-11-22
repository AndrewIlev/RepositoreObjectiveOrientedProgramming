import unittest

from app import Figure


class TestFigure(unittest.TestCase):
    def test_angles_for_each_figure(self) -> None:
        cases = (
            ("квадрат", [90, 90, 90, 90]),
            ("прямокутник", [90, 90, 90, 90]),
            ("трикутник", [60, 60, 60]),
        )
        for figure_type, expected_angles in cases:
            with self.subTest(figure_type=figure_type):
                figure = Figure(figure_type, 5)
                self.assertEqual(figure_type, figure.get_figure_type)
                self.assertEqual(5, figure.get_figure_length)
                self.assertEqual(expected_angles, figure.get_angles())

    def test_unknown_figure_type(self) -> None:
        with self.assertRaisesRegex(AssertionError, "Невідомий тип фігури"):
            Figure("коло", 5)

    def test_non_positive_length(self) -> None:
        for length in (0, -1):
            with self.subTest(length=length):
                with self.assertRaisesRegex(
                    AssertionError, "Довжина має бути більшою за 0"
                ):
                    Figure("квадрат", length)


if __name__ == "__main__":
    unittest.main()
