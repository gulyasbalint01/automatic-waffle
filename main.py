#heyo, if you want to run this, you need to put an openai api key in your environment variables in your system-wide environment variables. like such: OPENAI_API_KEY=<your key here>
#also, you need to install the openai python library. do that with pip install openai
#also also, you need to make an assistent on openai. do that here: https://platform.openai.com/assistants/new and then put the id of the assistant in line 38
#thats all the instructions i can think of rn. good luck!
#cherrs, have fun!

from openai import OpenAI
from time import sleep
client = OpenAI()

#dont touch this stuff, it was just for testing, it probably doesnt work anymore. i just left it here for reference. and for funsiedoodles.
#completion = client.chat.completions.create(
#  model="gpt-3.5-turbo",
#  messages=[
#    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#  ]
#)
#print(completion.choices[0].message)

thread = client.beta.threads.create()
def main():
    while True:
        inputstr = input("Enter your message: ")
        if inputstr == "exit":
            break
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=inputstr
        )

#thread_messages = client.beta.threads.messages.list(thread.id)
#print(thread_messages.data)

        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=''
        )



        while run.status != "completed":
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )


        thread_messages = client.beta.threads.messages.list(thread.id)
        #print(thread_messages.data)

        message = thread_messages.data[0]
        #print(str(message.content))
        mstr = str(message.content)
#if you take these out of comment, things WILL break. refer to line 11 for why it was left here.
#print(mstr.find("value='")+7)
#print((mstr.find("'),")-len(mstr))*-1)
        mstr = mstr[mstr.find("value='")+7:-((mstr.find("'),")-len(mstr))*-1)]
        mstra = mstr.split("\\n")
        #print(mstra)
        print("The AI says: ")
        for i in mstra:
            print(i)
        #print(mstr[mstr.find("value='")+7:-((mstr.find("'),")-len(mstr))*-1)])
    print("Goodbye!")
main()