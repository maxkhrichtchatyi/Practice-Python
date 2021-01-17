import time

import pykka

class Greeter(pykka.ThreadingActor):
    def __init__(self, greeting='Hi there!'):
        super().__init__()
        self.greeting = greeting
    def test(self):
        return self.greeting
    def on_receive(self, message):
        time.sleep(5)
        return 'Hi there!'


#
# actor_ref.tell('Hi!')
# # => Returns nothing. Will never block.
#
# answer = actor_ref.ask('Hi?')
# # => May block forever waiting for an answer
#
# answer = actor_ref.ask('Hi?', timeout=1)
# # => May wait 3s for an answer, then raises exception if no answer.

# future = actor_ref.ask('Hi?', block=False)
# => Will return a future object immediately.

# actor_ref.tell('Hi!')
actor_ref = Greeter.start(greeting='Hi you!')
proxy = actor_ref.proxy()
future = proxy.greeting
print(actor_ref.ask('test', block=False).get())
print(future.get())
# => May block forever waiting for an answer

#answer = future.get(timeout=0.1)