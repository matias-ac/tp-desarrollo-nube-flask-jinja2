import unittest


class SmokeTest(unittest.TestCase):
    def test_true_es_true(self):
        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()
