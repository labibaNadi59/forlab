from django.db import models
from accounts.models import Parent, Hospital
from vaccination.models import Child, Vaccine

# Create your models here.

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('completed', 'Completed'),
        ('missed', 'Missed'),
        ('cancelled', 'Cancelled'),
    )
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.child.name} - {self.vaccine.name} - {self.status}"


class Rating(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    score = models.IntegerField()
    review = models.TextField(blank=True)

    def __str__(self):
        return f"{self.hospital.name} - {self.score}/5"


class Reminder(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    reminder_date = models.DateField()
    message = models.TextField()

    def __str__(self):
        return f"Reminder for {self.appointment.child.name}"
