from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.

def greeting(request):
    return HttpResponse("Hi, welcome to my website!")

def goodbye(requests):
    return HttpResponse("<h1>Bye</h1><p>See you later!</p>")

def index(request):
    myname = "dang ha"
    taisan = ["dien thoai", "maytinh", "maybay", "nhieutien"]
    context = {"name": myname, "taisan": taisan}
    return render(request, "polls/index.html", context)

def viewlist(request):
    list_question = Question.objects.all()
    context = {"dsquest": list_question}
    return render(request, "polls/question_list.html", context)

def detailview(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request, "polls/detail_question.html", {"qs": q})

def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        dulieu = request.POST["choice"]
        c = q.choice_set.get(pk=dulieu)
    except:
        HttpResponse("loi khong co choice")
    c.vote = c.vote + 1
    c.save()
    return render(request, "polls/result.html", {"q": q})

