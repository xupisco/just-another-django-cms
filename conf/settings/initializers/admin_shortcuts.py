ADMIN_SHORTCUTS = [
    {
        'title': 'Authentication',
        'shortcuts': [
            {
                'title': 'Add user',
                'url_name': 'admin:dj_account_user_add',
            },
            {
                'title': 'Groups',
                'url_name': 'admin:auth_group_changelist',
            }
        ]
    },
]

ADMIN_SHORTCUTS_SETTINGS = {
    'show_on_all_pages': False,
    'hide_app_list': False,
    'open_new_window': False,
}
