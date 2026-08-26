from django.shortcuts import render
from .models import NazariiKolesnikovPortfolioItem


def home_page(request):
    projects = NazariiKolesnikovPortfolioItem.objects.all()
    return render(request, 'portfolio/index.html', { 'items': projects })