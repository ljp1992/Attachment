# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    doc_count = fields.Integer(compute='get_doc_count', string=u'附件数量', store=False)

    @api.multi
    def view_attachment_qdodoo(self):
        return {
            'type': 'ir.actions.act_window',
            'name': u'附件',
            'view_mode': 'tree,form',
            'view_type': 'form',
            # 'views': [(self.env.ref('sale.view_quotation_tree').id, 'tree'),
            #           (self.env.ref('sale.view_order_form').id, 'form')],
            'res_model': 'ir.attachment',
            'domain': [('res_model', '=', 'stock.production.lot'), ('res_id', '=', self.id)],
            'target': 'current',
            'context': {'default_res_model': 'stock.production.lot',
                        'default_res_id': self.id,},
        }

    def get_doc_count(self):
        attachment_obj = self.env['ir.attachment']
        for record in self:
            result = attachment_obj.search([('res_model', '=', 'stock.production.lot'), ('res_id', '=', record.id)])
            record.doc_count = len(result)


