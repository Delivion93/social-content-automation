# 🪺 Nidochus

**Creación inteligente de contenido multiagente para redes sociales mediante Inteligencia Artificial.**

Nidochus es una plataforma basada en una arquitectura multiagente capaz de generar campañas de marketing adaptadas a Instagram, Facebook y LinkedIn. El sistema utiliza modelos LLM locales mediante Ollama, LangGraph para la orquestación de agentes y ChromaDB como base de datos vectorial para implementar RAG (Retrieval-Augmented Generation).

---

# 🚀 Tecnologías utilizadas

- Python 3.13
- FastAPI
- LangGraph
- LangChain
- Ollama
- ChromaDB
- Docker & Docker Compose
- HTML, CSS y JavaScript
- Jinja2

---

# 📦 Ejecución con Docker

## 1. Construir e iniciar los contenedores

```bash
docker compose up --build
```

---

## 2. Descargar los modelos de Ollama (solo la primera vez)

Modelo LLM:

```bash
docker exec -it social-content-automation-ollama-1 ollama pull gemma3:4b
```

Modelo de embeddings para ChromaDB:

```bash
docker exec -it social-content-automation-ollama-1 ollama pull nomic-embed-text
```

---

## 3. Verificar los modelos instalados

```bash
docker exec -it social-content-automation-ollama-1 ollama list
```

Deberían aparecer:

```
gemma3:4b
nomic-embed-text
```

---

## 4. Abrir la aplicación

```
http://localhost:8000
```

---

# 📁 Arquitectura del proyecto

```
social-content-automation/

│
├── agents/
├── graph/
├── rag/
├── schemas/
├── services/
├── static/
├── templates/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── main.py
```

---

# 🤖 Arquitectura multiagente

El flujo principal de generación está coordinado mediante LangGraph.

Los agentes implementados son:

- Strategy Agent
- Copy Agent
- Image Prompt Agent
- Compliance Agent
- Editor Agent (Chat)

---

# 📚 RAG (Retrieval-Augmented Generation)

El Editor Agent utiliza ChromaDB para recuperar automáticamente las normas específicas de cada plataforma antes de modificar una campaña.

Fuentes utilizadas:

- Instagram
- Facebook
- LinkedIn

---

# 🐳 Docker

La aplicación se ejecuta mediante Docker Compose utilizando dos contenedores:

- FastAPI
- Ollama

Los modelos descargados se almacenan en un volumen persistente para evitar volver a descargarlos en futuros despliegues.

---

# 👨‍💻 Equipo

Proyecto desarrollado por el equipo **Nidochus** como solución basada en Inteligencia Artificial para la generación automática de contenido para redes sociales.