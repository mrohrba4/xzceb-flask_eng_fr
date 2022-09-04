import unittest

from xzceb-flask_eng_fr/final_project/machinetranslation/translator.py import french_to_english, english_to_french

class Test_translator(unittest.TestCase):
    def test_FTE(self, result):
        self.assertTrue(result['translations'][0]['translation'])

    def test_ETF(self, result):
        self.assertTrue(result['translations'][0]['translation'])


if __name__ == '__main__':
        unittest.main()