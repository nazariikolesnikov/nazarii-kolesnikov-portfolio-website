from django.contrib import admin
from .models import NazariiKolesnikovPortfolioItem


@admin.register(NazariiKolesnikovPortfolioItem)
class NazariiKolesnikovPortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', )

