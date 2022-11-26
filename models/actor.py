from odoo import models, fields, api
from . import persona

class Actor(models.Model):
    _name = 'teatro.actor'
    _description = 'Actores en obras de teatro'
    _inherit = 'teatro.persona'

    inicio_trayectoria = fields.Date(string='Fecha inicio trayectoria', required=True)
    personaje_interpretado = fields.Char(string='Personaje interpretado', required=True)

    obra_ids = fields.Many2many(comodel_name='teatro.obra', string='Obras')
