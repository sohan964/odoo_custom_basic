{
    'name': 'Real State',
    'version': "18.0.1.0.0",
    'license': "LGPL-3",
    'summary': """An Real State Module""",
    
    'author': "Sohan",
    'website':"https://developer-sohanur.web.app/",
    'category': "Business",
    'maintainer': "Betopia Group ltd",
    'sequence': 4,
    'data':[
        # security
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        # views
        "views/estate_property_views.xml",
        #MENUS
        "views/estate_menus.xml"

    ],
    'demo':[
        "demo/demo.xml"
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}