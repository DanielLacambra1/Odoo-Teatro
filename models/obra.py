from odoo import models, fields, api


class Obra(models.Model):
    _name = 'teatro.obra'
    _description = 'Obra de teatro'

    # campos: título de la obra, género, idioma original, duración (en horas y minutos), fecha de estreno y resumen.
    name = fields.Char(string='Título obra', required=True)
    genero = fields.Char(string='Género', required=True)
    idioma = fields.Char(string='Idioma', required=True)
    duracion = fields.Float(string='Duración', required=True)
    fecha_estreno = fields.Date(string='Fecha de estreno')
    resumen = fields.Text(string='Resumen', required=True)
    
    # relaciones con otras clases
    actor_ids = fields.Many2many(comodel_name='teatro.actor', string='Actores')
    director_ids = fields.Many2many(comodel_name='teatro.director', string='Directores')
    opinion_ids = fields.One2many(comodel_name='teatro.opinion', inverse_name='obra_id', string='Opiniones')
    #sala_id = fields.Many2one(comodel_name='teatro.sala', string='Sala')
    #promocion_ids = fields.Many2many(comodel_name='teatro.promocion', string='Promociones')


