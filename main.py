    def read_the_chats(self):
        chat_type = self.text.split(" ")

        if len(chat_type) < 3:
            send_message = (f"{ConstICO.WARNING} Укажите тип чата. Все типы:\n"
                            "все - читает все чаты\n"
                            "лс - читает лс\n"
                            "беседы - чититет беседы\n"
                            "группы - читает группы\n")
            self.edit_messages(self.api, self.peer_id, send_message, self.message_id)
            return

        if chat_type[2].lower() not in ['все', 'лс', 'беседы', 'группы']:
            send_message = (f"{ConstICO.WARNING} Укажите тип чата. Все типы:\n"
                            "все - читает все чаты\n"
                            "лс - читает лс\n"
                            "беседы - чититет беседы\n"
                            "группы - читает группы\n")
            self.edit_messages(self.api, self.peer_id, send_message, self.message_id)
            return

        dialogs = self.api.messages.getConversations(filter='unread')

        if chat_type[2].lower() == 'все':
            chats_count = 0
            send_message = f"{ConstICO.LOADING} [id{self.owner_id}|Читаю сообщения.]"
            self.edit_messages(self.api, self.peer_id, send_message, self.message_id)

            for chat in dialogs['items']:
                chats_count += 1
                peer_id = chat['conversation']['peer']['id']
                self.api.messages.markAsRead(peer_id=peer_id)
            send_message = f"{ConstICO.YES} Успешно прочитал все чаты\nВсего чатов: {chats_count}."
            self.edit_messages(self.api, self.peer_id, send_message, self.message_id)

        if chat_type[2].lower() == 'лс':
            chats_count = 0
            send_message = f"{ConstICO.LOADING} [id{self.owner_id}|Читаю сообщения.]"
            self.edit_messages(self.api, self.peer_id, send_message, self.message_id)

            for chat in dialogs['items']:
                if chat['conversation']['peer']['type'] == "user":
                    chats_count += 1
                    peer_id = chat['conversation']['peer']['id']
                    self.api.messages.markAsRead(peer_id=peer_id)
            send_message = f"{ConstICO.YES} Успешно прочитал лички\nВсего чатов: {chats_count}."
            self.edit_messages(self.api, self.peer_id, send_message, self.message_id)

        if chat_type[2].lower() == 'беседы':
            chats_count = 0
            send_message = f"{ConstICO.LOADING} [id{self.owner_id}|Читаю сообщения.]"
            self.edit_messages(self.api, self.peer_id, send_message, self.message_id)

            for chat in dialogs['items']:
                if chat['conversation']['peer']['type'] == "chat":
                    chats_count += 1
                    peer_id = chat['conversation']['peer']['id']
                    self.api.messages.markAsRead(peer_id=peer_id)
            send_message = f"{ConstICO.YES} Успешно прочитал беседы\nВсего чатов: {chats_count}."
            self.edit_messages(self.api, self.peer_id, send_message, self.message_id)

        if chat_type[2].lower() == 'группы':
            chats_count = 0
            send_message = f"{ConstICO.LOADING} [id{self.owner_id}|Читаю сообщения.]"
            self.edit_messages(self.api, self.peer_id, send_message, self.message_id)

            for chat in dialogs['items']:
                if chat['conversation']['peer']['type'] == "group":
                    chats_count += 1
                    peer_id = chat['conversation']['peer']['id']
                    self.api.messages.markAsRead(peer_id=peer_id)
            send_message = f"{ConstICO.YES} Успешно прочитал группы\nВсего чатов: {chats_count}."
            self.edit_messages(self.api, self.peer_id, send_message, self.message_id)
