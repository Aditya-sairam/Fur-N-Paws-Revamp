from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from .models import DogWalkerDetails
from .forms import DogWalkerDetailsForm
from .decorators import user_is_entry_author
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from urllib.parse import quote_plus

#imports for adding comments
from django.contrib.contenttypes.models import ContentType
from comments.models import Comment
from comments.forms import CommentForm
from django.http import HttpResponse, HttpResponseRedirect, Http404


@login_required
def dog_walker_details_entry_view(request):
	template_name = "DogWalker/dog_walker_details.html"
	form = DogWalkerDetailsForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		form = DogWalkerDetailsForm()
	context = {"form":form}
	return render(request,template_name,context)


def dog_walkers_list_view(request):
	qs_list = DogWalkerDetails.objects.all()
	#if request.user.is_authenticated:
	#	my_qs = DogWalkerDetails.objects.filter(Name=request.user)
	#	qs_list = (my_qs | qs_list).distinct()
	template_name = "DogWalker/card_test.html"

	paginator = Paginator(qs_list, 8)

	page = request.GET.get('page')
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		qs = paginator.page(1)
	except EmptyPage:
		qs = paginator.page(paginator.num_pages)
	context = {"object_list": qs}
	return render(request, template_name, context)
