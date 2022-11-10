from django.shortcuts import render
import random
import time
from agora_token_builder import RtcTokenBuilder
from django.http import JsonResponse




# Create your views here.
def getToken(request):
    appId = '76598159eca7474a9c50514cc3913b9d'
    appCertificate = "17e1b76f533e4363a5cef8f4498b95a3"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600 * 24
    currentTimeStamp = (time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid':uid}, safe=False)


def lobby(request):
    return render(request, 'lobby.html')

def room(request):
    return render(request, 'room.html')
