from django.urls import path
from .views import HomePageView, CreatePostView , ImageToTextView

urlpatterns = [
	path('', HomePageView.as_view(), name="home"),
	path('getBillAsJson/', ImageToTextView.as_view(), name='getBill'),
	path('uploadImage/', CreatePostView, name='upload'),
]