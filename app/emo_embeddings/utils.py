import numpy as np


def cosine_similarity(vec1, vec2):
    """
    Calculate the cosine similarity between two vectors. This metric evaluates the cosine of the angle between
    two vectors projected in a multi-dimensional space.

    Parameters:
        vec1 (list or np.array): The first vector.
        vec2 (list or np.array): The second vector.

    Returns:
        float: The cosine similarity between the two vectors.
    """
    # Convert input lists to numpy arrays
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    # Compute cosine similarity
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
