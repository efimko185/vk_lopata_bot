import messageHandler
import vk_api
import command_system as cs
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vkapi import vk_session, longpoll
from settings import token

def main():

	for event in longpoll.listen():

		if event.type == VkBotEventType.MESSAGE_NEW:
			cs.date()
			print('{}[Message from user {}]'.format(cs.dat, event.obj.from_id))
			try:
				cs.user_id = event.obj.from_id
				messageHandler.create_answer(event, token)
			except Exception as error:
				print('{}[Error][{}]'.format(cs.dat, error))
				messageHandler.create_answer_error(event, token)
#            print('Текст:', event.obj.text)


if __name__ == '__main__':
	main()

