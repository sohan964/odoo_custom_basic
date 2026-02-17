from odoo import fields, models

class CollegeStudent(models.Model):
    _name = "college.student" # this is the model(table) name
    _description = "College Student"

    #attributes/fields of the model
    admission_no = fields.Char(string="Admission No", required=True)
    admission_date = fields.Date(string="Admission Date", required=True)
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    father_name = fields.Char(string="Father's Name", required=True)
    mother_name = fields.Char(string="Mother's Name", required=True)
    communication_address = fields.Text(string="Communication Address", required=True)
    same_as_communication = fields.Boolean(string="Same as Communication", default=True)
    image_1920 = fields.Image(string="Student Image")

    # copyed from the res.bank model
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one('res.country.state', 'Fed. State', domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country')
    country_code = fields.Char(related='country_id.code', string='Country Code')
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")