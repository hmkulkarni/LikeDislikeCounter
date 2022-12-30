from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Set the default values for numLikes and numDislikes
numLikes = Like.objects.all().first().countLikes if Like.objects.exists() else 0
numDislikes = Dislike.objects.all().first().countDislikes if Dislike.objects.exists() else 0
def incrementLikes():
    global numLikes
    obj = Like.objects.all().first()
    obj.countLikes += 1
    numLikes += 1
    obj.save()

def incrementDislikes():
    global numDislikes
    obj = Dislike.objects.all().first()
    obj.countDislikes += 1
    numDislikes += 1
    obj.save()

@csrf_exempt
def index(request):
    global numLikes, numDislikes
    # If Like object doesn't exist, then create it
    if not Like.objects.exists():
        l = Like(countLikes=0)
        l.save()
        return render(request, 'index.html', {'numLikes': numLikes, 'numDislikes':  numDislikes})
    
    # If Dislike object doesn't exist, then create it
    if not Dislike.objects.exists():
        d = Dislike(countDislikes=0)
        d.save()
        return render(request, 'index.html', {'numLikes': numLikes, 'numDislikes': numDislikes})
    
    # If the button is clicked, then do this
    if request.method == "POST":
        # If like button is clicked, then call the incrementLikes() function
        if request.POST.get('like-btn'):
            incrementLikes()
        
        # If dislike button is clicked, then call the incrementDislikes() function
        if request.POST.get('dislike-btn'):
            incrementDislikes()
        
        return render(request, 'index.html', {'numLikes': numLikes, 'numDislikes': numDislikes})
    
    else:
        return render(request, 'index.html', {'numLikes': numLikes, 'numDislikes': numDislikes})