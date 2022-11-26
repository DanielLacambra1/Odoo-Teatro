from odoo import models, fields, api
from . import persona

class Opinion(models.Model):
    _name = 'teatro.opinion'
    _description = 'Opinión de una obra de teatro'

    persona = fields.Char(string='Nombre persona', required=True)
    edad = fields.Integer(string='Edad', required=True)
    fecha = fields.Date(string='Fecha', required=True)
    calificacion = fields.Integer(string='Calificación', required=True)
    comentarios = fields.Text(string='Comentarios')

    obra_id = fields.Many2one(comodel_name='teatro.obra', string='Obra')