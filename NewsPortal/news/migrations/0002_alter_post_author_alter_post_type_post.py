# Generated by Django 4.0 on 2022-01-12 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='type_post',
            field=models.CharField(choices=[('NWS', 'новость'), ('ART', 'статья')], default='NWS', max_length=3, verbose_name='Вид публикации'),
        ),
    ]
