import requests

def scan_url(target_url, word):
    """escanea un sitio web buscando una palabra especifica en las rutas"""
    
    # construye la url de prueba
    full_url = f"{target_url.rstrip('/')}/{word}"
    
    try:
        response = requests.get(full_url, timeout=5)
        
        # si la respuesta es 200, el recurso existe
        if response.status_code == 200:
            print(f"[+] encontrado: {full_url} (codigo {response.status_code})")
        elif response.status_code == 403:
            print(f"[!] acceso denegado: {full_url} (codigo {response.status_code})")
        elif response.status_code == 404:
            print(f"[-] no encontrado: {full_url} (codigo {response.status_code})")
        else:
            print(f"[?] estado desconocido: {full_url} (codigo {response.status_code})")
    
    except requests.exceptions.RequestException as e:
        print(f"[x] error al conectar con {full_url}: {e}")

def leer_wordlist(archivo):
    """lee un archivo de wordlist y devuelve una lista de palabras"""
    try:
        with open(archivo, 'r') as f:
            palabras = [linea.strip() for linea in f if linea.strip()]
        return palabras
    except FileNotFoundError:
        print(f"[x] error: no se encontro el archivo {archivo}")
        return []
    except Exception as e:
        print(f"[x] error al leer el archivo: {e}")
        return []

# --- parametros del escaneo ---
TARGET_URL = "http://127.0.0.1:8000"  # cambia por el sitio a escanear
WORDLIST_FILE = "wordlist.txt"         # archivo con la lista de palabras

# --- ejecutar escaneo ---
print(f"buscando palabras de '{WORDLIST_FILE}' en {TARGET_URL}...\n")

# leer la wordlist
palabras = leer_wordlist(WORDLIST_FILE)

if not palabras:
    print("[x] no se encontraron palabras para escanear")
else:
    print(f"[*] cargadas {len(palabras)} palabras para probar\n")
    for palabra in palabras:
        scan_url(TARGET_URL, palabra)
