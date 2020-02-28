import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import settings as s
import command_system as cs
from keyboards import keyboard

try:		
	cs.date()
	print('{}[Попытка авторизации группы...]'.format(cs.dat)) 
	group_vk_session = vk_api.VkApi(token=s.token)
	longpoll = VkBotLongPoll(group_vk_session, s.group_id)
	print('{}[Авторизация группы прошла успешно!]'.format(cs.dat)) 
	vk_session = vk_api.VkApi(s.login, s.password)
	print('{}[Попытка авторизации пользователя...]'.format(cs.dat)) 
	vk_session.auth()
	cs.date()
	print('{}[Авторизация пользователя прошла успешно!]'.format(cs.dat)) 
except vk_api.AuthError as error_msg:
	cs.date()
	print('{}[Ошибка авторизации!][{}]'.format(cs.dat, error_msg))

def get_random_wall_picture(group_id, token):
	max_num = vk_session.method('photos.get', {'owner_id':group_id, 'album_id':'wall', 'count':0, 'access_token':token})['count']
	num = random.randint(1, max_num)
	photo = vk_session.method('photos.get', {'owner_id':str(group_id), 'album_id':'wall', 'count':1, 'offset':num, 'access_token':token})['items'][0]['id']
	attachment = 'photo' + str(group_id) + '_' + str(photo)
	return attachment


def send_message(user_id, token, message, attachment=""):
	group_vk_session.method('messages.send', {'access_token':token, 'user_id':str(user_id), 'message':message, 'attachment':attachment, 'random_id':0, 'keyboard':keyboard.keyboard_1})

