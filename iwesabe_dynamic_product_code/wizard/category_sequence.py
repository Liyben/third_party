# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class CategorySequence(models.TransientModel):
    _name = 'category.sequence'
    _description = "Category Sequence"

    category_id = fields.Many2one('product.category')
    prefix = fields.Char('Prefix')
    padding = fields.Integer('Padding', default=4)

    def action_update_sequence(self):
        if not self.category_id:
            return
        if not self.category_id.product_sequence_id:
            categ_name = self.category_id.name.split(' ')
            name = [c_name.lower() for c_name in categ_name]
            values = {
                'name':'Category '+self.category_id.name,
                'implementation':'no_gap',
                'code':'.'.join(name),
                'prefix':self.prefix,
                'padding':self.padding,
            }
            sequence_id = self.env['ir.sequence'].sudo().create(values)
            self.category_id.product_sequence_id = sequence_id.id
        else:
            self.category_id.product_sequence_id.update({
                'prefix':self.prefix,
                'padding':self.padding,
            })