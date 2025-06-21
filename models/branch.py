from odoo import models,fields,api,_


class LogicBranches(models.Model):
    _name = 'op.branch'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Branch'

    name = fields.Char(string="Branch Name", required=1)
    branch_head_id = fields.Many2one('res.users', string="Branch Head", required=1)
    active = fields.Boolean(string='Active', default=True)
    state = fields.Selection([('draft','Draft'),('done','Done')], string="Status", default="draft")

    def action_archive(self):
        for record in self:
            record.active = False

    def action_unarchive(self):
        for record in self:
            record.active = True

    def act_confirm(self):
        self.state = 'done'

class EmployeeBranchInheritance(models.Model):
    _inherit = 'hr.employee'

    branch_id = fields.Many2one('op.branch', string="Branch")

