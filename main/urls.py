from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_data_list, name='main_data_list'),
    path('delete/', views.delete_data, name='delete_data'),
    path('upload-document/', views.upload_document, name='upload_document'),
    path('upload-document2/', views.upload_document2, name='upload_document2'),
    path('upload-document3/', views.upload_document3, name='upload_document3'),
    path('upload-document4/', views.upload_document4, name='upload_document4'),
    path('upload-document5/', views.upload_document5, name='upload_document5'),
    path('upload-document6/', views.upload_document6, name='upload_document6'),
]
