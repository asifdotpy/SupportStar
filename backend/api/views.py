from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import MessageSerializer, TrainingDataSerializer
from .models import Message
import requests

class ChatbotViewSet(viewsets.ModelViewSet):
    """
    A viewset for interacting with the chatbot.
    """
    # Specify the queryset and serializer_class attributes for your viewset
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    @action(detail=False, methods=['post'])
    def message(self, request):
        """
        Endpoint for sending messages to the chatbot and receiving responses.
        """
        # Get an instance of the serializer with the request data
        serializer = self.get_serializer(data=request.data)

        # Validate the request data using the serializer
        serializer.is_valid(raise_exception=True)

        # Get the user's message from the validated data
        message = serializer.data['message']

        # Send the message to the Rasa server and get the response
        response = requests.post('http://0.0.0.0:5005/webhooks/rest/webhook', json={'message': message})
        response_data = response.json()

        # Return the chatbot's response
        return Response(response_data)

    @action(detail=False, methods=['post'])
    def train(self, request):
        """
        Endpoint for training the chatbot's machine learning models using training data.
        """
        # Specify a different serializer class for this action
        serializer = TrainingDataSerializer(data=request.data)

        # Validate the request data using the serializer
        serializer.is_valid(raise_exception=True)

        # Get the training data from the validated data
        training_data = serializer.data

        # Send the training data to the Rasa server and get the response
        response = requests.post('http://0.0.0.0:5005/model/train', json=training_data)
        response_data = response.json()

        # Return information about the training process
        return Response(response_data)
