# Adaptive-Text

## Description
This Python project uses a Large Language Model (LLM) for rephrasing input text. It sends a user-input text to the LLM, receives a rephrased version, and logs the original, user input, and rephrased text to a file.

## Installation

### Prerequisites
- Python 3.8
- OpenAI API key

### Setup
1. **Clone the repository**
    ```bash
    git clone https://github.com/gabrpark/Adaptive-Text.git
    cd Adaptive-Text
    ```

2. **Create and activate a virtual environment (optional but recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your OpenAI API key**
    - Create a `.env` file in the project root.
    - Add your API key to the file:
        ```bash
        OPENAI_API_KEY='your-api-key-here'
        ```

## Usage

Run the main script from the command line:

```bash
python src/main.py
```

The program will output the rephrased text and log both the original and rephrased versions to `logs/rephrased_text_data.txt`.

## Structure

- `src/`: Contains the source code.
    - `main.py`: Entry point of the application.
    - `rephraser.py`: Handles the rephrasing logic.
    - `logger.py`: Manages logging functionalities.
- `logs/`: Stores the logs of rephrased texts.
- `tests/`: Contains unit tests for the application.
- `requirements.txt`: Lists the Python dependencies for the project.