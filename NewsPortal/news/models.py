from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        p_rat = self.post_set.aggregate(post_rating=Sum('rating'))
        post_rat = 0
        post_rat += p_rat.get('post_rating')

        c_rat = self.user.comment_set.aggregate(comment_rating=Sum('rating'))
        comment_rat = 0
        comment_rat += c_rat.get('comment_rating')
        self.rating = post_rat * 3 + comment_rat
        self.save()

    def __str__(self):
        return f'{self.user}'


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    d_time = models.DateTimeField(auto_now_add=True)
    type_post = models.CharField(max_length=3,
                              choices=[('NWS','новость'),('ART','статья')],
                              default='NWS')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    # slug = models.SlugField(max_length=128, unique=True)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[0:123]} ...'

    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, blank=True)
    d_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f'{self.text}'

#
# class New(models.Model):
#     title = models.CharField(
#         max_length=128,
#         # unique=True,
#     )
#     text = models.TextField()
#     d_time = models.DateTimeField(auto_now_add=True)
#     slug = models.SlugField(max_length=128, unique=True)
#
#     # category = models.ForeignKey(
#     #     to='Category',
#     #     on_delete=models.CASCADE,
#     #     # related_name='all_news',
#     # )
#
#     def get_absolute_url(self):
#         return reverse('detail', kwargs={'slug': self.slug})
#
#     def __str__(self):
#         # return '{}'.format(self.title)
#         return f'{self.title}'

    # class Meta:
    #     verbose_name = 'Новость'
    #     verbose_name_plural = 'Новости'

