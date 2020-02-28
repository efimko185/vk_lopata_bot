import command_system
import vkapi
import settings
import os

def kill():
	if command_system.user_id in settings.admins:
		message = 'Ня. Пока'
		os._exit(0)
	else:
		message = 'Хм, ты не админ!'
	return message, ''

kill_command = command_system.Command()

kill_command.keys = ['']
kill_command.admin_keys = ['умри', '/kill']
kill_command.admin_description = 'Отключение бота'
kill_command.process = kill