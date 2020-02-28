import command_system
import vkapi
import settings

def anime():
   # Получаем случайную картинку из паблика
   attachment = vkapi.get_random_wall_picture(-45739204, settings.access_token)
   message = 'Любуйся'
   return message, attachment

anime_command = command_system.Command()

anime_command.keys = ['аниме', '2д']
anime_command.description = 'Кину случайный аниме-арт'
anime_command.process = anime
anime_command.admin_keys = ['']