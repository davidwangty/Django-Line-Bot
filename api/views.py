import os
from datetime import datetime

from django.shortcuts import render
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

AccessToken = os.environ['ChannelAccessToken']

line_bot_api = LineBotApi(AccessToken)


def pushTextMessage(id, message):
    line_bot_api.push_message(
        id, TextSendMessage(text=message)
    )


def replyTextMessage(reply_token, message):
    line_bot_api.reply_message(
        reply_token,
        TextSendMessage(text=message)
    )


def getGroupMemberProfile(group_id, member_id):
    profile = line_bot_api.get_group_member_profile(group_id, member_id)

    return profile
