# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    account = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)
    rank = models.ForeignKey('Rank', models.DO_NOTHING)
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'account'


class Chat(models.Model):
    chat_id = models.IntegerField(primary_key=True)
    account = models.CharField(max_length=50)
    b_account = models.IntegerField()
    content = models.TextField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'chat'


class ChatPhoto(models.Model):
    chat_photo_id = models.IntegerField(primary_key=True)
    account = models.CharField(max_length=50)
    b_account = models.IntegerField()
    photo_subname = models.CharField(max_length=50)
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'chat_photo'


class Dietitian(models.Model):
    account = models.CharField(primary_key=True, max_length=50)
    real_name = models.CharField(max_length=50)
    license_id = models.CharField(max_length=50)
    resume = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dietitian'


class EatType(models.Model):
    eat_type_id = models.IntegerField(primary_key=True)
    eat_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'eat_type'


class Eating(models.Model):
    eat_id = models.IntegerField(primary_key=True)
    account = models.CharField(max_length=50)
    menu_id = models.IntegerField()
    eat_type_id = models.IntegerField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'eating'


class Menu(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    restaurant = models.ForeignKey('Restaurant', models.DO_NOTHING)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    kcal = models.IntegerField()
    carbohydrate = models.FloatField(blank=True, null=True)
    protein = models.FloatField(blank=True, null=True)
    fat = models.FloatField(blank=True, null=True)
    sodium = models.FloatField(blank=True, null=True)
    dietary_fiber = models.FloatField(blank=True, null=True)
    edit_dietitian_id = models.CharField(max_length=50)
    last_rank = models.IntegerField()
    subname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'menu'


class MenuTag(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    tag_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'menu_tag'
        unique_together = (('menu_id', 'tag_id'),)


class MenuThumbs(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    account = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'menu_thumbs'
        unique_together = (('menu_id', 'account'),)


class Post(models.Model):
    post_id = models.IntegerField(primary_key=True)
    account = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    post_time = models.DateField()

    class Meta:
        managed = False
        db_table = 'post'


class PostMsg(models.Model):
    post_msg_id = models.IntegerField(primary_key=True)
    account = models.CharField(max_length=50)
    post_id = models.IntegerField()
    content = models.TextField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'post_msg'


class PostMsgThumbs(models.Model):
    account = models.CharField(primary_key=True, max_length=50)
    post_msg_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'post_msg_thumbs'
        unique_together = (('account', 'post_msg_id'),)


class PostPhoto(models.Model):
    post_photo_id = models.IntegerField(primary_key=True)
    post_id = models.IntegerField()
    photo_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post_photo'


class PostTag(models.Model):
    post_id = models.IntegerField(primary_key=True)
    tag_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'post_tag'
        unique_together = (('post_id', 'tag_id'),)


class PostThumbs(models.Model):
    post_id = models.IntegerField(primary_key=True)
    account = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'post_thumbs'
        unique_together = (('post_id', 'account'),)


class Rank(models.Model):
    rank_id = models.IntegerField(primary_key=True)
    rank_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rank'


class Report(models.Model):
    report_id = models.IntegerField(primary_key=True)
    account = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.TextField()
    time = models.DateField()
    report_type_id = models.IntegerField()
    object_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'report'


class ReportMsg(models.Model):
    report_msg_id = models.IntegerField(primary_key=True)
    report_id = models.IntegerField()
    account = models.CharField(max_length=50)
    content = models.TextField()
    time = models.DateField()

    class Meta:
        managed = False
        db_table = 'report_msg'


class ReportPhoto(models.Model):
    report_photo_id = models.IntegerField(primary_key=True)
    report_id = models.IntegerField()
    photo_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'report_photo'


class ReportType(models.Model):
    report_type_id = models.IntegerField(primary_key=True)
    report_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'report_type'


class Restaurant(models.Model):
    restaurant_id = models.IntegerField(primary_key=True)
    account = models.ForeignKey(Account, models.DO_NOTHING, db_column='account')
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True, null=True)
    business_hours = models.TextField(blank=True, null=True)
    resume = models.TextField(blank=True, null=True)
    license_id = models.CharField(max_length=50, blank=True, null=True)
    lat = models.FloatField()
    lon = models.FloatField()

    class Meta:
        managed = False
        db_table = 'restaurant'


# primary_key=True,
class RestaurantMsg(models.Model):
    restaurant_msg_id = models.IntegerField(primary_key=True)
    restaurant_id = models.IntegerField()
    account = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    time = models.DateField()

    class Meta:
        managed = False
        db_table = 'restaurant_msg'


class RestaurantMsgThumbs(models.Model):
    restaurant_msg_id = models.IntegerField(primary_key=True)
    account = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'restaurant_msg_thumbs'
        unique_together = (('restaurant_msg_id', 'account'),)


class RestaurantPhoto(models.Model):
    restaurant_photo_id = models.IntegerField(primary_key=True)
    restaurant_id = models.IntegerField()
    photo_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'restaurant_photo'


class RestaurantTag(models.Model):
    restaurant_id = models.IntegerField(primary_key=True)
    tag_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'restaurant_tag'
        unique_together = (('restaurant_id', 'tag_id'),)


class TagType(models.Model):
    tag_type_id = models.IntegerField(primary_key=True)
    tag_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tag_type'


class Tags(models.Model):
    tag_id = models.IntegerField(primary_key=True)
    tag_name = models.CharField(max_length=50)
    tag_type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tags'
