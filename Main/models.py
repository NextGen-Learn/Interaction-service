from django.db import models

class ChatRoom(models.Model):
    id = models.AutoField(primary_key=True)
    requester = models.IntegerField(blank=False)
    responder = models.IntegerField(blank=False)
    chat_type = models.CharField(max_length=50, blank=True)
    last_message = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Chat Room"
        verbose_name_plural = "Chat Rooms"
        ordering = ['-created_at']
        unique_together = ('requester', 'responder')

    def __str__(self):
        return f"ChatRoom {self.id} between requester {self.requester} and responder {self.responder}"
