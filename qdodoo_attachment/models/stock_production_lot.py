# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    doc_count = fields.Integer(compute='get_doc_count', string=u'附件数量', store=False)

    @api.multi
    def view_attachment_qdodoo(self):
        print self.env.ref('qdodoo_attachment.ir_attachment_search').id
        return {
            'type': 'ir.actions.act_window',
            'name': u'附件',
            'res_model': 'ir.attachment',
            'view_mode': 'tree,form',
            'view_type': 'form',
            'views': [(self.env.ref('qdodoo_attachment.ir_attachment_tree').id, 'tree'),
                      (self.env.ref('qdodoo_attachment.ir_attachment_form').id, 'form'),],
            'search_view_id': self.env.ref('qdodoo_attachment.ir_attachment_search').id,
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

class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    # @api.model
    # def create(self, vals):
    #     print vals
    #     if not vals.get('name'):
    #         vals['name'] = vals.get('file_name') or 'ljp'
    #     return super(IrAttachment, self).create(vals)



#
#     def _inverse_datas(self):
#         print '_inverse_datas'
#         location = self._storage()
#         for attach in self:
#             # compute the fields that depend on datas
#             print attach,attach.datas_fname
#             value = attach.datas
#             bin_data = value and value.decode('base64') or ''
#             vals = {
#                 'file_size': len(bin_data),
#                 'checksum': self._compute_checksum(bin_data),
#                 'index_content': self._index(bin_data, attach.datas_fname, attach.mimetype),
#                 'store_fname': False,
#                 'db_datas': value,
#             }
#             if value and location != 'db':
#                 # save it to the filestore
#                 vals['store_fname'] = self._file_write(value, vals['checksum'])
#                 vals['db_datas'] = False
#
#             # take current location in filestore to possibly garbage-collect it
#             fname = attach.store_fname
#             # write as superuser, as user probably does not have write access
#             super(IrAttachment, attach.sudo()).write(vals)
#             if fname:
#                 self._file_delete(fname)

