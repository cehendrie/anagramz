from anagramz.anagramz import Anagramz


class TestAnagramz(object):
    def test_generate_anagrams(self):
        anagramz = Anagramz()
        anagramz.generate_anagrams('abc')
        assert True

