from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from .models import (
    Question, Answer, Category, Expert_Category, Expert,
    Expert_answer, Pet, animal_ranking_Category, Post, 
    Photo, Events,animal_ranking, animal_ranking_Category,
    ForumQuestion,ForumAnswer
)
from .forms import QuestionForm , AnswerForm, ExpertForm, ExpertAnswerForm,PetForm, ForumQuestionForm, ForumAnswerForm, animalForm

from django.utils import timezone
from django.http import HttpResponse, HttpResponseNotAllowed
from django.core.paginator import Paginator  
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializer import MovieSerializer
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
)
from django.db.models import Q
from django.db.models import Count
from django.http import JsonResponse
import os
from django.core.files.storage import default_storage
from django.core.files import File
from django.core.files.base import ContentFile




class MovieViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = MovieSerializer

class UserPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html' #템플릿을 변경하려면 이와같은 형식으로 입력
    success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm
    
    def form_valid(self, form):
        if User.objects.filter(email=self.request.POST.get("email")).exists():
            return super().form_valid(form)
        else:
            return render(self.request, 'password_reset_done_fail.html')
            
class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_rest_done.html' #템플릿을 변경하려면 이와같은 형식으로 입력

def main(request, category_name='expert'):
    '''
    pybo 목록 출력
    '''
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

    expert = Expert.objects.all()
    category_list = Expert_Category.objects.all()
    #print(category_list)
    category = get_object_or_404(Expert_Category, name=category_name)
    question_list = Expert.objects.filter(category=category)
    ###expert_list변경

    page1 = request.GET.get('page1', '1')  # 페이지
    kw1 = request.GET.get('kw1', '')  # 검색어
    so1 = request.GET.get('so1', 'recent')  # 정렬기준

    animal = animal_ranking.objects.all()
    category_list1 = animal_ranking_Category.objects.all()
    category1 = get_object_or_404(animal_ranking_Category)
    question_list1 = animal_ranking.objects.filter(category=category1)

    if so1 == 'recent':
        # aggretation, annotation에는 relationship에 대한 역방향 참조도 가능 (ex. Count('voter'))
         question_list1 = question_list1.order_by('-create_date')


    # 정렬
    if so == 'recommend':
        # aggretation, annotation에는 relationship에 대한 역방향 참조도 가능 (ex. Count('voter'))
        question_list = question_list.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = question_list.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:
        question_list = question_list.order_by('-create_date')

    # 검색
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 질문 제목검색
            Q(content__icontains=kw) |  # 질문 내용검색
            Q(answer__content__icontains=kw) |  # 답변 내용검색
            Q(author__username__icontains=kw) |  # 질문 작성자검색
            Q(answer__author__username__icontains=kw)  # 답변 작성자검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(question_list,3)  # 페이지당 10개식 보여주기
    page_obj = paginator.get_page(page)
    max_index = len(paginator.page_range)

    paginator1 = Paginator(question_list1,3)  # 페이지당 10개식 보여주기
    page_obj1 = paginator1.get_page(page)
    max_index1 = len(paginator.page_range)

    context = {'question_list': page_obj, 'max_index': max_index, 'page': page, 'kw': kw, 'so': so,
               'category_list': category_list, 'category': category, 'expert':expert, 
               'question_list1': page_obj1, 'max_index1': max_index1, 'page1': page1, 'kw1': kw1, 'so1': so1,
               'category_list1': category_list1, 'category1': category1, 'animal':animal}
    
    return render(request, 'pybo/main.html', context)


def index(request, category_name='qna'):
    
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

    category_list = Category.objects.all()
    category = get_object_or_404(Category, name=category_name)
    question_list = Question.objects.filter(category=category)

    # 정렬
    if so == 'recommend':
        # aggretation, annotation에는 relationship에 대한 역방향 참조도 가능 (ex. Count('voter'))
        question_list = question_list.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = question_list.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:
        question_list = question_list.order_by('-create_date')

    # 검색
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 질문 제목검색
            Q(content__icontains=kw) |  # 질문 내용검색
            Q(answer__content__icontains=kw) |  # 답변 내용검색
            Q(author__username__icontains=kw) |  # 질문 작성자검색
            Q(answer__author__username__icontains=kw)  # 답변 작성자검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개식 보여주기
    page_obj = paginator.get_page(page)
    max_index = len(paginator.page_range)

    context = {'question_list': page_obj, 'max_index': max_index, 'page': page, 'kw': kw, 'so': so,
               'category_list': category_list, 'category': category}
    return render(request, 'pybo/question_list.html', context)
# Create your views here.

def index3(request, category_name='qna'):
   
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

    category_list = Category.objects.all()
    category = get_object_or_404(Category, name=category_name)
    question_list = Question.objects.filter(category=category)

    # 정렬
    if so == 'recommend':
        # aggretation, annotation에는 relationship에 대한 역방향 참조도 가능 (ex. Count('voter'))
        question_list = question_list.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = question_list.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:
        question_list = question_list.order_by('-create_date')

    # 검색
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 질문 제목검색
            Q(content__icontains=kw) |  # 질문 내용검색
            Q(answer__content__icontains=kw) |  # 답변 내용검색
            Q(author__username__icontains=kw) |  # 질문 작성자검색
            Q(answer__author__username__icontains=kw)  # 답변 작성자검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개식 보여주기
    page_obj = paginator.get_page(page)
    max_index = len(paginator.page_range)

    context = {'question_list': page_obj, 'max_index': max_index, 'page': page, 'kw': kw, 'so': so,
               'category_list': category_list, 'category': category}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    photo = Photo.objects.all()
    context = {'question': question, 'photo' : photo}
    return render(request, 'pybo/question_detail.html', context)



@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('pybo:detail', question_id=question.id), answer.id))
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)



@login_required(login_url='common:login')
def question_create(request, category_name):
   
    category = Category.objects.get(name=category_name)
    
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()
            question.category = category
            question.save()
            return redirect(category)
            
    else:  # request.method == 'GET'
        form = QuestionForm()
    context = {'form': form, 'category': category}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form, 'category': question.category}
    return render(request, 'pybo/question_form.html', context)



@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')



@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=answer.question.id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('pybo:detail', question_id=answer.question.id), answer.id))
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('pybo:detail', question_id=answer.question.id)




@login_required(login_url='common:login')
def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)



@login_required(login_url='common:login')
def answer_vote(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        answer.voter.add(request.user)
    return redirect('{}#answer_{}'.format(
                resolve_url('pybo:detail', question_id=answer.question.id), answer.id))




@login_required(login_url='common:login')
def user_profile(request):
    question_list = Question.objects.order_by('-create_date')
    category = Category.objects.order_by('id')
    answer_list = Answer.objects.order_by('-create_date')

    context = {'category': category, 'question_list': question_list, 'answer_list' : answer_list}
    return render(request, 'common/profile_base.html', context)

@login_required(login_url='common:login')
def user_question(request):
    question_list = Question.objects.order_by('-create_date')
    category = Category.objects.order_by('id')
    context = {'category': category, 'question_list': question_list}
    print(category)
    return render(request, 'common/profile_base.html', context)


@login_required(login_url='common:login')
def user_answer(request):
    question_list = Question.objects.order_by('-create_date')
    answer_list = Answer.objects.order_by('-create_date')
    category = Category.objects.order_by('id')
    context = {'category': category, 'question_list': question_list, 'answer_list' : answer_list}
    return render(request, 'common/profile_base.html', context)

@login_required(login_url='common:login')
def user_comment(request):
    return render(request, 'common/profile_comment.html')



# expert view/////////////////////////////////

def expert(request, category_name='expert'):
    '''
    pybo 목록 출력
    '''
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

    expert = Expert.objects.all()
    category_list = Expert_Category.objects.all()
    #print(category_list)
    category = get_object_or_404(Expert_Category, name=category_name)
    question_list = Expert.objects.filter(category=category)
    ###expert_list변경
    # 정렬
    if so == 'recommend':
        # aggretation, annotation에는 relationship에 대한 역방향 참조도 가능 (ex. Count('voter'))
        question_list = question_list.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = question_list.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:
        question_list = question_list.order_by('-create_date')

    # 검색
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 질문 제목검색
            Q(content__icontains=kw) |  # 질문 내용검색
            Q(answer__content__icontains=kw) |  # 답변 내용검색
            Q(author__username__icontains=kw) |  # 질문 작성자검색
            Q(answer__author__username__icontains=kw)  # 답변 작성자검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(question_list, 8)  # 페이지당 8개식 보여주기
    page_obj = paginator.get_page(page)
    max_index = len(paginator.page_range)

    context = {'question_list': page_obj, 'max_index': max_index, 'page': page, 'kw': kw, 'so': so,
               'category_list': category_list, 'category': category, 'expert':expert}
    return render(request, 'pybo/expert_list.html', context)

def expert_detail(request, question_id):
    question = get_object_or_404(Expert, pk=question_id)
    photo = Photo.objects.all()
    context = {'question': question, 'photo' : photo}
    return render(request, 'pybo/expert_detail.html', context)


@login_required(login_url='common:login')
def expert_create(request, category_name):
   
    category = Expert_Category.objects.get(name=category_name)
    print(category)
    expert = Expert.objects.all
    
    if request.method == 'POST':
       
        
        form = ExpertForm(request.POST, request.FILES)
        if form.is_valid():
            expert = form.save(commit=False)
            expert.author = request.user  # author 속성에 로그인 계정 저장
            expert.create_date = timezone.now()
            expert.category = category  
           
            expert.save()
           
            #return redirect(category)
            #return redirect('pybo:expert_detail')
            #expert = get_object_or_404(Question, pk=expert_id)
            context = {'question': expert, 'form': form}
            return render(request, 'pybo/expert_detail.html',context)
        else:
            print(form.errors)
    else:  # request.method == 'GET'
        form = ExpertForm()
   
    context = {'form': form, 'category': category, 'author' : request.user}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def expert_vote(request, expert_id):
    expert = get_object_or_404(Expert, pk=expert_id)
    if request.user == expert.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        expert.voter.add(request.user)
    return redirect('pybo:expert_detail', expert_id=expert.id)

@login_required(login_url='common:login')
def expert_answer_delete(request, answer_id):
    answer = get_object_or_404(Expert_answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('pybo:expert_detail', question_id=answer.question.id)

@login_required(login_url='common:login')
def expert_delete(request, question_id):
    question = get_object_or_404(Expert, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:expert_detail', question_id=question.id)
    question.delete()
    return redirect('pybo:expert')

@login_required(login_url='common:login')
def expert_modify(request, question_id):
    question = get_object_or_404(Expert, pk=question_id)
    if request.user != question.author:
        print('hi')
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:expert_detail', question_id=question.id)
    if request.method == "POST":
        form = ExpertForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('pybo:expert_detail', question_id=question.id)
    else:
        form = ExpertForm(instance=question)
    context = {'form': form, 'category': question.category}
    return render(request, 'pybo/question_form.html', context)



@login_required(login_url='common:login')
def expert_answer_modify(request, answer_id):
    answer = get_object_or_404(Expert_answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=answer.question.id)
    if request.method == "POST":
        form = ExpertAnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('pybo:expert_detail', question_id=answer.question.id), answer.id))
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/answer_form.html', context)

@login_required(login_url='common:login')
def expert_answer_create(request, question_id):
    question = get_object_or_404(Expert, pk=question_id)
    if request.method == "POST":
        form = ExpertAnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            print(question.id)
            return redirect('{}#answer_{}'.format(
                resolve_url('pybo:expert_detail', question_id=question.id), answer.id))
    else:
        form = ExpertAnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/expert_detail.html', context)

# expert view end ///////////////////////////////////////



def pet_create(request,question_id):
    pet = get_object_or_404(Pet, pk=question_id)
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return redirect('pybo:pet_create')
            context = {'pet': pet}
            return render(request, 'pybo/pet_create.html', context)
    else:
        form = PetForm()
    return render(request, 'pybo/pet_create.html', {'form': form})



def landing_page(request):
    #question_list = Question.objects.order_by('-create_date')
    #answer_list = Answer.objects.order_by('-create_date')
    #category = Category.objects.order_by('id')
    #context = {'category': category, 'question_list': question_list, 'answer_list' : answer_list}
    #print(category)
    return render(request, 'registration/landing.html')


# 2. group



@login_required(login_url='common:login')
def forumGroup(request):


    # questions = ForumQuestion.objects.all()

    questions = ForumQuestion.objects.all().order_by('-create_date')[:10]  # 최신순으로 정렬
    # photo = Photo.objects.all()
    votor = ForumQuestion.objects.all().values_list('voter', flat=True)

    for question in questions:
        
        answers = ForumAnswer.objects.filter(question=question)
        question.answers = answers
    
    context = {'questions': questions, 'votor' : votor}
    return render(request, '2.group/forum.html', context)



# 7. settig

def setting(request):
    #question_list = Question.objects.order_by('-create_date')
    #answer_list = Answer.objects.order_by('-create_date')
    #category = Category.objects.order_by('id')
    #context = {'category': category, 'question_list': question_list, 'answer_list' : answer_list}
    #print(category)
    return render(request, '7.setting/setting.html')

def dangbti(request):
    
    return render(request, 'pybo/mbti.html')









@login_required(login_url='common:login')
def calendar(request):  
    print('1')
    #category = Events.objects.order_by('id')
    author = request.user
    print(author)
    
    all_events = Events.objects.filter(author=author)
    print(all_events)
    #all_events = Events.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'pybo/calendar.html',context)
@login_required(login_url='common:login') 
def all_events(request):   
    print('2')
    author = request.user   
    print(author)                                                                                           
    all_events = Events.objects.filter(author=author)                                                                             
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'title': event.name,                                                                                         
            'id': event.id,                                                                                              
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
        })                                                                                                               
                                                                                                                      
    return JsonResponse(out, safe=False)                                                                                                              
                                                                                                                      
 
@login_required(login_url='common:login') 
def add_event(request):
    print('3')
    author = request.user
    print(author)
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end, author = author)
    event.save()
    data = {}
    return JsonResponse(data)

@login_required(login_url='common:login') 
def update(request):
    print('4')
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)
@login_required(login_url='common:login') 
def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)


# forum view///////////////////////

@login_required(login_url='common:login')
def forum(request):
    if request.method == 'POST':
        form = ForumQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('forum')
    else:
        form = ForumQuestionForm()
    questions = ForumQuestion.objects.all()
    context = {'questions': questions}
    return render(request, '2.group/forum.html', context)

@login_required(login_url='common:login')
def create_forum_question(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        
        # forum_img = request.FILES.get('forum_img')  # 이미지 파일 가져오기

        # forum_img = ForumQuestionForm(request.POST, request.FILES)
        # ForumQuestion 모델에 데이터 저장
        forum_question = ForumQuestion(
            author=request.user,
            subject=subject, 
            content=content,
            # forum_img=forum_img,
            modify_date=None,
            create_date=timezone.now(),
            category=None,
            )
        forum_question.save()
        response_data = {
            'id': forum_question.id,
            'author': forum_question.author.username,
            'subject': forum_question.subject,
            'content': forum_question.content,
            'create_date': forum_question.create_date.strftime('%Y-%m-%d %H:%M'),
        }
        return JsonResponse(response_data)
    
        # context = {'forum_question': forum_question}
        # return redirect('pybo:forumGroup')
    return render(request, '2.group/forum.html')

@login_required(login_url='common:login')
def forum_question_delete(request, question_id):
    question = get_object_or_404(ForumQuestion, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:forumGroup', question_id=question.id)
    question.delete()
    messages.success(request, '성공적으로 삭제되었습니다')
    return redirect('pybo:forumGroup')

@login_required(login_url='common:login')
def create_forum_answer(request, question_id):
    question = get_object_or_404(ForumQuestion, pk=question_id)
    if request.method == "POST":
        form = ForumAnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            print(question.id)
            return redirect('pybo:forumGroup')
    else:
        form = ForumAnswerForm()
    context = {'question': question, 'form': form}
    return render(request, '2.group/forum.html', context)

@login_required(login_url='common:login')
def forum_question_vote(request, question_id):
    
        question = ForumQuestion.objects.get(pk=question_id)
        if request.user in question.voter.all():
            question.voter.remove(request.user)
            voted = False
        else:
            question.voter.add(request.user)
            voted = True
        question.save()

        return JsonResponse({'success': True, 'voter_count': question.voter.count(), 'voted': voted})

@login_required(login_url='common:login')
def forum_answer_modify(request, answer_id):
    answer = get_object_or_404(ForumAnswer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:forumGroup', question_id=answer.question.id)
    if request.method == "POST":
        form = ForumAnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('pybo:forumGroup')
    else:
        form = ForumAnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/answer_form.html', context)

@login_required(login_url='common:login')
def forum_answer_delete(request, answer_id):
    answer = get_object_or_404(ForumAnswer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
        messages.success(request, '댓글이 성공적으로 삭제되었습니다')
    return redirect('pybo:forumGroup')

def fetch_more_posts(request):
    last_question_id = request.GET.get('last_question_id')  # 마지막으로 로드한 질문의 ID를 가져옴

    # 마지막으로 로드한 질문 ID보다 작은 ID를 가진 질문들을 가져옴
    questions = ForumQuestion.objects.filter(id__lt=last_question_id).order_by('-create_date')[:10]

    # 질문들을 JSON 형식으로 직렬화하여 응답
    data = {
        'questions': [
            {
                'id': question.id,
                'subject': question.subject,
                'content': question.content,
                'author': question.author.username,
                'create_date': question.create_date.isoformat(),
            }
            for question in questions
        ]
    }
    return render(request, '2.group/forum.html', data)


# forum end//////////////////////////////////







# animal contest view

def animalContest(request,category_name='animal_ranking'):
    
   
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

    animal = animal_ranking.objects.all()
    category_list = animal_ranking_Category.objects.all()
    #print(category_list)
    category = get_object_or_404(animal_ranking_Category, name=category_name)
    question_list = animal_ranking.objects.filter(category=category)
    ###expert_list변경
    # 정렬
    if so == 'recommend':
        # aggretation, annotation에는 relationship에 대한 역방향 참조도 가능 (ex. Count('voter'))
        question_list = question_list.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = question_list.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:
        question_list = question_list.order_by('-create_date')

    # 검색
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 질문 제목검색
            Q(content__icontains=kw) |  # 질문 내용검색
            Q(answer__content__icontains=kw) |  # 답변 내용검색
            Q(author__username__icontains=kw) |  # 질문 작성자검색
            Q(answer__author__username__icontains=kw)  # 답변 작성자검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(question_list, 4)  # 페이지당 4개식 보여주기
    page_obj = paginator.get_page(page)
    max_index = len(paginator.page_range)

    top_3_questions = question_list.order_by('-voter_count')[:3]  # voter_count 필드를 기준으로 정렬


    context = {'question_list': page_obj, 'max_index': max_index, 'page': page, 'kw': kw, 'so': so,
               'category_list': category_list, 'category': category, 'animal':animal, 'top_3_questions' : top_3_questions}
    return render(request, 'pybo/animal_contest.html', context)


@login_required(login_url='common:login')
def animalWrite(request,category_name='animal_ranking'):
   
    category = animal_ranking_Category.objects.get(name=category_name)
    aniaml = animal_ranking.objects.all
    form = animalForm(request.POST, request.FILES)
    if request.method == 'POST':
        
        form = animalForm(request.POST, request.FILES)
        if form.is_valid():
            aniaml = form.save(commit=False)
            aniaml.author = request.user  # author 속성에 로그인 계정 저장
            aniaml.create_date = timezone.now()
            aniaml.category = category  
           
            aniaml.save()
        
            context = {'aniaml': aniaml, 'form': form}
            return redirect('pybo:animalcontest', category_name='animal_ranking')
        else:
            print(form.errors)
    else:  # request.method == 'GET'
        form = animalForm()
    context = {'form': form, 'category': category}
    return render(request, 'pybo/question_form.html', context)



@login_required(login_url='common:login')
def animal_vote(request, question_id):
    question = get_object_or_404(animal_ranking, pk=question_id)

    if request.user not in question.voter.all():
        question.voter.add(request.user)
        question.voter_count += 1  # 추천수 증가
        question.save()
    
    question.voter.add(request.user)
    return redirect('pybo:animalcontest', category_name='animal_ranking')


def top_animal_ranking(request):
    top_ranking = animal_ranking.objects.order_by('-voter_count').first()  # 추천수가 가장 높은 항목 조회
    context = {'top_ranking': top_ranking}
    return render(request, 'pybo/animal_contest.html', context)











@login_required(login_url='common:login')
def train_gpt(request):
    author = request.user

    if request.method == "POST":
        #prompt = input("알렉산더 : ")
        
        #prompt = "오늘의 날짜는 2023년 7월 11일이고 내일의 날짜는 2023년 7월 12일이야. 일주일간의 반려동물 훈련 일정을 작성하되 훈련 시작일을 내일을 기준으로 줄바꿈('\n') 없이 start = Y-MM-DD HH:mm:ss, 훈련 내용을 title = 훈련내용, 훈련 종료일을 end = Y-MM-DD HH:mm:ss이런 형식으로 일주일치를 작성해줘. 이때 /n(줄바꿈)은 안써도 돼"
        pet_age = request.POST.get('pet-age','')
        pet_type = request.POST.get('pet-type','')
        #prompt = "오늘의 날짜는 2023년 7월 11일이고 내일의 날짜는 2023년 7월 12일이야. 일주일간의 반려동물 훈련 일정을 작성하되 훈련 시작일을 내일을 기준으로 줄바꿈('\n') 없이 start = Y-MM-DD HH:mm:ss, 훈련 내용을 title = 훈련내용, 훈련 종료일을 end = Y-MM-DD HH:mm:ss이런 형식으로 일주일치를 작성해줘. 이때 /n(줄바꿈)은 안써도 돼"
        prompt = pet_type+"과의 "+pet_age+"에 관한 하루치의 훈련 일정을 50글자 내외로 나눠서 만들어줘 근데 1.으로 시작해줘"
        print(prompt)
       
        return render(request, 'pybo/calendar.html', context)#, context)
    else:
        return render(request, 'pybo/calendar.html')#, context)
    
from django.contrib.auth import update_session_auth_hash

