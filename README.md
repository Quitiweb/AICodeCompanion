# AI Code Generator

An AI-powered Django application that generates Python code and unit tests based on natural language prompts. This project uses OpenAI's GPT model to create code implementations and corresponding test cases, automatically fixing any test failures.

## Features

- 🤖 AI-powered code generation using OpenAI's GPT-4o model
- ✅ Automatic test generation and validation
- 🔄 Self-healing code: automatically fixes failing tests
- 🌐 RESTful API for integration with other tools
- 💻 User-friendly web interface

## Prerequisites

- Python 3.11 or higher
- OpenAI API key
- Django and Django REST Framework
- Other dependencies (managed by the package manager)

## Dependencies

This project requires the following Python packages:
```
django
django-cors-headers
djangorestframework
openai
gunicorn
```

## Environment Variables

Create a `.env` file in the root directory and add:

```
OPENAI_API_KEY=your_openai_api_key
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Quitiweb/AICodeCompanion
cd AICodeCompanion
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver 0.0.0.0:5000
```

## Usage

### Web Interface

1. Open your browser and navigate to `http://localhost:5000`
2. Enter your code requirements in the prompt field
3. Specify the desired Python filename
4. Click "Generate Code"

### API Endpoints

#### Generate Code
```
POST /api/generate/
```

Request body:
```json
{
    "prompt": "Create a function that calculates the fibonacci sequence",
    "filename": "fibonacci.py"
}
```

Response:
```json
{
    "success": true,
    "code": "generated_code_content",
    "tests": "generated_test_content",
    "test_results": {
        "success": true,
        "output": "test_execution_output",
        "failures": 0,
        "errors": 0
    }
}
```

## Use Cases

1. **Quick Prototyping**
   ```
   Prompt: "Create a function that reads a CSV file and returns a dictionary"
   Filename: data_reader.py
   ```

2. **Algorithm Implementation**
   ```
   Prompt: "Implement a binary search tree with insert and search methods"
   Filename: binary_search_tree.py
   ```

3. **Test Generation**
   ```
   Prompt: "Create unit tests for a user authentication system"
   Filename: test_auth.py
   ```

## Features Coming Soon

- Support for multiple programming languages
- Parallel test execution
- Code review suggestions
- Custom test framework selection

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
