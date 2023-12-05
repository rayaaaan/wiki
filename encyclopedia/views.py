from django.shortcuts import render, HttpResponse
from markdown import markdown
from . import util




def index(request):
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