{
    'name': "Hospital Management System",
    'author': 'Betopia Group',
    'category': 'Hospital',
    'license': 'LGPL-3',
    'sequence': 1,
    'data':[
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/menu.xml'
    ],
    'depends':[
        'mail'
    ],
    'application': True,
    'installable': True,
}   