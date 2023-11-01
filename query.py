class Query:
    def __init__(self, query: str, inverted_index_with_elimination: list, inverted_index_without_elimination: list):
        self.query = query
        self.inverted_index_with_elimination = inverted_index_with_elimination
        self.inverted_index_without_elimination = inverted_index_without_elimination
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

    def boolean_search(self, operator_state: str, state: bool):
        if state:
            if operator_state == 'AND':
                term1_info = self.inverted_index_with_elimination[self.terms[0]]
                term2_info = self.inverted_index_with_elimination[self.terms[1]]
                term1_keys = term1_info.keys()
                term2_keys = term2_info.keys()
                result = [doc_id for doc_id in term1_keys if doc_id in term2_keys]
                return result
            elif operator_state == 'OR':
                term1_info = self.inverted_index_with_elimination[self.terms[0]]
                term2_info = self.inverted_index_with_elimination[self.terms[1]]
                term1_keys = term1_info.keys()
                term2_keys = term2_info.keys()
                result = list(set(term1_keys + term2_keys))
                return result
            elif operator_state == 'NOT':
                term1_info = self.inverted_index_with_elimination[self.terms[0]]
                term2_info = self.inverted_index_with_elimination[self.terms[1]]
                term1_keys = term1_info.keys()
                term2_keys = term2_info.keys()
                result = [doc_id for doc_id in term1_keys if doc_id not in term2_keys]
                return result
            else:
                raise Exception("Wrong Operator")
        else:
            if operator_state == 'AND':
                term1_info = self.inverted_index_without_elimination[self.terms[0]]
                term2_info = self.inverted_index_without_elimination[self.terms[1]]
                term1_keys = term1_info.keys()
                term2_keys = term2_info.keys()
                result = [doc_id for doc_id in term1_keys if doc_id in term2_keys]
                return result
            elif operator_state == 'OR':
                term1_info = self.inverted_index_without_elimination[self.terms[0]]
                term2_info = self.inverted_index_without_elimination[self.terms[1]]
                term1_keys = term1_info.keys()
                term2_keys = term2_info.keys()
                result = list(set(term1_keys + term2_keys))
                return result
            elif operator_state == 'NOT':
                term1_info = self.inverted_index_without_elimination[self.terms[0]]
                term2_info = self.inverted_index_without_elimination[self.terms[1]]
                term1_keys = term1_info.keys()
                term2_keys = term2_info.keys()
                result = [doc_id for doc_id in term1_keys if doc_id not in term2_keys]
                return result
            else:
                raise Exception("Wrong Operator")

    def start_boolean_query(self):
        if self.operator == 'AND':
            self.boolean_search(operator_state='AND', state=True)
        elif self.operator == 'OR':
            self.boolean_search(operator_state='OR', state=True)
        elif self.operator == 'NOT':
            self.boolean_search(operator_state='NOT', state=True)
        else:
            raise Exception("Not a Valid Operator")

    def proximity_search(self):
        area_covered = int(self.operator.split('/')[-1])  # The number we passed into the proximity query
        doc_ids = self.boolean_search(operator_state='AND', state=False)  # To get the doc ids that contains both of terms
        result = []
        term1_info = self.inverted_index_without_elimination[self.terms[0]]
        term2_info = self.inverted_index_without_elimination[self.terms[1]]
        for doc_id in doc_ids:
            term1_indexes = term1_info[doc_id]['indexes']
            term2_indexes = term2_info[doc_id]['indexes']
            for i in range(len(term1_indexes)):
                for j in range(len(term2_indexes)):
                    if i in range(j-area_covered, j+area_covered+1):
                        result.append(doc_id)
        return result