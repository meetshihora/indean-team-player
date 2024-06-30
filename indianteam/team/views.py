from django.shortcuts import render
from team.models import Team
# Create your views here.
def team(request):
    teamdetail = Team.objects.all().order_by('name')
    data = {'teamdetail': teamdetail}
    return render(request, 'team.html' , data)