from odoo import fields, models, api


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description="Patient Master"
    _inherit = ['mail.thread'] # inherit it to use the mail system in this model

    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string="DOB", required=True, tracking=True)
    gender = fields.Selection([('male', "Male"), ('female', 'Female')], string="Gender", tracking=True)