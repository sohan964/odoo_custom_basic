from odoo import models, fields, api


class HospitalAppointment(models.Model):
    _name="hospital.appointment"
    _description = "Appointment Master"
    _inherit = ['mail.thread']
    _rec_name = "patient_id" #this for show the name in the appointment route
    _rec_names_search = ['reference', 'patient_id'] #this one help to search by the field name added

    reference = fields.Char(string="Reference", default="New") #ondelete restrict about delete the person
    patient_id = fields.Many2one('hospital.patient', string="patient", ondelete="restrict") # make link(fk) to the patient table and hold 1 value 
    date_appointment = fields.Date(string="Appointment Date")
    date_of_birth = fields.Date(string="DOB", related="patient_id.date_of_birth")
    note = fields.Text(string="Note")
    #state for process
    state = fields.Selection([
        ('draft', 'Draft'), 
        ('confirmed','Confirmed'),
        ('ongoing', 'Ongoing'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], default="draft", tracking=True)

    #create One2many field
    appointment_line_ids = fields.One2many('hospital.appointment.line', 'appointment_id', string="Lines")
    #compute method creation
    total_qty = fields.Float(compute='_compute_total_qty', string="Total Quantity", store=True) #store means the field will store in the db

    #23.10
    #inheriting the create method to connect the reference field with sequence
    @api.model_create_multi # it will generate the sequence number of appointment
    def create(self, vals_list):
        print("odoo", vals_list)
        for vals in vals_list:
            if not vals.get('reference') or vals['reference']=='New':
                vals['reference']=self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super().create(vals_list)
    
    #methon that will calculate total qty
    @api.depends('appointment_line_ids')
    def _compute_total_qty(self):
        for rec in self:
            #manual sum
            # total_qty = 0
            # for line in rec.appointment_line_ids:
            #     total_qty = total_qty + line.qty
            rec.total_qty = sum(rec.appointment_line_ids.mapped('qty'))
    
    def action_confirm(self):
        for rec in self:
            rec.state='confirmed'

    def action_ongoing(self):
        for rec in self:
            rec.state='ongoing'
    
    def action_done(self):
        for rec in self:
            rec.state = 'done'
    
    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def _compute_display_name(self): #this function will show the display name with reference
        for rec in self:
            rec.display_name = f"[{rec.reference}] {rec.patient_id.name}"


#part of odoo17 no 6 video
class HospitalAppointmentLine(models.Model):
    _name="hospital.appointment.line"
    _description = "Appointment Master Line"

    appointment_id = fields.Many2one("hospital.appointment",string="Appointment Line")
    product_id = fields.Many2one("product.product", string="products", required=True)
    qty = fields.Float(string="Quantity")
