from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rockapi.views import register_user, login_user, TypeView, RockView
from django.conf.urls import include
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
    # The trailing_slash=False tells the router to accept /types instead of /types/.
router.register(r'types', TypeView, 'type')
    # The above line is what sets up the /types resource. 
    # The first parameter, r'types, is setting up the URL. 
    # The second TypeView is telling the server which view to use when it sees that url.
    # The third, type, is called the base name (could be any text). 
    ## You’ll only see the base name if you get an error in the server. It acts as a nickname for the resource and is usually the singular version of the URL.
router.register(r'rocks', RockView, 'rock')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
]
