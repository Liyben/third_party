# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ProductTemplate(models.Model):
	_inherit = 'product.template'

	def action_update_seq(self):
		if self.default_code:
			raise UserError(_("Please remove current default code.\nIt is only possible to update the product's internal reference if no internal reference has been added to the product."))
		sequence = self.categ_id.product_sequence_id.sudo().next_by_code(self.categ_id.product_sequence_id.code)
		self.default_code = sequence

class ProductProduct(models.Model):
	_inherit = 'product.product'

	def action_update_seq(self):
		if self.default_code:
			raise UserError(_("Please remove current default code.\nIt is only possible to update the product's internal reference if no internal reference has been added to the product."))
		sequence = self.categ_id.product_sequence_id.sudo().next_by_code(self.categ_id.product_sequence_id.code)
		self.default_code = sequence