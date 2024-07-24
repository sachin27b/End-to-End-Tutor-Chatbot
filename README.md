# End-to-End Chatbot Project
This project implements an end-to-end chatbot using Langchain, Pinecone, and Hugging Face embeddings.

The chatbot uses a retrieval-based approach for question answering. It leverages a vector store for efficient retrieval and a language model for generating responses.

### Key Components
- Langchain: Framework for building chains of language processing actions.
Pinecone: Vector database for storing and querying embeddings.
- Hugging Face Embeddings: Transformer model embeddings for text representation.
- CTransformers: Tool for loading and running transformer models in inference mode.

### Installation
Install the required dependencies:

bash
```
pip install langchain pinecone-client transformers sentence-transformers
```
### Usage
- Download Embeddings: Obtain embeddings using the sentence-transformers/all-MiniLM-L6-v2 model.
Initialize Pinecone: Set up Pinecone with your API key.
- Load Documents: Use a PDF loader to import and split your documents.
- Create and Query Vector Store: Create a vector store in Pinecone and perform queries.
- Set Up the LLM: Configure the language model for generating responses.
- Run the Chatbot: Interact with the chatbot by providing input prompts.