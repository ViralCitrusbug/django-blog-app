from msilib.schema import ListView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from ..mixin import LoginRequiredMixin



class IndexView(LoginRequiredMixin,TemplateView):
    template_name = 'customadmin/user-count.html'
    context = {}

    def get(self,request):
        self.context['all_users_count']=User.objects.all().exclude(is_staff=True).count()
        return render(request,self.template_name,self.context)

class UserList(ListView):
    model = User
    template_name = 'user/user-list.html'
    context_object_name = "users"
