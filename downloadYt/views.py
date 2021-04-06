from django.shortcuts import render
from downloadYt.forms import EntryForm
from pytube import YouTube
import requests
import mimetypes
from django.contrib import messages


# Create your views here.

# def Download(f):
    # fl_path = '/file/path'
    # filename = 'downloaded_file_name.extension'

    # fl = open(fl_path, 'r')
    # mime_type, _ = mimetypes.guess_type(fl_path)
    # response = HttpResponse(fl, content_type=mime_type)
    # response['Content-Disposition'] = "attachment; filename=%s" % filename
    # path="C:/"
    # f.download(path)


def index(request):
    vid=''
    path="D:/"
    form=EntryForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        link=form.cleaned_data.get('Input')
        try:
                
            yt=YouTube(link)    
            vid=yt.streams.filter(progressive=True).get_highest_resolution()
            try:
                vid.download(path)
                messages.success(request,"Download Completed")
            except:
                messages.warning(request,"Something went wrong. Try Again ")  
        except:

            messages.error(request,"Check your Internet connection before trying")    

        
        
        #   i=1
        # for strm in vid:
        #     # print(str(i)+""+str(strm)+"\n")
        #     a.append(str(i)+""+str(strm))
        #     i+=1
    

    context={
        'Streams' : vid,
    }


    return render(request,"index.html",context)