from django.shortcuts import render, get_object_or_404
from .models import Question, Choice, Test, User, Discipline, Theme, InfoUser
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
import random
# Create your views here.


def home(request):
    return render(request, 'system/home.html')


def about(request):
    return render(request, 'system/about.html')


def contact(request):
    return render(request, 'system/contact.html')


def discipline_list(request):
    dis = Discipline.objects.all()
    return render(request, 'system/dis_list.html', {'dis':dis})


def discipline_details(request, pk):
    dis = get_object_or_404(Discipline, pk = pk)
    return render(request, 'system/dis_details.html', {'dis': dis})


def theme_details(request, pk, theme_id):
    theme = get_object_or_404(Theme, pk = theme_id)
    return render(request, 'system/theme_details.html', {'theme': theme})


def test_details(request, pk, theme_id, test_id):
    test = get_object_or_404(Test, pk = test_id)
    return render(request, 'system/test_details.html', {'test': test})


def theme_list(request):
    theme = Theme.objects.all()
    return render(request, 'system/theme_list.html', {'theme': theme})

    
def test_list(request):
    test = Test.objects.all()
    return render(request, 'system/test_list.html', {'test': test})


def model_of_test(request, pk, theme_id, test_id):
    return render(request, 'system/model_test.html', {'pk': pk, 'theme_id': theme_id, 'test_id': test_id})



def fixed_test(request, pk, theme_id, test_id, number):
    test = get_object_or_404(Test, pk = test_id)
    count = test.question_set.count()
    if count >= number:
        question = test.question_set.all()[number-1:number].get()
        choices = question.choice_set.all().order_by('?')
        count = len(question.right_choice)
        return render(request, 'system/fixed_test.html', {'number': number, 'question': question, 
        'count': count, 'choices': choices})
    else:
        return HttpResponseRedirect(reverse('result', args = (test.id, )))


def vote(request, number, question_id):
    question = get_object_or_404(Question, pk=question_id)
    count = question.choice_set.count()
    test = get_object_or_404(Test, pk = question.test_id)
    theme = get_object_or_404(Theme, pk = test.theme_id)
    dis = get_object_or_404(Discipline, pk = theme.discipline_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        #return render(request, 'system/fixed_test.html', {
            #'question': question,
            #'error_message': "You didn't select a choice.",})
        return HttpResponseRedirect(reverse('fixed_test', args=(dis.id, theme.id, test.id, number, )))
    else:
        mas = question.right_choice.split(',')
        mas_count = len(mas)
        chet = 0
        for m in mas:
            if selected_choice.number == int(m):
                chet += 1
        test.bal += chet/mas_count
        test.save()        
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('fixed_test', args=(dis.id, theme.id, test.id, number+1, )))

def zero(request, test_id, user_id, ball):
    test = get_object_or_404(Test, pk = test_id)
    user = User.objects.get(pk = user_id)
    info = InfoUser.objects.create(user = user, test = test, count = test.bal, bal = ball)
    test.bal = 0
    test.save()
    return HttpResponseRedirect(reverse('profile', args=(user_id,)))


def bal(request, test_id):
    test = get_object_or_404(Test, pk = test_id)
    test.bal = 0
    test.save()
    return HttpResponseRedirect(reverse('test_list'))


def result(request, test_id):
    test = get_object_or_404(Test, pk = test_id)
    count = test.question_set.count()
    q = test.bal/count * 100
    ball = rating(q)
    return render(request, 'system/result.html', {'test': test, 'count': count, 'ball': ball})

def rating(q):
    ball = 0
    if q >= 30 and q <= 49:
        ball = 3
    elif q >= 50 and q <= 74:
        ball = 4
    elif q>=75 and q<=100:
        ball = 5
    return ball


def profile(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    info = user.infouser_set.all()
    return render(request, 'system/profile.html', {'info': info})