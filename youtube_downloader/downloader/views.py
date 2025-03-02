import os
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
import yt_dlp
import zipfile
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def download_playlist(request):
    if request.method == 'POST':
        playlist_url = request.POST.get('playlist_url')
        download_dir = os.path.join(os.path.expanduser("~"), "Desktop", "Youtube Playlist")
        os.makedirs(download_dir, exist_ok=True)

        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])

        zip_filename = os.path.join(download_dir, 'playlist.zip')
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(download_dir):
                for file in files:
                    zipf.write(os.path.join(root, file),
                               os.path.relpath(os.path.join(root, file), download_dir))

        response = FileResponse(open(zip_filename, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="playlist.zip"'
        return response

    return render(request, 'downloader/index.html')

