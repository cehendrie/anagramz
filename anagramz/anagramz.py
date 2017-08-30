class Anagramz(object):
    def generate_anagrams(self, str):

        chars = list(str)
        words = [ str ]
        current = chars

        for i in range(len(chars) - 1):
            char = current[0]
            current = current[1:]
            current.append(char)
            words.append("".join(current))
        print("words: {}".format(words))

        for word in words[1:]:
            for i in range(len(chars) - 1):
                char = current[0]
                current = current[1:]
                current.append(char)
                words.append("".join(current))
            print("words: {}".format(words))
