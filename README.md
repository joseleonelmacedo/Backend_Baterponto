# Running the application

### Install Python

### Install virtual env
```
pip install virtualenv
```

### Activate virtualenv

#### Navigate until the root folder
```
python -m virtualenv venv
```

#### Activate virtual env
```
. venv/Scripts/activate
```

#### Install dependencies
```
pip install -r requirements.txt
```

#### Install dependencies
```
python src/app.py
```


## Endpoints

### 1. Cadastro de Usuário

- **Endpoint:** `/sidi_ponto/v1/cadastro`
- **Método:** `POST`
- **Corpo (JSON):**
  ```json
  {
    "name": "Seu Nome",
    "email": "seu.email@exemplo.com",
    "password": "sua_senha"
  }
  ```

### 2. Login de Usuário

- **Endpoint:** `/sidi_ponto/v1/login`
- **Método:** `POST`
- **Corpo (JSON):**
  ```json
  {
    "email": "seu.email@exemplo.com",
    "password": "sua_senha"
  }
  ```

### 3. Registrar Entrada/Saída de Ponto

- **Endpoint:** `/sidi_ponto/v1/criar`
- **Método:** `POST`
- **Corpo (JSON):**
  ```json
  {
    "email": "seu.email@exemplo.com",
    "date": "DD-MM-AAAA",   // 23/11/2023
    "entries": "HH:MM",  // 08:00 -> Opcional
    "exits": "HH:MM"     // 18:00 -> Opcional
  }
  ```

### 4. Listar Registros de Ponto do Usuário

- **Endpoint:** `/sidi_ponto/v1/listar`
- **Método:** `POST`
- **Corpo (JSON):**
  ```json
  {
    "email": "seu.email@exemplo.com"
  }
  ```

## Exemplos de Requisições usando o Postman

1. **Cadastro de Usuário:**
   - **URL:** `http://localhost:5000/sidi_ponto/v1/cadastro`
   - **Corpo (JSON):**
     ```json
     {
       "name": "Fulano de Tal",
       "email": "fulano@exemplo.com",
       "password": "senha_segura"
     }
     ```

2. **Login de Usuário:**
   - **URL:** `http://localhost:5000/sidi_ponto/v1/login`
   - **Corpo (JSON):**
     ```json
     {
       "email": "fulano@exemplo.com",
       "password": "senha_segura"
     }
     ```

3. **Registrar Entrada de Ponto:**
   - **URL:** `http://localhost:5000/sidi_ponto/v1/criar`
   - **Corpo (JSON):**
     ```json
     {
       "email": "fulano@exemplo.com",
       "date": "2023-11-23",
       "entries": "09:00",
       "exits": ""
     }
     ```
    
3. **Registrar Saída de Ponto:**
   - **URL:** `http://localhost:5000/sidi_ponto/v1/criar`
   - **Corpo (JSON):**
     ```json
     {
       "email": "fulano@exemplo.com",
       "date": "2023-11-23",
       "entries": "",
       "exits": "17:00"
     }

4. **Listar Registros de Ponto do Usuário:**
   - **URL:** `http://localhost:5000/sidi_ponto/v1/listar`
   - **Corpo (JSON):**
     ```json
     {
       "email": "fulano@exemplo.com"
     }
     ```