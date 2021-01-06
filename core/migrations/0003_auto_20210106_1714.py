# Generated by Django 3.1.5 on 2021-01-06 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210106_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('default', models.BooleanField(default=False)),
                ('width', models.FloatField(default=100)),
                ('length', models.FloatField(default=100)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.imagealbum')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model', to='core.imagealbum'),
        ),
    ]
