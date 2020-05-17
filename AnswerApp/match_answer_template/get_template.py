from AnswerTemplatesManager import models
import re

# 抽象性不够


def get_template_need_replaced_words(template_strings):
    words = re.findall('[a-zA-Z0-9]+', template_strings)
    return words


def get_template_by_title(title, child_title):
    return models.get_template_by_title(title, child_title)

