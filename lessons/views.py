from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView
from django.core.paginator import Paginator


def lessons(request):
    lessons = Articles.objects.all()
    paginatior = Paginator(lessons, 4)
    page = request.GET.get('page')
    lessons = paginatior.get_page(page)
    return render(request, 'lessons/lessons.html', {'lessons': lessons})


class LessonDetailView(DetailView):
    model = Articles
    template_name = 'lessons/detail_view_les.html'
    context_object_name = 'lesson'