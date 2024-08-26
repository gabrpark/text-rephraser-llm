import redis


def connect_to_redis(host='localhost', port=6379, db=0):
    """
    Establishes a connection to a Redis database.

    Parameters:
        host (str): The hostname of the Redis server. Default is 'localhost'.
        port (int): The port number on which Redis is running. Default is 6379.
        db (int): The database number to connect to. Default is 0.

    Returns:
        Redis: A Redis connection object.
    """
    return redis.Redis(host=host, port=port, db=db)


def store_data(r, data_dict):
    """
    Stores a dictionary of word vectors in Redis.

    Parameters:
        r (Redis): A Redis connection object.
        data_dict (dict): A dictionary where keys are words and values are their corresponding vectors.
    """
    for word, vector in data_dict.items():
        # Convert vector to a comma-separated string for storage
        vector_str = ','.join(map(str, vector))
        r.set(word, vector_str)


def retrieve_vector(r, word):
    """
    Retrieves a vector from Redis and converts it back to a list of floats.

    Parameters:
        r (Redis): A Redis connection object.
        word (str): The word to retrieve the vector for.

    Returns:
        list: The vector as a list of floats, or None if the word is not found.
    """
    vector_str = r.get(word)
    # Decode the byte string and convert back to a list of floats
    return list(map(float, vector_str.decode('utf-8').split(','))) if vector_str else None
