from django.shortcuts import render
from app.forms import userForm
from app.sentiment import mlmodel
# Create your views here.
def home(request):
    return render(request,'app/home.html',{})

def index(request):
    form = userForm()
    return render(request,'app/index.html',{'form':form})

def result(request):
    username = request.POST['username']
    keyword = request.POST['keyword']
    print('-----------------------------')
    print(username)
    print(keyword)
    print('-----------------------------')
    result = mlmodel(keyword)
    print(result)
    if(result=='NEUTRAL'):
        #res_dict={'result_NEUTRAL':'https://img.icons8.com/emoji/452/neutral-face.png','NEU':'NEUTRAL'}
        res_dict={'result':'NEUTRAL'}
    elif(result=='POSITIVE'):
        #res_dict={'result_POSITIVE':'https://cdn.pixabay.com/photo/2017/03/05/21/55/emoticon-2120024_960_720.png','POS':'POSITIVE'}
        res_dict={'result':'POSITIVE'}
    elif(result=='NEGATIVE'):
        res_dict={'result':'NEGATIVE'}

    return render(request,'app/result.html',res_dict)

def accuracy(request):
    return render(request,'app/accuracy.html',{})

def code(request):
    return render(request,'app/code.html',{})