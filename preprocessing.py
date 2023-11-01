import os
import re


class PreProcess:
    def __init__(self, documents_directory: str = ".\\Documents"):
        self.directory = documents_directory
        self.docs = []
        self.load_docs()
        self.start()
        print(self.docs)

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

    def stemming(self):
        pass
    pass

    def stop_word_remover(self):
        pass

    def lemmatization(self):
        pass

    def tokenizing(self):
        pass

    def start(self):
        for i in range(len(self.docs)):
            self.docs[i] = self.case_folding(self.docs[i])  # Handle Upper cases
            self.docs[i] = self.special_characters_remover(self.docs[i])  # Eliminate Special Characters


a = PreProcess()
