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





