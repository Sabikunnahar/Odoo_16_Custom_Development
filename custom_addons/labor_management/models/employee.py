from odoo import fields, models, api

class LaborEmployee(models.Model):
    _name = "labor.employee"  # Corrected this line to use _name instead of name

    employee_name = fields.Char(string="Employee Name")
    address = fields.Char(string="Employee Address")
    skill = fields.Char(string="Employee Skills")
    salary = fields.Char(string="Employee Salary")


    @api.model
    def create(self, employee_name, address, skill, salary):
        new_employee_create = self.create({
            'employee_name': employee_name,
            'address': address,
            'skill': skill,
            'salary': salary,
        })
        return new_employee_create

