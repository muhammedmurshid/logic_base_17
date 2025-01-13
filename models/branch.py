from odoo import models,fields,api,_


class LogicBranches(models.Model):
    _name = 'logic.branches'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Branch'

    name = fields.Char(string="Branch Name", required=1)
    branch_head_id = fields.Many2one('res.users', string="Branch Head", required=1)
