from django.shortcuts import render
from .forms import SimpleForm

# Create your views here.
def home(request):
	context = {}
	template = 'home.html'
	return render(request, template, context)

def about(request):
	form = SimpleForm(request.POST)
	if form.is_valid():
		print request.POST
	context = {'form': form}
	template = 'about.html'
	return render(request, template, context)