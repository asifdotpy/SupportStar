from django.db import models

class Message(models.Model):
    """
    A model class for representing the messages that are sent and received by the chatbot.
    """
    text = models.TextField()
    sender = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.text}"

