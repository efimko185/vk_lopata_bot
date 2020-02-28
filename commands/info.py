import command_system
import settings

def info():
    message = 'Список команд:'
    for c in command_system.command_list:
        message += '\n&#8195;' + c.keys[0] + ' -- ' + c.description
    if command_system.user_id in settings.admins:
        message += '\n\n[Команды для админа]'
        for c in command_system.command_list:
            message += '\n&#8195;' + c.admin_keys[0] + ' -- ' + c.admin_description
    message = message.replace('\n&#8195; -- ', '') 
    return message, ''


info_command = command_system.Command()

info_command.keys = ['помощь', 'помоги', 'help']
info_command.description = 'Покажу список команд'
info_command.process = info
info_command.admin_keys = ['']