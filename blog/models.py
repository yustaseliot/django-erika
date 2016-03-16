# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core.validators import MaxLengthValidator

class Article(models.Model):
    author = models.ForeignKey('auth.User')
    article_title = models.CharField('Название статьи', max_length=200)
    article_short_text = models.TextField('Короткий текст статьи', validators=[MaxLengthValidator(1000)])
    article_text = models.TextField('Полный текст статьи')
    published_date = models.DateTimeField('Дата создания', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.article_title
