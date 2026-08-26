from django.db import models


class NazariiKolesnikovPortfolioItem(models.Model):
    title = models.CharField(max_length = 256, verbose_name = "Nazarii Kolesnikov's Portfolio")
    image = models.ImageField(upload_to = 'portfolio_images/', verbose_name = "Portfolio Image")
    description = models.TextField(blank = True, verbose_name = "Description")

    def __str__(self):
        return self.title