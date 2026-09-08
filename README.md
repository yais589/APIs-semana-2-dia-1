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
