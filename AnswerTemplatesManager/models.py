from django.db import models


# Create your models here.


class AnswerTemplate(models.Model):
    """
    """

    type = models.CharField(max_length=32, default="股票", verbose_name='主类别')
    child_type = models.CharField(max_length=32, blank=True, verbose_name='子类别')
    title = models.CharField(max_length=32, blank=True, verbose_name='主标题')
    child_title = models.CharField(max_length=32, blank=True, verbose_name='子标题')
    content = models.TextField(max_length=999, blank=True, verbose_name='内容')
    author = models.CharField(max_length=32, blank=True, verbose_name='作者')
    create_time = models.CharField(max_length=32, blank=True, verbose_name='最后更新时间')
    is_passed = models.BooleanField(verbose_name='是否审核通过', default=False)

    def __str__(self):
        return str(self.type) + ' ' + self.child_type + '' + self.title + ' ' + self.child_title

    class Meta:
        verbose_name = '回答模板'
        verbose_name_plural = "回答模板"


def get_template_by_title(title, child_title):
    """
    根据标题获得模板
    :param title:
    :param child_title:
    :return:
    """
    return AnswerTemplate.objects.filter(title=title, child_title=child_title)


def get_template_by_author(author):
    """
    根据用户获得模板
    :param author:
    :return:
    """
    return AnswerTemplate.objects.filter(author=author)


def get_all_templates():
    """
    得到所有模板
    :return:
    """
    return AnswerTemplate.objects.all()


def create_new_stock_template(title, child_title, content, author, create_time, is_passed):
    AnswerTemplate.objects.create(type="股票", child_type="股票", title=title, child_title=child_title, content=content,
                                  author=author, create_time=create_time, is_passed=is_passed)
