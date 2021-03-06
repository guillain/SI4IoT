#!/bin/bash

if [ "${1}" == "" ]; then
  echo "Thanks to add the comment"
  exit
fi

VERSION="2.0.0"
USER='guillain'
COMMENT="${VERSION}, ${1}"

add(){
  echo "add: ${1}, comment: ${2}, ${COMMENT}"
  git add "${1}"
  git commit -m "${2}, ${COMMENT}" "${1}"
}

git pull
add README.md 'REDAME file'
add LICENSE 'LICENSE file'
add requirements.txt 'Software requirement'
add SoI4IoT.wsgi 'Apache WSGI configuration file'
add conf/settings.cfg.default 'Default config file to use as template'
add conf/apache.conf.default 'Default apache web server to use as template'
add conf/apache-secure.conf.default 'Default secure apache config file to use as template'
add conf/mysql.sql 'MySQL structure'
add test/test.wsgi 'Test file for Apache WSGI'
add doc/install.md "Install doc file"
add doc/todo.md "ToDo doc file"
add doc/bug.md "Bug file"
add doc/Dashboard.png "Picture: Dashboard"
add doc/User.png "Picture: User"
add doc/List_User.png "Picture: List user"
add doc/Customer.png "Picture: Customer"
add doc/List_Customer.png "Picture: List customer"
add doc/Device.png "Picture: Device"
add doc/List_Device.png "Picture: List device"
add doc/Tracking.png "Picture: Tracking"
add doc/List_Tracking.png "Picture: List tracking"
add doc/Tracker.png "Picture: Tracker"
add SoI4IoT/__init__.py 'App init'
add SoI4IoT/static/image/loading.gif 'Animated gif'
add SoI4IoT/static/css/SoI4IoT.css 'CSS file of SoI4IoT'
add SoI4IoT/static/css/bootstrap.min.css 'CSS bootstrap'
add SoI4IoT/static/css/dd.basecoat.min.css 'CSS basecoat'
add SoI4IoT/static/js/dd.basecoat.min.js 'jS basecoat'
add SoI4IoT/static/js/jquery-1.9.0.js 'jQuery'
add SoI4IoT/static/js/SoI4IoT.js 'jQuery of SoI4IoT'
add SoI4IoT/static/js/jquery.popupoverlay.js 'Popup mgt'
add SoI4IoT/static/__init__.py 'App Init file that contain web login mgt'
add SoI4IoT/static/py/__init__.py 'App init'
add SoI4IoT/static/py/api.py 'Full REST API script'
add SoI4IoT/static/py/device.py 'Device script'
add SoI4IoT/static/py/user.py 'User script'
add SoI4IoT/static/py/customer.py 'Customer script'
add SoI4IoT/static/py/tracking.py 'Tracking script'
add SoI4IoT/static/py/tracker.py 'Tracker script'
add SoI4IoT/static/py/login.py 'Login script'
add SoI4IoT/static/py/tools.py 'Tools library as DB connection, wEvent...'
add SoI4IoT/static/py/dashboard.py 'Dashboard script'
add SoI4IoT/templates/dashboard.html "Dashboard for global map overview"
add SoI4IoT/templates/listDevice.html "List elements of the device DB"
add SoI4IoT/templates/device.html "Device form"
add SoI4IoT/templates/listUser.html "List elements of the user DB"
add SoI4IoT/templates/listCustomer.html "List elements of the user DB spe. for customer approch"
add SoI4IoT/templates/user.html "User form"
add SoI4IoT/templates/customer.html "customer form"
add SoI4IoT/templates/listTracking.html "List elements of the tracking DB"
add SoI4IoT/templates/tracking.html "Tracking form"
add SoI4IoT/templates/tracker.html "Tracker form"
add SoI4IoT/templates/flash.html "Flash message"
add SoI4IoT/templates/welcome.html "Welcome layout"
add SoI4IoT/templates/index.html "Main layout"
add SoI4IoT/templates/login.html "Login form"
add SoI4IoT/templates/map.html "Generic map form"
add SoI4IoT/templates/field/name.tpl "Template for name field"
add SoI4IoT/templates/field/group.tpl "Template for group field"
add SoI4IoT/templates/field/login.tpl "Template for login field"
add SoI4IoT/templates/field/admin.tpl "Template for admin field"
add run.dev 'TOOLS: bash script to run web server, for dev only'
add git.sh 'TOOLS: to comit easily the project to git'

git commit -m "${COMMENT}"
git push

exit 0
