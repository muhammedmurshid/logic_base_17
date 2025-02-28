{
    'name': 'Logic Base',
    'version': '1.0.0',
    'summary': 'logic Batches',
    'description': """
        A more detailed description of the module.
    """,
    'author': 'Murshid',
    'website': 'https://www.yourwebsite.com',
    'category': 'Specific Category',
    'license': 'LGPL-3',
    'depends': [
        'base', 'hr','openeducat_core',  # List of module dependencies

        # Add other module dependencies here
    ],
    'data': [
        # 'security/ir.model.access.csv',  # Access rights
        'security/base_group.xml',
        'security/ir.model.access.csv',
        'views/base.xml',
        'views/branch.xml',
        'views/class.xml',
        'data/reports.xml'

    ],

    'installable': True,
    'application': False,
    'auto_install': False,

}
