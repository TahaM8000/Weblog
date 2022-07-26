from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from posts.models import Post

class FieldsMixin():
    def dispatch(self,request,*args,**kwargs):
        self.fields = ['title','text','Cover','slug','status','Category']
        if request.user.is_staff:
            self.fields.append("Author")

        return super().dispatch(request, *args, **kwargs)

class FormValidCategoryMixin():
    def form_Valid(self, form):
            form.save()
            return super().form_Valid(form)

class FormValidMixin():
    def form_Valid(self, form):
        if self.request.user.is_staff:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.Author = self.request.user
            if not self.obj.status in ['d','i']:
                self.obj.status = 'd'

        return super().form_Valid(form)

class Form2ValidMixin():
    def form_Valid(self, form):
        if self.request.user.is_staff:
            self.obj = form.save(commit=False)
        return super().form_Valid(form)


class Form3ValidMixin():
    def form_Valid(self, form):
        if self.request.user.is_staff:
            self.obj = form.save(commit=False)
            self.obj.is_special_user = True
        return super().form_Valid(form)


class FieldsUserSituationMixin():
    def dispatch(self,request,*args,**kwargs):
        self.fields = ['is_author','special_user']

        return super().dispatch(request, *args, **kwargs)


class AuthorAccessMixin():
    def dispatch(self, request, pk,*args,**kwargs):
        post = get_object_or_404(Post,pk=pk)
        if post.Author == request.user or request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You can't see this page.")

class AuthorsAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff or request.user.is_author :
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect("account:profile")
        else:
            return redirect("account:login")


class SuperUserAccessMixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_staff :
            return super().dispatch(request,*args,**kwargs)
        else:
            raise Http404("You can't see this page.")






# import random
# class Rand():
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['number'] = random.randrange(1, 100)
#         return context
