from django.shortcuts import render, redirect
from .models import User, paragraph
import requests
from django.http import JsonResponse
import random
from django.contrib.auth import authenticate,login, logout
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download("punkt")
nltk.download("stopwords")


# Create your views here.
def index(request):
    return render(request, "index.html")

def login_page(request):
    return render(request, "login.html")

def signup_page(request):
    return render(request, "signup.html")

def signup_form(request):
    if request.method=="POST":
        username= request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        User.objects.create_user(username=username, email=email, password=password)
        return redirect(login_page)
    else:
        return redirect(signup_page)

def login_signup(request):
    return render(request, "login_signup.html")

def login_form(request):
    if request.method=="POST":
        username= request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user = authenticate(username=username, email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect(dashboard_page)
        else:
            return render(request, "login.html",{'error_message':'Invalid Credentials'})

def logout_user(request):
    logout(request)
    return redirect(index)

def dashboard_page(request):
    count= paragraph.objects.count()
    random_num= random.randint(1, count)
    para= paragraph.objects.get(para_num= random_num)
    request.session['News_para'] = para.paragraph
    result= None
    result= request.session.get("result", None)
    return render(request, "dashboard.html", {'paragraph': para.paragraph, 'username':request.user,'result': result})

# def newspage(request):
#     return render(request, "newspage.html")

# def fetchnews(request):
#     url = 'https://newsapi.org/v2/everything'
#     params = {
#         'q': 'apple',
#         'from': '2024-03-29',
#         'to': '2024-03-29',
#         'sortBy': 'popularity',
#         'apiKey': 'fbc16b8a6f9f4eb9b425a04ae9ae8c24'
#     }
#     response = requests.get(url, params=params)
#     data = response.json()
#     return JsonResponse(data)
#     # request.session['news_data'] = data

#     # return redirect(news)
#     # return render(request, 'news.html',{'news':data})

# def news(request):
#     news_data = request.session.get('news_data')
#     return render(request,'news.html', {'news_data':news_data})


def user_speech(request):
    if request.method=="POST":
        SpeechPara= request.POST.get("user's_speech")
        NewsPara= request.session.get("News_para", None)
        similarity_percentage = calculate_similarity(NewsPara, SpeechPara)
        comparison_result = "Your accuracy was :" + str(int(similarity_percentage)) + "%"
        request.session["result"]= comparison_result
        return redirect(dashboard_page)
            # request, 'dashboard.html', { 'result': comparison_result})


def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

    # Stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

    return stemmed_tokens

def calculate_similarity(text1, text2):
    # Preprocess the texts
    tokens1 = preprocess_text(text1)
    tokens2 = preprocess_text(text2)

    # Calculate the intersection of tokens
    intersection = set(tokens1) & set(tokens2)

    # Calculate the percentage of similarity
    similarity_percentage = (len(intersection) / len(tokens1)) * 100

    return similarity_percentage

