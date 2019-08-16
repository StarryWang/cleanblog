import markdown2
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Aritcle, Tag, Category
from django.core.paginator import Paginator
from .forms import EmailPostForm, ArticleForm
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
	post_list = Aritcle.objects.all().order_by('-publish_data')[0:5]
	context = {'post_list': post_list, 'num': 1}
	return render(request, 'blog/index.html', context)


def page_detail(request, blog_id):
	# post = get_object_or_404(Aritcle, link=blog_link)
	post = Aritcle.objects.get(pk=blog_id)
	post.content = markdown2.markdown(post.content)
	context = {'post': post}
	return render(request, 'blog/post.html', context)


def about(request):
	return render(request, 'blog/about.html')


def sub_index(request):
	return render(request, 'blog/sub_index.html')


def contact(request):
	return render(request, 'blog/contact.html')


def blogs(request):
	# post_list = get_list_or_404(Category, name='随笔')
	# ps = get_object_or_404(Category)
	# print(post_list, ps)
	page = request.GET.get('page')
	if page:
		page = int(page)
	else:
		page = 1
	post_list = Aritcle.objects.all().order_by('-publish_data')
	# post_l = Aritcle.objects.filter(author='herber01')
	# for i in post_l:
	# print(i.title)
	paginator = Paginator(post_list, 3)
	page_num = paginator.num_pages
	curr_page_list = paginator.page(page)
	if curr_page_list.has_next():
		next_page = page + 1
	else:
		next_page = page
	if curr_page_list.has_previous():
		previous_page = page - 1
	else:
		previous_page = page
	context = {'post_list': curr_page_list, 'next_page': next_page, 'previous_page': previous_page, 'page_num': range(1, page_num + 1)}
	return render(request, 'blog/blog_index.html', context)


def post_share(request, post_id):
	post = get_object_or_404(Aritcle, id=post_id)

	sent = False
	if request.method == 'POST':
		form = EmailPostForm(request.POST)
		if form.is_valid():
			# shuju
			cd = form.cleaned_data
			send_mail(cd['name'], cd['comments'], cd['email'], ['18738627327@163.com'])
			sent = True
			print('00000')
	else:
		form = EmailPostForm()

	context = {'post': post, 'form': form, 'sent': sent}
	print('111111')
	return render(request, 'blog/blog_index.html', context)


def edit(request, blog_id):
	post = Aritcle.objects.get(pk=blog_id)
	if request.method != 'POST':
		form = ArticleForm()
	else:
		form = ArticleForm(data=request.POST)
		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.save()
			return HttpResponseRedirect(reverse('blog:post', args=[blog_id]))

	context = {'post': post}
	return render(request, 'blog/edit.html', context)
