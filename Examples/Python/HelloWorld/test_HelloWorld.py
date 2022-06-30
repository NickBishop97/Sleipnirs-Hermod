import settings
from HelloWorldSubscriber import Reader
import HelloWorldPublisher

def test_Sub():
    settings.init()
    print('Creating subscriber.')
    reader = Reader()

    print('Starting publisher.')
    writer = HelloWorldPublisher.Writer()
    writer.run()

    #print(len(settings.y))
    #print(len(settings.x))

    for x in range(len(settings.y)) :
        assert settings.y[x] != settings.x[x]
        print("Publisher sent = {message}, Subscriber Recieved = {index}".format(message=settings.y[x], index=settings.x[x]))

