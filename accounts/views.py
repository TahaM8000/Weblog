from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from . import forms
from django.contrib.auth.views import LoginView
from django.views.generic import (
            ListView,
            CreateView,
            UpdateView,
            DeleteView,
            DetailView,)
from accounts.models import User
from posts import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from . import mixins

 # mixins.FormValidMixin,
#----------------------------------------------------------------------------------------------
class PostList(mixins.AuthorsAccessMixin,ListView):
    template_name = "accounts/adminlte/home.html"
    def get_queryset(self):
        if self.request.user.is_staff:
            return models.Post.objects.all()[::-1]
        else:
            return models.Post.objects.filter(Author=self.request.user)
#----------------------------------------------------------------------------------------------
class PostPreview(mixins.AuthorAccessMixin,DetailView):
    template_name = "posts/classBaseViews/Post_detail.html"
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(models.Post, pk=pk)
#----------------------------------------------------------------------------------------------
class PostUpdate(mixins.AuthorAccessMixin, mixins.FormValidMixin, mixins.FieldsMixin, UpdateView):
    template_name = "accounts/PostCrud/Post_create_update.html"
    model = models.Post
#----------------------------------------------------------------------------------------------
class PostDelete(mixins.SuperUserAccessMixin, mixins.FormValidMixin,DeleteView):
    template_name = "accounts/PostCrud/Post_delete.html"
    model = models.Post
    success_url = reverse_lazy('account:panelHome')
#----------------------------------------------------------------------------------------------
class PostCreate(mixins.FormValidMixin, mixins.FieldsMixin,mixins.AuthorsAccessMixin, CreateView):
    template_name = "accounts/PostCrud/Post_create_update.html"
    model = models.Post
    success_url = reverse_lazy('account:panelHome')

#----------------------------------------------------------------------------------------------
class Login(LoginView):
    def get_success_url(self):
        user = self.request.user

        if user.is_staff or user.is_author:
            return reverse_lazy('account:panelHome')
        else:
            return reverse_lazy('account:profile')
#----------------------------------------------------------------------------------------------
class CategoryCreate(mixins.AuthorsAccessMixin,mixins.FormValidCategoryMixin, CreateView):
    fields = ['title','Cover','slug','status']
    template_name = "accounts/PostCrud/Category_create_update.html"
    model = models.Category
    success_url = reverse_lazy('account:panelHome')
#----------------------------------------------------------------------------------------------
class Profile(LoginRequiredMixin, UpdateView):
    form_class = forms.ProfileForm
    template_name = "accounts/Profile.html"
    model = User
    success_url = reverse_lazy('account:panelHome')

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user' : self.request.user
        })
        return kwargs

#----------------------------------------------------------------------------------------------
class PasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('account:password_change_done')
#----------------------------------------------------------------------------------------------
@login_required
def loginview(request):
    return render(request,'accounts/loginview.html')



class UserList(mixins.SuperUserAccessMixin,ListView):
    template_name = "accounts/User_list/User_list.html"
    def get_queryset(self):
        return User.objects.all()














class AuthorToUser(mixins.SuperUserAccessMixin, mixins.Form2ValidMixin,UpdateView):
    template_name = "accounts/User_list/User_situation.html"
    model = User
    fields = ['is_author']
    success_url = reverse_lazy('account:userlist')


class Situation(mixins.SuperUserAccessMixin,mixins.FieldsUserSituationMixin,mixins.Form3ValidMixin,UpdateView):
        template_name = "accounts/User_list/User_situation2.html"
        model = User
        success_url = reverse_lazy('account:userlist')


class PostPublish(mixins.SuperUserAccessMixin, mixins.Form2ValidMixin,UpdateView):
    template_name = "accounts/PostCrud/Post_Publish.html"
    fields = ['status']
    model = models.Post
