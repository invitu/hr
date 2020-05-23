# Copyright 2020 INVITU
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Hr Attendance View Google Map',
    'summary': """
        With this module you can view the geolocation of attendances in a
        google map view.""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'INVITU,'
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/hr',
    'depends': [
        'hr_attendance_geolocation',
        'web_view_google_map',
    ],
    'data': [
        'views/hr_attendance_views.xml',
    ],
}
