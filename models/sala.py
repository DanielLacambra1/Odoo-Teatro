from odoo import models, fields, api

class Sala(models.Model):
    _name = 'teatro.sala'
    _description = 'Sala de teatro'

    nombre = fields.Char(string='Nombre sala', required=True)
    butacas = fields.Integer(strin='Butacas totales', required=True)

    obra_ids = fields.One2many(comodel_name='teatro.obra', inverse_name='sala_id', string='Obras')

