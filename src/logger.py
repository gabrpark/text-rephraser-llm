def add_text_to_file(user_input, paraphrased_text, file_name):
    """
    This function appends the user input and rephrased text to a log file.
    """
    with open(file_name, 'a') as file:  # 'a' mode opens the file for appending
        file.write(user_input + ": " + paraphrased_text + "\n")  # Appends the string and a newline to the file