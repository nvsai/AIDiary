from django.urls import path

from . import views

urlpatterns = [
    path("", views.EntryListView.as_view(), name="entry-list"),
    path(
        "entry/<int:pk>", views.EntryDetailView.as_view(), name="entry-detail"
    ),
    path("create", views.EntryCreateView.as_view(), name="entry-create"),
    path(
        "entry/<int:pk>/update",
        views.EntryUpdateView.as_view(),
        name="entry-update",
    ),
    path(
        "entry/<int:pk>/delete",
        views.EntryDeleteView.as_view(),
        name="entry-delete",
    ),
    path("stories", views.StoryListView.as_view(), name="story-list"),
    path(
        "story/<int:pk>", views.StoryDetailView.as_view(), name="story-detail"
    ),
    path("create-story", views.StoryCreateView.as_view(), name="story-create"),
    path(
        "story/<int:pk>/update",
        views.StoryUpdateView.as_view(),
        name="story-update",
    ),
    path(
        "story/<int:pk>/delete",
        views.StoryDeleteView.as_view(),
        name="story-delete",
    ),
    path("code",views.generatecode,name="generate-code"),
]
