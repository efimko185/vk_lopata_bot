import command_system
import vkapi
import settings

def memes():
   # Получаем случайную картинку из паблика
   attachment = vkapi.get_random_wall_picture(-settings.group_id, settings.access_token)
   message = 'Только не умри от смеха, прошу тебя'
   return message, attachment

memes_command = command_system.Command()

memes_command.keys = ['мем', 'мемы', 'смешно']
memes_command.description = 'Кину случайный мем из нашего паблика'
memes_command.process = memes
memes_command.admin_keys = ['']