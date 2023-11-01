from preprocessing import PreProcess


class Inverted_Index_Builder:
    def __init__(self, tokens: list):
        self.inverted_index = {}
        self.tokens = tokens

    def build(self):
        for doc_id, tokens in enumerate(self.tokens):
            for token_index, token in enumerate(self.tokens[doc_id]):
                if token not in self.inverted_index:
                    self.inverted_index[token] = {doc_id: {'frequency': 1, 'indexes': [token_index]}}
                elif token in self.inverted_index:
                    if doc_id in self.inverted_index[token]:
                        self.inverted_index[token][doc_id]['frequency'] += 1
                        self.inverted_index[token][doc_id]['indexes'].append(token_index)
                    elif doc_id not in self.inverted_index[token]:
                        self.inverted_index[token][doc_id] = {'frequency': 1, 'indexes': [token_index]}
                    else:
                        raise Exception("ERROR")
                else:
                    raise Exception("ERROR")

