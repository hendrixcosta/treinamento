# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class mymodule(models.Model):
#     _name = 'mymodule.mymodule'
#     _description = 'mymodule.mymodule'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields

class CursoModel(models.Model):
    _name = 'curso.model'
    name = fields.Char(required=True, string='titulo')
    description = fields.Char(string='descricao')