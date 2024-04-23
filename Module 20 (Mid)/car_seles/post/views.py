from django.shortcuts import render
from django.views.generic import DetailView
from . import forms
from . import models

class DetailCarView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'show_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            car = self.get_object()
            new_comment = comment_form.save(commit=False)
            new_comment.post = car
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
