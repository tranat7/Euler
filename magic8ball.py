import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask Again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very Doubtful']
print (messages[random.randint(0, len(messages)- 1)])
