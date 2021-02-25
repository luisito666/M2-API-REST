from django.db import models
from django.utils import timezone
from django.conf import settings

# Utils Timezone
from datetime import datetime, timedelta

# Translation
from django.utils.translation import gettext_lazy as _

# From local base models and managers
from ..base import (
    AbstractBaseAccount
)

# Local Manager
from .manager import AccountManager


class AbstractAccount(AbstractBaseAccount):
    login = models.CharField(unique=True, max_length=30)
    real_name = models.CharField(max_length=16)
    social_id = models.CharField(max_length=7, blank=True, null=True)
    email = models.CharField(max_length=64)
    phone1 = models.CharField(max_length=16, blank=True, null=True)
    phone2 = models.CharField(max_length=16, blank=True, null=True)
    zipcode = models.CharField(max_length=7)
    create_time = models.DateTimeField(default=timezone.now)
    question1 = models.CharField(max_length=48, blank=True, null=True)
    answer1 = models.CharField(max_length=48, blank=True, null=True)
    question2 = models.CharField(max_length=48, blank=True, null=True)
    answer2 = models.CharField(max_length=48, blank=True, null=True)
    is_testor = models.IntegerField(default=0)
    securitycode = models.CharField(max_length=192)
    newsletter = models.IntegerField(default=0)
    empire = models.IntegerField(default=0)
    name_checked = models.IntegerField(default=0)
    mileage = models.IntegerField(default=0)
    cash = models.IntegerField(default=0)
    coins = models.IntegerField(default=0)
    yenibirim = models.IntegerField(db_column='yeniBirim', default=0)  # Field name made lowercase.
    gold_expire = models.DateTimeField(default=settings.BUFFSTUF)
    silver_expire = models.DateTimeField(default=settings.BUFFSTUF)
    safebox_expire = models.DateTimeField(default=settings.BUFFSTUF)
    autoloot_expire = models.DateTimeField(default=settings.BUFFSTUF)
    fish_mind_expire = models.DateTimeField(default=settings.BUFFSTUF)
    marriage_fast_expire = models.DateTimeField(default=settings.BUFFSTUF)
    money_drop_rate_expire = models.DateTimeField(default=settings.BUFFSTUF)
    ttl_cash = models.IntegerField(default=0)
    ttl_mileage = models.IntegerField(default=0)
    channel_company = models.CharField(max_length=30, default='')
    last_play = models.DateTimeField(blank=True, null=True)
    usersession = models.CharField(max_length=32, blank=True, null=True)
    ban_reason = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255)
    email_onay = models.CharField(max_length=255)
    web_ip = models.CharField(max_length=15, blank=True, null=True)
    tel_onay = models.CharField(max_length=16)
    kod_sure = models.CharField(max_length=255)
    mail_degisim = models.CharField(max_length=255)
    email_kod = models.CharField(max_length=255)
    web_aktiviert = models.CharField(max_length=32, blank=True, null=True)
    web_admin = models.CharField(max_length=32)
    jcoins = models.IntegerField(default=0)
    deletion_token = models.CharField(max_length=40)
    passlost_token = models.CharField(max_length=40)
    email_token = models.CharField(max_length=40)
    new_email = models.CharField(max_length=64)

    objects = AccountManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['real_name', 'social_id', 'email']

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.login}'


class Account(AbstractAccount):
    """
        You can add more options to account
    """

    class Meta:
        """
            This are a legacy model and no need migrations.
        """
        managed = False
        db_table = 'account'
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')
