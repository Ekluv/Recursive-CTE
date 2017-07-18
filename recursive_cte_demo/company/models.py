from django.db import models

from cte_tree.models import CTENode


# Create your models here.

class Employee(CTENode):

    name = models.CharField(max_length=254)
    joining_date = models.DateField()
    age = models.PositiveIntegerField()
    birthdate = models.DateField()
    address = models.TextField()
    designation = models.CharField(max_length=254)
    # parent =  models.ForeignKey('self', blank=True, null=True, related_name='children'),
    # _cte_node_parent = 'manager'

    def __str__(self):
        return '%s' % (self.name)



# WITH recursive children AS (
#   SELECT id, name
#   FROM company_employee
#   UNION
#   SELECT company_employee.id, company_employee.name
#   FROM company_employee, children
#   WHERE company_employee.parent_id = children.id
# ) select id from TABLE company_employee where id=3;