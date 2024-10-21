# Gestor de Notas

## Objetivo
Iniciar un proyecto en Django personalizado con los apellidos de la pareja asignada. Este proyecto permitirá gestionar notas para cada usuario autenticado en el sistema.

## 1. Configuración del Proyecto

### 1.1 Nombre del Proyecto
Iniciar un nuevo proyecto de Django llamado `project_[Apellido1Apellido2]`, usando los apellidos de los integrantes del equipo.

### 1.2 Nombre de la Aplicación
Crear una nueva aplicación llamada `notes_[NombreApellido1Apellido2]` dentro del proyecto.

## 2. Modelos

En la aplicación `notes_[Apellido1Apellido2]`, crear un modelo `Note` con los siguientes campos:

- **user**: `ForeignKey` hacia la tabla `User`, con `on_delete=models.CASCADE` y `related_name='notes'`.
- **title**: `CharField`, para el título de la nota.
- **content**: `TextField`, para el contenido de la nota.
- **creation_date**: `DateTimeField`, con `auto_now_add=True`.

### Método especial `__str__`
Retornará el `title` de la nota.

## 3. Vistas y URLs

Implementar las vistas siguientes:

- **Lista de notas**: Mostrar todas las notas existentes.
- **Detalle de nota**: Ver el contenido de una nota específica.
- **Crear nota**: Formulario para crear una nueva nota.
- **Editar nota**: Formulario para modificar una nota existente.
- **Eliminar nota**: Opción para eliminar una nota.

Configura las URLs en `urls.py` de `notes_[Apellido1Apellido2]`:

- **Lista**: `('')`
- **Detalle**: `('<int:pk>/')`
- **Creación**: `('new/')`
- **Edición**: `('<int:pk>/edit/')`
- **Eliminación**: `('<int:pk>/delete/')`

## 4. Templates

En la carpeta `templates` dentro de `notes_[Apellido1Apellido2]`, crear los siguientes archivos:

- `note_list_[Apellido1Apellido2].html`: Para mostrar la lista de notas.
- `note_detail_[Apellido1Apellido2].html`: Para mostrar una nota individual.
- `note_edit_[Apellido1Apellido2].html`: Para crear/editar notas. Usar la misma plantilla en ambos casos.

## 5. Casos de Prueba

Escribir casos de prueba que cubran:

- Creación correcta de una nueva nota.
- Actualización de datos de una nota existente.
- Visualización de detalles de una nota.
- Eliminación de una nota.
- Carga de la lista de notas.

# Instrucciones Adicionales

## 6. Instrucciones adicionales:

### 6.1 Configuración de `settings.py`
- Actualiza `settings.py` para incluir `notes_[Apellido1Apellido2]` en `INSTALLED_APPS`.
- Configura las rutas de autenticación y redirecciona la raíz del servidor.

### 6.2 Migraciones
- Realiza las migraciones necesarias con:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

### 6.3 Ejecutar el Proyecto
- Ejecuta el proyecto con:
    ```bash
    python manage.py runserver
    ```

## 7. Entrega

Debes proporcionar el código completo, comprimido, con un archivo `INSTRUCCIONES_[Apellido1Apellido2]` que incluya:

- Nombres de los integrantes.
- Descripción de configuración, ejecución y pruebas del proyecto.

## 8. Evaluación

- Funcionalidad completa del proyecto (agregar, ver, editar, eliminar notas).
- Organización del código y correcta separación de lógica en vistas, URLs y modelos.
- Implementación y utilidad de los casos de prueba.
- Se penalizará con un punto menos por cada acción que no funcione y un punto si no está implementado su caso de prueba.
- Si la documentación o la base de datos SQLite es la misma que otro equipo, se bajará tres puntos de la calificación del examen.
