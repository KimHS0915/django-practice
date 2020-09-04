from django.shortcuts import render, HttpResponse, get_object_or_404

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
	post = get_object_or_404(Post, pk=pk)
	# try:
	# 	post = Post.objects.get(pk=pk)
	# except Post.DoesNotExist:
	# 	raise Http404
	return render(request, 'instagram/post_detail.html', {
		'post': post,
	})


def archives_year(request, year):
	return HttpResponse(f"{year} archives")
