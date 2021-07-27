from django.shortcuts import render, HttpResponse
from .models import page_info
from .tasks import req_page_stats
from collections import defaultdict         # 模板无法识别defaultdict 需要转换为普通的dict

# Create your views here.


def index(request):
    pi = page_info.objects.all()
    info = defaultdict(list)
    for p in pi:
        info[p.get_p_types_display()].append(p)
    return render(request, "nb/index.html", {'info': dict(info)})


def index_update(request):
    req_page_stats()
    pi = page_info.objects.all()
    info = defaultdict(list)
    for p in pi:
        info[p.get_p_types_display()].append(p)
    return render(request, "nb/index.html", {'info': dict(info)})