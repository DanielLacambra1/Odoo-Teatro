from odoo import models, fields, api

class Persona(models.Model):
    _name = 'teatro.persona'
    _description = 'Personas que trabajan en obra teatro. Para ser heredada'

    name = fields.Char(string='Nombre y apellidos', required=True)
    nacionalidad = fields.Char(string='Nacionalidad', required=True)
