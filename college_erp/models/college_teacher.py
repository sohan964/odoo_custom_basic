from odoo import fields, models

class CollegeTeacher(models.Model):
    _name = "college.teacher"
    _description = "College Teacher"

    # attributes/fields
    teacher_name = fields.Char(string="Teacher Name")
    teacher_code = fields.Char(string="Teacher Code")
    image_1920 = fields.Image(string="Teacher Image")
    teacher_email = fields.Char(string="Teacher Email")
    teacher_phone = fields.Char(string="Teacher Phone")
    
    teacher_joining_date = fields.Date(string="Joining Date")

    # teacher Permanate
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one('res.country.state', 'Fed. State', domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country')
    country_code = fields.Char(related='country_id.code', string='Country Code')

