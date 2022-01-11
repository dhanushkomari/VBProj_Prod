from django.shortcuts import render, resolve_url
from .serializers import VoiceSerializer, VersionSettingSerializer, FlatVersionSerializer, VasiSerializer, ChittiSerializer, EatNPlaySettingsSerializer
from .models import Voice, VersionSetting, FlatVersionSettings, ChittiSettings, VasiSettings, EatNPlaySettings
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from api import serializers
from datetime import date, datetime


# Create your views here.

#####################   VOICE API VIEWS    ######################
@api_view(['GET'])
def all(request):
    v = Voice.objects.all()
    serializer = VoiceSerializer(v, many = True)
    return Response(serializer.data)

@api_view(["POST"])
def postVoice(request):
    serializer = VoiceSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  def post(self, request, *args, **kwargs):
    file_serializer = VoiceSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

###################   VERSION SETTINGS VIEWS    ################

@api_view(['GET'])
def recent(request):
    try:
        v = VersionSetting.objects.latest('pk')
        serialzers = VersionSettingSerializer(v, many = False)
        return Response(serialzers.data)
    except:
        return HttpResponse('<br><br><center><h1>No Data Found, Please add some data</center></h1>')

@api_view(['GET'])
def ByVerName(request, ver_name):
    try:
        v = VersionSetting.objects.get(version_name = ver_name)
        serializers = VersionSettingSerializer(v, many = False)
        return Response(serializers.data)
    except:
        return HttpResponse('<br><br><center><h1>No Version Found with the name</center></h1>')


################  VERSION FLAT SETTINGS   ##########################
@api_view(['GET'])
def recent_flat(request):
    try:
        v = FlatVersionSettings.objects.latest('pk')
        serialzers = FlatVersionSerializer(v, many = False)
        return Response(serialzers.data)
    except:
        return HttpResponse('<br><br><center><h1>No Data Found, Please add some data</center></h1>')

@api_view(['GET'])
def ByFlatVerName(request, ver_name):
    try:
        v = FlatVersionSettings.objects.get(version_name = ver_name)
        serializers = FlatVersionSerializer(v, many = False)
        return Response(serializers.data)
    except:
        return HttpResponse('<br><br><center><h1>No Version Found with the name</center></h1>')


################      VOICE DOWNLOAD     ###########################
def VoiceDownload(request):
    v = Voice.objects.all()
    print(v)
    return render(request, 'api/all_voices.html', {'v':v})

##############   DATA FILETERS    ################
def Home(request):
    if request.method == "POST":
        if "two_dates" in request.POST:
            print('two dates')
            start_date = request.POST['start_date']
            end_date = request.POST['end_date']
            v = Voice.objects.filter(updated_at__range = (start_date, end_date))

            return render(request, 'api/all_voices.html', {'v':v})

        elif 'name_based_search' in request.POST:
            print('name search')
            v = Voice.objects.filter(bot_id__icontains = request.POST['search_by_name'])
            return render(request, 'api/all_voices.html', {'v':v})
    else:
        print('no')
        v = Voice.objects.all().distinct()
        print(v)
        return render(request, 'api/home.html')


def DayFilterView(request):
    v = Voice.objects.filter(updated_at__date = date.today())
    print(v)
    return render(request, 'api/all_voices.html', {'v':v})


#####  CHITTI VIEWS  #####
@api_view(['GET'])
def ChittiSettingsView(request):
    try:
        c = ChittiSettings.objects.latest('pk')
        serializer = ChittiSerializer(c, many = False)
        return Response(serializer.data)
    except:
        return HttpResponse('<br><br><center><h1>found an issue</center></h1>')
    
@api_view(['GET'])
def ByChittiVerName(request, ver_name):
    try:
        v = ChittiSettings.objects.get(version_name = ver_name)
        serializers = ChittiSerializer(v, many = False)
        return Response(serializers.data)
    except:
        return HttpResponse('<br><br><center><h1>No Version Found with the name</center></h1>')


#####  VASI VIEWS    #####
@api_view(['GET'])
def VasiSettingsView(request):
    try:
        v = VasiSettings.objects.latest('pk')
        serializer = VasiSerializer(v, many = False)
        return Response(serializer.data)
    except:
        return HttpResponse('<br><br><center><h1>found an issue</center></h1>')


@api_view(['GET'])
def ByVasiVerName(request, ver_name):
    try:
        v = VasiSettings.objects.get(version_name = ver_name)
        serializers = VasiSerializer(v, many = False)
        return Response(serializers.data)
    except:
        return HttpResponse('<br><br><center><h1>No Version Found with the name</center></h1>')


######    Eat N Play Views    #################
@api_view(['GET'])
def eatnplay(request):
    try:
        v = EatNPlaySettings.objects.latest('pk')
        serialzers = EatNPlaySettingsSerializer(v, many = False)
        return Response(serialzers.data)
    except:
        return HttpResponse('<br><br><center><h1>No Data Found, Please add some data</center></h1>')
