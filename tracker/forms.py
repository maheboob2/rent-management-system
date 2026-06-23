from django.forms import ModelForm
from .models import tenant,payment

class tenantform(ModelForm):

    class Meta:
        model=tenant
        fields=['name','phone','monthly_rent','join_date','is_active']

class paymentform(ModelForm):

    class Meta:
        model=payment
        fields=['tenant','month','amount','status','paid_date']
