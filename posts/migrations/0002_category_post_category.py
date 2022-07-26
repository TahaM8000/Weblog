# Generated by Django 4.0.6 on 2022-07-24 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='تیتر')),
                ('slug', models.SlugField(max_length=40, unique=True, verbose_name='آدرس')),
                ('Cover', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='تصویر')),
                ('status', models.CharField(choices=[('a', 'Active'), ('d', 'Deactive')], max_length=1, verbose_name='وضعیت')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='Category',
            field=models.ManyToManyField(related_name='posts', to='posts.category', verbose_name='دسته بندی'),
        ),
    ]
