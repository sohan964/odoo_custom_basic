from odoo import fields, api, models

class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "Patient Tags"
    _order = 'sequence, id' #this is for the handle sequence when drac and drop tags
    

    name = fields.Char(
        string="Name", required=True
    )
    sequence = fields.Integer(default=10)

