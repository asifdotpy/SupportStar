from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    """
    A serializer for sending messages to the chatbot and receiving responses.
    """
    message = serializers.CharField()

class TrainingDataSerializer(serializers.Serializer):
    """
    A serializer for training the chatbot's machine learning models using training data.
    """
    training_data = serializers.JSONField()

