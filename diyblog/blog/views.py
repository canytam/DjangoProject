from django.shortcuts import render
from .models import Author, Comment, Post

# Create your views here.
def index(request):
    num_posts = Post.objects.all().count()
    num_comments = Comment.objects.all().count()
    num_authors = Author.objects.all().count()
    context = {
        'num_posts': num_posts,
        'num_comments': num_comments,
        'num_authors': num_authors,
    }
    return render(request, 'index.html', context)

from django.views import generic

class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    
class PostDetailView(generic.DetailView):
    model = Post
    
class AuthorListView(generic.ListView):
    model = Author
 
class AuthorDetailView(generic.DetailView):
    model = Author

from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from datetime import datetime

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['message']
    
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.createTime = datetime.now()
        return super(CommentCreateView, self).form_valid(form)