from odoo import api, fields, models, _, tools

class LaborLocation(models.Model):
    _name = "labor.location"

    location_name = fields.Char(string="Location Name")
