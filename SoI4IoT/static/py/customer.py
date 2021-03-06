# Target: Request management
# Version: 0.1
# Date: 2017/02/05
# Mail: guillain@gmail.com
# Copyright 2017 GPL - Guillain

from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template, jsonify, send_file
from flask_paginate import Pagination, get_page_parameter
from werkzeug.utils import secure_filename
from tools import logger, exeReq, wEvent, getMaps,loginList, nameList

import re, os, sys, urllib

from flask import Blueprint
customer_app = Blueprint('customer_app', __name__)

# Conf app
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASK_SETTING')

# Customer creation form -------------------------------------------
@customer_app.route('/html/v1.0/customer/new', methods=['POST', 'GET'])
def newCustomer():
    try:
        wEvent('/html/v1.0/customer/new','request','Get new user','OK')
        return render_template('customer.html', maps = '')
    except Exception as e:
        wEvent('/html/v1.0/customer/new','request','Get new user','KO')
        return 'New error'

# Save Customer ---------------------------------------------------
@customer_app.route('/html/v1.0/customer/save', methods=['POST'])
def newCustomerSub():
    try:
        sql  = "INSERT INTO user SET login = '" + request.form['login'] + "', "
        sql += "  firstname = '" + request.form['firstname'] + "', lastname = '" + request.form['lastname'] + "', "
        sql += "  email = '" + request.form['email'] + "', address = '" +request.form['address'] + "', "
        sql += "  admin = '0', grp = 'customer', "
        sql += "  password = '" + request.form['password'] + "', enterprise = '" + request.form['enterprise'] + "', "
        sql += "  mobile = '" + request.form['mobile'] + "' "
        sql += "ON DUPLICATE KEY UPDATE "
        sql += "  firstname = '" + request.form['firstname'] + "', lastname = '" + request.form['lastname'] + "', "
        sql += "  email = '" + request.form['email'] + "', address = '" +request.form['address'] + "', "
        sql += "  admin = '0', grp = 'customer', "
        sql += "  password = '" + request.form['password'] + "', enterprise = '" + request.form['enterprise'] + "', "
        sql += "  mobile = '" + request.form['mobile'] + "';"
        exeReq(sql)
        wEvent('/html/v1.0/customer/save','exeReq','Save','OK')
        return 'Save OK'
    except Exception as e:
        wEvent('/html/v1.0/customer/save','exeReq','Save','KO')
        return 'Save error'

# View Customer ---------------------------------------------------
@customer_app.route('/html/v1.0/customer/view', methods=['POST', 'GET'])
def viewCustomer():
    try:
        sql  = "SELECT login, firstname, lastname, email, address, enterprise, mobile, password "
        sql += "FROM user WHERE login = '" + request.args['login'] + "' AND grp = 'customer';"
        view = exeReq(sql)
        wEvent('/html/v1.0/customer/view','exeReq','Get','OK')
        return render_template('customer.html', view = view[0], maps = getMaps())
    except Exception as e:
        wEvent('/html/v1.0/customer/view','exeReq','Get','KO')
        return 'View error'

# List Customer --------------------------------------------------------
@customer_app.route('/html/v1.0/customer/list', methods=['POST', 'GET'])
def listCustomer():
    try:
        # Pagination
        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        per_page = 20
        startat = page * per_page
        if startat <= per_page:
            startat = 0
        count = exeReq("SELECT count(*) FROM user WHERE grp = 'customer';")
        count = re.sub("[^0-9]", "","{}".format(count))
        pagination = Pagination(page=page, total=int(count), search=search, record_name='list', css_framework='foundation', per_page=per_page)

        # Get data
        list = exeReq("SELECT login, email, grp FROM user WHERE grp = 'customer';")

        wEvent('/html/v1.0/customer/list','exeReq','Get list','OK')
        return render_template('listCustomer.html', list = list, maps = getMaps(), pagination=pagination)
    except Exception as e:
        wEvent('/html/v1.0/customer/list','exeReq','Get list','KO')
        return 'List error'

# Delete Customer ---------------------------------------------------
@customer_app.route('/html/v1.0/customer/delete', methods=['POST', 'GET'])
def deleteCustomer():
    try:
        sql  = "UPDATE user SET grp = 'deleted' WHERE login = '" + request.args['login'] + "';"
        print sql
        exeReq(sql)
        wEvent('/html/v1.0/customer/delete','exeReq','Get','OK')
        return listCustomer()
    except Exception as e:
        wEvent('/html/v1.0/customer/delete','exeReq','Get','KO')
        return 'Delete error'

