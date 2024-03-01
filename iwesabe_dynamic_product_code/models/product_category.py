# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ProductCategory(models.Model):
	_inherit = 'product.category'

	product_sequence_id = fields.Many2one('ir.sequence', copy=False)

	def open_sequence_changes(self):
		action = self.env["ir.actions.actions"]._for_xml_id("iwesabe_dynamic_product_code.action_category_sequence")
			
		context = {
			'default_category_id':self.id,
		}
		if self.product_sequence_id:
			context['default_prefix'] = self.product_sequence_id.prefix
			context['default_padding'] = self.product_sequence_id.padding
		action['context'] = context
		return action