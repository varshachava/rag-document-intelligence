class Retriever:

    def __init__(self, embedding_service, vector_index):

        self.embedding_service = embedding_service

        self.vector_index = vector_index

    def retrieve(self, query, top_k):

        query_embedding = self.embedding_service.embed_query(query)

        docs = self.vector_index.search(query_embedding, top_k)

        return docs
