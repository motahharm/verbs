import unittest
import mazi

class TestMazi(unittest.TestCase):
    def test_goftan(self):
        verb = mazi.MaziVerb(1, 'گفتن', True)
        self.assertEqual(verb.sadeh(), 'گفتم')
        self.assertEqual(verb.estemrary(), 'می گفتم')
        self.assertEqual(verb.mostamar(), 'داشتم می گفتم')
        self.assertEqual(verb.naghly(), 'گفته ام')
        self.assertEqual(verb.eltezamy(), 'گفته باشم')
        self.assertEqual(verb.baid(), 'گفته بودم')
    def test_bordan(self):
        verb = mazi.MaziVerb(1, 'بردن', True)
        self.assertEqual(verb.sadeh(), 'بردم')
        self.assertEqual(verb.estemrary(), 'می بردم')
        self.assertEqual(verb.mostamar(), 'داشتم می بردم')
        self.assertEqual(verb.naghly(), 'برده ام')
        self.assertEqual(verb.eltezamy(), 'برده باشم')
        self.assertEqual(verb.baid(), 'برده بودم')

    def test_shenaseh_ha(self):
        self.assertEqual(mazi.get_bon_mozare('دادن'), 'داد')
        self.assertEqual(mazi.get_zamir(2, False), 'شما')
        self.assertEqual(mazi.get_gozashteh_baid(1, False), 'بودیم')
        self.assertEqual(mazi.get_gozashteh_eltezamy(2, True), 'باشی')
        self.assertEqual(mazi.get_gozashteh_mostamar(3, False), 'داشتند')
        self.assertEqual(mazi.get_gozashteh_naghly(1, True), 'ام')

if __name__ == '__main__':
    unittest.main()
