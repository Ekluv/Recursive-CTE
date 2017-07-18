from django.db import models

from cte_tree.models import CTENode


# Create your models here.

class Employee(CTENode):
    """
    inherit from CTENode
    this was an expirement using 3rd party package for CTE queries but doesnt work
    CTENode gives an extra field `parent` which is self referential foreignkey 
    like this parent =  models.ForeignKey('self', blank=True, null=True, related_name='children')
    """
    name = models.CharField(max_length=254)
    joining_date = models.DateField()
    age = models.PositiveIntegerField()
    birthdate = models.DateField()
    address = models.TextField()
    designation = models.CharField(max_length=254)

    def __str__(self):
        return '%s' % (self.name)
