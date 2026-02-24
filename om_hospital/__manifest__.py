{
    'name': "Hospital Management System",
    'author': 'Betopia Group',
    'category': 'Hospital',
    'license': 'LGPL-3',
    'sequence': 1,
    'data':[
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/sequence.xml',
        'views/appointment_line_views.xml',
        'views/appointment_views.xml',
        'views/patient_readonly_views.xml',
        'views/patient_views.xml',
        'views/patient_tag_views.xml',
        'views/menu.xml'
    ],
    'depends':[
        'base',
        'mail',
        'product'
       
    ],
    'application': True,
    'installable': True,
}   