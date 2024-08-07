from django.urls import path
from pybo.views import MovieViewSet
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path, include, re_path

app_name = 'pybo'

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    #path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('change-password/',auth_views.PasswordChangeView.as_view()),    
    path('answer/vote/<int:answer_id>/', views.answer_vote, name='answer_vote'),
    path('question/vote/<int:question_id>/', views.question_vote, name='question_vote'),
    path('expert/vote/<int:expert_id>/', views.expert_vote, name='expert_vote'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
    path('expert/answer/delete/<int:answer_id>/', views.expert_answer_delete, name='expert_answer_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('expert/modify/<int:question_id>/', views.expert_modify, name='expert_modify'),
    path('expert/answer/modify/<int:answer_id>/', views.expert_answer_modify, name='expert_answer_modify'),
    path('expert/question/delete/<int:question_id>/', views.expert_delete, name='expert_delete'),
    path('question_delete/<int:question_id>/', views.question_delete, name='question_delete'),



    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('index/', views.index, name='index'),
    path('', views.main, name='main'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('expert/answer/create/<int:question_id>/', views.expert_answer_create, name='expert_answer_create'),
    #path('question/create/', views.question_create, name='question_create'),
    path('profile/base/', views.user_profile, name='user_profile'),
    path('profile/question/', views.user_question, name='user_question'),
    path('profile/answer/', views.user_answer, name='user_answer'),
    path('profile/comment/', views.user_comment, name='user_comment'),
    path('password_reset/', views.UserPasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done/', views.UserPasswordResetDoneView.as_view(), name="password_reset_done"),
    path('question/craete/<str:category_name>/', views.question_create, name='question_create'),
    path('question/list/', views.index, name='index'),
    path('question/list/<str:category_name>/', views.index, name='index'),
    path('question/detail/<int:question_id>/', views.detail, name='detail'),
    path('expert/detail/<int:question_id>/', views.expert_detail, name='expert_detail'),
    path('expert/', views.expert, name='expert'),
    path('expert/craete/<str:category_name>/', views.expert_create, name='expert_create'),
    path('create/<int:question_id>', views.pet_create, name='pet_create'),
    path('dangbti/', views.dangbti, name='dangbti'),


    path('animal/contest/', views.animalContest, name='animal_contest'),
    # path('animal/ranking/', views.animalRanking, name='animal_ranking'),
    path('animal/write/', views.animalWrite, name='animal_write'),
    path('animal/contest/<str:category_name>/', views.animalContest, name='animalcontest'),
    #path('animal/ranking/', views.animalRanking, name='animal_ranking'),
    path('animal/write/<str:category_name>', views.animalWrite, name='animal_write'),
    path('animal/vote/<int:question_id>/', views.animal_vote, name='animal_vote'),

    path('train_gpt/', views.train_gpt, name='train_gpt'),
    path('registration/landing/', views.landing_page, name='landing_page'),


    # path('tanalyze/', views.Tanalyze, name='Tanalyze'),





    # group
    path('group/forum/', views.forumGroup, name='forumGroup'),
    
    path('group/create_forum_question/', views.create_forum_question, name='create_forum_question'),
    path('group/forum-get/', views.forum, name='forum'),
    path('group/fetch_more_posts/', views.fetch_more_posts, name='fetch_more_posts'),
    path('group/create_forum_answer/<int:question_id>/', views.create_forum_answer, name='create_forum_answer'),
    path('forum_answer/modify/<int:answer_id>/', views.forum_answer_modify, name='forum_answer_modify'),
    path('group/forum_question_vote/<int:question_id>/', views.forum_question_vote, name='forum_question_vote'),
    path('forum_answer/delete/<int:answer_id>/', views.forum_answer_delete, name='forum_answer_delete'),
    path('forum_question_delete/<int:question_id>/', views.forum_question_delete, name='forum_question_delete'),



    # setting
    path('setting/', views.setting, name='setting'),
    path('cal/',views.calendar, name='calendar'),
    path('all_events/',views.all_events, name='all_events'),
    path('add_event/',views.add_event, name='add_event'),
    path('update/',views.update, name='update'),
    path('remove/',views.remove, name='remove'),



]

