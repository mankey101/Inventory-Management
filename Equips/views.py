

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Equipment
from django.views import View
from django.views.generic import ListView, DetailView

