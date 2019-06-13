from django.urls import path
from .views import get_first_cric,get_capkeep,post_fav,get_cap,get_dat,get_btw,get_right,get_fav
 #from .views import get_capkeep

urlpatterns=[
    path('cricket/',get_first_cric),
    path('capwi/',get_capkeep),
    path('cap/',get_cap),
    path('fav/',post_fav),
    path('data/',get_dat),
    path('btw/',get_btw),
    path('right/',get_right),
    path('favv/',get_fav),
    #path('ho/',api_add_article)
]