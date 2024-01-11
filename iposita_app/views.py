from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import LocalPackage
from .forms import LocalPackageForm
from django.db.models import Sum
import csv


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

class PackageListView(LoginRequiredMixin, ListView):
    model = LocalPackage
    template_name = 'local_parcel.html'
    context_object_name = 'packages'
    # paginate_by = 3  # Pagination over-write

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['packages'] = context['packages'].filter(user=self.request.user)
    
    #     search_input = self.request.GET.get('search-area') or ''
    #     if search_input:
    #         context['packages'] = context['packages'].filter(
    #             sender_name__contains=search_input)

    #     context['search_input'] = search_input

    #     return context


class AddLocalPackageView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    model = LocalPackage
    form_class = LocalPackageForm
    template_name = 'add_item.html'
    success_message = "Package was added successfully"
    success_url = reverse_lazy('local')

@login_required
def index(request):
    packages = LocalPackage.objects.all()
    total_packages = LocalPackage.objects.all().count()
    total_packages_weight = LocalPackage.objects.aggregate(total=Sum('package_weight'))['total']
    total_packages_price = sum([package.package_price for package in packages])
    context = {
        'packages':packages,
        'total_packages':total_packages,
        'total_packages_weight':total_packages_weight,
        'total_packages_price':total_packages_price
    }
    return render(request, 'index.html', context)

@login_required
def detail(request):
    return render(request, 'detail.html', {})

@login_required
def export_packages(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['sender_name', 'sender_email', 'sender_address', 'sender_phone_number', 'recipient_name', 'recipient_email', 'recipient_address', 'recipient_phone_number', 'package_type', 'package_destination', 'package_weight', 'tracking_number', 'branch', 'is_exception', 'content'])

    for package in LocalPackage.objects.all().values_list('sender_name', 'sender_email', 'sender_address', 'sender_phone_number', 'recipient_name', 'recipient_email', 'recipient_address', 'recipient_phone_number', 'package_type', 'package_destination', 'package_weight', 'tracking_number', 'branch', 'is_exception', 'content'):
        writer.writerow(package)

    response['Content-Disposition'] = 'attachment; filename="packages.csv"'

    return response

