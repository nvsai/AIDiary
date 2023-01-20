from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.http import HttpResponse
from django.template import loader

from .models import Entry,Story


class LockedView(LoginRequiredMixin):
    login_url = "admin:login"


class EntryListView(LockedView, ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date_created")


class EntryDetailView(LockedView, DetailView):
    model = Entry


class EntryCreateView(LockedView, SuccessMessageMixin, CreateView):
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("entry-list")
    success_message = "Your new entry was created!"


class EntryUpdateView(LockedView, SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ["title", "content"]
    success_message = "Your entry was updated!"

    def get_success_url(self):
        return reverse_lazy("entry-detail", kwargs={"pk": self.object.pk})


class EntryDeleteView(LockedView, SuccessMessageMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    success_message = "Your entry was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

class StoryListView(LockedView, ListView):
    model = Story
    queryset = Story.objects.all().order_by("-date_created")


class StoryDetailView(LockedView, DetailView):
    model = Story


class StoryCreateView(LockedView, SuccessMessageMixin, CreateView):
    model = Story
    fields = ["title", "content"]
    success_url = reverse_lazy("story-list")
    success_message = "Your new entry was created!"


class StoryUpdateView(LockedView, SuccessMessageMixin, UpdateView):
    model = Story
    fields = ["title", "content"]
    success_message = "Your entry was updated!"

    def get_success_url(self):
        return reverse_lazy("story-detail", kwargs={"pk": self.object.pk})


class StoryDeleteView(LockedView, SuccessMessageMixin, DeleteView):
    model = Story
    success_url = reverse_lazy("story-list")
    success_message = "Your entry was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

def generatecode(request):
    template = loader.get_template('generate_code.html')
    return HttpResponse(template.render())