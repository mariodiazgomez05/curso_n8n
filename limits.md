# Limitaciones del Proyecto ChromaDB + n8n + Python Executor

Este documento resume las limitaciones actuales del proyecto y las soluciones propuestas para garantizar robustez, escalabilidad y seguridad en su uso.

---

## 1. Uso de Ngrok Gratuito

**Limitación:**

* Solo permite una sesión activa por cuenta.
* Las URLs son temporales y cambian cada vez que se reinicia.

**Soluciones:**

* Actualizar a **Ngrok Pro** para obtener subdominios fijos y múltiples túneles simultáneos.
* Alternativa: Desplegar en VPS (Hetzner, DigitalOcean) con dominio propio + HTTPS.

---

## 2. No Persistencia de Datos

**Limitación:**

* Al reiniciar el contenedor de ChromaDB, los datos se pierden.

**Solución:**

* Montar volumen persistente en `docker-compose.yml`:

  ```yaml
  volumes:
    - ./chroma-data:/data
  ```

---

## 3. Flask en Modo Desarrollo

**Limitación:**

* `python-executor` usa servidor de desarrollo Flask no apto para producción.

**Solución:**

* Usar `gunicorn` como servidor WSGI:

  ```dockerfile
  CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
  ```

---

## 4. Falta de Autenticación

**Limitación:**

* Cualquier usuario con la URL puede añadir documentos.

**Soluciones:**

* Añadir autenticación por token o cabecera de API key.
* O montar proxy NGINX con autenticación básica.

---

## 5. Sin Panel de Logs o Métricas

**Limitación:**

* Difícil monitoreo; hay que usar `docker logs`.

**Soluciones:**

* Añadir logging persistente en archivo.
* O montar Loki + Grafana (opcional).

---

## 6. Integración limitada en n8n

**Limitación:**

* n8n usa nodos HTTP genéricos, lo que complica interacciones con Chroma.

**Soluciones:**

* Crear nodo personalizado n8n para Chroma.
* O mejorar `python-executor` con endpoints más específicos y simples.

---

## 7. Sin Gestión de Errores HTTP

**Limitación:**

* No hay validaciones ni respuestas de error informativas.

**Solución:**

* Añadir manejo de excepciones en Flask:

  ```python
  return jsonify({"error": "Falta parametro X"}), 400
  ```

---

## 8. Entorno Compartido entre Usuarios

**Limitación:**

* Todos los alumnos usan misma instancia de ChromaDB.

**Soluciones:**

* Crear colección distinta por usuario (`pruebas_mario`, `pruebas_luisa`, etc.).
* Alternativa compleja: Instancia por alumno.

---

## 9. No Hay Interfaz de Administración

**Limitación:**

* Todo se hace por consola o `curl`, sin interfaz.

**Solución:**

* Crear frontend web básico en React o Flask para gestionar colecciones y documentos.

---

## 10. Dependencia del PC local

**Limitación:**

* Si el ordenador de Mario se apaga, se pierde todo.

**Solución:**

* Subir la solución a VPS con despliegue automatizado.
* Usar GitHub Actions o scripts para levantarlo rápidamente.

---


