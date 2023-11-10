import copy
import re
from Levenshtein import distance


class WildCard:
    def __init__(self, term: str, all_terms: list):
        self.term = term  # Term comes from query
        self.all_terms = all_terms  # All terms inside document collection
        self.k_gram_index = []  # K-gram indices related to Term that comes from query
        self.selected_term = ""  # Final selected term
        self.k_gram_builder()  # Build k-gram indices
        self.term_finder()  # Find most related term to the term comes from the query

    def k_gram_builder(self, k: int = 2):
        k_gram_index = []
        sub_strings = self.term.split("*")  # Separates the term from * indices
        while '' in sub_strings:  # If * is at the beginning or at the end it produces '' so I need to eliminate it
            sub_strings.remove('')
        for i in range(len(sub_strings)):  # Get all k-grams except first and last one
            k_gram_index.extend(self.indexer(sub_strings[i]))

        #  Start of the term
        if self.term[0] != '*':  # Add first k-gram if it does exist
            k_gram_index.append(f"^{self.term[0]}")
        #  End of the term
        if self.term[-1] != '*':  # Add last k-gram if it does exist
            k_gram_index.append(f"{self.term[-1]}$")
        # Results
        print("K-gram indexing : ")
        print(k_gram_index)
        self.k_gram_index = copy.deepcopy(k_gram_index)

    @staticmethod
    def indexer(term: str, k: int = 2):  # Get k-grams but not generate first and last one that needs ^ and $ signs
        result = []
        for i in range(len(term) - 1):
            result.append(term[i:i + 2])  # Split k by k
        return result

    def term_finder(self):
        selected_terms = []  # To keep selected terms
        for i in range(len(self.k_gram_index)):
            answers = []  # To keep all the terms related to each k-gram
            for j in range(len(self.all_terms)):
                if re.findall(self.k_gram_index[i], self.all_terms[j]):
                    answers.append(self.all_terms[j])
            answers = set(answers)  # Eliminate duplicate terms
            selected_terms.append(
                copy.deepcopy(answers))  # Append the set of terms that are related to k-gram index of i

        selected_terms_intersect = set.intersection(*selected_terms)  # Get the intersection from sets
        selected_terms_intersect = list(selected_terms_intersect)  # Convert it to list
        min_distance = distance(self.term, selected_terms_intersect[
            0])  # Calculate the minimum distance between first term with * inside with all the terms in answers
        min_term = selected_terms_intersect[0]
        for i in range(1, len(selected_terms_intersect)):  # get the minimum, e.g. for wildcard query c*ty we get city and creativity but city is much closer, so I used edit distance to choose the final term except just choose it randomly
            if min_distance > distance(self.term, selected_terms_intersect[i]):
                min_distance = distance(self.term, selected_terms_intersect[i])
                min_term = selected_terms_intersect[i]
        self.selected_term = min_term  # Final term
