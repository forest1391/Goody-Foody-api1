# Generated by Django 4.0.5 on 2022-09-30 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('chat_id', models.IntegerField(primary_key=True, serialize=False)),
                ('account', models.CharField(max_length=50)),
                ('b_account', models.IntegerField()),
                ('content', models.TextField()),
                ('time', models.TimeField()),
            ],
            options={
                'db_table': 'chat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ChatPhoto',
            fields=[
                ('chat_photo_id', models.IntegerField(primary_key=True, serialize=False)),
                ('account', models.CharField(max_length=50)),
                ('b_account', models.IntegerField()),
                ('photo_subname', models.CharField(max_length=50)),
                ('time', models.TimeField()),
            ],
            options={
                'db_table': 'chat_photo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dietitian',
            fields=[
                ('account', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=50)),
                ('license_id', models.CharField(max_length=50)),
                ('resume', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dietitian',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Eating',
            fields=[
                ('eat_id', models.IntegerField(primary_key=True, serialize=False)),
                ('account', models.CharField(max_length=50)),
                ('menu_id', models.IntegerField()),
                ('eat_type_id', models.IntegerField()),
                ('date', models.DateField()),
                ('kcal', models.IntegerField()),
                ('carbohydrate', models.FloatField(blank=True, null=True)),
                ('protein', models.FloatField(blank=True, null=True)),
                ('fat', models.FloatField(blank=True, null=True)),
                ('sodium', models.FloatField(blank=True, null=True)),
                ('dietary_fiber', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'eating',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EatType',
            fields=[
                ('eat_type_id', models.IntegerField(primary_key=True, serialize=False)),
                ('eat_type', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'eat_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('kcal', models.IntegerField()),
                ('carbohydrate', models.FloatField(blank=True, null=True)),
                ('protein', models.FloatField(blank=True, null=True)),
                ('fat', models.FloatField(blank=True, null=True)),
                ('sodium', models.FloatField(blank=True, null=True)),
                ('dietary_fiber', models.FloatField(blank=True, null=True)),
                ('edit_dietitian_id', models.CharField(max_length=50)),
                ('last_rank', models.IntegerField()),
                ('subname', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MenuTag',
            fields=[
                ('menu_id', models.IntegerField(primary_key=True, serialize=False)),
                ('tag_id', models.IntegerField()),
            ],
            options={
                'db_table': 'menu_tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MenuThumbs',
            fields=[
                ('menu_id', models.IntegerField(primary_key=True, serialize=False)),
                ('account', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'menu_thumbs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.IntegerField(primary_key=True, serialize=False)),
                ('account', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True, null=True)),
                ('post_time', models.DateField()),
            ],
            options={
                'db_table': 'post',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PostMsg',
            fields=[
                ('post_msg_id', models.IntegerField(primary_key=True, serialize=False)),
                ('account', models.CharField(max_length=50)),
                ('post_id', models.IntegerField()),
                ('content', models.TextField()),
                ('time', models.TimeField()),
            ],
            options={
                'db_table': 'post_msg',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PostMsgThumbs',
            fields=[
                ('account', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('post_msg_id', models.IntegerField()),
            ],
            options={
                'db_table': 'post_msg_thumbs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PostPhoto',
            fields=[
                ('post_photo_id', models.IntegerField(primary_key=True, serialize=False)),
                ('post_id', models.IntegerField()),
                ('photo_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'post_photo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('post_id', models.IntegerField(primary_key=True, serialize=False)),
                ('tag_id', models.IntegerField()),
            ],
            options={
                'db_table': 'post_tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PostThumbs',
            fields=[
                ('post_id', models.IntegerField(primary_key=True, serialize=False)),
                ('account', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'post_thumbs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('rank_id', models.IntegerField(primary_key=True, serialize=False)),
                ('rank_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'rank',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.IntegerField(primary_key=True, serialize=False)),
                ('account', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('time', models.DateField()),
                ('report_type_id', models.IntegerField()),
                ('object_id', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'report',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReportMsg',
            fields=[
                ('report_msg_id', models.IntegerField(primary_key=True, serialize=False)),
                ('report_id', models.IntegerField()),
                ('account', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('time', models.DateField()),
            ],
            options={
                'db_table': 'report_msg',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReportPhoto',
            fields=[
                ('report_photo_id', models.IntegerField(primary_key=True, serialize=False)),
                ('report_id', models.IntegerField()),
                ('photo_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'report_photo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReportType',
            fields=[
                ('report_type_id', models.IntegerField(primary_key=True, serialize=False)),
                ('report_type', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'report_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('restaurant_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('business_hours', models.TextField(blank=True, null=True)),
                ('resume', models.TextField(blank=True, null=True)),
                ('license_id', models.CharField(blank=True, max_length=50, null=True)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
            options={
                'db_table': 'restaurant',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RestaurantMsg',
            fields=[
                ('restaurant_msg_id', models.IntegerField(primary_key=True, serialize=False)),
                ('restaurant_id', models.IntegerField()),
                ('account', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True, null=True)),
                ('time', models.DateField()),
            ],
            options={
                'db_table': 'restaurant_msg',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RestaurantMsgThumbs',
            fields=[
                ('restaurant_msg_id', models.IntegerField(primary_key=True, serialize=False)),
                ('account', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'restaurant_msg_thumbs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RestaurantPhoto',
            fields=[
                ('restaurant_photo_id', models.IntegerField(primary_key=True, serialize=False)),
                ('restaurant_id', models.IntegerField()),
                ('photo_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'restaurant_photo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RestaurantTag',
            fields=[
                ('restaurant_id', models.IntegerField(primary_key=True, serialize=False)),
                ('tag_id', models.IntegerField()),
            ],
            options={
                'db_table': 'restaurant_tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('tag_id', models.IntegerField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(max_length=50)),
                ('tag_type_id', models.IntegerField()),
            ],
            options={
                'db_table': 'tags',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TagType',
            fields=[
                ('tag_type_id', models.IntegerField(primary_key=True, serialize=False)),
                ('tag_type', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tag_type',
                'managed': False,
            },
        ),
    ]
