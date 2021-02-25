from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import TemplateView
from .models import Yogacourse
from django.http import HttpResponseRedirect


class Home(TemplateView):
    template_name = 'account/home.html'


def schedule(request):
    courses = Yogacourse.objects.all().order_by('datetime_start')
    booked = False
    for course in courses:
        if course.books.filter(id=request.user.id).exists():
            booked = True
    context = {'courses':courses, 'booked':booked}
    return render(request, 'course/schedule.html', context)

def course_detail(request, pk):
    course = Yogacourse.objects.get(id=pk)
    booked = False
    if course.books.filter(id=request.user.id).exists():
        booked = True
    context = {'course':course, 'booked':booked}
    return render(request, 'course/detail.html', context)


def BookView(request, pk):
    course = get_object_or_404(Yogacourse, 
                                id=request.POST.get('course_id'))
    booked = False
    if course.books.filter(id=request.user.id).exists():
        course.books.remove(request.user)
        booked = False
    else:
        course.books.add(request.user)
        booked = True
    return HttpResponseRedirect(
                        reverse('yogastudio:schedule'))
    #return HttpResponseRedirect(reverse('yogastudio:course_detail',args=[pk]))