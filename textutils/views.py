from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")
    # params={'name':'Harry', 'work':'Coder'}
    # return render(request, 'index.html', params)
    # return HttpResponse("Home")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)

def removepunc(request):
    djtext = request.GET.get('text','default')
    return HttpResponse("Removepunc")

def capfirts(request):
    return HttpResponse("Capitalize First")

def newlineremove(request):
    return HttpResponse("New line remover")

def spaceremove(request):
    return HttpResponse("Space remover")

def charcount(request):
    return HttpResponse("Character Counter")
    
def about(request):
    return HttpResponse("About this View <br> <a href='/'>Back</a>")

def personal_navigator(request):
    return HttpResponse('''<h1>Personal Navigator</h1>
    <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&i"> Django Playlist</a> <br>
    <a href="https://fastbadge.addnectarstudio.com/"> Fastbadge</a> <br>
    <a href="https://www.youtube.com/"> Youtube</a> <br>
    <a href="https://stackoverflow.com/"> Stack Overflow</a><br>
    <a href="https://mail.google.com/"> Gmail </a>
    ''')