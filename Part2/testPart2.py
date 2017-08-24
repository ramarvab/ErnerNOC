import unittest
import part2

class MyTestCase(unittest.TestCase):
    testFile = "/Users/rama.arvabhumi/Desktop/Erner/all-data/csv/6.csv"
    def test_statistics(self):
        hourlystats,dailystats = part2.calculatestats(self.testFile)
        self.assertEqual(hourlystats[0][0], 551.7462)
        self.assertEqual(dailystats[0][0],10773.7671)
        self.assertEqual(hourlystats[0][3],50.1587)
        self.assertEqual(dailystats[0][3],37.5393)


if __name__ == '__main__':
	unittest.main()