# -*- coding: utf-8 -*-
# from odoo import http


# class IntPurchaseStockUom(http.Controller):
#     @http.route('/int_purchase_stock_uom/int_purchase_stock_uom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/int_purchase_stock_uom/int_purchase_stock_uom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('int_purchase_stock_uom.listing', {
#             'root': '/int_purchase_stock_uom/int_purchase_stock_uom',
#             'objects': http.request.env['int_purchase_stock_uom.int_purchase_stock_uom'].search([]),
#         })

#     @http.route('/int_purchase_stock_uom/int_purchase_stock_uom/objects/<model("int_purchase_stock_uom.int_purchase_stock_uom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('int_purchase_stock_uom.object', {
#             'object': obj
#         })
