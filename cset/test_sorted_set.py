import unittest
from sorted_set import SortedSet

class MyTestCase(unittest.TestCase):
    def test_empty(self):
        s = SortedSet([])

    def test_from_sequence(self):
        s = SortedSet([7,8,3,1])

    def test_with_duplicates(self):
        s = SortedSet([7, 7, 7])

    def test_from_iterable(self):
        def gen6482():
            yield 6
            yield 4
            yield 8
            yield 2

        g = gen6482()
        s = SortedSet(g)

    def test_default(self):
        s = SortedSet()

class TestContainerProtocol(unittest.TestCase):

    def setUp(self) -> None:
        self.s = SortedSet([6,7,4,5])

    def test_positive_contained(self):
        self.assertTrue(6 in self.s)

    def test_negative_contained(self):
        self.assertFalse(8 in self.s)

    def test_positive_not_contained(self):
        self.assertTrue(8 not in self.s)

    def test_negative_not_contained(self):
        self.assertFalse(6 not in self.s)

class TestSizedProtocol(unittest.TestCase):

    def test_empty(self):
        s = SortedSet()
        self.assertEqual(len(s), 0)

    def test_one(self):
        s = SortedSet([2])
        self.assertEqual(len(s),1)

    def test_n(self):
        s = SortedSet(range(10))
        self.assertEqual(len(s), 10)

    def test_with_duplicates(self):
        s = SortedSet([5,5,5])
        self.assertEqual(len(s),1)

class TestIterableProtocol(unittest.TestCase):
    def setUp(self) -> None:
        self.s = SortedSet([5,7,2,2,6])

    def test_iter(self):
        i = iter(self.s)
        self.assertEqual(next(i), 2)
        self.assertEqual(next(i), 5)
        self.assertEqual(next(i), 6)
        self.assertEqual(next(i), 7)
        self.assertRaises(StopIteration, lambda: next(i))

    def test_for_loop(self):
        index = 0
        expected = [2,5,6,7]
        for item in self.s:
            self.assertEqual(item, expected[index])
            index += 1

class TestSequenceProtocol(unittest.TestCase):
    def setUp(self) -> None:
        self.s = SortedSet([1,4, 9,13,15])

    def test_index_zero(self):
        self.assertEqual(self.s[0], 1)

    def test_index_four(self):
        self.assertEqual(self.s[4], 15)

    def test_index_one_beyond_end(self):
        with self.assertRaises(IndexError):
            self.s[5]

    def test_index_minus_one(self):
        self.assertEqual(self.s[-1],15)

    def test_index_minus_five(self):
        self.assertEqual(self.s[-5],1)

    def test_index_one_before_beginning(self):
        with self.assertRaises(IndexError):
            self.s[-6]

    def test_slice_from_start(self):
        self.assertEqual(self.s[:3], SortedSet([1,4,9]))

    def test_slice_from_end(self):
        self.assertEqual(self.s[3:], SortedSet([13, 15]))

    def test_slice_empty(self):
        self.assertEqual(self.s[10:], SortedSet())

    def test_slice_arbitrary(self):
        self.assertEqual(self.s[2:4], SortedSet([9,13]))

    def test_full_slice(self):
        self.assertEqual(self.s[:], self.s)

    def test_reversed(self):
        s = SortedSet([4,5,6])
        r = reversed(s)
        self.assertEqual(next(r), 6)
        self.assertEqual(next(r), 5)
        self.assertEqual(next(r), 4)
        with self.assertRaises(StopIteration):
            next(r)

    def test_index_positive(self):
        s = SortedSet([4,5,6])
        self.assertEqual(s.index(5),1)

    def test_index_negative(self):
        s = SortedSet([4,5,6])
        with self.assertRaises(ValueError):
            s.index(8)

    def test_count_zero(self):
        s = SortedSet([1,5])
        self.assertEqual(s.count(2), 0)

    def test_count_one(self):
        s = SortedSet([1,5,6,7])
        self.assertEqual(s.count(5),1)

class TestReprProtocol(unittest.TestCase):
    def test_repr_empty(self):
        s = SortedSet()
        self.assertEqual(repr(s),'SortedSet()')

    def test_repr_some(self):
        s = SortedSet([9,4,6])
        self.assertEqual(repr(s),'SortedSet([4, 6, 9])')

class TestEqualityProtocol(unittest.TestCase):
    def test_positive_equal(self):
        self.assertTrue(SortedSet([4,6,5]) == SortedSet([6,4,5]))

    def test_negative_equal(self):
        self.assertFalse(SortedSet([4,6,5]) == SortedSet([8,10,9]))

    def test_type_mismatch(self):
        self.assertFalse(SortedSet([4,5,6]) == [4,5,6])

    def test_identity(self):
        s = SortedSet([5, 4])
        self.assertTrue(s == s)

class TestInEqualityProtocol(unittest.TestCase):
    def test_positive_unequal(self):
        self.assertTrue(SortedSet([4,6,5]) != SortedSet([1,2,3]))

    def test_negative_equal(self):
        self.assertFalse(SortedSet([4,6,5]) != SortedSet([4,5,6]))

    def test_type_mismatch(self):
        self.assertTrue(SortedSet([4,5,6]) != [4,5,6])

    def test_identity(self):
        s = SortedSet([5, 4])
        self.assertFalse(s != s)

if __name__ == '__main__':
    unittest.main()
