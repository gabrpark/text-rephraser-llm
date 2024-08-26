import torch
import spacy
from scipy.spatial.distance import cosine
from transformers import AutoModel, AutoTokenizer, BertModel, BertTokenizer
from openai import OpenAI
from transformers import T5EncoderModel, T5Tokenizer

openai = OpenAI()


class Similarity:
    """
    A class to compute similarity between two texts using different language models like BERT, LLAMA-2, and T5.
    """

    def __init__(self):
        """
        Initializes the Similarity instance.
        """
        pass

    def compare_bert(self, text1, text2):
        """
        Compute the similarity between two texts using the BERT model.

        Parameters:
            text1 (str): The first text string.
            text2 (str): The second text string.

        Returns:
            float: The cosine similarity between the two text embeddings.
        """
        # Load pre-trained model and tokenizer
        model_name = 'bert-base-uncased'
        tokenizer = BertTokenizer.from_pretrained(model_name)
        model = BertModel.from_pretrained(model_name)

        # Encode the texts
        inputs1 = tokenizer(text1, return_tensors="pt",
                            padding=True, truncation=True)
        inputs2 = tokenizer(text2, return_tensors="pt",
                            padding=True, truncation=True)

        # Generate embeddings
        with torch.no_grad():
            outputs1 = model(**inputs1)
            outputs2 = model(**inputs2)

        # Use the mean of the last hidden states as the sentence embedding
        embedding1 = outputs1.last_hidden_state.mean(dim=1).numpy()[0]
        embedding2 = outputs2.last_hidden_state.mean(dim=1).numpy()[0]

        # Compute cosine similarity
        similarity = 1 - cosine(embedding1, embedding2)

        return similarity

    def compare_llama2(self, text1, text2):
        """
        Compute the similarity between two texts using the LLAMA-2 model.

        Parameters:
            text1 (str): The first text string.
            text2 (str): The second text string.

        Returns:
            float: The cosine similarity between the two text embeddings.
        """
        # Initialize LLAMA-2 model and tokenizer
        model_name = 'meta-llama/Llama-2-7b-chat-hf'
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModel.from_pretrained(model_name)

        # Encode the texts
        inputs1 = tokenizer(text1, return_tensors="pt",
                            padding=True, truncation=True)
        inputs2 = tokenizer(text2, return_tensors="pt",
                            padding=True, truncation=True)

        # Generate embeddings
        with torch.no_grad():
            outputs1 = model(**inputs1)
            outputs2 = model(**inputs2)

        # Use the mean of the last hidden states as the sentence embedding
        embedding1 = outputs1.last_hidden_state.mean(dim=1).numpy()[0]
        embedding2 = outputs2.last_hidden_state.mean(dim=1).numpy()[0]

        # Compute cosine similarity
        similarity = 1 - cosine(embedding1, embedding2)

        return similarity

    def compare_t5(self, text1, text2):
        """
        Compute the similarity between two texts using the T5 model.

        Parameters:
            text1 (str): The first text string.
            text2 (str): The second text string.

        Returns:
            float: The cosine similarity between the two text embeddings.
        """
        # Initialize the T5 model and tokenizer
        model_name = 't5-small'  # You can choose other sizes like 't5-base', 't5-large'
        tokenizer = T5Tokenizer.from_pretrained(model_name)
        model = T5EncoderModel.from_pretrained(model_name)

        # Function to generate embeddings using T5

        def get_embedding(text, tokenizer, model):
            inputs = tokenizer(text, return_tensors="pt",
                               padding=True, truncation=True, max_length=512)
            with torch.no_grad():
                outputs = model(input_ids=inputs.input_ids,
                                attention_mask=inputs.attention_mask)
            # Return the mean of the embeddings
            return outputs.last_hidden_state.mean(dim=1).numpy()

        # Generate embeddings
        embedding1 = get_embedding(text1, tokenizer, model).flatten()
        embedding2 = get_embedding(text2, tokenizer, model).flatten()

        # Compute cosine similarity between the embeddings
        similarity = 1 - cosine(embedding1, embedding2)

        return similarity
