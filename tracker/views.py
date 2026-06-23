from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from .forms import tenantform,paymentform
from .models import tenant,payment
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from datetime import datetime
from .forms import tenantform

# Create your views here.


@login_required
def tenant_form(request):
     
    if request.method=="POST":
         form=tenantform(request.POST)

         if form.is_valid():
               form.save()
         return redirect("tenant_list")   
          
    else:
         form=tenantform()

    return render(request,"tracker/tenantadd.html",{'form':form})

@login_required
def tenant_list(request):
      tenantlist=tenant.objects.all()

      # search/filter
      search=request.GET.get("search")
      if search:
            tenantlist=tenantlist.filter(
                  name__icontains=search
            )

      # pagination
      paginator = Paginator(tenantlist, 7)
      page_number = request.GET.get("page")
      page_obj = paginator.get_page(page_number)

      context={
            'tenantlist':tenantlist,
            'page_obj':page_obj
      }

      return render(request,"tracker/tenantList.html",context)

def tenant_edit(request,id):
     Tenant= get_object_or_404(tenant,id=id)

     if request.method =="POST":
          form=tenantform(request.POST,instance=Tenant)

          if form.is_valid():
               form.save()
               return redirect("tenant_list")
          
     else:
               form=tenantform(instance=Tenant)

     return render(request,"tracker/tenantedit.html",{"form":form})


def tenant_delete(request,id):
      Tenant_obj=get_object_or_404(tenant,id=id)
      
      if request.method=="POST":
            Tenant_obj.delete()

            return redirect("tenant_list")
      
      return render(request,"tracker/tenantdelete.html",{"tenant":Tenant_obj})


def payment_form(request):
     if request.method=="POST":
            form=paymentform(request.POST)

            if form.is_valid():
                  form.save()

     else:
           form=paymentform()

     return render(request,"tracker/paymentsform.html",{'form':form}) 

@login_required
def payment_list(request):
      months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}
      tenantlist=tenant.objects.all()

      total_expected=tenantlist.aggregate(total=Sum('monthly_rent'))['total'] or 0

      month=request.GET.get("month")
      year=request.GET.get("year")


      paymentlist=payment.objects.all()

      collected_amount=paymentlist.filter(status='paid').aggregate(total=Sum('amount'))['total'] or 0
      

      heading="all payments"

      if month and year:

            paymentlist=paymentlist.filter(
                  paid_date__month=month,
                  paid_date__year=year
            )
           
            heading = f"{months[int(month)]} {year} Payments"
            
      current_year=datetime.now().year   

      #search

      search=request.GET.get("search")
      if search:
            paymentlist=paymentlist.filter(
                  tenant__name__icontains=search
            )

      # pagination

      paginator = Paginator(paymentlist, 7)
      page_number = request.GET.get("page")
      page_obj = paginator.get_page(page_number)
     
   
   
      context={
            'paymentlist':paymentlist,
            'collected_amount':collected_amount,
            'total_expected':total_expected,
            'current_year':current_year,
            'heading':heading,
            'page_obj': page_obj
           
            
      }
         

      return render(request,"tracker/paymentlist.html",context)

def payment_edit(request,id):

    payment_obj=get_object_or_404(payment,id=id)

    if request.method=="POST":
          form=paymentform(request.POST,instance=payment_obj)

          if form.is_valid():
               form.save()

               return redirect("payment_list")
    else:
          form=paymentform(instance=payment_obj)

    return render(request,"tracker/paymentedit.html",{"form":form})     

def payment_delete(request,id):
      payment_obj=get_object_or_404(payment,id=id)

      if request.method=="POST":
            payment_obj.delete()

            return redirect("payment_list")

      return render(request,"tracker/paymentdelete.html",{"payment":payment_obj})

def home(request):

      return render(request,"tracker/home.html")

@login_required
def dashboard(request):

      tenantlist=tenant.objects.all()
      is_active=tenant.objects.filter(is_active=True).count()

      paymentlist=payment.objects.all()
      amount=payment.objects.filter(status='paid').aggregate(total=Sum('amount'))['total'] or 0
      unpaid=payment.objects.filter(status='unpaid').count()
     
      pending_payments=payment.objects.filter(status='pending')

      # search
      search=request.GET.get("search")
      if search:
            tenantlist=tenantlist.filter(
                    name__icontains=search
            )

            paymentlist=paymentlist.filter(
                  tenant__name__icontains=search
            )
      last_payment=paymentlist.order_by('-id')[:6]

      # calculating pending dues
      pending_dues=[]

      tenants=tenant.objects.all()
      
      for tenant_list in tenants:
            total_paid=payment.objects.filter(tenant=tenant_list).aggregate(total=Sum('amount'))['total'] or 0
            pending=tenant_list.monthly_rent-total_paid
            

            if pending>0:

                  pending_dues.append({
                        'name':tenant_list.name,
                        'due':pending
                  })

      context={

            'names':tenantlist,
            'count':tenantlist.count(),
            'is_active':is_active,
            'last_payment':last_payment,
            'paymentlist':paymentlist,
            'amount':amount,
            'unpaid':unpaid,
            'pending_payments':pending_payments,
            'pending_due': pending_dues

      }
      

      return render(request,"tracker/dashboard.html",context)

      

      


         

