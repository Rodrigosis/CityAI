from openai import OpenAI

client = OpenAI(
  organization='',
  project='proj_000000000000000000000',
  api_key='sk-svcacct-0000000000000000000000000000000000000000000000000000000000000000000000000000'
)

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say this is a test"}],
    temperature=0.7
)

print(stream)
