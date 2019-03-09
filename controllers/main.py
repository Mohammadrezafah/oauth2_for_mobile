from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import Session, DataSet
import operator
import werkzeug


class AuthSignup(http.Controller):

    @http.route('/web/session/oauth', type='json', auth="none", cors="*")
    def action_signin_oauth(self, db, provider, params):
        request.session.db = db
        credentials = request.env[
            'res.users'].sudo().auth_oauth(provider, params)
        if credentials:
            db = credentials[0]
            login = credentials[1]
            password = credentials[2]
            a = request.session.authenticate(db, login, password)
            if not a:
                return credentials
        return request.env['ir.http'].session_info()
