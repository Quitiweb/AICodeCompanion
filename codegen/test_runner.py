import unittest
import sys
import io
from contextlib import redirect_stdout

def run_tests(test_filename):
    try:
        # Capture stdout
        output = io.StringIO()
        with redirect_stdout(output):
            # Load the test module
            module_name = test_filename[:-3]  # Remove .py extension
            __import__(module_name)
            
            # Run the tests
            loader = unittest.TestLoader()
            suite = loader.loadTestsFromName(module_name)
            runner = unittest.TextTestRunner(stream=output)
            result = runner.run(suite)
            
        return {
            'success': result.wasSuccessful(),
            'output': output.getvalue(),
            'failures': len(result.failures),
            'errors': len(result.errors)
        }
        
    except Exception as e:
        return {
            'success': False,
            'output': str(e),
            'failures': 0,
            'errors': 1
        }
