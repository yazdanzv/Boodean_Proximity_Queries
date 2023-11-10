from Levenshtein import distance
import random


class MissSpell:
    def __init__(self, term: str, terms_list: list):
        self.term = term  # Term comes from query
        self.terms_list = terms_list  # All terms that exists in document collection
        self.target_terms = []  # All terms that satisfy the conditions
        self.distances = []  # All edit distances with all the terms in the document collection
        self.selected_term = ""  # Final selected term
        self.start()  # Start the procedure

    def start(self):
        for term in self.terms_list:  # Calculating edit distances with all terms inside the document collection
            self.distances.append(distance(self.term, term))
        min_distance = min(self.distances)  # Get minimum distance
        min_index_list = []
        for i in range(len(self.distances)):  # Find all term's indices with minimum distance
            if self.distances[i] == min_distance:
                min_index_list.append(i)
        for i in range(len(min_index_list)):  # Find all terms with minimum distance
            self.target_terms.append(self.terms_list[min_index_list[i]])
        self.target_terms = list(set(self.target_terms))  # Eliminate duplicate terms and make all the terms unique inside the list
        # Results of the selected terms
        print("Target Terms")
        print(self.target_terms)
        self.selected_term = random.choice(self.target_terms)  # Select final term randomly from all the terms that satisfy the condition
        # Results of selected term
        print("Selected Term")
        print(self.selected_term)



