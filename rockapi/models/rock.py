from django.db import models
from django.contrib.auth.models import User

# this model is a bit more sophisticated than type bc we have some foreign keys
# the first is the built-in django user table that we get out of the box. we don't touch or see it but we get to work with it
# we've imported this above ("User")
# we have a foreign key to that bc as the users are adding new rocks to the client collection, 
## we have to assign that particular user to that rock 
# for a related name, we have 'collection'; for every user, there will be a property on it called "collection"
## and that will be a list of all of the rocks that are owned by that user 
# we have another foreign key called "Type". this is as the users in the client choose the dropdown for the type of rock it is.
# then a name of the rock
# then a weight in kilograms. this is a decimal field so we're saying five maxiumum characters with two decimal places

class Rock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collection')
    type = models.ForeignKey("Type", on_delete=models.CASCADE, related_name='rocks')
    name = models.CharField(max_length=155)
    weight = models.DecimalField(max_digits=5, decimal_places=2)