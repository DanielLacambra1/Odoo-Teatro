from odoo import models, fields

class Promocion(models.Model):
    _name = 'teatro.promocion'
    _description = 'Promoción de obra de teatro'

    descripcion = fields.Text(string='Descripción', required=True)
    descuento = fields.Integer(string='Descuento', required=True)

    obra_ids = fields.Many2many(comodel_name='teatro.obra', string='Obras')