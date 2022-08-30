from django.urls import path
from hello import views
from hello.models import LogMessage
from hello.views import remove

home_list_view = views.HomeListView.as_view(
    # :5 limits the results to the five most recent
    queryset=LogMessage.objects.order_by("-log_date")[:5],
    context_object_name="message_list",
    template_name="hello/home.html",
)
urlpatterns = [
    path("", home_list_view, name="home"),
    path("log/", views.log_message, name="log"),
    path("remove/<int:id>", views.remove, name='delete_object'),
]
