from django.conf.urls import url, include
from django.views.generic import DetailView, ListView
from blog.models import Post

urlpatterns = [url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:20],
										   template_name="blog/blog.html"), name='blog'),
				url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name='blog/post.html'), )]