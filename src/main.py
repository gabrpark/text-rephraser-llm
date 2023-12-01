from rephraser import get_completion_from_messages
from logger import add_text_to_file


def main():
    # Assign the original text
    original_text = """Climate change is one of the most significant challenges facing humanity."""

    # Assign the user query
    user_input = """confused"""

    # Define the delimiter to be used for the system message and the user query
    delimiter = "####"

    # Set up the system message to be sent to messages to the model
    system_message = f"""
    Rephrase the original text with the user query.
    The user query will be delimited with four hashtags,\
    i.e. {delimiter}.
    
    Original text: {original_text}
    """

    # Set up the user message to be sent to messages to the model
    user_message = f"""
    The text is {user_input}"""

    # Set up the messages to be sent to the model, including the system message and the user query
    messages = [
        {'role': 'system',
         'content': system_message},
        {'role': 'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]

    # Rephrase the original text with the user query and print the result
    paraphrased_text = get_completion_from_messages(messages, temperature=0.7)

    # Save the paraphrased text to the output file
    output_filename = "../logs/rephrased_text_data.txt"  # Define the output file name

    # Add the paraphrased text to the output file
    if paraphrased_text:
        add_text_to_file(user_input, paraphrased_text, output_filename)
        print("Text has been rephrased and logged.")
    else:
        print("Failed to rephrase the text.")

    # Print the original and paraphrased text
    print("Original:", original_text)
    print("Rephrased:", paraphrased_text)


if __name__ == "__main__":
    main()
