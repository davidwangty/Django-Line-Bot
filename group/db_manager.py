from . import models


def get_line_group(line_id):
    line_group = models.LineGroup.objects.filter(group_line_id=line_id).first()
    return line_group


def get_emba_line_group(group_id):
    line_groups = models.LineGroup.objects.filter(emba_group=group_id)
    return line_groups
