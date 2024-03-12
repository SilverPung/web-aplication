from django import forms
from .models import Conversation, ConversationMessage


class NewConversationForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields=['content']
        widgets = {
            'content': forms.Textarea(
                attrs={'placeholder': 'Type a message...', 'class': 'w-full py-4 px-6 rounded-xl border'}),
        }