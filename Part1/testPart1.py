import unittest
import part1
class MyTestCase(unittest.TestCase):
	testFile = "/Users/rama.arvabhumi/Desktop/Test"
	def test_numOf0sAndNans(self):

		trueNumOf0sAndNans = 6
		entry = part1.rankFiles(self.testFile)[0]
		self.assertEqual(entry[0][0], trueNumOf0sAndNans)
	def test_percentage(self):
		totalpercentage ="20.0%"
		entry = part1.rankFiles(self.testFile)[0]
		self.assertEqual(entry[0][2], totalpercentage)

	def test_stremaswith0and1(self):
		testpath = "/Users/rama.arvabhumi/Desktop/Test1"
		ignoredfiles = part1.rankFiles(testpath)[1]
		print(ignoredfiles)
		self.assertEqual(ignoredfiles[0],"6.csv")

if __name__ == '__main__':
	unittest.main()