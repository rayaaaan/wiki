from django.shortcuts import render, HttpResponse
from django.contrib import messages
from markdown import markdown

from random import choice
from . import util




def index(request):
    if request.method=="POST":
        title=request.POST["title_new_page"]
        if request.POST["index"]=="1":
            if title in util.list_entries():
                return render(request, "encyclopedia/go-back.html")
            if "my_entries" not in request.session:
                request.session["my_entries"]=[]
            if not request.session["my_entries"]:
                request.session["my_entries"]=[]
        request.session["my_entries"].append(title)
        request.session.save()
        messages.success(request, f"{title} added successfully.")
        content=request.POST["text"]
        util.save_entry(title, content)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
    
    
    
def title(request, name):
    path=f"C:\\Users\\OMEN 16\\Desktop\\django\\wiki\\entries\\{name}.md"
    with open(path, "r") as filee:
        file=markdown(filee.read())
            
    return render(request, "encyclopedia/title.html", {
        "html_content":file
    })



def search(request):
    p=request
    name=request.POST['querry']
    return title(p, name)


def add_page(request):
    if request.method=="GET":
        return render(request, "encyclopedia/add-page.html",)
    
    
    
    
def random(request):
    random=choice(util.list_entries())
    return title(request, random)



def my_pages(request):
    return render(request, "encyclopedia/my_pages.html",{
        "my_entries":request.session["my_entries"]
    })
    
    
    
    
def chose(request):
    return render(request, "encyclopedia/chose-page.html",{
        "my_entries":request.session["my_entries"]
    })

def edit(request, page):
    file=f"C:\\Users\\OMEN 16\\Desktop\\django\\wiki\\entries\\{page}.md"
    with open(file,"r") as file:
        content=file.read()  
    return render(request, "encyclopedia/edit-page.html",{
        "page":page,
        "content":content,
    })