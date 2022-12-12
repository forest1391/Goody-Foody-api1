# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
from django.core.serializers import serialize


class Account(models.Model):
    account = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100)
    rank = models.ForeignKey('Rank', models.DO_NOTHING)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'account'


class AccountPhoto(models.Model):
    account_photo_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, models.DO_NOTHING, db_column='account')
    photo_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_photo'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
        # , db_column='account'
    account = models.ForeignKey(Account, models.DO_NOTHING)
    b_account = models.CharField(max_length=100)
    content = models.TextField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'chat'


class ChatPhoto(models.Model):
    chat_photo_id = models.AutoField(primary_key=True)
    account = models.CharField(max_length=100)
    b_account = models.IntegerField()
    photo_subname = models.CharField(max_length=100)
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'chat_photo'


class Dietitian(models.Model):
    account = models.CharField(primary_key=True, max_length=100)
    real_name = models.CharField(max_length=100)
    license_id = models.CharField(max_length=100)
    resume = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dietitian'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EatType(models.Model):
    eat_type_id = models.IntegerField(primary_key=True)
    eat_type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'eat_type'


class Eating(models.Model):
    eat_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, models.DO_NOTHING, db_column='account')
    menu_id = models.IntegerField(blank=True, null=True)
    eat_type_id = models.IntegerField()
    date = models.DateField()
    kcal = models.IntegerField(blank=True, null=True)
    carbohydrate = models.FloatField(blank=True, null=True)
    protein = models.FloatField(blank=True, null=True)
    fat = models.FloatField(blank=True, null=True)
    sodium = models.FloatField(blank=True, null=True)
    dietary_fiber = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eating'


class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    restaurant_id = models.IntegerField()
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    kcal = models.IntegerField(blank=True, null=True)
    carbohydrate = models.FloatField(blank=True, null=True)
    protein = models.FloatField(blank=True, null=True)
    fat = models.FloatField(blank=True, null=True)
    sodium = models.FloatField(blank=True, null=True)
    dietary_fiber = models.FloatField(blank=True, null=True)
    edit_dietitian_id = models.CharField(max_length=100, blank=True, null=True)
    last_rank = models.CharField(max_length=100, blank=True, null=True)
    subname = models.CharField(max_length=100, blank=True, null=True)

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
    account = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'menu_thumbs'
        unique_together = (('menu_id', 'account'),)


# class Newtable(models.Model):
#     test = models.AutoField()
#     test1 = models.CharField(max_length=-1)
#
#     class Meta:
#         managed = False
#         db_table = 'newtable'


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, models.DO_NOTHING, db_column='account')
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    post_time = models.DateField(blank=True, null=True)
    post_photo = models.CharField(max_length=100, blank=True, null=True)
    tag = models.ForeignKey('Tags', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'


class PostMsg(models.Model):
    post_msg_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, models.DO_NOTHING, db_column='account')
    post = models.ForeignKey(Post, models.DO_NOTHING)
    content = models.TextField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'post_msg'


class PostMsgThumbs(models.Model):
    account = models.CharField(primary_key=True, max_length=100)
    post_msg_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'post_msg_thumbs'
        unique_together = (('account', 'post_msg_id'),)


class PostPhoto(models.Model):
    post_photo_id = models.IntegerField(primary_key=True)
    post_id = models.IntegerField()
    photo_name = models.CharField(max_length=200, blank=True, null=True)

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
    account = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'post_thumbs'
        unique_together = (('post_id', 'account'),)


class Rank(models.Model):
    rank_id = models.IntegerField(primary_key=True)
    rank_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'rank'


class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, models.DO_NOTHING, db_column='account')
    title = models.CharField(max_length=100)
    content = models.TextField()
    time = models.DateField()
    report_type_id = models.IntegerField(blank=True, null=True)
    object_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report'


class ReportMsg(models.Model):
    report_msg_id = models.IntegerField(primary_key=True)
    report_id = models.IntegerField()
    account = models.CharField(max_length=100)
    content = models.TextField()
    time = models.DateField()

    class Meta:
        managed = False
        db_table = 'report_msg'


class ReportPhoto(models.Model):
    report_photo_id = models.IntegerField(primary_key=True)
    report_id = models.IntegerField()
    photo_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'report_photo'


class ReportType(models.Model):
    report_type_id = models.IntegerField(primary_key=True)
    report_type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'report_type'


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, models.DO_NOTHING, db_column='account')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True, null=True)
    business_hours = models.TextField(blank=True, null=True)
    resume = models.TextField(blank=True, null=True)
    license_id = models.CharField(max_length=100, blank=True, null=True)
    lat = models.FloatField(max_length=100, blank=True, null=True)
    lon = models.FloatField(max_length=100, blank=True, null=True)
    tag = models.ForeignKey('Tags', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurant'


class RestaurantMsg(models.Model):
    restaurant_msg_id = models.AutoField(primary_key=True)
    restaurant_id = models.IntegerField()
    account = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurant_msg'


class RestaurantMsgThumbs(models.Model):
    restaurant_msg_id = models.IntegerField(primary_key=True)
    account = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'restaurant_msg_thumbs'
        unique_together = (('restaurant_msg_id', 'account'),)


class RestaurantPhoto(models.Model):
    restaurant_photo_id = models.IntegerField(primary_key=True)
    restaurant_id = models.IntegerField()
    photo_name = models.CharField(max_length=100)
    restaurant_image = models.ImageField(null=True, blank=True, upload_to="images/")

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
    tag_type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tag_type'


class Tags(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=100)
    tag_type_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'

class LocView(models.Model):
    restaurant_id = models.IntegerField(blank=True, null=True)
    account = models.CharField(max_length=100, blank=True, null=False, primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    business_hours = models.TextField(blank=True, null=True)
    resume = models.TextField(blank=True, null=True)
    license_id = models.CharField(max_length=100, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'loc_view'