from openai import OpenAI

client=OpenAI(api_key="org-qtdJKMRkCH20UU6CVGFqap4o")

completion=client.chat.completions.create(
  model='gpt-3.5-turbo',
  messages=[
    {
      'role':'system','content':'You are a voice asssisstant named jarvis, you are skilled in tasks like Alexa and Google'
    },{
      'role':'user',"Content":"What is force"
    }
  ]
)
print(completion.choices[0].message)