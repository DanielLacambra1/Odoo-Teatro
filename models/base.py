from odoo import models, fields, api

class Base(models.Model):
    _name = 'teatro.base'
    _description = 'Base class to be inherited'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
