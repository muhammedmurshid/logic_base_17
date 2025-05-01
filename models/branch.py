from odoo import models,fields,api,_


class LogicBranches(models.Model):
    _name = 'op.branch'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Branch'

    name = fields.Char(string="Branch Name", required=1)
    branch_head_id = fields.Many2one('res.users', string="Branch Head", required=1)
    active = fields.Boolean(string='Active', default=True)

    def action_archive(self):
        for record in self:
            record.active = False

    def action_unarchive(self):
        for record in self:
            record.active = True

