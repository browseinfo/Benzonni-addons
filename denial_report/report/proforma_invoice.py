# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014-Today BrowseInfo (<http://www.browseinfo.in>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time
from openerp.osv import osv
from openerp.tools.translate import _
from openerp.report import report_sxw
from datetime import datetime
from openerp.modules.module import get_module_resource

class proforma_invoice(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(proforma_invoice, self).__init__(cr, uid, name, context=context)
        self.init_bal_sum = 0.0
        self.localcontext.update({
            'time': time,
            'get_date': self._get_date,
            'get_qty_format': self._get_qty_format,
            'get_delivery_number': self._get_delivery_number,
            })
            
    def _get_date(self,date):
        if date:
            date_list = date.split(' ')
            date1 = datetime.strptime(date_list[0], '%Y-%m-%d')
            date1 = date1.strftime('%d-%b-%y')
            return date1
        
    def _get_qty_format(self,obj):
        total_qty = 0.0
        for line in obj.invoice_line:
            total_qty = line.quantity
            qty = str(total_qty)
            qty1 = qty.split('.')
        return qty1[0]

    def _get_delivery_number(self, origin):
        if origin:
            do_id = self.pool.get('stock.picking').search(self.cr,self.uid,[('origin','=',origin)])
            pick_obj = self.pool.get('stock.picking').browse(self.cr, self.uid, do_id[0])
            return pick_obj.name
        else:
            return ' ' 
        
class report_proforma_invoice_qweb(osv.AbstractModel):
    _name = 'report.denial_report.report_proforma_invoice'
    _inherit = 'report.abstract_report'
    _template = 'denial_report.report_proforma_invoice'
    _wrapped_report_class = proforma_invoice

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
