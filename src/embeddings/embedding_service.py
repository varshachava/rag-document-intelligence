from sentence_transformers import SentenceTransformer

class EmbeddingService:

    def __init__(self, model_name):

        self.model = SentenceTransformer(model_name)

    def embed_documents(self, documents):

        embeddings = self.model.encode(

            documents,

            batch_size=32,

            show_progress_bar=True

        )

        return embeddings

    def embed_query(self, query):

        return self.model.encode([query])
