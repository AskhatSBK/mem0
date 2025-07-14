import os
from mem0 import Memory

config = {
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
            "model": "bge-m3:567m",
            # Alternatively, you can use "snowflake-arctic-embed:latest"
            "ollama_base_url": "http://localhost:11434",
        },
    },
}

m = Memory.from_config(config)
m = Memory()
