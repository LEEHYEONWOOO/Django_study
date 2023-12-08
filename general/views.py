from django.core.exceptions import ImproperlyConfigured
from django.db.models import Count, Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy

from general.forms import GeneralInfoUpdateForm, OfficeUpdateForm
from general.models import GeneralInfo, Office, Employee, Car
from seoulsoft.lib import CustomUpdateView, CustomListView, CustomCreateView, erp_log_fn
from seoulsoft.val import management_json_key, init_emp_status
from general.forms import OfficeCreateForm


# from general.forms import GeneralInfoUpdateForm


class ViewCompanyManagement(CustomUpdateView):
    success_url = reverse_lazy('view_company_management')
    permission_required_get = 'general.view_general'
    permission_required_post = 'general.change_general'

    template_name = 'view_company_management.html'
    form_class = GeneralInfoUpdateForm
    model = GeneralInfo

    def has_permission(self):
        if self.request.method == 'GET':
            self.permission_required = self.permission_required_get
        else:
            self.permission_required = self.permission_required_post
        return super().has_permission()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        formdata = GeneralInfoUpdateForm
        context['formdata'] = formdata

        return context

    def get_object(self, queryset=None):
        obj, flag = GeneralInfo.objects.get_or_create(pk=1)
        return obj

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     dic = {}
    #
    #     return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        return redirect(self.success_url)


class ViewOfficeInfo(CustomListView):
    permission_required = ''
    model = Office
    template_name = 'view_office_info.html'


class AddOfficeInfo(CustomCreateView):
    permission_required = ''
    form_class = OfficeCreateForm
    template_name = 'add_office_info.html'
    success_url = reverse_lazy('view_office_info')


class ChangeOfficeInfo(CustomUpdateView):
    permission_required = ''
    model = Office
    form_class = OfficeUpdateForm
    template_name = 'change_office_info.html'
    success_url = reverse_lazy('view_office_info')

    # def get_success_url(self):
    #     return self.success_url

    def form_valid(self, form):
        erp_log_fn(self.request, self.__str__() + "_success")
        self.success_url = form.save()
        return HttpResponseRedirect(self.get_success_url())



class ViewEmpInfo(CustomListView):
    permission_required = ''
    model = Employee
    template_name = 'view_emp_info.html'
