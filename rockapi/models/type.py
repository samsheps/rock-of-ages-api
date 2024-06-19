from django.db import models

# This is the model that we will interact with, and it has 
# a 1-1 relationship with the user model that lives inside Django.

# with django, we don't specify the ID field when we're modeling the database
# the name of our field is "label"; from the models package
# it's a character field/varchar, and that character length max is 155 characters 
# we then need to import this into our dunder init (__init__.py) to ensure it's part of the models package
class Type(models.Model):
    label = models.CharField(max_length=155)