
from django.conf import settings
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
import youtube_dl



def sound_downloader(track):

            track_url = track

            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': '../public_html/media/%(title)s.%(ext)s',
                'noplaylist': False,
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(track_url, download=False)
                title = info.get("title", "u title")
                ydl.download([track_url])
                return title


def home(request):
    return render(request, 'download/soundcloud.html')

@api_view(['POST', 'GET'])
def download(request):
    try:
        url = request.POST['url']

        title = sound_downloader(track=url)

        name = f"{title}.mp3".replace("/", "_")

        
        file_path = os.path.join(settings.MEDIA_ROOT, name)
       
        return render(request, "download/song.html", {"audio_name": name})


    except Exception as e:
        return Response({"error": str(e)}, status=500)


