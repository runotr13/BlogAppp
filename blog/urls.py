from django.urls import path
from .views import post_create, post_delete, post_detail,post_list, post_update,add_like
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('create/',post_create,name='create'),
    path('',post_list,name='list'),
    path('detailowner/<int:id>',post_update,name='detailowner'),
    path('postDelete/<int:id>',post_delete,name="postDelete"),
    path('postDetail/<int:id>',post_detail,name="postDetail"),
    path('add_like/<int:id>',add_like,name="addlike"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)