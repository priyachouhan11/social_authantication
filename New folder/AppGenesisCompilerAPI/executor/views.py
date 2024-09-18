from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import subprocess

from executor.models import CodeSnippet
from executor.serializers import CodeSnippetSerializers


class CodeExecutionView(APIView):
    serializer_class =  CodeSnippetSerializers
    queryset = CodeSnippet.objects.all()
    
    def post(self, request, *args, **kwargs):
        code = request.data.get("code")
        language = request.data.get("language")

        if not code or not language:
            return Response({"error": "Code and language are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Determine the command to run based on the programming language
        if language == "python":
            cmd = ["python3", "-c", code]
        elif language == "javascript":
            cmd = ["node", "-e", code]
        elif language == "bash":
            cmd = ["bash", "-c", code]
        else:
            return Response({"error": "Unsupported language."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
            return Response({"output": result.stdout, "error": result.stderr})
        except subprocess.TimeoutExpired:
            return Response({"error": "Code execution timed out."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
