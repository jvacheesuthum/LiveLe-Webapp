from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from .models import Current, Slides, Votes
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

@login_required
def index(request):
    try:
	current = Current.objects.get(owner = request.user)
    except Current.DoesNotExist:
	current = Current(owner = request.user, slide_name = 'first', page = 1)
	current.save()
    return HttpResponseRedirect(reverse('slides:lecture'))

@login_required
def lecturer(request):
    return HttpResponseRedirect(reverse('slides:lecture', args=[1]))

@login_required
def student(request):
    return HttpResponseRedirect(reverse('slides:lecture', args=[0]))

@login_required
def lecture(request):
    current = get_object_or_404(Current, owner = request.user)
    '''
    qs = Slides.objects.filter(slide_text=current.slide_name)
    qs = qs.filter(page = current.page)
    slide = qs.reverse()[:1]
    return render(request, 'slides/index.html', {'slide': slide})
    '''
    try:
	current_slide = Slides.objects.get(slide_text = current.slide_name, page= current.page)
    except Slides.DoesNotExist:
	return HttpResponseNotFound()
    canVote = Current.objects.get(owner = current_slide.lecturer, slide_name = current_slide.slide_text).page >= current.page
    if(canVote and request.user.groups.filter(name = 'Student').count() == 1):
        try:
            myvote = Votes.objects.get(user = request.user, slide = current_slide)
        except Votes.DoesNotExist:
            v = Votes(user = request.user, slide = current_slide, value = 0)
            v.save()

    good = Votes.objects.filter(slide = current_slide, value = 0).count()
    bad = Votes.objects.filter(slide = current_slide, value = 1).count()
    total = good + bad
    if (total == 0):
	total = 1
	good = 1
    if(request.user.groups.filter(name = 'Lecturer').count() == 1):
        return render(request, 'slides/lecture.html', {'slide':current_slide, 'lecturer':True, 'votes_amplified':bad *100 / total, 'votes_rest': good*100/total})
    else:
        return render(request, 'slides/lecture.html', {'slide':current_slide, 'student':True, 'votes_amplified':bad*100/total, 'votes_rest': good*100/ total})

@login_required
def next_page(request):
    current = get_object_or_404(Current, owner = request.user)
    try:
        slide = Slides.objects.get(page = current.page + 1)
        current.page += 1
        current.save()
    except Slides.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('slides:lecture'))

@login_required
def prev_page(request):
    current = get_object_or_404(Current, owner = request.user)
    try:
        slide = Slides.objects.get(page = current.page - 1)
        current.page -= 1
        current.save()
    except Slides.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('slides:lecture'))

@login_required
def curr_page(request):
    mycurr = get_object_or_404(Current, owner = request.user)
    lecturer = Slides.objects.get(slide_text = mycurr.slide_name, page=1).lecturer
    try:
	lecture_curr = Current.objects.get(slide_name = mycurr.slide_name, owner = lecturer)
	mycurr.page = lecture_curr.page
	mycurr.save()
    except Slides.DoesNotExist:
        return HttpResponseNotFound()
    return HttpResponseRedirect(reverse('slides:lecture'))

@login_required
def vote_up(request):
    current = get_object_or_404(Current, owner = request.user)
    '''
    qs = Slides.objects.filter(slide_text=current.slide_name)
    qs = qs.filter(page = current.page)
    slide = qs.reverse()[:1]
    return render(request, 'slides/index.html', {'slide': slide})
    '''
    current_slide = Slides.objects.get(slide_text = current.slide_name, page= current.page)

    if (Current.objects.get(owner = current_slide.lecturer, slide_name = current_slide.slide_text).page >= current.page):
	try:
	    v = Votes.objects.get(user = request.user, slide = current_slide)
	    v.value = 0
	    v.save()
	except Votes.DoesNotExist:
	    v = Votes(user = request.user, slide = current_slide, value = 0)
	    v.save()
    else:
	pass
    return HttpResponseRedirect(reverse('slides:lecture'))

@login_required
def vote_down(request):
    current = get_object_or_404(Current, owner = request.user)
    '''
    qs = Slides.objects.filter(slide_text=current.slide_name)
    qs = qs.filter(page = current.page)
    slide = qs.reverse()[:1]
    return render(request, 'slides/index.html', {'slide': slide})
    '''
    current_slide = Slides.objects.get(slide_text = current.slide_name, page= current.page)

    if (Current.objects.get(owner = current_slide.lecturer, slide_name = current_slide.slide_text).page >= current.page):
	try:
	    v = Votes.objects.get(user = request.user, slide = current_slide)
	    v.value = 1
	    v.save()
	except Votes.DoesNotExist:
	    v = Votes(user = request.user, slide = current_slide, value = 1)
	    v.save()
    else:
	pass
    return HttpResponseRedirect(reverse('slides:lecture'))

'''
@login_required
def home(request):
    return HttpResponseRedirect(reverse('slides:index', args=[request.user.username]))
'''
def login(request):
    return HttpResponseRedirect('/login/')

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')