import unittest
from src.one.keeping_the_last_n_items import example

def peek(iterable):
    try:
        first, rest = next(iterable)
    except StopIteration:
        return None
    return first, itertools.chain([first], rest)


class TestUM(unittest.TestCase):
    def setUp(self):
        pass
    def test_search(self):
        search_results = example.search(['python']*10,'python',5)
        first, rest = next(search_results)
        self.assertEquals(first,'python')

        self.assertIsNone(peek(example.search(['jython']*10,'python',5)))

    def test_deque(self):
        search_results = example.search(['python']*10,'python',5)
        result_list = list(search_results)
        deque = result_list[0][1]
        self.assertEquals(5,deque.maxlen) 


if __name__ == "__main__":
    unittest.main()
