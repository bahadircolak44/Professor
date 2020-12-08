from django import forms
from api.db_models.comment import Comment


class CommentSerializer(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['id', 'comment', 'like_count']
