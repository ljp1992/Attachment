# -*- coding: utf-8 -*-
from odoo import http

# class QdodooLotAttachment(http.Controller):
#     @http.route('/qdodoo_lot_attachment/qdodoo_lot_attachment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qdodoo_lot_attachment/qdodoo_lot_attachment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('qdodoo_lot_attachment.listing', {
#             'root': '/qdodoo_lot_attachment/qdodoo_lot_attachment',
#             'objects': http.request.env['qdodoo_lot_attachment.qdodoo_lot_attachment'].search([]),
#         })

#     @http.route('/qdodoo_lot_attachment/qdodoo_lot_attachment/objects/<model("qdodoo_lot_attachment.qdodoo_lot_attachment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qdodoo_lot_attachment.object', {
#             'object': obj
#         })