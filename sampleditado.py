import requests
from bs4 import BeautifulSoup, Comment
import re

def extraer_emails(texto):
    """extrae direcciones de correo electronico usando expresion regular"""
    patron_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(patron_email, texto)

url = "http://127.0.0.1:8000/victima.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#  extraer todos los enlaces
enlaces = [a["href"] for a in soup.find_all("a", href=True)]
print("=== enlaces encontrados ===")
print('\n'.join(enlaces))

#  extraer todos los comentarios html
print("\n=== comentarios encontrados ===")
comentarios = soup.find_all(string=lambda texto: isinstance(texto, Comment))
for comentario in comentarios:
    print(comentario.strip())

#  extraer direcciones de correo electronico
print("\n=== correos electronicos encontrados ===")
# de etiquetas <a> con mailto:
emails_mailto = [a["href"][7:] for a in soup.find_all("a", href=True) if a["href"].startswith("mailto:")]
# de texto en la pagina usando regex
emails_texto = extraer_emails(response.text)
# combinar y eliminar duplicados
todos_emails = list(set(emails_mailto + emails_texto))
print('\n'.join(todos_emails))
