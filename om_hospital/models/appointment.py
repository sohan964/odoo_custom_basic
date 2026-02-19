from odoo import models, fields, api


class HospitalAppointment(models.Model):
    _name="hospital.appointment"
    _description = "Appointment Master"
    _rec_name = "patient_id" #this for show the name in the appointment

    reference = fields.Char(string="Reference", default="New")
    patient_id = fields.Many2one('hospital.patient', string="patient") # make link to the patient table
    date_appointment = fields.Date(string="Appointment Date")
    note = fields.Text(string="Note")
    #23.10
    #inheriting the create method
    @api.model_create_multi
    def create(self, vals_list):
        print("odoo", vals_list)
        return super().create(vals_list)
