from string_utils import StringUtils # type: ignore

string_utils = StringUtils ()

def test_capitalize(self):
        self.assertEqual(self.utils.capitalize("skypro"), "Skypro")
        self.assertEqual(self.utils.capitalize("hello world!"), "Hello world!")
        self.assertEqual(self.utils.capitalize(""), "")

def test_trim(self):
        self.assertEqual(self.utils.trim("   skypro"), "skypro")
        self.assertEqual(self.utils.trim("Hello World!   "), "Hello World!   ")
        self.assertEqual(self.utils.trim(""), "")

def test_contains(self):
        self.assertTrue(self.utils.contains("SkyPro", "S"))
        self.assertFalse(self.utils.contains("SkyPro", "U"))
        self.assertTrue(self.utils.contains("test string", "t"))
        self.assertFalse(self.utils.contains("test string", "z"))

def test_delete_symbol(self):
        self.assertEqual(self.utils.delete_symbol("SkyPro", "k"), "SyPro")
        self.assertEqual(self.utils.delete_symbol("SkyPro", "Pro"), "Sky")
        self.assertEqual(self.utils.delete_symbol("Hello World", "l"), "Heo Wor")
        self.assertEqual(self.utils.delete_symbol("Hello World", ""), "Hello World")

#if __name__ == '__main__':
#    unittest.main ()
