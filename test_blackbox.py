import unittest

from T9Pad import T9Pad


class TestT9Pad(unittest.TestCase):
    def setUp(self):
        self.pad = T9Pad()

    def test_get_key_code(self):
        self.pad.add_key(2, "abc")
        self.pad.add_key(3, "def")
        self.assertEqual(2, self.pad.get_key_code('a'))
        self.assertEqual(2, self.pad.get_key_code('b'))
        self.assertEqual(2, self.pad.get_key_code('c'))
        self.assertEqual(3, self.pad.get_key_code('d'))
        self.assertEqual(3, self.pad.get_key_code('e'))
        self.assertEqual(3, self.pad.get_key_code('f'))

    def test_get_key_code_error(self):
        self.pad.add_key(2, "abc")
        self.pad.add_key(3, "def")
        with self.assertRaises(ValueError):
            self.pad.get_key_code('z')

    def test_get_pad_letters(self):
        self.pad.add_key(2, "abc")
        self.pad.add_key(3, "def")
        self.pad.add_key(4, "ghi")
        self.pad.add_key(5, "jkl")
        self.pad.add_key(6, "mno")
        self.pad.add_key(7, "pqrs")
        self.pad.add_key(8, "tuv")

        # Test a partially completed numeric pad
        letters = list("abcdefghijklmnopqrstuv")
        self.assertTrue(set(letters).issubset(self.pad.get_pad_letters()))
        self.assertTrue(set(self.pad.get_pad_letters()).issubset(letters))
        self.assertEqual(len(letters), len(self.pad.get_pad_letters()))

        # Test a fully completed numeric pad
        self.pad.add_key(9, "wxyz")
        letters = list("abcdefghijklmnopqrstuvwxyz")
        self.assertTrue(set(letters).issubset(self.pad.get_pad_letters()))
        self.assertTrue(set(self.pad.get_pad_letters()).issubset(letters))
        self.assertEqual(len(letters), len(self.pad.get_pad_letters()))

    def test_get_pad_letters_empty(self):
        self.assertTrue(len(self.pad.get_pad_letters()) == 0)

    def test_word_to_t9(self):
        self.pad.add_key(2, "abc")
        self.pad.add_key(3, "def")
        self.pad.add_key(4, "ghi")
        self.pad.add_key(5, "jkl")
        self.pad.add_key(6, "mno")
        self.pad.add_key(7, "pqrs")
        self.pad.add_key(8, "tuv")
        self.pad.add_key(9, "wxyz")

        self.assertTrue(self.pad.is_textonym("good", "home"))
        self.assertTrue(self.pad.is_textonym("hood", "home"))
        self.assertTrue(self.pad.is_textonym("good", "hood"))

    def test_word_to_t9_false(self):
        self.pad.add_key(2, "abc")
        self.pad.add_key(3, "def")
        self.pad.add_key(4, "ghi")
        self.pad.add_key(5, "jkl")
        self.pad.add_key(6, "mno")
        self.pad.add_key(7, "pqrs")
        self.pad.add_key(8, "tuv")
        self.pad.add_key(9, "wxyz")

        self.assertFalse(self.pad.is_textonym("good", "hoods"))
        self.assertFalse(self.pad.is_textonym("good", "hogs"))
        self.assertFalse(self.pad.is_textonym("boo", "good"))
        self.assertFalse(self.pad.is_textonym("doly", "doll"))


if __name__ == '__main__':
    unittest.main()
