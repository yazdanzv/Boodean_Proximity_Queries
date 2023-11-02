from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


class Query:
    def __init__(self, query: str, inverted_index_with_elimination: list, inverted_index_without_elimination: list,
                 doc_numbers: int):  # Get Both Optimized Inverted Indexes, WITH and WITHOUT elimination and the number of documents
        self.query = query  # The query the user entered
        self.inverted_index_with_elimination = inverted_index_with_elimination  # Inverted Index WITH elimination
        self.inverted_index_without_elimination = inverted_index_without_elimination  # Inverted Index WITHOUT elimination
        self.docs_number = doc_numbers  # Number of documents, used for NOT query
        self.query_state = ""  # Can be boolean or proximity to invoke suitable method
        self.boolean_operators = ['AND', 'OR', 'NOT']  # Boolean operators that we can handle
        self.terms = []  # List to keep terms or term in it (For one of the types of NOT query we have one term)
        self.operator = ""  # Operator keeper
        self.query_opener()
        self.state_determiner()
        self.start()

    def query_opener(self):  # Opens the query string and defines operator and terms or term
        stemmer = PorterStemmer()  # Stemming the terms before doing the query
        lemmatizer = WordNetLemmatizer()  # Doing Lemmatization before doing the query
        terms = self.query.split(" ")
        if len(terms) == 3:  # For another queries
            self.terms.append(lemmatizer.lemmatize(stemmer.stem(terms[0]), pos='v'))
            self.terms.append(lemmatizer.lemmatize(stemmer.stem(terms[-1]), pos='v'))
            self.operator = terms[1]
        elif len(terms) == 2:  # For NOT query with one term
            self.terms.append(lemmatizer.lemmatize(stemmer.stem(terms[1]), pos='v'))
            self.operator = terms[0]  # Equal to NOT

    def state_determiner(self):  # Defines the state of the query, it can be boolean or proximity
        if self.operator in self.boolean_operators:
            self.query_state = "boolean"
        else:
            if 'NEAR' in self.operator:
                self.query_state = 'proximity'
            else:
                raise Exception("ERROR")

    def boolean_search(self, operator_state: str, state: bool):  # Do the selected boolean search on the documents
        if state:  # For tokens WITH elimination
            if operator_state == 'AND':  # AND query
                term1_info = self.inverted_index_with_elimination[self.terms[0]]
                term2_info = self.inverted_index_with_elimination[self.terms[1]]
                term1_keys = term1_info.keys()
                term2_keys = term2_info.keys()
                result = [doc_id for doc_id in term1_keys if doc_id in term2_keys]
                return result
            elif operator_state == 'OR':  # OR query
                term1_info = self.inverted_index_with_elimination[self.terms[0]]
                term2_info = self.inverted_index_with_elimination[self.terms[1]]
                term1_keys = list(term1_info.keys())
                term2_keys = list(term2_info.keys())
                result = list(set(term1_keys + term2_keys))
                return result
            elif operator_state == 'NOT' and len(self.terms) == 2:  # NOT query with two terms
                term1_info = self.inverted_index_with_elimination[self.terms[0]]
                term2_info = self.inverted_index_with_elimination[self.terms[1]]
                term1_keys = term1_info.keys()
                term2_keys = term2_info.keys()
                result = [doc_id for doc_id in term1_keys if doc_id not in term2_keys]
                return result
            elif operator_state == 'NOT' and len(self.terms) == 1:  # NOT query with one term
                term1_info = self.inverted_index_with_elimination[self.terms[0]]
                term1_keys = term1_info.keys()
                result = [doc_id for doc_id in range(self.docs_number) if doc_id not in term1_keys]
                return result
            else:
                raise Exception("Wrong Operator")
        else:  # For tokens WITHOUT elimination
            if operator_state == 'AND':  # AND query
                term1_info = self.inverted_index_without_elimination[self.terms[0]]
                term2_info = self.inverted_index_without_elimination[self.terms[1]]
                term1_keys = term1_info.keys()
                term2_keys = term2_info.keys()
                result = [doc_id for doc_id in term1_keys if doc_id in term2_keys]
                return result
            elif operator_state == 'OR':  # OR query
                term1_info = self.inverted_index_without_elimination[self.terms[0]]
                term2_info = self.inverted_index_without_elimination[self.terms[1]]
                term1_keys = term1_info.keys()
                term2_keys = term2_info.keys()
                result = list(set(term1_keys + term2_keys))
                return result
            elif operator_state == 'NOT':  # NOT query with two terms
                term1_info = self.inverted_index_without_elimination[self.terms[0]]
                term2_info = self.inverted_index_without_elimination[self.terms[1]]
                term1_keys = term1_info.keys()
                term2_keys = term2_info.keys()
                result = [doc_id for doc_id in term1_keys if doc_id not in term2_keys]
                return result
            elif operator_state == 'NOT' and len(self.terms) == 1:  # NOT query with one term
                term1_info = self.inverted_index_without_elimination[self.terms[0]]
                term1_keys = term1_info.keys()
                result = [doc_id for doc_id in range(self.docs_number) if doc_id not in term1_keys]
                return result
            else:
                raise Exception("Wrong Operator")

    def start_boolean_query(self):  # Start method for boolean queries
        if self.operator == 'AND':
            print(self.boolean_search(operator_state='AND', state=True))
        elif self.operator == 'OR':
            print(self.boolean_search(operator_state='OR', state=True))
        elif self.operator == 'NOT':
            print(self.boolean_search(operator_state='NOT', state=True))
        else:
            raise Exception("Not a Valid Operator")

    def proximity_search(self):  # Do the proximity search on the documents
        area_covered = int(self.operator.split('/')[-1])  # The number we passed into the proximity query
        doc_ids = self.boolean_search(operator_state='AND',
                                      state=False)  # To get the doc ids that contains both of terms
        result = []  # Result that method returns at the end
        #  Used tokens WITHOUT elimination to do the proximity query right, so we need every single term in the document
        term1_info = self.inverted_index_without_elimination[
            self.terms[0]]  # Information about terms1 in Optimized Inverted Index
        term2_info = self.inverted_index_without_elimination[
            self.terms[1]]  # Information about terms2 in Optimized Inverted Index
        for doc_id in doc_ids:
            term1_indexes = term1_info[doc_id]['indexes']  # The indexes that term1 happened in selected document id
            term2_indexes = term2_info[doc_id]['indexes']  # The indexes that term2 happened in selected document id
            for i in range(
                    len(term1_indexes)):  # Search for indexes that are in the range user wanted in the proximity query
                for j in range(len(term2_indexes)):
                    if term1_indexes[i] in range(term2_indexes[j] - area_covered - 1,
                                                 term2_indexes[j] + area_covered + 2):
                        result.append(doc_id)
        return result

    def start_proximity_search(self):  # Start method for proximity query
        print(self.proximity_search())

    def start(self):  # Start method of the query that can handle which start method we need
        if self.query_state == 'boolean':
            self.start_boolean_query()
        elif self.query_state == 'proximity':
            self.start_proximity_search()
        else:
            raise Exception('Not a Valid Query State')
