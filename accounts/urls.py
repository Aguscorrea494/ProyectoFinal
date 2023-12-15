from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import login_request, register_request, update_request, update_avatar

urlpatterns = [
   path('login/', login_request),
   path('register/', register_request),
   path('logout/', LogoutView.as_view(template_name="Accounts/logout.html"), name="Logout"),
   path('update/', update_request),
   path('avatar/', update_avatar, name="Avatar"),

   ]