from django.db import models

TYPE_CHOICES = [('warning', 'Warning'), ('notice', 'Notice')]
OPTIONAL_CHOICES = [('default', 'Default'), ('all-pages', 'All Pages')]

# Create your models here.
class GlobalMessage(models.Model):
  title = models.CharField(max_length=100, blank=True, default='')
  message = models.TextField(max_length=1000, blank=True, default='')
  type = models.CharField(choices=TYPE_CHOICES, default='warning', max_length=100)
  optional = models.CharField(choices=OPTIONAL_CHOICES, default='default', max_length=100)
  all_tenants = models.BooleanField(default=True)
  hub_international = models.BooleanField(default=False)
  inova = models.BooleanField(default=False)
  insurance_hunter = models.BooleanField(default=False)
  pc_insurance = models.BooleanField(default=False)
  smart_coverage = models.BooleanField(default=False)
  
  def __str__(self):
        return self.title
