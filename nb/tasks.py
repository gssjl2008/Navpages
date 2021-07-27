from celery import shared_task
from nb.models import page_info
import requests
from requests.adapters import HTTPAdapter

# 关闭警告提示
#  WARNING/ForkPoolWorker-8] /Users/wuxing/pyenvs/nb_pages/lib/python3.8/site-packages/urllib3/connectionpool.py:1013: InsecureRequestWarning: Unverified HTTPS request is being made to host '192.168.50.101'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
#   warnings.warn(
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

@shared_task
def req_page_stats():
    pi = page_info.objects.all()
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=0))  # 设置重试次数为0次
    s.mount('https://', HTTPAdapter(max_retries=0))
    for p in pi:
        try:
            resp = s.get(p.p_src, timeout=3, verify=False)                  # verfiy 跳过验证
            # print("resp status code: ", resp.status_code, p.p_src)
            stats = resp.status_code
            if str(stats)[0] in ("2", "3"):
                p.p_stats = 1
            else:
                p.p_stats = 0
        except requests.exceptions.ConnectionError:
            p.p_stats = 0
        p.save()
