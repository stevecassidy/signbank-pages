# -*- coding: utf-8 -*-
"""
URLs for pages.
"""
from django.urls import path
from .views import AttachmentView

app_name = 'pages'

urlpatterns = [
    path('attachments', AttachmentView.as_view())
]


# urlpatterns = patterns('',

#     (r'^$', 'django.views.generic.list_detail.object_list',
#        {'queryset': Attachment.objects.all(),
#         'template_name': 'list.html',
#        }, "attachments"),
#     (r'^upload/', 'signbank.attachments.views.upload_file'),
# )