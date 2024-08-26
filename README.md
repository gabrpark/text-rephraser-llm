# Real-Time Interactive Text Rephrasing App

## Description
This is a capstone project for the Master of Science in Data Science program at the Rochester Institute of Technology (RIT). The project aims to develop an interactive machine learning system using a mobile application that rephrases text using a Large Language Model (LLM) and adapts to the user's emotional response to the rephrased text. The application is built using the Flutter framework and using the OpenAI API.
This system sends a user-input text to the OpenAI API, receives a rephrased version, and logs the original, user inputs, and rephrased text to a file.

## Installation

### Prerequisites
- Python 3.9
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
    docker compose up -d
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
python app/adaptator.py
```

The program outputed the rephrased text and log both the original and rephrased versions to `logs/logs.txt`.

The adjustable parameters are:
- `original_text (String)`: The text to be rephrased.
- `current_text (String)`: The current version of the text.
- `selected_sentence_index (Integer)`: The index of the selected sentence within the text.
- `current_emotion (String)`: The current emotional tone of the text.
- `target_emotion (String)`: The target emotional tone desired for the text.

## Structure

- `app/`: Contains the source code.
    - `adaptator.py`: Runs the main script.
    - `similarity.py`: Contains the semantic similarity algorithm.
    - `utils.py`: Contains utility functions.
    - `emo_embeddings/`: Contains the emotional embeddings.
        - `data_redis.py`: Performs the data retrieval from the Redis database.
        - `embd_data_loader.py`: Initializes the emotional embeddings from GloVe txt to the Redis database.
        - `emo_embeddings.py`: Accesses the emotional embeddings.
        - `utils.py`: Contains utility functions.
    - `api/`: Contains the API configuration.
        - `models/`: Contains the API models.
            - `model.py`: Contains the API model.
        - `routes/`: Contains the API routes.
            - `routes.py`: Contains the API routes.
        - `utils/`: Contains the API utility functions.
            - `auth.py`: Contains the API authentication functions.
        - `config.py`: Contains the API configuration.
- `logs/`: Stores the logs of rephrased texts.
- `visualizations/`: Contains the visualizations of the adaptive process.
- `requirements.txt`: Lists the Python dependencies for the project.
- `Dockerfile`: Contains the Docker configuration.
- `docker-compose.yml`: Contains the Docker Compose configuration.
- `README.md`: The project's main documentation.
- `run.py`: Runs the main script.
- `wsgi.py`: Contains the WSGI configuration.
- `.gitignore`: Lists files and directories to be ignored by Git.
