# -*- coding: utf-8 -*-
"""
Database models for pages.
"""

from __future__ import absolute_import, unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group


class Page(models.Model):
    """
    A page of content for the site.
    """

    url = models.CharField(_('URL'), max_length=100, db_index=True)
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('content'), blank=True)
    template_name = models.CharField(_('template name'), max_length=70, blank=True,
                                        help_text=_("Example: 'pages/contact_page.html'. If this isn't provided, the system will use 'pages/default.html'."))
    publish = models.BooleanField(_('publish'), help_text=_("If this is checked, the page will be included in the site menus."))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, help_text=_("Leave blank for a top level menu entry.  Top level entries that have sub-pages should be empty as they will not be linked in the menu."))
    index = models.IntegerField(_('ordering index'), default=0, help_text=_('Used to order pages in the menu'))
    group_required = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, help_text=_("This page will only be visible to members of this group, leave blank to allow anyone to access."))

    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')
        ordering = ('url', 'index')

    def get_absolute_url(self):
        """
        Return the URL for this page
        """
        return self.url

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        return "%s -- %s" % (self.url, self.title)
