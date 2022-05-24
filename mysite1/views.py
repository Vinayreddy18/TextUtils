#i have created this -vinay reddy
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyzer(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    upper = request.POST.get('upper', 'off')
    newlineremover=request.POST.get('newlineremover','off')
    lowercase=request.POST.get('lowercase','off')
    spaceremover = request.POST.get('spaceremover', 'off')
    if removepunc =="on":
        punctuations = "!>?"
        analy = ""
        for char in djtext:
            if char not in punctuations:
                analy=analy+char
        params={'purpose':'Removed punctations','analyzed_text':analy}
        djtext=analy
        # return render(request,'analyze.html',params)
    if (upper=="on"):
        analy=""
        for char in djtext:
            analy=analy+char.upper()
        params={'purpose':'Changed to uppper case','analyzed_text':analy}
        djtext = analy
        # return render(request,'analyze.html',params)
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analy
        # return render(request,'analyze.html',params)
    if (lowercase=="on"):
        analy=""
        for char in djtext:
            analy+=char.lower()
        params={'purpose':'converted to lower case','analyzed_text':analy}
        djtext = analy
        # return render(request,'analyze.html',params)
    if (spaceremover == "on"):
        analy = ""
        for index,char in enumerate(djtext):
            if (djtext[index]==' ' and djtext[index+1]==' '):
                pass
            else:
                analy=analy+char
        params = {'purpose': 'Successfully', 'analyzed_text': analy}
        djtext=analy
        # return render(request, 'analyze.html', params)
    if (newlineremover!="on" and spaceremover!="on" and lowercase!="on" and upper!="on" and removepunc!="on"):
        return HttpResponse("ERROR")
    return render(request, 'analyze.html', params)

