import os
from mem0 import Memory

config = {
        "vector_store": {
        "provider": "qdrant",
        "config": {
            "collection_name": "test",
            "host": "localhost",
            "port": 6333,
            "embedding_model_dims": 768,  # Change this according to your local model's dimensions
        },
    },
    "llm": {
        "provider": "vllm",
        "config": {
            "model": "unsloth/gemma-3-1b-it",
            "vllm_base_url": "http://localhost:8000/v1",
            "temperature": 0.1,
            "max_tokens": 2000,
        }
    },
        "embedder": {
        "provider": "ollama",
        "config": {
            "model": "bge-m3:567m"
        }
    }
}

m = Memory.from_config(config)
m = Memory()
