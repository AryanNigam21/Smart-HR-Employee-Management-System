from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import csv

@login_required
def employee_report(request):
    # Add role checks and queryset scoping before exposing real employee data.
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="employee-report.csv"'
    writer = csv.writer(response)
    writer.writerow(["Employee code", "Name", "Department", "Job title"])
    return response
