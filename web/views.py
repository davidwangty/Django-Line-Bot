# -*- coding: utf-8 -*-
# 設定檔案編碼
import os

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import (
    HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
)
from linebot import (
    WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)

from line_api import service as line_service
from group import views as group_api

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
                line_service.replyTextMessage(
                    event.reply_token,
                    message.text+'  有聽到哦～'
                )

        elif event.type == 'follow':
            pass
        elif event.type == 'join':
            pass

    return HttpResponse()
