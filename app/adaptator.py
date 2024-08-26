from utils import split_sentences, concatenate_sentences, create_prompt_messages, get_completion_from_messages
from similarity import Similarity
from emo_embeddings.emo_embeddings import EmoEmbeddings


class Adaptator:
    """
    A class for adapting text based on user feedback to align with a target emotional response. It uses LLM
    to rephrase text and evaluates the adaptations through emotional and semantic similarity metrics.
    """

    def __init__(self, original_text, current_text, selected_sentence_index, current_emotion, target_emotion):
        """
        Initializes the Adaptator instance with the necessary text inputs and emotional states.

        Parameters:
            original_text (str): The original version of the text.
            current_text (str): The current version of the text that may already have been modified.
            selected_sentence_index (int): Index of the sentence selected for emphasis or modification.
            current_emotion (str): The user's current emotional response to the text.
            target_emotion (str): The desired emotional response that the rephrased text should evoke.
        """
        self.original_text = original_text
        self.current_text = current_text
        self.selected_sentence_index = selected_sentence_index
        self.current_emotion = current_emotion
        self.target_emotion = target_emotion
        self.rephrased_text = None
        self.emoemb = EmoEmbeddings()

    def adapt(self):
        """
        Performs the adaptation of the text based on the specified target emotion and user feedback,
        using LLM to generate a new version of the text.

        Returns:
            tuple: Contains the rephrased text, original-current text similarity,
                   current-rephrased text similarity, and emotion vector similarity.
        """

        # Define the delimiter to be used for the system message and the user query
        delimiter = "####"

        # Set up the system message to be sent to messages to the model
        system_message = f"""
        Rephrase the current text to feel more {self.target_emotion} from reading the {self.current_text}. This was the original text: {self.original_text}. User emotional feedback is marked using the delimiter {delimiter}.
        """

        # Prepare the prompt message based on current emotion
        user_message = f"""
        User emotional feedback:
        {delimiter}{self.current_emotion}{delimiter}

        if {self.current_emotion} == "confused":
            simplify the text to make it easier to understand.
        
        if {self.current_emotion} == "bored":
            make the text more engaging and interesting.
        
        if {self.current_emotion} == "angry":
            make the text more calming and soothing.
        
        if {self.current_emotion} == "sad":
            make the text more uplifting and positive.
        """

        # Set up the messages to be sent to the model, including the system message and the user query
        messages = [
            {'role': 'system', 'content': system_message.strip()},
            {'role': 'user', 'content': user_message.strip()},
        ]

        # Get the completion from the model API. Rephrase the source text with the user emotion and print the result
        self.rephrased_text = get_completion_from_messages(
            messages, temperature=0.7)
        print("\n[REPHRASED_TEXT]:\n", self.rephrased_text)

        # Semantic similarity check
        # TODO: Put a threshold for the similarity distance. If below the threshold, rephrase again. <0.9
        similarity = Similarity()
        sim_dict_orig_curr = similarity.compare_bert(
            self.original_text, self.current_text)
        sim_dist_prev_curr = similarity.compare_bert(
            self.current_text, self.rephrased_text)

        # Calculate emotion embeddings vector similarity
        emotion_distance = self.emoemb.calculate_similarity(
            self.current_emotion, self.target_emotion)

        # Log the instance of the adaptation
        print(
            f"\nCurrent Emotion: {self.current_emotion}, Target Emotion: {self.target_emotion}")
        print(
            f"\nSimilarity between Original and Current Text: {sim_dict_orig_curr}")
        print(
            f"\nSimilarity between Current and Rephrased Text: {sim_dist_prev_curr}")
        print(
            f"\nEmotion Distance between Current and Target Emotion: {emotion_distance}")

        return self.rephrased_text, sim_dict_orig_curr, sim_dist_prev_curr, emotion_distance


if __name__ == "__main__":
    # Example usage of the Adaptator class
    original_text = ("In mathematics, the Hodge conjecture is a major unsolved problem in algebraic geometry and complex geometry "
                     "that relates the algebraic topology of a non-singular complex algebraic variety to its subvarieties. In "
                     "simple terms, the Hodge conjecture asserts that the basic topological information like the number of holes "
                     "in certain geometric spaces, complex algebraic varieties, can be understood by studying the possible nice "
                     "shapes sitting inside those spaces, which look like zero sets of polynomial equations. The latter objects "
                     "can be studied using algebra and the calculus of analytic functions, and this allows one to indirectly "
                     "understand the broad shape and structure of often higher-dimensional spaces which can not be otherwise "
                     "easily visualized. More specifically, the conjecture states that certain de Rham cohomology classes are "
                     "algebraic; that is, they are sums of Poincaré duals of the homology classes of subvarieties.")
    current_text = ("In the vast world of mathematics lies a perplexing enigma known as the Hodge conjecture. It's like tumbling into a bottomless sea of intricate shapes where algebra and calculus unlock secrets to unveil hidden patterns. These enigmatic patterns offer glimpses into spaces that defy visualization, alluding to the number of 'holes' in intricate algebraic forms. Essentially, this conjecture suggests that certain classes share a profound link with algebra, hinting at a captivating interplay between geometry and algebra.")
    selected_sentence_index = 3
    target_emotion = "joy"
    current_emotion = "confused"

    adpt = Adaptator(original_text, current_text, selected_sentence_index,
                     target_emotion, current_emotion)

    adpt.adapt()
