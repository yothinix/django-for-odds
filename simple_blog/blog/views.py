from django.views.generic import DetailView, ListView, TemplateView
from django.http import JsonResponse

from .models import Blog


class SimpleBlogView(TemplateView):
    template_name = "simple_blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        my_blog = Blog.objects.get(id=kwargs.get("blog_id"))

        context["title"] = my_blog.title
        context["content"] = my_blog.content
        context["created_by"] = my_blog.created_by
        context["created_at"] = my_blog.created

        return context


class SimpleBlogDetailView(DetailView):
    model = Blog
    pk_url_kwarg = "id"
    context_object_name = "blog"


class MultipleBlogView(ListView):
    model = Blog
    context_object_name = "blogs"


class BlogApiView(TemplateView):
    def get(self, request, *args, **kwargs):
        blog_list = []

        blogs = Blog.objects.all()
        for item in blogs:
            blog_list.append({
                'id': item.id,
                'title': item.title,
                'content': item.content
            })           

        return JsonResponse({'blogs': blog_list})
