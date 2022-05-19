from django.shortcuts import render
import requests

# Create your views here.
def exhange(request):
	response = requests.get(url='https://api.exchangerate-api.com/v4/latest/USD').json()
	currencies = response.get('rates')

	if request.method == 'GET':

		context = {
			'currencies': currencies
		}

		return render(request, 'exhange/index.html', context=context)

	if request.method == 'POST':

		from_amount = float(request.POST.get('from_amount'))
		from_curr = request.POST.get('from_curr')
		to_curr = request.POST.get('to_curr')

		converter_amount = round((currencies[to_curr] /  currencies[from_curr]) * float(from_amount), 2)

		context = {
			'currencies': currencies,
			'converter_amount': converter_amount
		}

		return render(request, 'exhange/index.html', context=context)