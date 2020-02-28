import command_system
import vkapi
import settings

def anime():
   # Получаем случайную картинку из паблика
   attachment = 'photo-150438165_456239046'
   message = 'Ха!'
   return message, attachment

anime_command = command_system.Command()

anime_command.keys = ['хентай', 'hentai']
anime_command.description = 'Кину случайный хентай-арт'
anime_command.process = anime
anime_command.admin_keys = ['']