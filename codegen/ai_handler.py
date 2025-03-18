from decouple import config
from openai import OpenAI

# the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
# do not change this unless explicitly requested by the user
OPENAI_API_KEY = config("OPENAI_API_KEY")
openai = OpenAI(api_key=OPENAI_API_KEY)

def generate_code_and_tests(prompt, filename):
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are a Python expert that generates code and unit tests. "
                    "Provide response in JSON format with 'code' and 'tests' keys."
                },
                {
                    "role": "user",
                    "content": f"Generate Python code and unit tests for the following task:\n{prompt}\n"
                    f"The code should be saved in {filename}. Generate comprehensive unit tests."
                }
            ],
            response_format={"type": "json_object"}
        )
        
        result = response.choices[0].message.content
        return result['code'], result['tests']
        
    except Exception as e:
        raise Exception(f"Failed to generate code: {str(e)}")
