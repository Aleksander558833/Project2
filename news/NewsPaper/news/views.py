from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from  django.urls import reverse_lazy
from .models import Post
from .filters import PostFilter
from .forms import PostForm

class PostList(ListView):
    model = Post
    # ordering = 'category'
    template_name = 'News.html'
    context_object_name = 'news'
    ordering = '-time_in'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'Post'

class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'

    def from_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user.author

        if 'news/create' in self.request.path:
            post.field = 'NE'
        else:
            post.field = 'AR'
        return super().form_valid(form)

class NewsUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'

class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')

class ArticleCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'article_create.html'

class ArticleUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'article_create.html'

class ArticleDelete(DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('post_list')




