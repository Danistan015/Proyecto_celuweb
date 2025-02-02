# Instagram Scraper 🖼️

Este proyecto es una aplicación que combina **Selenium** y **Flask** para realizar scraping de fotos en Instagram basado en un hashtag. Con esta herramienta puedes descargar imágenes, guardar sus datos en un archivo CSV y obtener estadísticas como el promedio de "Me Gusta" (esta funcionalidad aun no esta completa). 🚀

---

## Características ✨

- **Inicio de sesión automático**: Usa cookies o credenciales para iniciar sesión en Instagram.
- **Búsqueda por hashtag**: Encuentra y descarga imágenes relacionadas con un hashtag específico.
- **Archivo CSV**: Genera un archivo con datos de las imágenes descargadas.
- **Estadísticas básicas**: Calcula el promedio de "Me Gusta".
- **Interfaz web amigable**: Una sencilla página HTML con formulario para manejar el scraping.

---

## Tecnologías utilizadas 🛠️

- **Python 3.9+**
- **Flask**: Para la interfaz web.
- **Selenium**: Para automatizar la interacción con Instagram.
- **WebDriver Manager**: Gestión automática del driver de Chrome.
- **HTML y CSS**: Para la presentación visual.

---

## Instalación y configuración ⚙️

### Requisitos previos

1. **Python 3.9+** instalado.
2. **Google Chrome** instalado en tu sistema.
3. **Credenciales de Instagram** válidas.

### Pasos para instalar

1. Clona el repositorio:
 
   git clone https://github.com/tu-usuario/instagram-scraper.git
   cd instagram-scraper
Instala las dependencias:

pip install -r requirements.txt
Configura tus credenciales de Instagram en el archivo instagram_scraper.py:

USER_IG = 'tu_usuario_instagram'
PASS_IG = 'tu_contraseña'
Asegúrate de tener el archivo CSS en static/styles.css.


python app.py
Abre tu navegador y ve a:

http://127.0.0.1:5000/

Uso 🚀
En la interfaz, ingresa el hashtag que deseas buscar.
Define el número mínimo de fotos que deseas descargar.
Haz clic en "Iniciar Scraping".
Las fotos se guardarán en una carpeta con el nombre del hashtag, y los datos se almacenarán en un archivo CSV.
Estructura del proyecto 📂
app.py: Código principal de la aplicación Flask.
instagram_scraper.py: Funciones de scraping e interacción con Instagram.
static/styles.css: Archivo CSS con los estilos de la página.
templates/index.html: Página HTML que sirve como interfaz.
requirements.txt: Lista de dependencias necesarias.


Notas 📝
Evita exceder los límites de acceso de Instagram. Usar esta herramienta de manera excesiva puede bloquear tu cuenta temporalmente.
Las cookies se guardan en instagram1.cookies para facilitar inicios de sesión futuros.
Puedes ajustar los parámetros de scraping directamente en instagram_scraper.py.
