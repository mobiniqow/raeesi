import random
from collections import defaultdict

from django.db.migrations import state
from django.db.models import Count, Q
from django.views.generic import TemplateView

from blog.models import SubCategory, Post, Comment
from contact.models import Settings, Part
from web.models import Banners


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = defaultdict(list)
        banners = Banners.objects.all()
        posts = list(Post.objects.all().order_by('created_at'))
        topposts = list(Post.objects.all().order_by('created_at'))
        random_banner = random.choice(banners)
        top_posts = random.sample(posts, 3)
        top8_posts = random.sample(topposts, 8)
        top10_posts = random.sample(topposts, 10)
        for result in SubCategory.objects.values('parent__name', 'name', 'parent__id').annotate().order_by(
                'parent__name', ):
            users[result['parent__name']].append(result)
        context['model'] = dict(users)
        context['banner'] = random_banner
        context['top3'] = top_posts
        context['top8'] = top8_posts
        context['top10popular'] = top10_posts
        # por bahs tarin ha
        context['top10discuss'] = top10_posts
        context['top10choice'] = top10_posts
        context['top10last'] = top10_posts
        top_day_news = Post.objects.order_by('views', 'created_at').last()
        top_day_views = Comment.objects.filter(post_id=top_day_news.id).count()
        context['top_day_news'] = top_day_news
        context['top_day_views'] = top_day_views
        top_top_news_with_video = Post.objects.filter(state=Post.Type.VIDEO).order_by('views', 'created_at')
        context['top_top_news_with_video'] = top_top_news_with_video
        top_top_news_with_image = Post.objects.filter(state=Post.Type.PICTURE).order_by('views', 'created_at')[:4]
        context['top_top_news_with_image'] = top_top_news_with_image
        settings = Settings.objects.first()
        context['settings'] = settings
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parts'] = Part.objects.all()
        return context


class AboutUsView(TemplateView):
    template_name = 'about-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parts'] = Part.objects.all()
        settings = Settings.objects.first()
        context['settings'] = settings
        return context


class SearchView(TemplateView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        if 'value' in self.kwargs:
            search_key = self.kwargs['value']
            posts = posts.filter(Q(title__contains=search_key))
        context['posts'] = posts
        settings = Settings.objects.first()
        context['settings'] = settings
        return context


class CategoryView(TemplateView):
    template_name = 'category.html'


class ShowNewsView(TemplateView):
    template_name = 'show-news.html'
