import requests


def verificarSite(url):
	try:
		requests.get(url)
	except:
		print("\033[31mO site está inacessível!\033[m")
	else:
		print("\033[33mO site está acessível!\033[m")
