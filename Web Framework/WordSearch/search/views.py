# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

array = ('word1', 'word2', 'word3', 'word4', 'word5')


def search(request):
    context = {
        'arrays': array,
    }
    return render(request, 'search.html', context)


def train(request):
    pass
