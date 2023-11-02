from preprocessing import PreProcess


class Inverted_Index_Builder:
    def __init__(self, tokens: list):
        self.inverted_index_optimized = {}  # Optimized Inverted Index that I made myself that contains frequency and the index of the occurrence of the terms
        self.inverted_index = {}  # Simple Inverted Index that only contains the ids of the documents that contains selected term
        self.tokens = tokens  # Given tokens to work with them

    def build_optimized(self):  # The method to build Optimized Inverted Index, Structure -> {Term : {doc_id : {'frequency' : NUM, 'indexes' : [NUM, NUM, ...]}, ...}, ...}
        for doc_id, tokens in enumerate(self.tokens):
            for token_index, token in enumerate(self.tokens[doc_id]):
                if token not in self.inverted_index_optimized:
                    self.inverted_index_optimized[token] = {doc_id: {'frequency': 1, 'indexes': [token_index]}}
                elif token in self.inverted_index_optimized:
                    if doc_id in self.inverted_index_optimized[token]:
                        self.inverted_index_optimized[token][doc_id]['frequency'] += 1
                        self.inverted_index_optimized[token][doc_id]['indexes'].append(token_index)
                    elif doc_id not in self.inverted_index_optimized[token]:
                        self.inverted_index_optimized[token][doc_id] = {'frequency': 1, 'indexes': [token_index]}
                    else:
                        raise Exception("ERROR")
                else:
                    raise Exception("ERROR")

    def build(self):  # The method to build Simple Inverted Index, Structure -> {Term : [DOC_ID, DOC_ID, ...], ...}
        for doc_id, tokens in enumerate(self.tokens):
            for token_index, token in enumerate(self.tokens[doc_id]):
                if token not in self.inverted_index:
                    self.inverted_index[token] = [doc_id]
                elif token in self.inverted_index_optimized:
                    self.inverted_index[token].append(doc_id)
                else:
                    raise Exception("ERROR")

