# OpenAI Response Generator

This is a simple Python script that uses the OpenAI API to generate a quick response based on a given model ID.

## Requirements

- An OpenAI API key: https://beta.openai.com/docs/api-reference/authentication
- Python 3.11 OR Docker

## Usage

There are two ways to run this project: using Docker or using Python.

### Using Docker

Docker is a tool that allows you to run applications in isolated and portable environments. You can use Docker to run this project without worrying about dependencies or compatibility issues.

To run the project using Docker, use the following steps:

1. Install Docker on your machine: https://docs.docker.com/get-docker/
2. Build the Docker image using the provided Dockerfile. For example:

`docker build -t openai-response-generator .`

This will create an image called `openai-response-generator` on your machine.
3. Either:
- Create a file called `openai_api_key.txt` in any directory of your choice, and paste your OpenAI API key in it
- Create a Docker secret called `openai_api_key` that contains your OpenAI API key using this command:
`echo "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" | docker secret create openai_api_key -`
where `sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` is your OpenAI API key.
4. Run the Docker container using the first command if you made a file, or the second command if you made a secret:

- `docker run -it -v /path/to/openai_api_key.txt:/run/secrets/openai_api_key -e MODEL_ID=model_id openai-response-generator`
- `docker run -it --secret openai_api_key -e MODEL_ID=model_id openai-response-generator`

Where:

- `/path/to/openai_api_key.txt` is the absolute path to the file that contains your OpenAI API key.
- `model_id` is the ID of the model to generate a response from.

The script will print the generated response to the standard output.

### Using Python

Python is a popular programming language that you can use to run this project directly on your machine. You need to install Python and some libraries before running the script.

To run the project using Python, use the following steps:

1. Install Python 3.11 on your machine: https://www.python.org/downloads/
2. Install OpenAI Python library using this command:

`pip install openai`

3. Set your OpenAI API key as an environment variable or create a file that contains it:

- To set it as an environment variable, use this command:

`export OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

where `sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` is your OpenAI API key.

- To create a file that contains it, create a file called `openai_api_key.txt` in the same directory as your script, and paste your OpenAI API key in it.

4. Clone or download this repository to your local machine.
5. Run the script using this command:

`python main.py model_id`

where:

- `model_id` is the ID of the model to generate a response from.

The script will print the generated response to the standard output.

## Notes
- The script uses a max_tokens parameter of 30 to limit the number of tokens used by the OpenAI API and reduce the costs.
- The script uses a stop parameter of ‘\n’ to end the response at the first newline character.