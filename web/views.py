import random
from collections import defaultdict
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
import json
from blog.models import SubCategory, Post, Comment, HashtagNew
from contact.models import Settings, Part
from web.models import Banners


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = defaultdict(list)
        top_banners = Banners.objects.filter(state=Banners.State.TOP_BANNER)
        side_banners = list(Banners.objects.filter(state=Banners.State.SIDE_BANNER))
        posts = list(Post.objects.all().order_by('created_at'))
        most_popular = list(Post.objects.all().order_by('views').order_by('created_at')[:10])
        most_discuss = list(
            Comment.objects.filter().order_by('post').order_by('created_at').values('post').distinct()[:10])
        most_discuss = [x['post'] for x in most_discuss]
        most_discuss = list(Post.objects.filter(pk__in=most_discuss))
        for i in range(len(most_popular) - len(most_discuss)):
            most_discuss.append(most_popular[i])
        most_last = list(Comment.objects.filter().order_by('post').order_by('created_at').values('post')[:10])

        most_last = [x['post'] for x in most_last]
        most_last = list(Post.objects.filter(pk__in=most_last))
        for i in range(len(most_popular) - len(most_last)):
            most_last.append(most_popular[i])
        most_choice = list(
            Comment.objects.filter().order_by('post').order_by('created_at').values('post')[:10])
        most_choice = [x['post'] for x in most_choice]
        most_choice = list(Post.objects.filter(pk__in=most_choice))
        for i in range(len(most_popular) - len(most_choice)):
            most_choice.append(most_popular[i])
        top_banner = random.choice(top_banners)
        side_banners = random.sample(side_banners, 2)
        top_posts = random.sample(posts, 3)
        top8_posts = random.sample(posts, 8)
        for result in SubCategory.objects.values('parent__name', 'name', 'parent__id').annotate().order_by(
                'parent__name', ):
            users[result['parent__name']].append(result)
        context['model'] = dict(users)
        context['top_banner'] = top_banner
        context['side_banners'] = side_banners
        context['top3'] = top_posts
        context['top8'] = top8_posts
        context['top10popular'] = most_popular
        context['top10discuss'] = most_discuss
        context['top10choice'] = most_choice
        context['top10last'] = most_last
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
        users = defaultdict(list)
        top_banners = Banners.objects.filter(state=Banners.State.TOP_BANNER)
        side_banners = list(Banners.objects.filter(state=Banners.State.SIDE_BANNER))
        posts = list(Post.objects.all().order_by('created_at'))
        most_popular = list(Post.objects.all().order_by('views').order_by('created_at')[:10])
        most_discuss = list(
            Comment.objects.filter().order_by('post').order_by('created_at').values('post').distinct()[:10])
        most_discuss = [x['post'] for x in most_discuss]
        most_discuss = list(Post.objects.filter(pk__in=most_discuss))
        for i in range(len(most_popular) - len(most_discuss)):
            most_discuss.append(most_popular[i])
        most_last = list(Comment.objects.filter().order_by('post').order_by('created_at').values('post')[:10])

        most_last = [x['post'] for x in most_last]
        most_last = list(Post.objects.filter(pk__in=most_last))
        for i in range(len(most_popular) - len(most_last)):
            most_last.append(most_popular[i])
        most_choice = list(
            Comment.objects.filter().order_by('post').order_by('created_at').values('post')[:5])
        most_choice = [x['post'] for x in most_choice]
        most_choice = list(Post.objects.filter(pk__in=most_choice))
        for i in range(5 - len(most_choice)):
            most_choice.append(most_popular[i])
        top_banner = random.choice(top_banners)
        side_banners = random.sample(side_banners, 2)
        top_posts = random.sample(posts, 3)
        top8_posts = random.sample(posts, 8)
        for result in SubCategory.objects.values('parent__name', 'name', 'parent__id').annotate().order_by(
                'parent__name', ):
            users[result['parent__name']].append(result)
        context['model'] = dict(users)
        context['top_banner'] = top_banner
        context['side_banners'] = side_banners
        context['top3'] = top_posts
        context['top8'] = top8_posts
        context['posts'] = posts[:9]
        context['top10popular'] = most_popular
        context['top10discuss'] = most_discuss
        context['top5choice'] = most_choice
        context['top10last'] = most_last
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


class CategoryView(TemplateView):
    template_name = 'category.html'


class ShowNewsView(TemplateView):
    template_name = 'show-news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_key = self.kwargs['id']
        post = get_object_or_404(Post, id=search_key)
        hashtags = HashtagNew.objects.filter(post_id=post.id).distinct()[:5]
        relational = list(HashtagNew.objects.filter(hashtag_id__in=hashtags.values('hashtag_id')).exclude(
            post_id__in=hashtags.values('post_id'))[:3])
        offers = Post.objects.all().exclude(id=post.id).order_by('views')[:8]
        context['post'] = post
        top_banners = Banners.objects.filter(state=Banners.State.TOP_BANNER)
        side_banners = list(Banners.objects.filter(state=Banners.State.SIDE_BANNER))
        top_banner = random.choice(top_banners)
        side_banners = random.sample(side_banners, 2)
        most_popular = list(Post.objects.all().order_by('views').order_by('created_at')[:10])
        most_discuss = list(
            Comment.objects.filter().order_by('post').order_by('created_at').values('post').distinct()[:10])
        most_discuss = [x['post'] for x in most_discuss]
        most_discuss = list(Post.objects.filter(pk__in=most_discuss))
        for i in range(len(most_popular) - len(most_discuss)):
            most_discuss.append(most_popular[i])
        most_last = list(Comment.objects.filter().order_by('post').order_by('created_at').values('post')[:10])
        most_last = [x['post'] for x in most_last]
        most_last = list(Post.objects.filter(pk__in=most_last))
        for i in range(len(most_popular) - len(most_last)):
            most_last.append(most_popular[i])
        users = defaultdict(list)
        for result in SubCategory.objects.values('parent__name', 'name', 'parent__id').annotate().order_by(
                'parent__name', ):
            users[result['parent__name']].append(result)

        for i in range(3 - len(relational)):
            relational.append(most_popular[i])
        context['model'] = dict(users)
        context['top10last'] = most_last
        context['top10popular'] = most_popular
        context['top10discuss'] = most_discuss
        context['top_banner'] = top_banner
        context['side_banners'] = side_banners
        context['hashtags'] = hashtags
        context['relational'] = relational
        context['offers'] = offers
        post.views += 1
        post.save()
        return context


def send_comment(request, post_id):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        content = request.POST.get('comment')
        response_data = {}

        try:
            post = Post.objects.get(id=post_id)
            Comment(post=post, email=email, content=content, name=name).save()

        except Exception as e:
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json",
                status=400
            )

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json",
            status=200
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
