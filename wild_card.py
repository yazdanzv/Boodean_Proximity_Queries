import copy
import re
import random
from Levenshtein import distance


class WildCard:
    def __init__(self, term: str, all_terms: list):
        self.term = term
        self.all_terms = all_terms
        self.k_gram_index = []
        self.selected_term = ""
        self.k_gram_builder()
        self.term_finder()

    def k_gram_builder(self, k: int = 2):
        k_gram_index = []
        sub_strings = self.term.split("*")
        while '' in sub_strings:
            sub_strings.remove('')
        for i in range(len(sub_strings)):
            k_gram_index.extend(self.indexer(sub_strings[i]))

        while [] in k_gram_index:
            k_gram_index.remove([])

        #  Start of the term
        if self.term[0] != '*':
            k_gram_index.append(f"^{self.term[0]}")
        #  End of the term
        if self.term[-1] != '*':
            k_gram_index.append(f"{self.term[-1]}$")
        print("K-gram indexing : ")
        print(k_gram_index)
        self.k_gram_index = copy.deepcopy(k_gram_index)

    @staticmethod
    def indexer(term: str, k: int = 2):
        result = []
        for i in range(len(term) - 1):
            result.append(term[i:i + 2])
        return result

    def term_finder(self):
        selected_terms = []
        for i in range(len(self.k_gram_index)):
            answers = []
            for j in range(len(self.all_terms)):
                if re.findall(self.k_gram_index[i], self.all_terms[j]):
                    answers.append(self.all_terms[j])
            answers = set(answers)
            selected_terms.append(copy.deepcopy(answers))

        selected_terms_intersect = set.intersection(*selected_terms)
        selected_terms_intersect = list(selected_terms_intersect)
        min_distance = distance(self.term, selected_terms_intersect[0])
        min_term = selected_terms_intersect[0]
        for i in range(1, len(selected_terms_intersect)):
            if min_distance > distance(self.term, selected_terms_intersect[i]):
                min_distance = distance(self.term, selected_terms_intersect[i])
                min_term = selected_terms_intersect[i]
        self.selected_term = min_term
