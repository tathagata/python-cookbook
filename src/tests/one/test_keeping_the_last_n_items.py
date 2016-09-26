import unittest
from src.one.keeping_the_last_n_items import example
import os
from urllib.request import urlopen, Request
from future.standard_library import install_aliases
install_aliases()

def peek(iterable):
    try:
        first, rest = next(iterable)
    except StopIteration:
        return None
    return first, itertools.chain([first], rest)


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.filename = 'somefile.txt'
        with open(self.filename,'w') as f:
            f.write('python '*10)

    def test_search(self):
        search_results = example.search(['python']*10,'python',5)
        first, rest = next(search_results)
        self.assertEquals(first,'python')

        self.assertIsNone(peek(example.search(['jython']*10,'python',5)))

    def test_deque(self):
        search_results = example.search(['python']*10,'python',10)
        result_list = list(search_results)
        deque = result_list[0][1]
        self.assertEquals(10,deque.maxlen)

        search_results_with_no_default_quelen  = example.search(['python']*10,'python')
        search_results_list = list(search_results_with_no_default_quelen)
        deque=search_results_list[0][1]
        self.assertEquals(5,deque.maxlen)

        search_results_with_no_default_quelen = example.search(['python']*10,'python',-1)
        with self.assertRaises(ValueError):
            search_results_list = list(search_results_with_no_default_quelen)

    def test_multiple_use_of_search(self):
        search_in_file = example.search(open(self.filename),'python',5)
        self.assertEquals(5, list(search_in_file)[0][1].maxlen)

        search_in_web = example.search(urlopen('http://pyvideo.org/category/50/pycon-us-2014').readlines(), 'pyvideo',5)
        self.assertEquals(5, list(search_in_web)[0][1].maxlen)

    def tearDown(self):
        os.remove(self.filename)

if __name__ == "__main__":
    unittest.main()
