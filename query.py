class Query:
    def __init__(self, query: str, inverted_index: list):
        self.query = query
        self.inverted_index = inverted_index
        self.query_state = ""
        self.boolean_operators = ['AND', 'OR', 'NOT']
        self.terms = []
        self.operator = ""

    def query_opener(self):
        terms = self.query.split(" ")
        self.terms.append(terms[0])
        self.terms.append([terms[-1]])
        self.operator = terms[1]

    def state_determiner(self):
        if self.operator in self.boolean_operators:
            self.query_state = "boolean"
        else:
            if 'NEAR' in self.operator:
                self.query_state = 'proximity'
            else:
                raise Exception("ERROR")

    def boolean_search(self):
        if self.operator == 'AND':
            term1_info = self.inverted_index[self.terms[0]]
            term2_info = self.inverted_index[self.terms[1]]
            term1_keys = term1_info.keys()
            term2_keys = term2_info.keys()
            result = [doc_id for doc_id in term1_keys if doc_id in term2_keys]
            return result
        elif self.operator == 'OR':
            term1_info = self.inverted_index[self.terms[0]]
            term2_info = self.inverted_index[self.terms[1]]
            term1_keys = term1_info.keys()
            term2_keys = term2_info.keys()
            result = list(set(term1_keys + term2_keys))
            return result
        elif self.operator == 'NOT':
            term1_info = self.inverted_index[self.terms[0]]
            term2_info = self.inverted_index[self.terms[1]]
            term1_keys = term1_info.keys()
            term2_keys = term2_info.keys()
            result = [doc_id for doc_id in term1_keys if doc_id not in term2_keys]
            return result
        else:
            raise Exception("Wrong Operator")

    def proximity_search(self):
        area_covered = int(self.operator.split('/')[-1])  # The number we passed into the proximity query





