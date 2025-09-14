# TP_Automation_CodigoFacilito

Este proyecto implementa pruebas automatizadas end to end (E2E) utilizando:
- 🐍 Python
- 🧪 Pytest como framework de testing
- 🕸️ Selenium WebDriver para interacción con el navegador
- 🧱 Patrón Page Object Model (POM) para mantener el código limpio y reutilizable

Las pruebas están diseñadas para validar flujos clave en la aplicación, como login, registro, navegación por categorías, y procesos de compra.

Arquitectura del proyecto:

📁 tests/                → Archivos de test organizados por funcionalidad  
📁 pages/                → Clases POM de cada página de la web  
📁 utils/                → Helpers como driver factory, generadores de datos, config.py y dotenv  
📄 conftest.py           → Fixtures compartidos  
📄 pytest.ini            → Configuración de Pytest  
📄 requirements.txt      → Dependencias del proyecto

Requisitos previos:
- Python 3.10+
- Google Chrome (u otro navegador compatible)
- pip (instalador de paquetes)

Instalar dependencias:
pip install -r requirements.txt

Ejecutar los tests:
Desde la raíz del proyecto, ejecutá:
👉 Para correr todos los tests:
pytest -v
👉 Para correr un archivo específico:
pytest tests/test_login_and_sign_up.py
👉 Para correr por markers (ej: login):
pytest tests/test_navigation_and_content.py -m navigation

markers:
- api = API related tests
- e2e = End to end flow test
- happy_path = Happy path tests
- fail = Fail intended tests
- login = Login flow related tests
- sign_up = Sign un flow related tests
- search = Search flow related tests
- shop = Shop flow related test
- navigation = Navigation related tests
- content_verification = Content like text verification tests
- 

Actualmente se utiliza Chrome por defecto.  
La configuración está en `utils/driver_factory.py`.

Opcionalmente podés modificarlo para correr en modo headless, otros navegadores, etc.
Para realizar los test en modo headless (sin visual del navegador) modificar el archivo:
conftest.py linea 16
Con visual del navegador: driver = create_driver(headless=headless)
Cambiar el valor de headless a True:
Sin visual del navegador: driver = create_driver(headless=True)





📌 Faltantes a mi gusto:
- Agregar los locator faltantes de la cart_page.
- Crear todos los métodos custom para cada product_number en la product_detail_page.
- Arreglar algunos locator, en lugar de usar XPATH, usar TAG_NAME o CSS_SELECTOR de ser posible.
- Validar todo en el formulario de checkout.
- Validar headings y textos, que digan lo que deben decir.
- Validar que el botón "-" en la product detail page no haga nada, o que se encuentre deshabilitado preferentemente.
- Test para validar que se actualice correctamente la cantidad de productos que se muestra al apretar los botones "-" y "+" en la product detail page.
- Test para validar que el precio se actualice correctamente al agregar productos.
- Test para validar que el precio en la product details page y el cart sean el mismo.
- Test para validar que el precio en el detalle del cart y el Order summary sean iguales.
- Test para validar la suma de valores en el Order summary, tanto en el cart como en el checkout.
- Test para validar por qué a veces los placeholder cambian aleatoriamente.
- Test para validar etiquetas/labels y placeholder de los input.

Tests que agregaría:
- Validar la aparición de un mensaje de que el producto fue agregado al carrito satisfactoriamente.
- Validar la aparición de un mensaje de que el producto fue marcado como favorito, también de que seguramente la visual del botón cambie, por ejemplo un cambio de color por CSS.
- Validar mensajes de error en el login o sign up, en caso de que fueran custom y no de navegador.
- Validar el search flow, que aparezcan resultados válidos relacionados a la búsqueda, por ejemplo que contentan la palabra buscada.


📌To Do / Ideas futuras
- Integración con CI (GitHub Actions)
- Soporte multi-navegador
- Generación de reportes HTML automáticos


