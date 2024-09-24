from django.db import models



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="kategoriya nomi")

    def get_newses(self):
        newses = self.news_set.filter(is_active = True)
        return newses

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

class Tags(models.Model):
    name = models.CharField(max_length=50, verbose_name="Taglar nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Taglar"

class News(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nomi")
    slug = models.SlugField(max_length=255, verbose_name="Slug")
    description = models.TextField(blank=True, null=True, verbose_name="Matni")
    image = models.ImageField(upload_to="news/image/", blank=True, null=True, verbose_name="Rasmi")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqt")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Maqola kategoriyasi")
    tags = models.ManyToManyField(Tags, verbose_name="Taglar")
    is_active = models.BooleanField(default=True, verbose_name="Saytga chiqarish")
    is_banner = models.BooleanField(default=False, verbose_name="Bannerga chiqarish")

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1f4C-cWV03_czRXhL1THkOdS9RDnAtPxRnA&s"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"


