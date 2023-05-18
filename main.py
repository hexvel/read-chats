def read_the_chats(self):
    chat_type = self.text.lower().split(" ")

    if len(chat_type) < 3 or chat_type[2].lower() not in ['все', 'лс', 'беседы', 'группы']:
        send_message = (f"{Icons.WARNING} Укажите тип чата. Все типы:\n"
                        "все - читает все чаты\nлс - читает лс\n"
                        "беседы - читает беседы\nгруппы - читает группы\n")
        self.edit_messages(self.api, self.peer_id, send_message, self.message_id)
        return

    chat_types = {'лс': 'user', 'беседы': 'chat', 'группы': 'group'}
    dialogs = self.api.messages.getConversations(filter='unread')

    if chat_type[2].lower() == 'все':
        chats_count = 0
        send_message = f"{Icons.LOADING} [id{self.owner_id}|Читаю сообщения.]"
        self.edit_messages(self.api, self.peer_id, send_message, self.message_id)

        for chat in dialogs['items']:
            chats_count += 1
            peer_id = chat['conversation']['peer']['id']
            self.api.messages.markAsRead(peer_id=peer_id)
        send_message = f"{Icons.YES} Успешно прочитал все чаты\nВсего чатов: {chats_count}."
        self.edit_messages(self.api, self.peer_id, send_message, self.message_id)

    if chat_type[2].lower() in chat_types.keys():
        chats_count = 0
        send_message = f"{Icons.LOADING} [id{self.owner_id}|Читаю сообщения.]"
        self.edit_messages(self.api, self.peer_id, send_message, self.message_id)

        for chat in dialogs['items']:
            if chat['conversation']['peer']['type'] == chat_types[chat_type[2].lower()]:
                chats_count += 1
                peer_id = chat['conversation']['peer']['id']
                self.api.messages.markAsRead(peer_id=peer_id)
        send_message = f"{Icons.YES} Успешно прочитал сообщения\nВсего чатов: {chats_count}."
        self.edit_messages(self.api, self.peer_id, send_message, self.message_id)
