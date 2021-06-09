from rest_framework.response import Response
from core.models import Quizzes, Questions
from django.shortcuts import render
from rest_framework import generics
from .serializers import QuizSerializer,RandomQuestionSerializer
from rest_framework.views import APIView


# Create your views here.



class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


class RandomQuestion(APIView):
    def get(self,request,format=None,**kwargs):
        question = Questions.objects.filter(quiz__title__contains=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question,many=True)
        return Response(serializer.data)

