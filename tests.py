import unittest
import helpers
import efficiency

class TestAdd(unittest.TestCase):
    def test_getProbOfEachChar(self):
        self.assertEqual(helpers.getProbOfEachChar('Hello'), {'H': 0.2, 'e': 0.2, 'l': 0.4, 'o': 0.2})
        self.assertEqual(helpers.getProbOfEachChar('aaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccddddddddddddddddddddddddddddddeeeee'),
                        {'d': 0.3,'b':0.28,'a': 0.22, 'c': 0.15, 'e': 0.05}
        )
    
    def test_reverse_dict(self):
        self.assertEqual(helpers.reverse_dict({'a': 0.4, 'b': '0.2'}), {'0.2': 'b', 0.4: 'a'})
        self.assertEqual(helpers.reverse_dict({'a': 'apple', 'b': 'bear'}), {'bear': 'b', 'apple': 'a'})

    def test_efficiency(self):
        self.assertEqual(efficiency.calc_efficiency('Hello', ['00', '01', '10', '10', '11'], efficiency.EncodeStanderd.ASCII), 75)
        self.assertEqual(efficiency.calc_efficiency('Hello', ['100', '101', '0', '0', '11'], efficiency.EncodeStanderd.ASCII), 75)
        self.assertEqual(efficiency.calc_efficiency('Hello', ['100', '101', '0', '0', '11'], efficiency.EncodeStanderd.UNICODE), 87.5)

if __name__ == '__main__':
    unittest.main()