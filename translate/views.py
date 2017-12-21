from django.shortcuts import render
from .forms import TestTranslateForm
from googletrans import Translator
from django.http import JsonResponse
from .models import TestTranslate
from django.template.loader import render_to_string

def home(request):
	form = TestTranslateForm(request.POST or None)

	translator = Translator(service_urls=[
      'translate.google.com',]
      )

	if form.is_valid():
		instance = form.save(commit=False)
		trans = form.cleaned_data['text']	
		lang = form.cleaned_data['language']	
		try:
			transe = translator.translate(trans,dest=lang)
			laste_data = transe.text
			data = {'laste':laste_data}
			return JsonResponse(data)
		except:
			laste_data = 'somthing whent wrong try auther alnguage.'
	else:
		laste_data = 'no data please insert some data'

	context = {
	"form":form,
		'translated_data':laste_data,
	}
	return render(request,"index.html",context)


