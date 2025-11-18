# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, list_of_anagrams):
        sorted_word = sorted(self.word)
        return [anagram for anagram in list_of_anagrams if sorted(anagram.lower()) == sorted_word and anagram.lower() != self.word]
    

listen = Anagram("listen")
listen.match(["enlists", "google", "inlets", "banana"])
print(listen.match(["enlists", "google", "inlets", "banana"]))  # Output should be ['inlets']