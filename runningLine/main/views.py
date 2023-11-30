from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from .models import Requests
import datetime

from moviepy.editor import *
from os import path

def main(request):
    return HttpResponse('''
                        <div style="display: flex; align-items: center; flex-direction: column;">
                        <h4 style="font-size: 3rem">Hi there!</h4>
                        <p style="font-size: 1rem">Type: '/ + any text' to your browser address bar to get your running line video</p>
                        </div>''')

def runningLine(request):
        
        save(request)

        # current_directory = os.path.dirname(os.path.realpath(__file__))

        def makeRuningLine(text, size=(100, 100), duration=3, textColor='white', backgroundColor=[0, 0, 0]):
            
            textVideo = TextClip(text, color=textColor, fontsize=size[0] / 10,).set_duration(duration)
            textSize = textVideo.size
            textVideo = textVideo.set_position(lambda t: (size[0] - t * (size[0] + textSize[0]) / duration, (size[1] / 2) - (textSize[1] / 2)))
            backgroundVideo = ColorClip(size=size, color=backgroundColor, duration=duration)
            runingLine = CompositeVideoClip([backgroundVideo, textVideo])
            return runingLine

        def saveVideo(video, fps=60):
            video.write_videofile('Runing line.mp4', fps)

        text = request.path[1:]
        video = makeRuningLine(text)
        saveVideo(video)

        video = open('Runing line.mp4', 'rb')

        response = HttpResponse(video)  
        response['Content-Type']='application/octet-stream'  
        response['Content-Disposition']='attachment;filename="Running line.mp4"'  
        return response


def save(request):   
    saved_request = Requests.objects.create(request=request.path[1:], date=datetime.datetime.now())
    saved_request.save()