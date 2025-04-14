# Extractor de Requerimientos con DSPy

Este proyecto utiliza DSPy y modelos de lenguaje grandes (LLM's) para extraer automáticamente requerimientos estructurados a partir de transcripciones de reuniones de levantamiento de requerimientos.

## Descripción

El extractor de requerimientos analiza transcripciones de reuniones y extrae de forma inteligente:

- Requerimientos funcionales
- Requerimientos no funcionales
- Personas interesadas (stakeholders)
- Elementos de acción
- Preguntas abiertas
- Restricciones del proyecto

Esta herramienta es útil para equipos de desarrollo de software que desean automatizar y simplificar el proceso de documentación de requerimientos, asegurando que no se pierda información importante durante las reuniones con clientes.

## Requisitos

- Python 3.8 o superior
- DSPy
- Acceso a la API de Groq (API key)
- python-dotenv (opcional, solo si su entorno no carga archivos .env automáticamente)

## Instalación

1. Clone este repositorio:

   ```
   git clone https://github.com/yourusername/requirements-extractor.git
   cd requirements-extractor
   ```

2. Instale las dependencias usando uv:

   ```
   uv init
   uv sync
   ```

   > **Nota**: Si prefiere usar pip en lugar de uv, puede instalar las dependencias con:
   >
   > ```
   > pip install dspy groq python-dotenv
   > ```

3. Configure su API key de Groq. Tiene dos opciones:

   **Opción A: Usar variables de entorno directamente**

   ```
   export GROQ_API_KEY="su_api_key_aquí"
   ```

   **Opción B: Crear un archivo .env**

   Cree un archivo llamado `.env` en el directorio raíz del proyecto con el siguiente contenido:

   ```
   GROQ_API_KEY=su_api_key_aquí
   ```

   En algunos entornos, el archivo `.env` se cargará automáticamente. Si no funciona, puede instalar python-dotenv:

   ```
   uv add python-dotenv
   ```

   ó

   ```
   pip install python-dotenv
   ```

   Y modificar el inicio de su script para cargar explícitamente las variables:

   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()  # Carga variables desde .env
   ```

   No olvide agregar `.env` a su archivo `.gitignore` para evitar compartir sus claves de API:

## Uso

1. Prepare una transcripción de reunión y guárdela como archivo de texto (por ejemplo, `transcripcion_reunion.txt`).

2. Ejecute el script:

   ```
   python main.py
   ```

3. El script analizará la transcripción y mostrará los requerimientos extraídos organizados en categorías.

## Ejemplo de salida

```
=== REQUERIMIENTOS FUNCIONALES ===
1. Sistema de gestión de inventario en tiempo real
2. Escaneo de códigos de barras/QR para productos
3. Gestión de múltiples ubicaciones dentro del almacén
...

=== REQUERIMIENTOS NO FUNCIONALES ===
1. Acceso desde dispositivos móviles y tablets robustas
2. Integración con sistema contable SAP Business One
3. Seguridad con diferentes niveles de acceso
...

=== PERSONAS INTERESADAS ===
1. María Rodríguez (MR) - Gerente de Proyecto
2. Carlos Vega (CV) - Analista de Sistemas
...
```

## Personalización

Puede modificar la clase `RequirementsExtraction` para cambiar los campos de salida o ajustar las descripciones según sus necesidades específicas.

## Cómo funciona

El proyecto utiliza DSPy, un framework para programación con modelos de lenguaje, para estructurar la extracción de información. El flujo es el siguiente:

1. Se define una firma (`Signature`) que especifica los campos de entrada y salida.
2. Se implementa un módulo (`Module`) que utiliza el razonamiento paso a paso (`ChainOfThought`) para extraer información estructurada.
3. El script lee la transcripción, aplica el extractor y muestra los resultados organizados.

## Solución de problemas

### Problemas con caracteres especiales

Si encuentra problemas con caracteres acentuados o especiales, asegúrese de que:

- Los archivos de texto estén guardados en codificación UTF-8
- Al abrir archivos, use `encoding="UTF-8"` (como ya está configurado en el código)

## Contribuir

Las contribuciones son bienvenidas. Por favor, abra un issue para discutir cambios importantes antes de enviar un pull request.

## Licencia

[Especifique su licencia aquí, por ejemplo MIT, Apache 2.0, etc.]
