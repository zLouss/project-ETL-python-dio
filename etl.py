import pandas as pd
import openai

df = pd.read_csv('diabetes_prediction_dataset - diabetes_prediction_dataset.csv.csv')
lista_linhas = df.to_dict(orient='records')
# print(lista_linhas)

openai_api_key = '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'

openai.api_key = openai_api_key

def generate_ai_pos(data):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
          "role": "system",
          "content": "Você é um especialista em medicina"
      },
      {
          "role": "user",
          "content": f"Defina o risco de desenvolvimento de diabetes dos dados: {data} e dê recomendações para que a doença não evolua. (Máximo 100 caracteres)"
      }
    ]
  )
  return completion.choices[0].message.content.strip('\"')

for data in lista_linhas:
  resultado = generate_ai_pos(data)
  data['Resultado'] = resultado

print(lista_linhas)