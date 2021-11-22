from django.urls import path, include
from .views import TrainModelView, DownloadModelView, PredictModelView

urlpatterns = [
    path('train_model/', TrainModelView.as_view()),
    path('downloaded_models/', DownloadModelView.as_view()),
    path('predict/', PredictModelView.as_view()),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),

]