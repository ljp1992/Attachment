# -*- coding: utf-8 -*-
{
    'name': "qdodoo_attachment",

    'summary': """  """,

    'description': """
1.批次号上传附件

bug:
1.search视图指定失败
2.上传文件时,名字没有实时变化
    """,

    'author': "青岛欧度软件技术有限责任公司",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        'views/stock_production_lot.xml',
        'views/ir_attachment.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'application': True,
}