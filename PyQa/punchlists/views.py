from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext, loader
from punchlists.models import Punchlist, Issue, Browser, OS, Reporter, Status, Notes
from datetime import datetime
from django.core.urlresolvers import reverse

def index(request):
	#Output a list of punchlists with links to view that lists issues
	latest_punchlist_list = Punchlist.objects.order_by('-punchlist_date')

	template = loader.get_template('punchlists/index.html')

	context = {'latest_punchlist_list': latest_punchlist_list}

	return render(request, 'punchlists/index.html', context)
	

def issues(request, punchlist_id):
	punchlist 	= get_object_or_404(Punchlist, pk=punchlist_id)
	browsers  	= Browser.objects.all()
	oses  		= OS.objects.all()
	reporters  	= Reporter.objects.all()

	return render(request, 'punchlists/issues.html', {'punchlist': punchlist, 'browsers': browsers, 'reporters': reporters, 'oses': oses})

def reportissue(request, punchlist_id):
	#get the punchlist they are adding the issue to
	p 			= get_object_or_404(Punchlist, pk=punchlist_id)
	reporter 	= Reporter.objects.get(pk=request.POST['reporter_id'])
	os 			= OS.objects.get(pk=request.POST['os_id'])
	browser 	= Browser.objects.get(pk=request.POST['browser_id'])
	status 		= Status.objects.get(pk=1) #mark them all as new

	reported_date 	= datetime.now()
	url 			= request.POST['url']
	issue_text 		= request.POST['issue_text']
	notes 			= request.POST['notes']

	#add the issue
	newissue = p.issue_set.create(reporter=reporter,browser=browser,os=os,status=status,reported_date=reported_date,url=url,issue_text=issue_text)

	#add the notes if they put any in
	if notes:
		note = newissue.notes_set.create(note=notes)

	#send them back to the list of issues on the punchlist
	return HttpResponseRedirect(reverse('punchlists:issues', args=(p.id,)))

def question_issue(request, punchlist_id, issue_id):
	return HttpResponse("Ok you're sending over a question for this issue:  %s." % issue_id)

def set_issue_to_review(request, punchlist_id, issue_id):
	# Update the issue and set the status to "Ready for Review"
	issue_for_review = Issue.objects.get(pk=issue_id)

	review_status = Status.objects.get(status_text="Ready for Review")

	issue_for_review.status = review_status
	issue_for_review.save()

	return HttpResponseRedirect(reverse('punchlists:issues', args=(punchlist_id,)))

def set_issue_as_complete(request, punchlist_id, issue_id):
	# Update the issue and set the status to "Complete"
	issue_for_completion = Issue.objects.get(pk=issue_id)

	complete_status = Status.objects.get(status_text="Complete")

	issue_for_completion.status = complete_status
	issue_for_completion.save()

	return HttpResponseRedirect(reverse('punchlists:issues', args=(punchlist_id,)))

def set_issue_as_new(request, punchlist_id, issue_id):
	return HttpResponse("Ok you're marking this issue as new (taking it's setting off basically):  %s." % issue_id)

def add_note(request, punchlist_id, issue_id):
	notes 			= request.POST['notes']
	issue_for_note  = Issue.objects.get(pk=issue_id)

	if notes:
		note = issue_for_note.notes_set.create(note=notes)

	response = "200"

	return HttpResponse(response)

def delete_issue(request, punchlist_id, issue_id):
	issue_for_deletion = Issue.objects.get(pk=issue_id)

	issue_for_deletion.delete()

	return HttpResponseRedirect(reverse('punchlists:issues', args=(punchlist_id,)))
