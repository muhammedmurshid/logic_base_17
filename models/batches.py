from odoo import fields,models,api,_

class LogicBaseBatches(models.Model):
    _name = "logic.batches"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    _description = 'Batch'

    name = fields.Char(string="Name")
    coordinator_id = fields.Many2one('res.users', string="Coordinator")
    batch_code = fields.Char(string="Batch Code")
    course_id = fields.Many2one('')
