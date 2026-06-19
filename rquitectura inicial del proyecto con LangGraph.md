# Arquitectura inicial del proyecto con LangGraph

La aplicación se implementará como un flujo de trabajo basado en LangGraph, donde cada agente será un nodo especializado dentro del grafo.

## Flujo principal

START
↓
Strategist Agent
↓
Copywriter Agent
↓
Compliance Agent
↓
END

## Descripción de los nodos

### 1. Strategist Agent

Responsabilidad:

* Analizar la información proporcionada por el usuario.
* Definir la idea principal de la campaña.
* Identificar el público objetivo.
* Establecer el tono de comunicación.

Entrada:

* Producto o servicio.
* Público objetivo.
* Descripción de la marca.

Salida:

* Nombre de la campaña.
* Concepto principal.
* Tono de comunicación.

---

### 2. Copywriter Agent

Responsabilidad:

* Generar contenido adaptado a diferentes redes sociales.

Entrada:

* Concepto de campaña.
* Tono de comunicación.

Salida:

* Copy para Instagram.
* Copy para Facebook.
* Copy para LinkedIn.

---

### 3. Compliance Agent

Responsabilidad:

* Revisar la calidad del contenido generado.
* Verificar que el tono sea coherente.
* Detectar posibles problemas de cumplimiento.

Entrada:

* Contenido generado por el Copywriter Agent.

Salida:

* Estado de aprobación.
* Lista de observaciones o recomendaciones.

---

## Estado compartido (State)

Todos los nodos compartirán un estado común que se irá enriqueciendo durante la ejecución del flujo.

Ejemplo de información almacenada en el State:

* producto
* audiencia
* descripcion_marca
* campaign_name
* concept
* tone
* instagram_post
* facebook_post
* linkedin_post
* approved
* feedback

---

## Posible extensión futura

Si el tiempo lo permite, se añadirá un nodo adicional:

Strategist Agent
↓
Prompt Designer Agent
↓
Generación de imágenes

Este agente será responsable de crear prompts optimizados para modelos de generación de imágenes (DALL-E, Flux, Stable Diffusion, etc.).

La arquitectura está diseñada para permitir la incorporación de nuevos nodos sin modificar el flujo principal.
