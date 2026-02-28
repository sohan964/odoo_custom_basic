from odoo import models, fields


class MiniPartner(models.Model):
    _name = "mini.partner"
    _description = "Mini Contact"

    # Basic info
    name = fields.Char(required=True)
    email = fields.Char()
    phone = fields.Char()
    mobile = fields.Char()

    # Company flag
    is_company = fields.Boolean(string="Is a Company")

    # Relationship (VERY IMPORTANT)
    parent_id = fields.Many2one(
        'mini.partner',
        string="Parent Company"
    )

    child_ids = fields.One2many(
        'mini.partner',
        'parent_id',
        string="Contacts"
    )

    # Active field
    active = fields.Boolean(default=True)