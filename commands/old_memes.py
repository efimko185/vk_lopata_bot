import command_system
import vkapi
import settings
from random import choice

public = [-132938840, -140764973, -188275337]

def old_memes():
   
   attachment = vkapi.get_random_wall_picture(choice(public), settings.access_token)
   message = 'Эх, ностальгия'
   return message, attachment
old_memes_command = command_system.Command()

old_memes_command.keys = ['баян', 'старый мем']
old_memes_command.description = 'Кину старый мем'
old_memes_command.process = old_memes
old_memes_command.admin_keys = ['']