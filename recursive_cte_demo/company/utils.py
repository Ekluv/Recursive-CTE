from company.models import Employee

def get_decendents_of_employee(employee_id):
    query = """
            WITH recursive children AS (
            SELECT *
            FROM company_employee where id= {0}
            UNION
            SELECT company_employee.*
            FROM company_employee, children
            WHERE company_employee.parent_id = children.id
            ) 
            select * from children
            """.format(employee_id)
    query_set = Employee.objects.raw(query)
    return list(query_set)

def get_ancestors_of_employee(employee_id):
    query = """
            WITH recursive children AS (
            SELECT id, name, parent_id
            FROM company_employee
            WHERE id = {0}
            UNION
            SELECT company_employee.id, company_employee.name, company_employee.parent_id
            FROM company_employee, children
            WHERE children.parent_id = company_employee.id
            ) select * from  children
            """.format(employee_id)

    query_set = Employee.objects.raw(query)
    return list(query_set)


def serialize_tree(employee, parent_child_map):
    employee.sub_emp = parent_child_map.get(employee.id, [])
    if not employee.sub_emp:
        return
    for emp in employee.sub_emp:
        serialize_tree(emp, parent_child_map)


def get_subtree_of_employee(employee_id):
    employees = get_decendents_of_employee(employee_id)
    parent_child_map = {}

    for employee in employees:
        # if employee.parent_id:
            if not parent_child_map.get(employee.parent_id):
                parent_child_map[employee.parent_id] = []
            parent_child_map[employee.parent_id].append(employee)
    for employee in employees:
        serialize_tree(employee, parent_child_map)
    if employees:
        return employees[0]
    else:
        None


def serialize_ancestor_tree(employee, id_object_map):
    employee.parents = id_object_map.get(employee.parent_id, [])
    if not employee.parent_id:
        return
    for emp in employee.parents:
        serialize_ancestor_tree(emp, id_object_map)


def get_ancestor_tree(employee_id):
    employees = get_ancestors_of_employee(employee_id)
    id_object_map = {}
    for employee in employees:
        id_object_map.setdefault(employee.id, [])
        id_object_map[employee.id].append(employee)

    for employee in employees:
        serialize_ancestor_tree(employee, id_object_map)
    return employees[0] if employees else None


