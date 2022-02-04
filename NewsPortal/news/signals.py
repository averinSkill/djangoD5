# D6.4
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import mail_managers

from .models import Post, Category, User


# D6.4
# created - булевая, есть или нет объект в БД
@receiver(post_save, sender=Post)
def notify_managers_appointment(sender, instance, created, **kwargs):
    if created:
        subject = f'{instance.title} {instance.d_time.strftime("%d %m %Y")}'
    else:
        subject = f'Публикация изменена {instance.title} {instance.d_time.strftime("%d %m %Y")}'

    categ = instance.category.all().values()
    # subscribers =
    print('TYPE POST', f'{instance.type_post}')
    print('КАТЕГОРИЯ', f'{categ}')
    # user = self.request.user
    # user_id = self.request.user.id
    # # sub_category - это все категории подписчика!!
    # sub_category = Category.objects.all().filter(subscribers=self.request.user.id)

    mail_managers(
        subject=subject,
        message=instance.text,
    )
    print('Опубликована новая статья: ', f'{instance.title} {instance.d_time.strftime("%d %m %Y")}')

