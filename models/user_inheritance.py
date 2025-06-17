from odoo import fields,models,api,_

class InheritUserDetails(models.Model):
    _inherit = 'res.users'

    # designation = fields.Char(related='employee_id.job_title', string="Designation")
    # department_id = fields.Char(related="employee_id.department_id.name", string="Department")
