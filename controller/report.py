from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal
class CustomPortal(CustomerPortal):
    @http.route('/my/order/<int:order_id>', type='http', auth='user')
    def portal_my_order(self, order_id, download=False, **kwargs):
        sale_order = request.env['sale.order'].sudo().browse(order_id)
        if not sale_order.exists():
            return request.redirect('/my/orders')
        if download:
            pdf, _ = request.env['ir.actions.report']._render_qweb_pdf('sale.report_saleorder', [order_id])
            pdfhttpheaders = [
                ('Content-Type', 'application/pdf'),
                ('Content-Length', len(pdf)),
                ('Content-Disposition', 'attachment; filename="%s.pdf"' % (sale_order.name)),
            ]
            return request.make_response(pdf, headers=pdfhttpheaders)
        return request.redirect(sale_order.get_portal_url())
