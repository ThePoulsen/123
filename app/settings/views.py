## -*- coding: utf-8 -*-

from flask import Blueprint, render_template, url_for, g, request, redirect, session, json
from app.admin.services import requiredRole, loginRequired
from app import db
from forms import companyForm
from authAPI import authAPI
from app.crud.tenantCRUD import getTenant
from app.crud.userCRUD import getUsers, getContactPerson
import flask_sijax

settingsBP = Blueprint('settingsBP', __name__, template_folder='templates')

@flask_sijax.route(settingsBP, '/company')
@requiredRole(u'Administrator')
@loginRequired
def companyView():

    kwargs = {'title':'Company information',
              'formWidth':'350'}
    form = companyForm()

    if getTenant():
        tenant = getTenant()
        if getContactPerson():
            if g.sijax.is_sijax_request:
                g.sijax.register_object(SijaxHandler)
                return g.sijax.process_request()
            contact = getContactPerson()
            form = companyForm(regNo=tenant[u'regNo'],
                               companyName=tenant[u'name'],
                               addr=tenant[u'addr'],
                               addr2=tenant[u'addr2'],
                               postcode=tenant[u'postcode'],
                               city=tenant[u'city'],
                               contactName = str(contact['uuid']),
                               phone=contact['phone'],
                               email=contact['email'])

        users = [(str(r['uuid']),str(r['name']+' - '+r['email'])) for r in getUsers()['users']]

        form.contactName.choices = users
    return render_template('settings/companyView.html', form=form, **kwargs)


@settingsBP.route('/settings')
@requiredRole(u'Administrator')
@loginRequired
def settingsView():
    kwargs = {'title':'Settings',
              'formWidth':'350'}
    return render_template('settings/settingsView.html', **kwargs)
