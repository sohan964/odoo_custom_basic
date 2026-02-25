from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = 'account.move' #inheriting account.move model

    appointment_id = fields.Many2one(
        'hospital.appointment', string="Appointment" # making FK
    )
