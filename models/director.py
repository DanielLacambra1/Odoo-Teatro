from odoo import models, fields, api
from . import persona

class Director(models.Model):
    _name = 'teatro.director'
    _description = 'Director de la obra de teatro'
    _inherit = 'teatro.persona'

    experiencia = fields.Char(string='Experiencia', required=True)
    conocimientos = fields.Char(string='Conocimientos', required=True)
    destrezas = fields.Char(string='Destrezas', required=True)

    obra_ids = fields.Many2many(comodel_name='teatro.obra', string='Obras')
    