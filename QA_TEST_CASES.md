# Listado casos de pruebas manuales QA para Cuidos

## 1. Registro, autenticación y grupos

- Verificar que un usuario pueda registrarse con datos válidos.  
- Validar que no se pueda registrar con un email ya usado o datos inválidos (email mal formado, contraseña débil).  
- Probar que el usuario pueda iniciar sesión con credenciales correctas y no con incorrectas.  
- Probar la recuperación de contraseña vía email.  
- Verificar que un usuario pueda ingresar un código de grupo para unirse a un grupo existente.  
- Verificar que se muestre un mensaje de error claro si el código de grupo es inválido o expirado.  
- Validar si el usuario puede pertenecer a más de un grupo simultáneamente.  
- Comprobar que al pertenecer a varios grupos, el usuario pueda navegar y ver correctamente la información de cada uno.  
- Verificar que al salir de un grupo, el usuario pierda acceso a sus datos y tareas.  

## 2. Creación y gestión de grupos

- Verificar que un usuario pueda crear un grupo con datos válidos.  
- Validar que se genere un código único para invitar usuarios al grupo.  
- Probar la edición de la información del grupo (nombre, descripción).  
- Verificar que el listado de miembros del grupo se actualice al agregar o eliminar usuarios.  
- Probar que un grupo solo pueda eliminarse bajo condiciones específicas (ej. sin tareas activas).  

## 3. Asignación de tareas y AI

- Verificar que la IA sugiera tareas basadas en preferencias, habilidades y disponibilidad de usuarios.  
- Comprobar que los usuarios vean claramente las tareas asignadas por la IA.  
- Validar que la IA no sobrecargue a un solo usuario ni asigne tareas repetidas.  
- Probar la posibilidad de modificar manualmente una asignación propuesta por la IA y guardar los cambios.  
- Verificar que la IA se reajuste después de cambios manuales (si corresponde).  

## 4. Gestión y seguimiento de tareas

- Verificar creación, edición y eliminación de tareas con campos obligatorios (nombre, responsable, fecha, descripción).  
- Comprobar que las tareas cambien correctamente de estado (pendiente, en progreso, completada).  
- Verificar que se envíen notificaciones sobre cambios de estado o fechas próximas.  
- Probar que los usuarios puedan añadir comentarios o evidencia a tareas (fotos, notas).  

## 5. Reportes visuales y estadísticas

- Verificar que los reportes muestren datos reales y actualizados de distribución de tareas.  
- Probar que gráficos y tablas sean claros, comprensibles y responsivos.  
- Validar la exportación o compartición de reportes (si está disponible).  

## 6. Usabilidad y experiencia

- Probar navegación fluida entre pantallas, grupos y tareas.  
- Verificar que todos los botones y enlaces funcionen correctamente y tengan texto descriptivo.  
- Comprobar que la app sea responsiva en distintos dispositivos (móvil, tablet).  
- Validar mensajes de error claros y útiles para el usuario.  

## 7. Seguridad y permisos

- Probar que usuarios no autenticados no puedan acceder a funcionalidades internas o datos privados.  
- Verificar que solo los miembros de un grupo puedan ver y modificar sus tareas.  
- Comprobar que un usuario no pueda acceder o modificar datos de grupos a los que no pertenece.  

## 8. Casos especiales y concurrencia

- Verificar manejo correcto de usuarios con roles o pertenencias múltiples en grupos.  
- Probar que la IA funcione correctamente bajo carga con múltiples usuarios y tareas.  
- Verificar estabilidad y manejo correcto de cambios simultáneos por varios usuarios.  

## 9. Accesibilidad

- Probar navegación completa por teclado (sin usar mouse).  
- Verificar que el tamaño de fuente sea legible y permita ajuste según configuración del dispositivo o navegador.  
- Comprobar que los iconos SVG usados sigan el diseño Material 3 o el diseño visual oficial de la app.  
- Verificar que los contrastes de color cumplan con estándares WCAG para accesibilidad visual.  
- Probar compatibilidad con lectores de pantalla (VoiceOver, NVDA, JAWS).  
- Verificar que los elementos interactivos tengan etiquetas accesibles (aria-labels, roles).  
