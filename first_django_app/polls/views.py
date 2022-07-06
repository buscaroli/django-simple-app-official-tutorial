from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello World! This is poll index!")


def detail(request, question_id):
    return HttpResponse(f"You are looking at question {question_id}.")


def results(request, question_id):
    response = f"Results for question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"Voting on question {question_id}.")
