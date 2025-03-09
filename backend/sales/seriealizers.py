from rest_framework import serializers
from .models import QueryHistory

class CustomQuerySerializer(serializers.Serializer):
    database_type = serializers.ChoiceField(choices=(('mysql', 'MySQL'), ('postgresql', 'PostgreSQL'), ('sqlite', 'SQLite'), ('global', 'Global')))
    query = serializers.CharField()

class OpenAIQuerySerializer(serializers.Serializer):
    user_prompt = serializers.CharField()

class QueryHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryHistory
        fields = '__all__'


