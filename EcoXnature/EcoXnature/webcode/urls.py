from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='webcode'),
    path('about/',views.about,name='webcode'),
    path('features/',views.features,name='webcode'),
    path('dashboard/',views.dashboard,name='webcode'),
    path('games/',views.gameslist,name='webcode'),
    path('games/game1/',views.game1,name='webcode'),
    path('games/game2/',views.game2,name='webcode'),
]
