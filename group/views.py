# -*- coding: utf-8 -*-
# 設定檔案編碼
from line_api import service as line_service
from . import db_manager


def group_repost(event):
    # Get group line id
    line_id = 'aaa'
    from_group = db_manager.get_line_group(line_id)
    emba_group_id = from_group.emba_group
    emba_line_groups = db_manager.get_emba_line_group(emba_group_id)

    for group in emba_line_groups:
        if group.id != from_group.id:
            message = 'from ' + group.group_name
            message += event.message
            line_service.pushTextMessage(group.group_line_id, message)

    # Record message
