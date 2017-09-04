from django import forms
from django.contrib import admin
from .models import Page
from django.utils.translation import ugettext_lazy as _
from django_summernote.admin import SummernoteModelAdmin


class PageForm(forms.ModelForm):
    url = forms.RegexField(label=_("URL"), max_length=100, regex=r'^[-\w/]+$',
        help_text = _("Example: '/about/contact/'. Make sure to have leading"
                      " and trailing slashes."),
        error_message = _("This value must contain only letters, numbers,"
                          " underscores, dashes or slashes."))

    class Meta:
        model = Page
        exclude = []

class PageAdmin(SummernoteModelAdmin):
    form = PageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'parent', 'index', 'publish', 'content' )}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('group_required', 'template_name')}),
    )
    list_display = ('url', 'title', 'parent', 'index')
    list_filter = ('publish', 'group_required')
    search_fields = ('url', 'title')

admin.site.register(Page, PageAdmin)


