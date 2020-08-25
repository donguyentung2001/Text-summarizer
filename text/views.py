from django.shortcuts import render
from django.shortcuts import redirect
from .cosine_similarity import summarize as summarize
# Create your views here.

def text_sum(request): 
    if request.method == "POST": 
        input=request.POST.get("text_unsum")
        request.session['summary']=input 
        return redirect('/summary/')
    else: 
        return render(request,"text/text_sum.html")

def summary(request): 
    new_text= summarize(request.session['summary'])
    return render(request,"text/summary.html", {"summary": new_text})
