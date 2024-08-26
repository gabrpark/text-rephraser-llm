from emo_embeddings import data_redis
from emo_embeddings import utils

# Establish a connection to the Redis database
r = data_redis.connect_to_redis()


class EmoEmbeddings:
    """
    A class to handle operations related to emotional embeddings including retrieving embeddings and
    calculating similarities between emotions.
    """

    def __init__(self):
        """
        Initializes the EmoEmbeddings instance.
        """
        pass

    def get_embedding(self, emotion):
        """
        Retrieves the vector embedding for a given emotion from Redis.

        Parameters:
            emotion (str): The emotion for which to retrieve the embedding.

        Returns:
            np.array: The vector embedding of the given emotion.
        """

        vector = data_redis.retrieve_vector(r, emotion)
        return vector

    def calculate_similarity(self, emotion1, emotion2):
        """
        Calculates the cosine similarity between the embeddings of two emotions.

        Parameters:
            emotion1 (str): The first emotion.
            emotion2 (str): The second emotion.

        Returns:
            float: The cosine similarity between the two emotions' embeddings, or
            None if either word's embedding is not found.
        """
        vector1 = self.get_embedding(emotion1)
        vector2 = self.get_embedding(emotion2)

        if vector1 and vector2:
            similarity = utils.cosine_similarity(vector1, vector2)
            return similarity
        else:
            print(f"Word not found in Redis")
            return None


if __name__ == '__main__':
    word1 = 'interesting'
    word2 = 'boring'
    emoemb = EmoEmbeddings()
    similarity = emoemb.calculate_similarity(word1, word2)
    print(f"Similarity between {word1} and {word2} is {similarity}")
