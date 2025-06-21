from odoo import fields,models, _, api

class InheritBranches(models.TransientModel):
    _inherit = 'enrollment.batch.wizard'

    branch_id = fields.Many2one('op.branch', string="Branch")


