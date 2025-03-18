from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CodeGenerationSerializer
from .ai_handler import generate_code_and_tests
from .file_handler import save_files
from .test_runner import run_tests

def index(request):
    return render(request, 'codegen/index.html')

class GenerateCodeView(APIView):
    def post(self, request):
        serializer = CodeGenerationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            filename = serializer.validated_data['filename']
            prompt = serializer.validated_data['prompt']
            
            if not filename.endswith('.py'):
                filename = f"{filename}.py"
                
            # Generate code and tests using AI
            code, tests = generate_code_and_tests(prompt, filename)
            
            # Save the files
            test_filename = f"test_{filename}"
            save_files(filename, code, test_filename, tests)
            
            # Run tests
            test_results = run_tests(test_filename)
            
            if not test_results['success']:
                # If tests fail, try to fix the code
                fixed_code, fixed_tests = generate_code_and_tests(
                    f"Fix the following code and tests to make them pass:\nCode:\n{code}\nTests:\n{tests}\nTest failures:\n{test_results['output']}",
                    filename
                )
                save_files(filename, fixed_code, test_filename, fixed_tests)
                test_results = run_tests(test_filename)
            
            return Response({
                'success': True,
                'code': code,
                'tests': tests,
                'test_results': test_results
            })
            
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
