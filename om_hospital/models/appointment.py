from odoo import models, fields, api


class HospitalAppointment(models.Model):
    _name="hospital.appointment"
    _description = "Appointment Master"
    _rec_name = "patient_id" #this for show the name in the appointment route

    reference = fields.Char(string="Reference", default="New")
    patient_id = fields.Many2one('hospital.patient', string="patient") # make link to the patient table
    date_appointment = fields.Date(string="Appointment Date")
    note = fields.Text(string="Note")
    #23.10
    #inheriting the create method to connect the reference field with sequence
    @api.model_create_multi 
    def create(self, vals_list):
        print("odoo", vals_list)
        for vals in vals_list:
            if not vals.get('reference') or vals['reference']=='New':
                vals['reference']=self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super().create(vals_list)
