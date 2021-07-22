from . import views
from application.utils import path

urlpatterns = [
    path(r"/", views.index),
    path(r'/detail/<int:user_id>',views.detail),
    path(r'/read/<int:user_id>',views.read),
]