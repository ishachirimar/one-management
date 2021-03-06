# Generated by Django 3.0.1 on 2020-01-03 22:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('url_name', models.CharField(max_length=25)),
                ('is_visible', models.BooleanField(default=False)),
                ('is_radio', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='BoardGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('url_name', models.CharField(max_length=25)),
                ('is_visible', models.BooleanField(default=False)),
                ('is_group', models.BooleanField(default=True)),
                ('is_radio', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='EyeColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eye_color', models.PositiveSmallIntegerField(choices=[(0, '----'), (1, 'Blue'), (2, 'Blue/Green'), (3, 'Blue/Grey'), (4, 'Green'), (5, 'Hazel'), (6, 'Brown'), (7, 'Grey'), (8, 'Green/Grey'), (9, 'Green/Brown'), (10, 'Black'), (11, 'DarkBrown')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='HairColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hair_color', models.PositiveSmallIntegerField(choices=[(0, '----'), (1, 'Blonde'), (2, 'Dark Blonde'), (3, 'Dark Brown'), (4, 'Light Brown'), (5, 'Auburn'), (6, 'Brown'), (7, 'Brunette'), (8, 'Black'), (9, 'Red'), (10, 'Silver'), (11, 'Grey'), (12, 'Light Blonde'), (13, 'Salt & Pepper'), (14, 'Strawberry Blonde'), (15, 'Light Red'), (16, 'Chestnut'), (17, 'Brown Venetian')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PersonGender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.PositiveSmallIntegerField(choices=[(0, 'MALE'), (1, 'FEMALE')])),
            ],
        ),
        migrations.CreateModel(
            name='PersonHeight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ht_feet', models.PositiveSmallIntegerField()),
                ('ht_inches', models.DecimalField(decimal_places=1, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='PersonInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('full_name', models.CharField(max_length=80)),
                ('linebreak_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('thumbnail', models.ImageField(upload_to='image/%Y/%m/%d')),
                ('instagram', models.URLField()),
                ('belongs_to_board', models.ManyToManyField(to='Person.Board')),
                ('belongs_to_board_group', models.ManyToManyField(to='Person.BoardGroup')),
                ('gender', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Person.PersonGender')),
            ],
        ),
        migrations.CreateModel(
            name='PersonSizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.PositiveSmallIntegerField(choices=[(0, 'None'), (1, '0-4'), (2, '6-12'), (3, '12 And Up')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SiteMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='SiteMenu', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='SuitSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suit_inches', models.PositiveSmallIntegerField()),
                ('suit_letter', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='VideoGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('visible', models.BooleanField(default=False)),
                ('belongs_to_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Person.PersonInformation')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.URLField()),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('belongs_to_gallery', models.ManyToManyField(to='Person.VideoGallery')),
                ('belongs_to_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Person.PersonInformation')),
            ],
        ),
        migrations.CreateModel(
            name='PictureGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('visible', models.BooleanField(default=False)),
                ('belongs_to_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Person.PersonInformation')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pictureL', models.ImageField(upload_to='image/%Y/%m/%d')),
                ('pictureR', models.ImageField(null=True, upload_to='image/%Y/%m/%d')),
                ('is_linked', models.BooleanField(default=False)),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('belongs_to_gallery', models.ManyToManyField(to='Person.PictureGallery')),
                ('belongs_to_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Person.PersonInformation')),
            ],
        ),
        migrations.AddField(
            model_name='personinformation',
            name='size_group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Person.PersonSizes'),
        ),
        migrations.CreateModel(
            name='MaleSpec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoe_size', models.DecimalField(decimal_places=1, max_digits=4)),
                ('waist', models.PositiveSmallIntegerField()),
                ('inseam', models.PositiveSmallIntegerField()),
                ('belongs_to_person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Person.PersonInformation')),
                ('eye_color', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Person.EyeColor')),
                ('hair_color', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Person.HairColor')),
                ('height', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Person.PersonHeight')),
                ('suit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Person.SuitSize')),
            ],
        ),
        migrations.CreateModel(
            name='FemaleSpec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoe_size', models.DecimalField(decimal_places=1, max_digits=4)),
                ('bust', models.PositiveSmallIntegerField()),
                ('waist', models.PositiveSmallIntegerField()),
                ('hips', models.PositiveSmallIntegerField()),
                ('belongs_to_person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Person.PersonInformation')),
                ('eye_color', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Person.EyeColor')),
                ('hair_color', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Person.HairColor')),
                ('height', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Person.PersonHeight')),
            ],
        ),
        migrations.AddField(
            model_name='boardgroup',
            name='belongs_to_menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Person.SiteMenu'),
        ),
        migrations.AddField(
            model_name='boardgroup',
            name='person_permissions',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='board',
            name='belongs_to_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Person.BoardGroup'),
        ),
        migrations.AddField(
            model_name='board',
            name='person_permissions',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='BaseLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('url_name', models.CharField(max_length=25)),
                ('is_visible', models.BooleanField(default=False)),
                ('instagram_url', models.URLField(null=True)),
                ('belongs_to_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Person.SiteMenu')),
            ],
        ),
    ]
