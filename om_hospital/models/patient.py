from odoo import fields, models, api, _
from odoo.exceptions import UserError,ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description="Patient Master"
    _inherit = ['mail.thread'] # inherit it to use the mail system in this model

    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string="DOB", required=True, tracking=True)
    gender = fields.Selection([('male', "Male"), ('female', 'Female')], string="Gender", tracking=True)

    #this way define many2many fields in odoo
    # model name, hospital.patient and patient.tag link table(will auto generate), patient_id column, tag_id, column
    tag_ids = fields.Many2many('patient.tag', 'patient_tag_rel', 'patient_id', 'tag_id', string="Tags")




    #way 1 to show delete error
    #this way inherit the delete/unlink method
    def unlink(self):
        #here will be our logic and pass by the super
        for rec in self:
            domain = [('patient_id', '=', rec.id)]
            appointments = self.env['hospital.appointment'].search(domain)
            if appointments:
                raise UserError(_("You cann't delete the patient now. \n Appointments exist of this patient:%s"%rec.name))
        return super().unlink()
    
    #way 2 to show delete error
    # @api.ondelete(at_uninstall=False)
    # def _check_patient_appointments(self):
    #     for rec in self:
    #         domain = [('patient_id', '=', rec.id)]
    #         appointments = self.env['hospital.appointment'].search(domain)
    #         if appointments:
    #             raise UserError(_("You cann't delete the patient now. \n Appointments exist of this patient:%s"%rec.name))


