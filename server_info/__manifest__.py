{
    'name': 'Server Info',
    'summary': 'Settings tab with automatically updated server informations',
    'description': '''
    This module add new tab 'Server Info' in settings.
    This tab contains automatically updated informations about server cpu, ram and disk usage.
    It also allows you to change frequency of informations updates.
    Add a new system parameter to specify the host name.
    ''',
    'author': 'myOdoo.pl',
    'website': 'https://myodoo.pl',
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
        'data/settings_records.xml',
        'data/system_parameters.xml'
    ],
    'qweb': [
        'static/src/xml/auto_update.xml',
        'description/usage.png'
    ],
    'installable': True,
    'auto_install': False
}
