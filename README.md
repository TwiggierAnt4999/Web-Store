Materia: Tópicos Avanzados de Programación
Alumno: Gálvez Cadenas Oscar 
Docente: Caballero Alfaro Arístides
Proyecto: TechStore – Catálogo de Productos
Ejecución: Desplegado en Render (Hosting Web)

Objetivo
Desarrollar una aplicación web en Python con Flet, que muestre un catálogo de productos tecnológicos en formato de tarjetas reutilizables. El propósito es aplicar conceptos de programación modular, diseño de interfaces gráficas y despliegue en un servicio de hosting en la nube (Render).

Desarrollo
- Se definió un modelo de datos con dataclass Producto, que contiene atributos como id, nombre, descripcion, precio y ruta_imagen.
- Se creó un componente reutilizable TarjetaProducto, que muestra:
- Imagen del producto.
- Nombre y descripción.
- Precio en formato destacado.
- Botones de interacción (favorito y agregar al carrito).
- Se generó una lista de productos tecnológicos (Laptop, Mouse, Teclado, Monitor, Audífonos).
- Se construyó la interfaz con un Row que organiza las tarjetas de manera responsiva y con estilo visual moderno.
- Se configuró la aplicación para ejecutarse en WEB_BROWSER, con un directorio de assets para las imágenes.
- Finalmente, se desplegó en Render, permitiendo acceso público al catálogo desde cualquier navegador.

Ejecución en Render
- El proyecto fue lanzado en Render, lo que permite:
- Acceso remoto al catálogo desde cualquier dispositivo con navegador.
- Distribución sencilla sin necesidad de instalación local.
- Escalabilidad y disponibilidad en la nube.

Resultados
- La aplicación muestra correctamente las tarjetas de productos con diseño atractivo.
- El catálogo es dinámico y organizado, con botones de interacción.
- El despliegue en Render asegura que el proyecto esté disponible en línea.

Conclusiones
- La práctica permitió reforzar conocimientos sobre:
- Uso de dataclasses para modelar datos.
- Creación de componentes reutilizables en Flet.
- Diseño de interfaces responsivas y modernas.
- Despliegue de aplicaciones Python en la nube mediante Render.
- Este proyecto constituye un ejemplo funcional de cómo integrar programación modular, diseño visual y despliegue web en un entorno real de hosting.