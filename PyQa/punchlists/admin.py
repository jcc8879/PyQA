from django.contrib import admin
from punchlists.models import Issue, Browser, Reporter, OS, Punchlist, Status


class IssueAdmin(admin.ModelAdmin):
	list_display = ('reported_date', 'status', 'issue_text', 'url', 'reporter')

admin.site.register(Issue, IssueAdmin)

admin.site.register(Browser)

admin.site.register(Reporter)

admin.site.register(OS)

admin.site.register(Punchlist)

admin.site.register(Status)