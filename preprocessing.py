import os
import re
import copy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')


class PreProcess:
    def __init__(self, documents_directory: str = ".\\Documents"):
        self.directory = documents_directory
        self.docs = []
        self.tokens = []
        self.stemmed_tokens = []
        self.lemmatized_tokens = []
        self.load_docs()
        self.start()

    def load_docs(self):
        # Loop through the files in the directory
        for filename in os.listdir(self.directory):
            if filename.endswith(".txt"):  # Ensure the file is a text file
                file_path = os.path.join(self.directory, filename)
                with open(file_path, "r") as file:
                    text = file.read()
                    self.docs.append(text)

    @staticmethod
    def case_folding(text: str):  # Lower case all the existing characters in the documents
        return text.lower()

    @staticmethod
    def special_characters_remover(text: str):  # Eliminates all the special characters like {, . : ; }
        normalized_text = re.sub(r'[^\w\s]', '', text)
        return normalized_text

    def tokenize(self):
        for i in range(len(self.docs)):
            self.tokens.append(word_tokenize(self.docs[i]))

    def stop_word_remover(self):
        stop_words = set(stopwords.words('english'))
        tokens_without_stopwords = []
        for i in range(len(self.tokens)):
            tokens = [word for word in self.tokens[i] if word not in stop_words]
            tokens_without_stopwords.append(copy.deepcopy(tokens))
        self.tokens = copy.deepcopy(tokens_without_stopwords)

    def stemming(self):
        stemmer = PorterStemmer()
        stemmed_tokens_list = []
        for i in range(len(self.tokens)):
            stemmed_tokens = [stemmer.stem(word) for word in self.tokens[i]]
            stemmed_tokens_list.append(stemmed_tokens)
        self.tokens = copy.deepcopy(stemmed_tokens_list)

    def lemmatization(self):
        lemmatizer = WordNetLemmatizer()
        lemmatized_words_list = []
        for i in range(len(self.tokens)):
            lemmatized_words = [lemmatizer.lemmatize(word, pos="v") for word in self.tokens[i]]
            lemmatized_words_list.append(lemmatized_words)
        self.tokens = copy.deepcopy(lemmatized_words_list)

    def start(self):
        for i in range(len(self.docs)):
            self.docs[i] = self.case_folding(self.docs[i])  # Handle Upper cases
            self.docs[i] = self.special_characters_remover(self.docs[i])  # Eliminate Special Characters
        self.tokenize()
        print(self.docs)
        print(self.tokens)
        print(len(self.tokens))
        self.stop_word_remover()
        print(self.tokens)
        print(len(self.tokens))
        self.stemming()
        print(self.tokens)
        print(len(self.tokens))
        self.lemmatization()
        print(self.tokens)
        print(len(self.tokens))
