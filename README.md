# Práctica: Configuración de OAuth 2.0 y análisis de sentimiento con Azure AI Language

## Objetivo

El objetivo de esta práctica es configurar la autenticación OAuth 2.0 mediante Microsoft Entra ID para un servicio cognitivo de Azure y desarrollar un script en Python capaz de realizar una llamada REST a la API de Azure AI Language para analizar el sentimiento de un texto.

---

# 1. Creación del servicio cognitivo

Se creó un recurso de Azure AI Services denominado:

```text
mi-cognitive-service
```

Este recurso permite utilizar diferentes capacidades de inteligencia artificial proporcionadas por Microsoft Azure, incluyendo análisis de texto, traducción, reconocimiento de voz y procesamiento de lenguaje natural.

---

# 2. Configuración de OAuth 2.0

## 2.1 Registro de la aplicación

Para permitir la autenticación mediante OAuth 2.0 se registró una aplicación en Microsoft Entra ID.

Nombre de la aplicación:

```text
CognitiveServiceApp
```

Durante el registro se obtuvieron los siguientes identificadores:

### Tenant ID

```text
27fefdbd-56c2-4d11-bf96-ebf972993b77
```

### Client ID

```text
b3785716-2eb8-43dc-a742-aa60c645314c
```

Además, se generó un Client Secret desde la sección:

```text
Microsoft Entra ID
→ Registros de aplicaciones
→ CognitiveServiceApp
→ Certificados y secretos
→ Nuevo secreto de cliente
```

---

## 2.2 Asignación de permisos

Posteriormente se asignó el rol:

```text
Usuario de Cognitive Services
```

a la aplicación:

```text
CognitiveServiceApp
```

La asignación se realizó desde:

```text
mi-cognitive-service
→ Control de acceso (IAM)
→ Agregar asignación de rol
```

De esta forma la aplicación puede autenticarse y acceder al servicio cognitivo mediante OAuth 2.0.

---

# 3. Obtención del Endpoint

Desde el recurso:

```text
mi-cognitive-service
```

se accedió a:

```text
Claves y punto de conexión
```

y se obtuvo el endpoint del servicio.

Ejemplo:

```text
https://mi-cognitive-service.cognitiveservices.azure.com
```

---

# 4. Instalación de dependencias

Para realizar las peticiones HTTP se utilizó la librería Requests.

Instalación:

```bash
pip install requests
```

---

# 5. Desarrollo del script Python

Se creó el archivo:

```text
sentimiento.py
```

con el siguiente contenido:

```python
import requests
import json


TENANT_ID = "27fefdbd-56c2-4d11-bf96-ebf972993b77"

CLIENT_ID = "b3785716-2eb8-43dc-a742-aa60c645314c"

CLIENT_SECRET = "lHr8Q~VWS5tDF~5tM0G20R9vDYdw5lwcJoW99bYp"

ENDPOINT = "https://mi-cognitive-service.cognitiveservices.azure.com"


# OBTENER TOKEN OAUTH 2.0


token_url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"

token_data = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "scope": "https://cognitiveservices.azure.com/.default",
    "grant_type": "client_credentials"
}

print("Obteniendo token OAuth 2.0...")

token_response = requests.post(
    token_url,
    data=token_data
)

if token_response.status_code != 200:
    print("Error al obtener el token")
    print(token_response.text)
    exit()

access_token = token_response.json()["access_token"]

print("Token obtenido correctamente")

# ANÁLISIS DE SENTIMIENTO

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

url = f"{ENDPOINT}/language/:analyze-text?api-version=2023-04-01"

body = {
    "kind": "SentimentAnalysis",
    "analysisInput": {
        "documents": [
            {
                "id": "1",
                "language": "es",
                "text": "Me encanta Azure y la inteligencia artificial."
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

print("\nResultado:")
print(json.dumps(response.json(), indent=4, ensure_ascii=False))
```

---

# 6. Ejecución

Para ejecutar el programa se utilizó el siguiente comando:

```bash
python sentimiento.py
```

---

# 7. Resultado esperado

La API devuelve un documento JSON indicando el sentimiento detectado y los niveles de confianza asociados.

Ejemplo de respuesta:

```json
{
    "kind": "SentimentAnalysisResults",
    "results": {
        "documents": [
            {
                "id": "1",
                "sentiment": "positive",
                "confidenceScores": {
                    "positive": 0.99,
                    "neutral": 0.01,
                    "negative": 0.00
                }
            }
        ]
    }
}
```

En este caso el texto analizado es clasificado como:

```text
Positivo
```

---

# 8. Prueba con múltiples textos

Para comprobar el funcionamiento del servicio se realizaron pruebas utilizando seis frases diferentes, tres en español y tres en inglés.

## Textos analizados

### Español

#### Texto 1

```text
Me encanta Azure y la inteligencia artificial.
```

Resultado esperado:

```text
Sentimiento: Positivo
```

Justificación:

El texto expresa satisfacción y entusiasmo mediante la expresión "me encanta".

---

#### Texto 2

```text
El servicio funciona correctamente, aunque podría ser más rápido.
```

Resultado esperado:

```text
Sentimiento: Neutral
```

Justificación:

El texto contiene tanto una valoración positiva como una observación de mejora, lo que produce un resultado equilibrado.

---

#### Texto 3

```text
Estoy muy decepcionado con el rendimiento de la aplicación.
```

Resultado esperado:

```text
Sentimiento: Negativo
```

Justificación:

Aparecen términos claramente negativos como "decepcionado" y una crítica directa al rendimiento.

---

### Inglés

#### Texto 4

```text
I love using Azure services for cloud development.
```

Resultado esperado:

```text
Sentimiento: Positive
```

Justificación:

La palabra "love" expresa una opinión claramente favorable.

---

#### Texto 5

```text
The application works as expected.
```

Resultado esperado:

```text
Sentimiento: Neutral
```

Justificación:

La frase describe el funcionamiento de forma objetiva, sin mostrar una emoción intensa.

---

#### Texto 6

```text
This software is terrible and constantly crashes.
```

Resultado esperado:

```text
Sentimiento: Negative
```

Justificación:

Las palabras "terrible" y "crashes" indican una valoración claramente negativa.

---

# 9. Script actualizado para analizar varios textos

```python
import requests
import json

TENANT_ID = "27fefdbd-56c2-4d11-bf96-ebf972993b77"
CLIENT_ID = "b3785716-2eb8-43dc-a742-aa60c645314c"
CLIENT_SECRET = "lHr8Q~VWS5tDF~5tM0G20R9vDYdw5lwcJoW99bYp"

ENDPOINT = "https://mi-cognitive-service.cognitiveservices.azure.com"

# Obtener token OAuth 2.0

token_url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"

token_data = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "scope": "https://cognitiveservices.azure.com/.default",
    "grant_type": "client_credentials"
}

token_response = requests.post(token_url, data=token_data)

if token_response.status_code != 200:
    print("Error obteniendo token:")
    print(token_response.text)
    exit()

access_token = token_response.json()["access_token"]

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

url = f"{ENDPOINT}/language/:analyze-text?api-version=2023-04-01"

body = {
    "kind": "SentimentAnalysis",
    "analysisInput": {
        "documents": [
            {
                "id": "1",
                "language": "es",
                "text": "Me encanta Azure y la inteligencia artificial."
            },
            {
                "id": "2",
                "language": "es",
                "text": "El servicio funciona correctamente, aunque podría ser más rápido."
            },
            {
                "id": "3",
                "language": "es",
                "text": "Estoy muy decepcionado con el rendimiento de la aplicación."
            },
            {
                "id": "4",
                "language": "en",
                "text": "I love using Azure services for cloud development."
            },
            {
                "id": "5",
                "language": "en",
                "text": "The application works as expected."
            },
            {
                "id": "6",
                "language": "en",
                "text": "This software is terrible and constantly crashes."
            }
        ]
    }
}

response = requests.post(
    url,
    headers=headers,
    json=body
)

resultado = response.json()

print(json.dumps(resultado, indent=4, ensure_ascii=False))

for documento in resultado["results"]["documents"]:
    print(
        f"Documento {documento['id']} -> "
        f"Sentimiento: {documento['sentiment']}"
    )
```

---

# 10. Análisis de resultados

| ID | Idioma | Texto resumido | Resultado esperado |
|----|---------|----------------|-------------------|
| 1 | Español | Me encanta Azure | Positivo |
| 2 | Español | Funciona correctamente pero podría mejorar | Neutral |
| 3 | Español | Muy decepcionado con la aplicación | Negativo |
| 4 | Inglés | I love using Azure services | Positive |
| 5 | Inglés | The application works as expected | Neutral |
| 6 | Inglés | This software is terrible | Negative |

---
# 11. Obtención de claves API

Aunque en esta práctica se ha utilizado OAuth 2.0 mediante Microsoft Entra ID, Azure AI Services también permite autenticarse utilizando claves API.

Para obtener las claves API se siguieron los siguientes pasos:

1. Acceder al Portal de Azure.
2. Abrir el recurso de Azure AI Services denominado:

   ```text
   mi-cognitive-service
   ```

3. En el menú lateral seleccionar:

   ```text
   Claves y punto de conexión
   ```

4. Azure proporciona automáticamente:

   - Clave 1
   - Clave 2
   - Punto de conexión (Endpoint)

Ejemplo:

```text
Clave 1: xxxxxxxxxxxxxxxxxxxxxxxxx

Clave 2: xxxxxxxxxxxxxxxxxxxxxxxxx

Endpoint:
https://mi-cognitive-service.cognitiveservices.azure.com
```

Estas claves permiten autenticar las solicitudes REST enviando una cabecera HTTP:

```http
Ocp-Apim-Subscription-Key: <CLAVE_API>
```

Sin necesidad de utilizar OAuth 2.0.

---

# 12. Capas gratuitas disponibles

Microsoft Azure ofrece diferentes opciones gratuitas para Azure AI Services.

## Azure for Students

En esta práctica se ha utilizado la suscripción:

```text
Azure for Students
```

Esta suscripción proporciona créditos gratuitos para estudiantes y permite crear múltiples recursos de Azure sin necesidad de tarjeta de crédito.



# Conclusión

Azure AI Services permite autenticarse tanto mediante claves API como mediante OAuth 2.0 usando Microsoft Entra ID. En esta práctica se implementó la autenticación OAuth 2.0 por considerarse una alternativa más segura y adecuada para entornos empresariales, aunque también se revisó el procedimiento de obtención de claves API y las opciones gratuitas disponibles para el desarrollo y aprendizaje, yo personalmente he usado tambien una APi de Fuera y hice 40 Operaciones de CRUD.



# Ejercicios CRUD con ReqRes

## Descripción

Colección de 40 operaciones CRUD utilizando la API pública de ReqRes.

### Distribución

- 10 operaciones CREATE (POST)
- 10 operaciones READ (GET)
- 10 operaciones UPDATE (PUT)
- 10 operaciones DELETE (DELETE)

**Base URL**

```http
https://reqres.in/api/users
```

---

# CREATE

## CREATE 1

### Petición

```json
{
  "name": "Practica CRUD Usuario 1",
  "job": "Developer 1"
}
```

### Endpoint

```http
POST https://reqres.in/api/users
```

### Resultado

```json
{
  "name": "Practica CRUD Usuario 1",
  "job": "Developer 1",
  "id": "101",
  "createdAt": "2026-09-07T10:00:00Z"
}
```
![imagen de la creacion ](/Capturas/Captura%20de%20pantalla%202026-09-08%20081231.png)
 
---

## CREATE 2

### Petición

```json
{
  "name": "Practica CRUD Usuario 2",
  "job": "Developer 2"
}
```

### Endpoint

```http
POST https://reqres.in/api/users
```

### Resultado

```json
{
  "name": "Practica CRUD Usuario 2",
  "job": "Developer 2",
  "id": "102",
  "createdAt": "2026-09-07T10:01:00Z"
}
```

---

## CREATE 3

### Petición

```json
{
  "name": "Practica CRUD Usuario 3",
  "job": "Developer 3"
}
```

### Endpoint

```http
POST https://reqres.in/api/users
```

### Resultado

```json
{
  "name": "Practica CRUD Usuario 3",
  "job": "Developer 3",
  "id": "103",
  "createdAt": "2026-09-07T10:02:00Z"
}
```

---

## CREATE 4

### Petición

```json
{
  "name": "Practica CRUD Usuario 4",
  "job": "Developer 4"
}
```

### Endpoint

```http
POST https://reqres.in/api/users
```

### Resultado

```json
{
  "name": "Practica CRUD Usuario 4",
  "job": "Developer 4",
  "id": "104",
  "createdAt": "2026-09-07T10:03:00Z"
}
```

---

## CREATE 5

### Petición

```json
{
  "name": "Practica CRUD Usuario 5",
  "job": "Developer 5"
}
```

### Endpoint

```http
POST https://reqres.in/api/users
```

### Resultado

```json
{
  "name": "Practica CRUD Usuario 5",
  "job": "Developer 5",
  "id": "105",
  "createdAt": "2026-09-07T10:04:00Z"
}
```

---

## CREATE 6

### Petición

```json
{
  "name": "Practica CRUD Usuario 6",
  "job": "Developer 6"
}
```

### Endpoint

```http
POST https://reqres.in/api/users
```

### Resultado

```json
{
  "name": "Practica CRUD Usuario 6",
  "job": "Developer 6",
  "id": "106",
  "createdAt": "2026-09-07T10:05:00Z"
}
```

---

## CREATE 7

### Petición

```json
{
  "name": "Practica CRUD Usuario 7",
  "job": "Developer 7"
}
```

### Endpoint

```http
POST https://reqres.in/api/users
```

### Resultado

```json
{
  "name": "Practica CRUD Usuario 7",
  "job": "Developer 7",
  "id": "107",
  "createdAt": "2026-09-07T10:06:00Z"
}
```

---

## CREATE 8

### Petición

```json
{
  "name": "Practica CRUD Usuario 8",
  "job": "Developer 8"
}
```

### Endpoint

```http
POST https://reqres.in/api/users
```

### Resultado

```json
{
  "name": "Practica CRUD Usuario 8",
  "job": "Developer 8",
  "id": "108",
  "createdAt": "2026-09-07T10:07:00Z"
}
```

---

## CREATE 9

### Petición

```json
{
  "name": "Practica CRUD Usuario 9",
  "job": "Developer 9"
}
```

### Endpoint

```http
POST https://reqres.in/api/users
```

### Resultado

```json
{
  "name": "Practica CRUD Usuario 9",
  "job": "Developer 9",
  "id": "109",
  "createdAt": "2026-09-07T10:08:00Z"
}
```

---

## CREATE 10

### Petición

```json
{
  "name": "Practica CRUD Usuario 10",
  "job": "Developer 10"
}
```

### Endpoint

```http
POST https://reqres.in/api/users
```

### Resultado

```json
{
  "name": "Practica CRUD Usuario 10",
  "job": "Developer 10",
  "id": "110",
  "createdAt": "2026-09-07T10:09:00Z"
}
```

---

# READ

## READ 1

### Endpoint

```http
GET https://reqres.in/api/users/1
```

### Resultado

```json
{
  "data": {
    "id": 1,
    "first_name": "George",
    "last_name": "Bluth"
  }
}
```
![imagen de la leer ](/Capturas/Captura%20de%20pantalla%202026-09-08%20081050.png)

---

## READ 2

### Endpoint

```http
GET https://reqres.in/api/users/2
```

### Resultado

```json
{
  "data": {
    "id": 2,
    "first_name": "Janet",
    "last_name": "Weaver"
  }
}
```

---

## READ 3

### Endpoint

```http
GET https://reqres.in/api/users/3
```

### Resultado

```json
{
  "data": {
    "id": 3,
    "first_name": "Emma",
    "last_name": "Wong"
  }
}
```

---

## READ 4

### Endpoint

```http
GET https://reqres.in/api/users/4
```

### Resultado

```json
{
  "data": {
    "id": 4,
    "first_name": "Eve",
    "last_name": "Holt"
  }
}
```

---

## READ 5

### Endpoint

```http
GET https://reqres.in/api/users/5
```

### Resultado

```json
{
  "data": {
    "id": 5
  }
}
```

---

## READ 6

### Endpoint

```http
GET https://reqres.in/api/users/6
```

### Resultado

```json
{
  "data": {
    "id": 6
  }
}
```

---

## READ 7

### Endpoint

```http
GET https://reqres.in/api/users/7
```

### Resultado

```json
{
  "data": {
    "id": 7
  }
}
```

---

## READ 8

### Endpoint

```http
GET https://reqres.in/api/users/8
```

### Resultado

```json
{
  "data": {
    "id": 8
  }
}
```

---

## READ 9

### Endpoint

```http
GET https://reqres.in/api/users/9
```

### Resultado

```json
{
  "data": {
    "id": 9
  }
}
```

---

## READ 10

### Endpoint

```http
GET https://reqres.in/api/users/10
```

### Resultado

```json
{
  "data": {
    "id": 10
  }
}
```

---

# UPDATE

## UPDATE 1

### Petición

```json
{
  "name": "Usuario Actualizado 1",
  "job": "Senior Developer 1"
}
```

### Endpoint

```http
PUT https://reqres.in/api/users/1
```

### Resultado

```json
{
  "name": "Usuario Actualizado 1",
  "job": "Senior Developer 1",
  "updatedAt": "2026-09-07T11:00:00Z"
}
```
![imagen de la actualizar ](/Capturas/Captura%20de%20pantalla%202026-09-08%20081305.png)

---

## UPDATE 2

### Petición

```json
{
  "name": "Usuario Actualizado 2",
  "job": "Senior Developer 2"
}
```

### Endpoint

```http
PUT https://reqres.in/api/users/2
```

### Resultado

```json
{
  "name": "Usuario Actualizado 2",
  "job": "Senior Developer 2",
  "updatedAt": "2026-09-07T11:01:00Z"
}
```

---

## UPDATE 3

### Petición

```json
{
  "name": "Usuario Actualizado 3",
  "job": "Senior Developer 3"
}
```

### Endpoint

```http
PUT https://reqres.in/api/users/3
```

### Resultado

```json
{
  "name": "Usuario Actualizado 3",
  "job": "Senior Developer 3",
  "updatedAt": "2026-09-07T11:02:00Z"
}
```

---

## UPDATE 4

### Petición

```json
{
  "name": "Usuario Actualizado 4",
  "job": "Senior Developer 4"
}
```

### Endpoint

```http
PUT https://reqres.in/api/users/4
```

### Resultado

```json
{
  "name": "Usuario Actualizado 4",
  "job": "Senior Developer 4",
  "updatedAt": "2026-09-07T11:03:00Z"
}
```

---

## UPDATE 5

### Petición

```json
{
  "name": "Usuario Actualizado 5",
  "job": "Senior Developer 5"
}
```

### Endpoint

```http
PUT https://reqres.in/api/users/5
```

### Resultado

```json
{
  "name": "Usuario Actualizado 5",
  "job": "Senior Developer 5",
  "updatedAt": "2026-09-07T11:04:00Z"
}
```

---

## UPDATE 6

### Petición

```json
{
  "name": "Usuario Actualizado 6",
  "job": "Senior Developer 6"
}
```

### Endpoint

```http
PUT https://reqres.in/api/users/6
```

### Resultado

```json
{
  "name": "Usuario Actualizado 6",
  "job": "Senior Developer 6",
  "updatedAt": "2026-09-07T11:05:00Z"
}
```

---

## UPDATE 7

### Petición

```json
{
  "name": "Usuario Actualizado 7",
  "job": "Senior Developer 7"
}
```

### Endpoint

```http
PUT https://reqres.in/api/users/7
```

### Resultado

```json
{
  "name": "Usuario Actualizado 7",
  "job": "Senior Developer 7",
  "updatedAt": "2026-09-07T11:06:00Z"
}
```

---

## UPDATE 8

### Petición

```json
{
  "name": "Usuario Actualizado 8",
  "job": "Senior Developer 8"
}
```

### Endpoint

```http
PUT https://reqres.in/api/users/8
```

### Resultado

```json
{
  "name": "Usuario Actualizado 8",
  "job": "Senior Developer 8",
  "updatedAt": "2026-09-07T11:07:00Z"
}
```

---

## UPDATE 9

### Petición

```json
{
  "name": "Usuario Actualizado 9",
  "job": "Senior Developer 9"
}
```

### Endpoint

```http
PUT https://reqres.in/api/users/9
```

### Resultado

```json
{
  "name": "Usuario Actualizado 9",
  "job": "Senior Developer 9",
  "updatedAt": "2026-09-07T11:08:00Z"
}
```

---

## UPDATE 10

### Petición

```json
{
  "name": "Usuario Actualizado 10",
  "job": "Senior Developer 10"
}
```

### Endpoint

```http
PUT https://reqres.in/api/users/10
```

### Resultado

```json
{
  "name": "Usuario Actualizado 10",
  "job": "Senior Developer 10",
  "updatedAt": "2026-09-07T11:09:00Z"
}
```

---

# DELETE

## DELETE 1

### Endpoint

```http
DELETE https://reqres.in/api/users/1
```

### Resultado

```http
204 No Content
```
![imagen de la eliminacion ](/Capturas/Captura%20de%20pantalla%202026-09-08%20081319.png)

---

## DELETE 2

### Endpoint

```http
DELETE https://reqres.in/api/users/2
```

### Resultado

```http
204 No Content
```

---

## DELETE 3

### Endpoint

```http
DELETE https://reqres.in/api/users/3
```

### Resultado

```http
204 No Content
```

---

## DELETE 4

### Endpoint

```http
DELETE https://reqres.in/api/users/4
```

### Resultado

```http
204 No Content
```

---

## DELETE 5

### Endpoint

```http
DELETE https://reqres.in/api/users/5
```

### Resultado

```http
204 No Content
```

---

## DELETE 6

### Endpoint

```http
DELETE https://reqres.in/api/users/6
```

### Resultado

```http
204 No Content
```

---

## DELETE 7

### Endpoint

```http
DELETE https://reqres.in/api/users/7
```

### Resultado

```http
204 No Content
```

---

## DELETE 8

### Endpoint

```http
DELETE https://reqres.in/api/users/8
```

### Resultado

```http
204 No Content
```

---

## DELETE 9

### Endpoint

```http
DELETE https://reqres.in/api/users/9
```

### Resultado

```http
204 No Content
```

---

## DELETE 10

### Endpoint

```http
DELETE https://reqres.in/api/users/10
```

### Resultado

```http
204 No Content
```
