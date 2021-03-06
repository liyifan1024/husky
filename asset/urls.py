from django.urls import path
from asset import views

app_name = "asset"

urlpatterns = [
    path('ecs-create', views.EcsCreateView.as_view(), name='ecs-create'),
    path('ecs-list', views.EcsListView.as_view(), name='ecs-list'),
    path('ecs-update-<int:pk>', views.EcsUpdateView.as_view(), name='ecs-update'),
    path('ecs-detail-<int:pk>', views.EcsDetailView.as_view(), name='ecs-detail'),
    path('ecs-delete', views.EcsDeleteView.as_view(), name='ecs-delete'),
]
