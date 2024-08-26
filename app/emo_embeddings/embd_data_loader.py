import data_redis


def load_data(file_path):
    """
    Load embeddings from a text file where each line contains a word followed by its vector components.

    Parameters:
        file_path (str): Path to the file containing word embeddings.

    Returns:
        dict: A dictionary where keys are words and values are their corresponding vector embeddings.
    """
    data = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            word = parts[0]
            vector = list(map(float, parts[1:]))
            data[word] = vector
    return data


if __name__ == '__main__':
    # Define the path to the embedding file
    path = 'app/emo_embeddings/'
    file_path = 'em-glove.6B.300d-20epoch.txt'
    # Load the data from file
    data_dict = load_data(path + file_path)

    # Connect to Redis
    r = data_redis.connect_to_redis()

    # Store the data in Redis
    data_redis.store_data(r, data_dict)
