from django.db import models
import os

# Create your models here.


# def user_directory_path(instance, filename):
#     ext = filename.split('.').pop()
#     filename = '{0}{1}.{2}'.format(instance.p_name, instance.identity_card, ext)
#     return os.path.join(instance.major.name, filename)

class page_info(models.Model):

    page_status = [
        (0, 'off'),
        (1, 'on')
    ]

    page_types = [
        (0, '未分类'),
        (1, '账号管理'),
        (2, '开发类'),
        (3, '运维类')
    ]

    # p_id = models.IntegerField(verbose_name="主键", auto_created=True, primary_key=True, editable=False)
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(verbose_name="页面名称", max_length=10, blank=False, null=False)
    p_desc = models.CharField(verbose_name="页面描述", max_length=100, blank=False, null=False)
    p_img = models.ImageField(verbose_name="图片路径", upload_to='nb/ico/%Y/%m/%d/', blank=False, null=False)
    p_src = models.CharField(verbose_name="页面链接", max_length=100, blank=False, null=False)
    p_gov = models.CharField(verbose_name="官网地址", max_length=100, blank=False, null=False, default="官网地址")
    p_gov_src = models.CharField(verbose_name="官网链接", max_length=100, blank=False, null=False)
    p_doc = models.CharField(verbose_name="帮助文档", max_length=100, blank=True, null=True)
    p_doc_src = models.CharField(verbose_name="官方文档链接", max_length=100, blank=True, null=True)
    p_stats = models.IntegerField(verbose_name="页面状态", choices=page_status, default=0)
    p_types = models.IntegerField(verbose_name="页面类别", choices=page_types, default=0)

    def __str__(self):
        return self.p_name

    class Meta:
        verbose_name = "页面信息"
        verbose_name_plural = "页面信息"



