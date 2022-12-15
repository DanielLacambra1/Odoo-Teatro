from odoo import models, fields, api

class Promocion(models.Model):
    _name = 'teatro.promocion'
    _description = 'Promoción de obra de teatro'

    descripcion = fields.Text(string='Descripción', required=True)
    finpromo = fields.Date(string='Fin de promo')
    numeroPromo = fields.Integer(string='Número de promos')
    descuentoPorcentaje = fields.Integer(string='Descuento', required=True)
    total = fields.Integer(string='Total')

    promoVersion1 = fields.Integer(string='Duración promo Version 1 (días)')
    promoVersion2 = fields.Integer(string='Duración promo Version 2 (días)')
    mediaPromosV1y2 = fields.Integer(string='Media días promos v1 y v2')

    obra_ids = fields.Many2many(comodel_name='teatro.obra', string='Obras')

    # campo onchange. numeroPromo descuentoPorcentaje = total
    @api.onchange('numeroPromo','descuentoPorcentaje')
    def _onchange_total(self):
        self.total = self.numeroPromo * (self.descuentoPorcentaje / 100)

    # media de valores enteros almacenados en los registros
    @api.onchange('promoVersion1','promoVersion2')
    def _onchange_media(self):
        self.mediaPromosV1y2 = (self.promoVersion1 + self.promoVersion2)/2

        