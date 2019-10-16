import requests
from django.shortcuts import render
from .models import Info

def index(request):
	appid = ''              # айдишник для доступа к API
	url = 'https://'+appid  # URL дающий инфу от сервера, не забыть вставить конструкцию q={}

	url_info = Info.objects.all() # вся инфа из URL

	all_info = [] # здесь будет лежать инфа полученная из URL

	for info in url_info:

		res = requests.get(url.format(info.name)).json()

		server_info = {		# список информации, которую нужно достать из URL, обозначено условно
			'inf': info.name,
			'1': res["inf_1"],
			'2': res["inf_2"],
			'3': res["inf_3"]
		}
		all_info.append(server_info)
	
	context = {'all_info':all_info}	#контекст для html

	return render(request, 'requester/index.html', context)