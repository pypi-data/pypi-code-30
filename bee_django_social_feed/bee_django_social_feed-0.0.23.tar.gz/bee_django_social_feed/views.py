# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from datetime import datetime, timedelta
from django.http import JsonResponse
from bee_django_social_feed.models import Feed, FeedComment, FeedEmoji, FeedImage, AlbumPhoto, Album
# from django.core.serializers import serialize
from dss.Serializer import serializer
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from bee_django_social_feed.exports import get_classmates
from bee_django_social_feed import signals
from django.db import transaction
from django.db.models import Q
from bee_django_course.utils import page_it
import pytz
# Create your views here.

user_model = get_user_model()

def index(request):

    return render(request, 'bee_django_social_feed/index.html', context={
    })


# 获取所有日志
def feeds(request):
    page = request.GET.get('page')

    # 依据type的值，判断是取所有日志，还是单个用户的日志，或者同班同学的
    type = request.GET.get('type')
    if type == '0':
        feeds = Feed.objects.order_by('-created_at')
    elif type == '1':
        user_id = request.GET.get('user_id')
        user = get_object_or_404(user_model, pk=user_id)
        feeds = Feed.objects.filter(publisher=user).order_by('-created_at')
    elif type == '2':
        user_id = request.GET.get('user_id')
        classmates = get_classmates(user_id)
        feeds = Feed.objects.filter(publisher__in=classmates).order_by('-created_at')
    else:
        feeds = Feed.objects.order_by('-created_at')

    paginator = Paginator(feeds, 10)
    try:
        data = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        data = []

    for e in data:
        e.emojis = e.feedemoji_set.all()
        for i in e.emojis:
            i.user_data = user_model.objects.values('id', 'username', 'first_name').get(pk=i.user_id)
        e.comments = e.feedcomment_set.order_by('-created_at')
        for j in e.comments:
            j.user_data = user_model.objects.values('id', 'username', 'first_name').get(pk=j.user_id)
        e.publisher_data = user_model.objects.values('id', 'username', 'first_name').get(pk=e.publisher_id)

        if e.type == 0:
            e.images = e.feedimage_set.all()
        elif e.type == 2:
            if e.album:
                e.images = e.album.albumphoto_set.all()
            else:
                e.images = []
        else:
            e.images = []

    return JsonResponse(data={
        'feeds': serializer(data, output_type='json', datetime_format='string'),
        'page': page,
        'request_user_id': request.user.id,
        'can_manage': request.user.has_perm('bee_django_social_feed.can_manage_feeds'),
    })


# 发表日志
@transaction.atomic
def create_feed(request):
    if request.method == "POST":
        # 日志每天只能发3篇
        today = timezone.now().date()
        tz = pytz.timezone('Asia/Shanghai')
        today_start = datetime(today.year, today.month, today.day, tzinfo=tz)
        today_end = today_start + timedelta(hours=24)
        feeds_of_today = Feed.objects.filter(publisher=request.user, type=0,
                                             created_at__gte=today_start, created_at__lt=today_end)
        if feeds_of_today.count() >= 3:
            return JsonResponse(data={
                'rc': -1,
                'message': '发表失败！每天只能发3篇',
                'new_feeds': []
            })

        content = request.POST.get('content')
        new_feed = Feed.objects.create(content=content, publisher=request.user)

        for i in request.FILES.getlist('files'):
            image = FeedImage.objects.create(image=i, feed=new_feed)

        feeds = [new_feed, ]
        for i in feeds:
            i.emojis = []
            i.comments = []
            i.publisher_data = user_model.objects.values('id', 'username', 'first_name').get(pk=i.publisher_id)
            i.images = i.feedimage_set.all()

        # 发送发表日志的信号
        signals.user_feed_created.send(sender=Feed, feed_id=new_feed.id)

        feeds = serializer(feeds, output_type='json', datetime_format='string')

        return JsonResponse(data={
            'rc': 0,
            'message': '发表成功',
            'new_feeds': feeds
        })


# 删除日志
def delete_feed(request, feed_id):
    feed = get_object_or_404(Feed, pk=feed_id)
    if request.method == "POST":
        if request.user.has_perm('bee_django_social_feed.can_manage_feeds') or request.user == feed.publisher:
            signals.user_feed_delete.send(sender=Feed, feed_publisher=feed.publisher, feed_type=feed.type)

            feed.delete()
            return JsonResponse(data={
                'rc': 0,
                'message': '删除成功'
            })
        else:
            return JsonResponse(data={
                'rc': -1,
                'message': '权限不足'
            })


# 删除日志评论
def delete_feed_comment(request, feed_comment_id):
    comment = get_object_or_404(FeedComment, pk=feed_comment_id)
    if request.method == "POST":
        if request.user.has_perm('bee_django_social_feed.can_manage_feeds') or request.user == comment.user:
            comment.delete()
            return JsonResponse(data={
                'rc': 0,
                'message': '删除成功'
            })
        else:
            return JsonResponse(data={
                'rc': -1,
                'message': '权限不足'
            })


# 点赞
def create_emoji(request, feed_id):
    if request.method == "POST":
        feed = get_object_or_404(Feed, pk=feed_id)

        # 检查用户是否已经点过赞了
        emojis = feed.feedemoji_set.filter(user=request.user)
        if emojis.exists():
            message = '你已经点过赞了'
            new_emoji = None
        else:
            new_emoji = feed.feedemoji_set.create(user=request.user)
            signals.user_feed_emojied.send(sender=Feed, feed_id=feed.id, emojier=request.user)
            message = '点赞成功'

        emojis = [new_emoji,]
        for i in emojis:
            i.user_data = user_model.objects.values('id', 'username', 'first_name').get(pk=i.user_id)
        return JsonResponse(data={
            'message': message,
            'new_emoji': serializer(emojis, output_type='json', datetime_format='string')
        })


# 发表对日志的评论
def create_comment(request, feed_id):
    if request.method == "POST":
        feed = get_object_or_404(Feed, pk=feed_id)

        comment_text = request.POST.get('comment')
        new_comment = feed.feedcomment_set.create(comment=comment_text, user=request.user)
        message = '评论成功'
        signals.user_feed_replied.send(sender=Feed, feed_id=feed.id, replier=request.user)

        comments = [new_comment,]
        for i in comments:
            i.user_data = user_model.objects.values('id', 'username', 'first_name').get(pk=i.user_id)
        return JsonResponse(data={
            'message': message,
            'new_comments': serializer(comments, output_type='json', datetime_format='string')
        })


# 美好的生活页面 显示所有用户的albums的页面
def albums(request):

    return render(request, 'bee_django_social_feed/albums.html', context={
        'user_id': request.user.id,
    })


# 获取albums实际数据
def get_albums(request):
    page = request.GET.get('page')
    # 自己的显示所有，别人的只显示审核通过的
    albums = Album.objects.filter((Q(status__in=[1,2])&~Q(user=request.user)) | Q(user=request.user))

    paginator = Paginator(albums, 25)
    try:
        data = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        data = []

    for e in data:
        e.cover_image = e.albumphoto_set.first().thumbnail_url
        e.user_name = e.user.first_name or e.user.username

    data_albums = serializer(data, output_type='json', datetime_format='string')

    return JsonResponse(data={
        'albums': data_albums,
        'page': page,
    })


# 获取相册详情
def album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)

    album.photos = album.albumphoto_set.all()
    album.user_name = album.user.first_name or album.user.username

    data_album = serializer(album, output_type='json', datetime_format='string')

    return JsonResponse(data={
        'album': data_album,
    })


# 创建相册
@transaction.atomic
def create_album(request):
    if request.method == "POST":
        # 每天只能发1篇
        today = timezone.now().date()
        tz = pytz.timezone('Asia/Shanghai')
        today_start = datetime(today.year, today.month, today.day, tzinfo=tz)
        today_end = today_start + timedelta(hours=24)
        count_of_today = Album.objects.filter(user=request.user,
                                             created_at__gte=today_start, created_at__lt=today_end).count()
        if count_of_today >= 1:
            return JsonResponse(data={
                'rc': -1,
                'message': '发表失败！每天只能发1篇',
                'albums': [],
            })

        file_list = request.FILES.getlist('files')
        if not file_list:
            return JsonResponse(data={
                'rc': -1,
                'albums': [],
                'message': '上传图片不能为空',
            })

        note = request.POST.get('note')
        new_album = Album.objects.create(user=request.user, note=note)

        for i in request.FILES.getlist('files'):
            image = AlbumPhoto.objects.create(image=i, album=new_album)

        # 构造其他需要的数据
        new_album.cover_image = new_album.albumphoto_set.first().thumbnail_url
        new_album.user_name = request.user.first_name or request.user.username

        new_albums = [new_album, ]
        data_albums = serializer(new_albums, output_type='json', datetime_format='string')

        return JsonResponse(data={
            'rc': 0,
            'albums': data_albums,
            'message': '上传成功',
        })


# 管理上传的美好生活
def manage_albums(request):
    type = request.GET.get('type')

    if type == 'finished':
        album_list = Album.objects.filter(~Q(status=0))
    else:
        album_list = Album.objects.filter(status=0)

    data = page_it(request, query_set=album_list)
    return render(request, 'bee_django_social_feed/manage_albums.html', context={
        'albums': data,
        'type': type,
    })


# 管理查看单个相册，并评分
@transaction.atomic
def manage_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)

    if request.method == "POST":
        level = request.POST.get('level')
        print request.POST
        if level == "1":
            album.status = 1
            message = '审核成功'
            album.create_feed()
        elif level == "2":
            album.status = 2
            message = '审核成功'
            album.create_feed()
        elif level == "3":
            album.status = 3
            message = '阻止成功'
        else:
            message = '未知评分类型'

        album.save()
        # 美好生活审核后的信号
        signals.user_album_checked.send(sender=Album, album_id=album.id)
        return JsonResponse(data={
            'message': message,
        })
    else:
        return render(request, 'bee_django_social_feed/manage_album.html', context={
            'album': album,
        })


# 修改图片的描述
def update_album_photo_note(request, album_photo_id):
    if request.method == "POST":
        album_photo = get_object_or_404(AlbumPhoto, pk=album_photo_id)
        new_note = request.POST.get('note')
        album_photo.note = new_note
        album_photo.save()

        return JsonResponse(data={
            'message': '修改成功',
        })