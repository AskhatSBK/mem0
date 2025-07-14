curl -X POST http://localhost:4000/graphql \
  -H "Content-Type: application/json" \
  -d '{
    "query": "mutation Ask($input: AskInput!) { ask(input: $input) { messages { role content } conversationId } }",
    "variables": {
      "input": {
        "conversationId": "123456",
        "messages": [
          {
            "role": "user",
            "content": "У меня аллергия на арахис"
          }
        ]
      }
    }
  }'
