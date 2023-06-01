{
    'name': 'Server Info',
    'summary': '',
    'description': '''
    
    ''',
    'author': 'Liyben',
    'website': 'https://liyben.com',
    'category': 'Technical',
    'version': '11.0.1.0.1',
    'license': 'LGPL-3',
    'images': ['static/description/banner.png', 'static/description/usage.png'],
    'external_dependencies': {
        "python": ["psutil","netifaces","socket"]
    },
    'depends': [
        'base_setup',
        'web'
    ],
    'data': [
        'views/fields.xml',
        'data/system_parameters.xml'
    ],
    'qweb': [
        'description/usage.png'
    ],
    'installable': True,
    'auto_install': False
}
