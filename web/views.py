import os
from datetime import datetime

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import (
    HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
)
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
from linebot.models import (
    MessageEvent, JoinEvent, TextMessage, TextSendMessage, ImageSendMessage,
    responses
)

from api import views as line_api

ChannelSecret = os.environ['ChannelSecret']

parser = WebhookParser(ChannelSecret)


@csrf_exempt
@require_http_methods(['POST'])
def callback(request):
    body = request.body.decode('utf-8')
    signature = request.META['HTTP_X_LINE_SIGNATURE']

    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        return HttpResponseForbidden()
    except LineBotApiError:
        return HttpResponseBadRequest()

    for event in events:
        print('事件: ', type(event), '\n', event)
        if event.type == 'message':
            message = event.message
            if message.type == 'text':
                # Reply what bot recieve
                line_api.replyTextMessage(event.reply_token, message.text+'  有聽到哦～')
        elif event.type == 'follow':
            pass
        elif event.type == 'join':
            pass

    return HttpResponse()
