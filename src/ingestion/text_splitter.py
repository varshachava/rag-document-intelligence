class TextSplitter:

    def __init__(self, chunk_size=400):

        self.chunk_size = chunk_size

    def split(self, documents):

        chunks = []

        for document in documents:

            start = 0

            while start < len(document):

                chunk = document[start:start+self.chunk_size]

                chunks.append(chunk)

                start += self.chunk_size

        return chunks
