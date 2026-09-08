import requests
import json


TENANT_ID = "27fefdbd-56c2-4d11-bf96-ebf972993b77"

CLIENT_ID = "b3785716-2eb8-43dc-a742-aa60c645314c"

CLIENT_SECRET = "lHr8Q~VWS5tDF~5tM0G20R9vDYdw5lwcJoW99bYp"


ENDPOINT = "https://mi-cognitive-service.cognitiveservices.azure.com/"

# ========================================
# OBTENER TOKEN OAUTH 2.0
# ========================================

token_url = (
    f"https://login.microsoftonline.com/"
    f"{TENANT_ID}/oauth2/v2.0/token"
)

token_data = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "scope": "https://cognitiveservices.azure.com/.default",
    "grant_type": "client_credentials"
}

print("Obteniendo token...")

token_response = requests.post(
    token_url,
    data=token_data
)

if token_response.status_code != 200:
    print("Error al obtener token")
    print(token_response.text)
    exit()

access_token = token_response.json()["access_token"]

print("Token obtenido correctamente")



url = f"{ENDPOINT}/language/:analyze-text?api-version=2023-04-01"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

body = {
    "kind": "SentimentAnalysis",
    "analysisInput": {
        "documents": [
            {
                
                "id": "1",
                
                "language": "es",
                
                "text": "Me encanta Microsoft Azure porque facilita mucho el trabajo."
                
                }
        ]
    }
}

print("Analizando sentimiento...")

response = requests.post(
    url,
    headers=headers,
    json=body
)

print("\nRESULTADO:")
print(json.dumps(response.json(), indent=4, ensure_ascii=False))