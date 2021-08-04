from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),   #dispaly all shows
    path('shows', views.index),   #dispaly all shows
    path('shows/new', views.add_show),   #form to create show
    path('shows/create', views.create_show),   #Post request to create show 
    path('shows/<int:show_id>', views.view_show), #display page for specific show
    path('shows/<int:show_id>/edit', views.edit_show), #form to update show
    path('shows/<int:show_id>/update', views.update_show), #post request to update show
    path('shows/<int:show_id>/destroy', views.destroy_show), #delete show
]