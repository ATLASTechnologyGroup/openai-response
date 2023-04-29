import os
import sys
import openai


def print_usage():
    print('Usage: python main.py <model_id>')
    print()
    print('Arguments:')
    print('  model_id: The ID pointing to an OpenAI model under the provided OpenAI API Key')
    print()
    print('Example:')
    print('  python main.py ft-user-20220101-123456789')
    print()
    print('If on Windows, you need to provide the file key as a mounted file at /app/openai_api_key.txt, otherwise, use Docker secrets')
    print()
    print('Example:')
    print(r'  -v C:\Users\windows.user\Documents\openai_api_key.txt:/app/openai_api_key.txt')


def generate_response(model_id):
    response = openai.Completion.create(
        engine=model_id,
        prompt='quick response',
        # This is so that during testing, we don't accidentally use a ton of tokens, to help limit our costs
        max_tokens=30,
        stop=['\n']
    )

    print(response['choices'][0]['text'])


if __name__ == '__main__':
    if len(sys.argv) != 2\
            or '--help' in sys.argv:
        print('Usage: python main.py <model_id>')
        sys.exit(1)

    model_id_arg = sys.argv[1]

    env_api_key = os.getenv("OPENAI_API_KEY")
    if env_api_key:
        openai.api_key = env_api_key
    else:
        with open('/app/openai_api_key.txt', 'r') as api_key:
            openai.api_key = api_key.read().strip()
    generate_response(model_id_arg)
