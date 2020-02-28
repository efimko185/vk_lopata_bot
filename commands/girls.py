import command_system
import vkapi
import settings

def girls():
   # Получаем случайную картинку из паблика
   attachment = vkapi.get_random_wall_picture(-111044288, settings.access_token)
   message = 'Дрочи, дорогуша❤'
   return message, attachment

girls_command = command_system.Command()

girls_command.keys = ['тян', 'тяночка']
girls_command.description = 'Кину пикчу с красивой тяночкой'
girls_command.process = girls
girls_command.admin_keys = ['']