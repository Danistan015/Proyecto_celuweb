from flask import Flask, render_template, request, jsonify
from selenium.webdriver.support.ui import WebDriverWait
from instagram_scraper import iniciar_chrome, login_instagram, descargar_fotos_instagram

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el scraper
@app.route('/scrape', methods=['POST'])
def scrape():
    hashtag = request.form['hashtag']
    minimo = int(request.form.get('minimo', 300))  # Valor por defecto 300
    
    try:
        # Iniciar Chrome
        driver = iniciar_chrome()
        wait = WebDriverWait(driver, 10)
        
        # Iniciar sesión en Instagram
        res = login_instagram(driver, wait)
        
        if res == "ERROR":
            driver.quit()
            return jsonify({'status': 'error', 'message': 'Error al iniciar sesión en Instagram.'})
        
        # Ejecutar el scraper para descargar fotos
        descargar_fotos_instagram(driver, hashtag, minimo,wait)
        
        driver.quit()
        
        return jsonify({'status': 'success', 'message': f'Se han descargado fotos de #{hashtag}'})
    
    except Exception as e:
        # En caso de error
        return jsonify({'status': 'error', 'message': f'Ocurrió un error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
