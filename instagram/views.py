from django.shortcuts import render, HttpResponse

from .models import Post

# Create your views here.
def post_list(request):
	qs = Post.objects.all()
	q = request.GET.get('q', '')
	if q:
		qs = qs.filter(message__icontains=q)
	return render(request, 'instagram/post_list.html', {
		'post_list': qs,
		'q': q,
	})


def post_detail(request, pk):
	response = HttpResponse()
	response.write("Hello World, ")
	response.write("Hello Python, ")
	response.write("Hello Django")
	return response