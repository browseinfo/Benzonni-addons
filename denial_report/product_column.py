# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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

from openerp import tools
from openerp.osv import osv, fields
from openerp.tools.translate import _

import openerp.addons.decimal_precision as dp

class product_template(osv.osv):
    _inherit="product.template"
    _columns={
        'chair_base':fields.char('Chair Base'),
        'mechanism':fields.char('Mechanism'),
        'armrest':fields.char('Armrest'),
        'castor':fields.char('Castor'),
        'seat_cushion':fields.char('Seat Cushion'),
        'upholstery':fields.char('Upholstery'),
    }

class account_invoice(osv.osv):
    _inherit="account.invoice"
    _columns={
        'validity_term':fields.char('Validity Term'),
        'credit_term':fields.char('Credit Term'),
        'shipping_term':fields.char('Shipping Term'),
        'f_o_c':fields.text('F.O.C'),
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
