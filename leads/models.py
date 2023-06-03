from django.db import models

class Agent(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    is_staff = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Lead(models.Model):

    MARRIED_STATUS = (
        ('single', 'single'),
        ('married', 'married'),
        ('divorced', 'divorced'),
        ('prefer not to say', 'prefer not to say'),
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(default=0)
    state = models.CharField(max_length=100, null=True)
    marrital_status = models.CharField(max_length=50, choices=MARRIED_STATUS)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
