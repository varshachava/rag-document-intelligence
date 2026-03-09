from dataclasses import dataclass

@dataclass
class ModelConfig:

    embedding_model_name: str = "sentence-transformers/all-MiniLM-L6-v2"

    qa_model_name: str = "distilbert-base-cased-distilled-squad"

    chunk_size: int = 400

    top_k: int = 3
