import os

class DocumentLoader:

    def __init__(self, data_directory):

        self.data_directory = data_directory

    def load_documents(self):

        documents = []

        for filename in os.listdir(self.data_directory):

            file_path = os.path.join(self.data_directory, filename)

            if not filename.endswith(".txt"):
                continue

            with open(file_path, "r", encoding="utf-8") as file:

                content = file.read()

                documents.append(content)

        return documents
