from openai import OpenAI


def ai():

    client=OpenAI(api_key="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")

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"you are virtual assistant named ultron skilled in general task like alexa and google cloud"},
        {"role":"user","content":"what is coding"}
        ]
    )

    print(completion.choices[0].message.content)


# i can also include open ai just add this function in the main code and BUY OPEN AI API KEY ACCESS