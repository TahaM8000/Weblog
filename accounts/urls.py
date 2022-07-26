from django.contrib.auth import views as viewsD
from django.urls import path
from . import views as viewsA


app_name= 'account'


urlpatterns = [
    path('', viewsA.PostList.as_view() ,name='panelHome'),
    path('Post/create/', viewsA.PostCreate.as_view() ,name='create'),
    path('Post/preview/<int:pk>', viewsA.PostPreview.as_view() ,name='preview'),
    path('Post/update/<int:pk>', viewsA.PostUpdate.as_view() ,name='update'),
    path('Category/create/', viewsA.CategoryCreate.as_view() ,name='create-category'),
    path('Post/delete/<int:pk>', viewsA.PostDelete.as_view() ,name='delete'),
    path('profile/', viewsA.Profile.as_view() ,name='profile'),
    path('Users/AuthorToUser/<int:pk>',viewsA.AuthorToUser.as_view(),name='AuthorToUser'),
    path('Users/situation/<int:pk>',viewsA.Situation.as_view(),name='situation'),
    path('Users/',viewsA.UserList.as_view(),name='userlist'),
    path('Post/Publish/<int:pk>', viewsA.PostPublish.as_view() ,name='publish'),
    path('Ran/', viewsA.Ran.as_view() ,name='login'),

]
