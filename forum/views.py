from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Response
from .forms import NewQuestion, NewReplyForm, NewResponseForm, Search
from django.urls import reverse
# Create your views here.


def homePage(request):
    questions = Question.objects.all().order_by('-created_at')

    if request.method == "POST":
        form = Search(request.POST)
        if form.is_valid():
            item = form.cleaned_data["item"]

            queryset = Question.objects.filter(title__icontains=item)
            context = {
                'searched': queryset,
                'form': Search()
            }
            return render(request, "forum/search.html", context)
    context = {
        'questions': questions,
        'new_question':NewQuestion(),
        'form': Search()
    }

    return render(request, 'forum/home.html', context)


@login_required()
def newQuestionPage(request):
    form = NewQuestion()

    if request.method == 'POST':
        form = NewQuestion(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()

            return redirect(to='forum-home')

    context = {'form': form}
    return render(request, 'forum/new-question.html', context)


def questionPage(request, id):
    response_form = NewResponseForm()
    reply_form = NewReplyForm()

    if request.method == 'POST':
        response_form = NewResponseForm(request.POST)
        if response_form.is_valid():
            response = response_form.save(commit=False)
            response.user = request.user
            response.question = Question(id=id)

            response.save()
            question = Question.objects.get(id=id)
            question.answers += 1
            question.save()
            return redirect(to='forum-home')

    question = Question.objects.get(id=id)
    question.views += 1
    question.save()
    context = {
        'question': question,
        'response_form': response_form,
        'reply_form': reply_form,
    }
    return render(request, 'forum/question.html', context)


@login_required()
def replyPage(request):
    if request.method == 'POST':
        form = NewReplyForm(request.POST)
        if form.valid():
            question_id = request.POST.get('question')
            parent_id = request.POST.get('parent')
            reply = form.save(commit=False)
            reply.user = request.user
            reply.question = Question(id=question_id)
            reply.parent = Response(id=parent_id)
            reply.save()

            return redirect(to='forum-home')

    return redirect('forum-home')
