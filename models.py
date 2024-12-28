from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_lenght=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

class PetOwner(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField()
    owner = models.ForeignKey(PetOwner, on_delete=models.CASCADE, related_name='pets')

class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="appointments")
    status = models.CharField(max_length=20, default='pending')

class MedicaRecord(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE,related_name='medical_record')
    symptoms = models.TextField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
