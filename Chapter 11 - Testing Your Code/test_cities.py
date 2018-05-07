import unittest
from city_country import city_country

class TestCityCountry(unittest.TestCase):
    """Tests for city_country.py"""

    def test_city_country(self):
        """Will 'Copenhagen, Denmark' work?"""
        test_result = city_country('Copenhagen', 'Denmark')
        self.assertEqual(test_result, 'Copenhagen, Denmark')

    def test_city_country_population(self):
        """Will 'London, Great Britain, 8700000' work?"""
        test_result = city_country('London', 'Great Britain', 8700000)
        self.assertEqual(test_result, 'London, Great Britain - population 8700000')

unittest.main()