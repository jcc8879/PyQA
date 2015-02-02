from django.db import models

# Create your models here.
class Punchlist(models.Model):
	punchlist_name = models.CharField(max_length=200)
	punchlist_date = models.DateTimeField('date created')
	
	def __str__(self):
		return self.punchlist_name

	def get_incomplete_issues(self):
		return self.issue_set.exclude(status_id=4)

	def get_complete_issues(self):
		return self.issue_set.filter(status_id=4)

class Reporter(models.Model):
	reporter_name = models.CharField(max_length=200)

	def __str__(self):
		return self.reporter_name

class Browser(models.Model):
	browser_name = models.CharField(max_length=200)
	browser_ver  = models.CharField(max_length=200)
	def __str__(self):
		return self.browser_name

class OS(models.Model):
	os_name = models.CharField(max_length=200)
	def __str__(self):
		return self.os_name

class Status(models.Model):
	status_text = models.CharField(max_length=200)

	def __str__(self):
		return self.status_text

class Issue(models.Model):
	punchlist 		= models.ForeignKey(Punchlist)
	reporter 		= models.ForeignKey(Reporter)
	browser 		= models.ForeignKey(Browser)
	os 				= models.ForeignKey(OS)
	status			= models.ForeignKey(Status)
	reported_date 	= models.DateTimeField('date published')
	url 			= models.CharField(max_length=500)
	issue_text 		= models.CharField(max_length=5000)
	#notes 			= models.CharField(max_length=5000, blank=True)

	def __str__(self):
		return self.issue_text

	def get_latest_note(self):
		return self.notes_set.latest('note_date')

class Notes(models.Model):
	issue = models.ForeignKey(Issue)
	note  = models.CharField(max_length=5000)
	note_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.note

