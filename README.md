
# Curso de Automatización n8n con ChromaDB

## Estructura del Proyecto

Este paquete contiene:
- `chroma-server`: Imagen oficial de ChromaDB (puerto 8000)
- `python-executor`: Microservicio en Python que se conecta a ChromaDB
- `ngrok`: Configuración para exponer ambos servicios con URLs públicas

## Requisitos

- Docker + Docker Compose
- Cuenta de ngrok gratuita: https://dashboard.ngrok.com

## Pasos para montar todo

1. Clona el repositorio o descomprime el zip.
2. Edita `ngrok/ngrok.yml` y pon tu `authtoken` personal.
3. Ejecuta los contenedores:

```bash
docker compose up --build -d
```

4. En otra terminal, lanza ngrok:

```bash
ngrok start --all --config ngrok/ngrok.yml
```

5. Accede a los servicios:
   - Python Executor: `https://<ngrok-url-ejecutor>/run`
   - ChromaDB: `https://<ngrok-url-chroma>/docs` (requiere que la imagen tenga API pública)

## Notas

- Puedes editar `python-executor/app.py` para lanzar tareas vía n8n.
- Desde n8n puedes llamar al executor con HTTP Request Node.
- El executor puede importar `chromadb.HttpClient(...)` y apuntar al host `chroma-server:8000`.

