from django.contrib import admin
from .models import Like, Dislike

# Register your models here.
class NumberOfLikes(admin.ModelAdmin):
    model = Like
    fields = ['countLikes']
    
class NumberOfDislikes(admin.ModelAdmin):
    model = Dislike
    fields = ['countDislikes']

admin.site.register(Like, NumberOfLikes)
admin.site.register(Dislike, NumberOfDislikes)