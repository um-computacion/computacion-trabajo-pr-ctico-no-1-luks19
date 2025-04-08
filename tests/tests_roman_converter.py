import unittest
from src.roman_converter import decimal_to_roman
class TestRomanConverter(unittest.TestCase):

    def test_conversion_simple(self):
        self.assertEqual(decimal_to_roman(1), 'I')
        self.assertEqual(decimal_to_roman(5), 'V')
        self.assertEqual(decimal_to_roman(10), 'X')
        self.assertEqual(decimal_to_roman(50), 'L')
        self.assertEqual(decimal_to_roman(100), 'C')
        self.assertEqual(decimal_to_roman(500), 'D')
        self.assertEqual(decimal_to_roman(1000), 'M')

    def test_substraction(self):
        self.assertEqual(decimal_to_roman(4), 'IV')
        self.assertEqual(decimal_to_roman(9), 'IX')
        self.assertEqual(decimal_to_roman(40), 'XL')
        self.assertEqual(decimal_to_roman(90), 'XC')
        self.assertEqual(decimal_to_roman(400), 'CD')
        self.assertEqual(decimal_to_roman(900), 'CM')

    def test_range(self):
        self.assertEqual(decimal_to_roman(3999), 'MMMCMXCIX')

    def test_complex_numbers(self):
        self.assertEqual(decimal_to_roman(1234), 'MCMXCIX')
        self.assertEqual(decimal_to_roman(7651), 'MMCCCXLV')
        self.assertEqual(decimal_to_roman(7653), 'MMMDXX')
        self.assertEqual(decimal_to_roman(764), 'DCCCLXXXVIII')
             
if __name__ == '__main__':
    unittest.main()