import unittest

class testcal(unittest.TestCase):
  def test_msg(self):
    a = 'some'
    b = 'some'
    self.assertEqual(a,b)

if __name__ == '__main__':
  unittest.main()
