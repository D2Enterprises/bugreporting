from django.shortcuts import render, redirect
from .models import BugReport
from .forms import BugReportForm

def bug_report_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'bugs/bug_report_list.html', {'bugs': bugs})

def bug_report_detail(request, pk):
    bug = BugReport.objects.get(pk=pk)
    return render(request, 'bugs/bug_report_detail.html', {'bug': bug})

def bug_report_create(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bug_report_list')
    else:
        form = BugReportForm()
    return render(request, 'bugs/bug_report_form.html', {'form': form})