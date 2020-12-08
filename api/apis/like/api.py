from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import status

from api.apis.like.serializers import CommentSerializer
from api.db_models.comment import Comment


class LikeViewSet(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''

    def post(self, request, *args, **kwargs):
        comment_id = request.GET.get('comment_id')
        comment = Comment.objects.filter(id=comment_id).first()
        comment.like_count += 1
        comment.save()
        return HttpResponse(status=status.HTTP_200_OK)
