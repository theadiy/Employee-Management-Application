from django.db import models

# Create your models here.
class Employee:
    def __init__(self, id, ename, email_id, joining_date, location):
        self.id = id
        self.ename = ename
        self.email_id = email_id
        self.joining_date = joining_date
        self.location = location

    
    
