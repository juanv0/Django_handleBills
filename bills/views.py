from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, View
from django.urls import reverse_lazy
import json
from .models import Image
from .forms import PostForm
from .billsRecognizer import detect_text, get_invoice_date, get_invoice_number, get_invoice_total
# Create your views here.


class HomePageView(ListView):
	model = Image
	template_name = 'home.html'


class ImageToTextView(View):
	model = Image
	form_class = PostForm
	template_name = 'post.html'
	
	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'form':form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, request.FILES)
		if form.is_valid():
			words = detect_text(request.FILES.get('cover'))
			number = get_invoice_number(words)
			total = get_invoice_total(words)
			date = get_invoice_date(words)
			response_body = {"Invoice Number": number, "Invoice Total": total, "Invoice Date": date}
			return HttpResponse(json.dumps(response_body), content_type='application/json')
			
		return render(request, self.template_name, {'form': form})


class CreatePostView(CreateView):
	model = Image
	form_class = PostForm
	template_name = 'post.html'
	success_url = reverse_lazy('home')
