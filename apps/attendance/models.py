from django.conf import settings
from django.db import models
from django.utils import timezone

class AttendanceRecord(models.Model):
    class Status(models.TextChoices):
        PRESENT = "PRESENT", "Present"
        ABSENT = "ABSENT", "Absent"
        HALF_DAY = "HALF_DAY", "Half day"
        LEAVE = "LEAVE", "Leave"
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="attendance_records")
    work_date = models.DateField(default=timezone.localdate)
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PRESENT)
    class Meta:
        constraints = [models.UniqueConstraint(fields=["employee", "work_date"], name="unique_employee_attendance_day")]
        ordering = ["-work_date"]
