import unittest
from set import Set


class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        assert len(s.set.buckets) == 8
        assert s.size() == 0
        assert s.set.items() == []

    def test_init_with_elements(self):
        s = Set(['Sunny', 'Ouyang'])
        assert len(s.set.buckets) == 8
        assert s.size() == 2
        # assert s.set.items() == [('Ouyang', None), ('Sunny', None)]

    def test_contains(self):
        s = Set()
        s.add('Sunny')
        assert s.contains('Sunny') == True
        assert s.contains('Stephen') == False

    def test_add(self):
        s = Set()
        assert s.size() == 0
        s.add('Sunny')
        assert s.size() == 1
        assert s.set.items() == [('Sunny', None)]

    def test_remove(self):
        s = Set(['Sunny', 'Ouyang'])
        assert s.size() == 2
        # assert s.set.items() == [('Ouyang', None), ('Sunny', None)]
        s.remove('Sunny')
        assert s.size() == 1
        assert s.set.items() == [('Ouyang', None)]

    def test_union(self):
        s = Set(['Sunny', 'Ouyang'])
        new_s = Set(['Stephen', 'Ouyeezy'])
        assert s.size() == 2
        # assert s.set.items() == [('Ouyang', None), ('Sunny', None)]
        s = s.union(new_s)
        assert s.size() == 4


    def test_intersect(self):
        s = Set(['Sunny', 'Ouyang'])
        assert s.size() == 2
        new_s = Set(['Stephen', 'Ouyang'])
        s = s.intersect(new_s)
        assert s.size() == 1
        assert s.set.items() == [('Ouyang', None)]

    def test_difference(self):
        s = Set(['Sunny', 'Ouyang'])
        assert s.size() == 2
        new_s = Set(['Stephen', 'Ouyang'])
        s = s.difference(new_s)
        assert s.size() == 2

    def test_is_subset(self):
        s = Set(['Sunny', 'Ouyang'])
        new_s = Set(['Ouyang'])
        assert s.is_subset(new_s) == True



if __name__ == '__main__':
    unittest.main()
