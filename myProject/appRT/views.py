from django.shortcuts import render
from django.views.generic import TemplateView
from appRT.models import Post

# Create your views here.
def index(request):
	return render(request, 'appRT/home.html')

class DisplayMovieView(TemplateView):
    template_name = "appRT/details.html"

    def get_context_data(self, **kwargs):
        context = super(DisplayMovieView, self).get_context_data(**kwargs)
        context['data'] = Post.objects.get(position=self.kwargs.get('position', None))
        return context

