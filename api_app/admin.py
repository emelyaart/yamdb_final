from django.contrib import admin
from users.models import CustomUser
from artworks.models import Category, Genre, Title, Review, Comment


admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title)
admin.site.register(Review)
admin.site.register(Comment)
