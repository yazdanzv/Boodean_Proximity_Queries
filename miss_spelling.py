from Levenshtein import distance
import random


class MissSpell:
    def __init__(self, term: str, terms_list: list):
        self.term = term
        self.terms_list = terms_list
        self.target_terms = []
        self.distances = []
        self.selected_term = ""
        self.start()

    def start(self):
        for term in self.terms_list:
            self.distances.append(distance(self.term, term))
        min_distance = min(self.distances)
        min_index_list = []
        for i in range(len(self.distances)):
            if self.distances[i] == min_distance:
                min_index_list.append(i)
        for i in range(len(min_index_list)):
            self.target_terms.append(self.terms_list[min_index_list[i]])
        self.target_terms = list(set(self.target_terms))
        print("Target Terms")
        print(self.target_terms)
        self.selected_term = random.choice(self.target_terms)
        print("Selected Term")
        print(self.selected_term)


# terms = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', 'in', 'the', 'heart', 'of', 'the', 'city', 'a', 'bustling', 'marketplace', 'comes', 'to', 'life', 'exploring', 'distant', 'galaxies', 'astronomers', 'make', 'groundbreaking', 'discoveries', 'ancient', 'civilizations', 'left', 'behind', 'mysteries', 'waiting', 'to', 'be', 'unraveled', 'amidst', 'the', 'chaos', 'a', 'lone', 'musician', 'plays', 'a', 'soulful', 'melody', 'on', 'the', 'streets', 'sailing', 'across', 'the', 'open', 'ocean', 'a', 'ship', 'embarks', 'on', 'a', 'grand', 'adventure', 'in', 'the', 'depths', 'of', 'the', 'forest', 'a', 'hidden', 'waterfall', 'awaits', 'the', 'curious', 'traveler', 'scientists', 'unveil', 'a', 'revolutionary', 'technology', 'that', 'changes', 'the', 'world', 'through', 'the', 'lens', 'of', 'a', 'camera', 'moments', 'are', 'captured', 'and', 'memories', 'preserved', 'a', 'culinary', 'masterpiece', 'is', 'crafted', 'with', 'love', 'and', 'creativity', 'in', 'the', 'kitchen', 'the', 'sound', 'of', 'laughter', 'echoes', 'through', 'a', 'sunlit', 'park', 'on', 'a', 'perfect', 'day', 'explorers', 'venture', 'into', 'the', 'unknown', 'seeking', 'answers', 'to', 'ageold', 'questions', 'an', 'artists', 'canvas', 'becomes', 'a', 'canvas', 'for', 'imagination', 'and', 'selfexpression', 'stories', 'of', 'courage', 'and', 'heroism', 'inspire', 'the', 'next', 'generation', 'of', 'leaders', 'beneath', 'the', 'starry', 'night', 'sky', 'dreams', 'take', 'flight', 'on', 'the', 'wings', 'of', 'hope', 'in', 'the', 'digital', 'age', 'information', 'flows', 'freely', 'connecting', 'people', 'worldwide', 'a', 'peaceful', 'garden', 'offers', 'a', 'sanctuary', 'for', 'quiet', 'contemplation', 'and', 'reflection', 'as', 'the', 'sun', 'sets', 'the', 'horizon', 'is', 'painted', 'with', 'hues', 'of', 'orange', 'and', 'purple', 'mystical', 'creatures', 'and', 'legends', 'come', 'to', 'life', 'in', 'the', 'pages', 'of', 'a', 'timeless', 'book', 'in', 'the', 'heart', 'of', 'the', 'city', 'diverse', 'cultures', 'converge', 'celebrating', 'unity', 'the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', 'in', 'the', 'heart', 'of', 'the', 'city', 'a', 'bustling', 'marketplace', 'comes', 'to', 'life', 'with', 'joy', 'exploring', 'distant', 'galaxies', 'astronomers', 'make', 'groundbreaking', 'discoveries', 'about', 'the', 'universe', 'ancient', 'civilizations', 'left', 'behind', 'mysteries', 'waiting', 'to', 'be', 'unraveled', 'by', 'archaeologists', 'amidst', 'the', 'chaos', 'a', 'lone', 'musician', 'plays', 'a', 'soulful', 'melody', 'on', 'the', 'streets', 'of', 'the', 'vibrant', 'city', 'sailing', 'across', 'the', 'open', 'ocean', 'a', 'ship', 'embarks', 'on', 'a', 'grand', 'adventure', 'to', 'uncharted', 'islands', 'in', 'the', 'depths', 'of', 'the', 'forest', 'a', 'hidden', 'waterfall', 'awaits', 'the', 'curious', 'traveler', 'seeking', 'serenity', 'scientists', 'unveil', 'a', 'revolutionary', 'technology', 'that', 'changes', 'the', 'world', 'of', 'medicine', 'through', 'the', 'lens', 'of', 'a', 'camera', 'moments', 'are', 'captured', 'and', 'memories', 'preserved', 'for', 'generations', 'a', 'culinary', 'masterpiece', 'is', 'crafted', 'with', 'love', 'and', 'creativity', 'in', 'the', 'kitchen', 'of', 'a', 'renowned', 'chef', 'the', 'sound', 'of', 'laughter', 'echoes', 'through', 'a', 'sunlit', 'park', 'on', 'a', 'perfect', 'summer', 'day', 'explorers', 'venture', 'into', 'the', 'unknown', 'seeking', 'answers', 'to', 'ageold', 'questions', 'in', 'uncharted', 'territories', 'an', 'artists', 'canvas', 'becomes', 'a', 'canvas', 'for', 'imagination', 'and', 'selfexpression', 'through', 'vivid', 'colors', 'stories', 'of', 'courage', 'and', 'heroism', 'inspire', 'the', 'next', 'generation', 'of', 'leaders', 'worldwide', 'beneath', 'the', 'starry', 'night', 'sky', 'dreams', 'take', 'flight', 'on', 'the', 'wings', 'of', 'hope', 'and', 'aspiration', 'in', 'the', 'digital', 'age', 'information', 'flows', 'freely', 'connecting', 'people', 'globally', 'via', 'the', 'internet', 'a', 'peaceful', 'garden', 'offers', 'a', 'sanctuary', 'for', 'quiet', 'contemplation', 'and', 'reflection', 'amid', 'the', 'urban', 'hustle', 'as', 'the', 'sun', 'sets', 'the', 'horizon', 'is', 'painted', 'with', 'hues', 'of', 'orange', 'and', 'purple', 'creating', 'a', 'breathtaking', 'view', 'mystical', 'creatures', 'and', 'legends', 'come', 'to', 'life', 'in', 'the', 'pages', 'of', 'a', 'timeless', 'fantasy', 'book', 'filled', 'with', 'enchantment', 'in', 'the', 'heart', 'of', 'the', 'city', 'diverse', 'cultures', 'converge', 'celebrating', 'unity', 'and', 'cultural', 'exchange']
#
# term = 'het'
#
# a = MissSpell(term, terms)
# a.start()


