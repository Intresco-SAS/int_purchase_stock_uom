# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    def _prepare_stock_move_vals(self, picking, price_unit, product_uom_qty, product_uom):
        res = super(PurchaseOrderLine, self)._prepare_stock_move_vals(picking, price_unit, product_uom_qty, product_uom)
        if picking.picking_type_id.use_purchase_uom:
            res.update({
                'product_uom': self.product_uom.id,
                'product_uom_qty': self.product_qty,
            })
        return res
