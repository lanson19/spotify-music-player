from django.shortcuts import render

# Create your views here.
def index(request, *args, **kwargs):
    return render(request, '/Users/Lukas/Desktop/Programming/spotify-music-player/music_controller/frontend/templates/frontend/index.html')