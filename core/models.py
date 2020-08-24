from django.db import models
from django.contrib.postgres.search import SearchVectorField
import uuid
import datetime



def timestamp_now():
    return datetime.datetime.now()

class Sellers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    created_at = models.DateTimeField(default=timestamp_now())
    updated_at = models.DateTimeField(default=timestamp_now())
    is_manufacturer = models.BooleanField(default=False)
    portifolio_size = models.IntegerField(null=True)
    search_vector = SearchVectorField(null=True)
    plan_type = models.CharField(max_length=16, null=True)
    signup_origin = models.CharField(max_length=16, null=True)
    about = models.TextField(max_length=255, null=True)
    brand = models.CharField(max_length=16, null=True)
    payment_blocked_reason = models.CharField(max_length=16, null=True)
    payment_blocked = models.BooleanField(default=False)
    ie = models.CharField(max_length=16, null=True)
    features = models.CharField(max_length=16, null=True)
    crt = models.CharField(max_length=16, null=True)
    certificate_url = models.CharField(max_length=16, null=True)
    paused = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)
    origin = models.CharField(max_length=16, null=True)
    iugu_account_id = models.CharField(max_length=16, null=True)
    company_name = models.CharField(max_length=16, null=True)
    cnpj = models.CharField(max_length=11, null=True)
    mobile_phone = models.CharField(max_length=16, null=True)
    olist_responsible = models.CharField(max_length=16, null=True)
    has_withdraw_rejection = models.BooleanField(default=False)
    blocked_reason = models.CharField(max_length=16, null=True)
    last_blocked_on = models.DateField(null=True)
    branded_stores = models.CharField(max_length=16, null=True)
    owner_id = models.UUIDField(null=True)
    invoice_initial_number = models.IntegerField(null=True)
    business_type = models.CharField(max_length=16, null=True)
    invoice_default_serial_number = models.IntegerField(max_length=16, null=True)
    invite_id = models.UUIDField(null=True)
    account_executive_id = models.UUIDField(null=True)
    phone = models.CharField(max_length=16, null=True)
    logo_url = models.CharField(max_length=16, null=True)
    terms_of_use_version = models.IntegerField(null=True)
    status = models.CharField(max_length=16, null=True)




