from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
# from datetime import datetime
from datetime import timedelta
from datetime import date, timezone


# from dateutil.relativedelta import relativedelta

class ClassMaster(models.Model):
    _name = 'op.class'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    _description = 'Class'

    active = fields.Boolean(default=True)
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company.id)
    date = fields.Date(string="Date", index=True)
    batch_id = fields.Many2one('op.batch', string="Batch", required=1)
    # line_base_ids = fields.One2many('student.base.lines', 'class_base_id', string='Students')
    name = fields.Char(string="Class", index=True, required=1)
    code = fields.Char(string="Code", index=True)
    note = fields.Text(string='Notes')
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('inactive', 'Inactive'),
        ('active', 'Active')], default='draft')
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    coordinator_id = fields.Many2one('res.users', string="Academic Coordinator",)
    approve_id = fields.Many2one('res.users', string="Approved By", default=lambda self: self.env.user.id, readonly="1",
                                 tracking=True)
    # tutor_id = fields.Many2one('res.users', string="Faculty",domain=[('faculty_check','=',True)])
    # student_id = fields.Many2one('res.partner', string="Student")
    total_seats = fields.Integer(string="Total Seats")
    available_seats = fields.Integer(string="Available Seats", readonly="1")
    create_date = fields.Datetime(string="Create Date", tracking=True, default=date.today())

    @api.onchange('batch_id')
    def _onchange_batch_owner(self):
        if self.batch_id:
            if self.batch_id.initiated_id:
                self.coordinator_id = self.batch_id.initiated_id.id

