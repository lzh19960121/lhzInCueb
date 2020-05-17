from django.http import JsonResponse

from AnswerTemplatesManager import models


def get_template_by_author(author):
    templates = [one.__dict__ for one in models.get_template_by_author(author)]
    return JsonResponse({'list': templates, 'code': 0})
