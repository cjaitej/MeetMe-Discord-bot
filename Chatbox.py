class Chatbox:
    global users_list
    global waiting_state
    global running_state

    users_list = []
    waiting_state = []
    running_state = []

    def __init__(self, author):
        self.author = author
        users_list.append(self.author.id)
        self.waiting_status = True
        self.running_status = False
        self.connected_to = None

    def join(self):
        if len(waiting_state)>0:
            user = self.del_from_waiting_state()
            user.connected_to = self
            self.connected_to = user
            self.add_to_running_state()
            user.add_to_running_state()
            return user
        else:
            self.add_to_waiting_state()
            return "waiting."

    def leave(self):
        print(users_list)
        self.del_from_running_state()
        users_list.remove(self.author.id)
        print("Chat ended.")

    def check(author):
        return author.id in users_list

    def connect(self):
        if len(waiting_state) == 0:
            self.add_to_waiting_state()
        else:
            user2 = self.del_from_waiting_state()
            self.connected_to = user2
            user2.connected_to = self

    def add_to_waiting_state(self):
        self.waiting_status = True
        waiting_state.append(self)

    def del_from_waiting_state(self):
        user = waiting_state.pop()
        user.waiting_state_status = False
        return user

    def add_to_running_state(self):
        self.running_status = True
        running_state.append(self.author)

    def del_from_running_state(self):
        running_state.remove(self.author)
        self.running_status = False












