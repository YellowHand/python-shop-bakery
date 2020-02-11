from .models import Client


def menu_links(request):
	links = Client.objects.all()
	return dict(links=links)