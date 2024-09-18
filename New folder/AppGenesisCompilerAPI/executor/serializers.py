from rest_framework import serializers

from executor.models import CodeSnippet

class CodeSnippetSerializers(serializers.ModelSerializer):
  class Meta:
    model = CodeSnippet
    fields = '__all__'