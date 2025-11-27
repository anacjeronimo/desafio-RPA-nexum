from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def buscar_preco_mercado_livre():
    options = Options()
    options.add_argument("--headless")  # roda em segundo plano
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://lista.mercadolivre.com.br/xbox-series-s")
        driver.implicitly_wait(5)

        item = driver.find_element(By.CSS_SELECTOR, ".ui-search-result__content")
        titulo = item.find_element(By.CSS_SELECTOR, ".ui-search-item__title").text
        preco = item.find_element(By.CSS_SELECTOR, ".andes-money-amount__fraction").text
        preco = float(preco.replace(".", "").replace(",", "."))

        return {
            "loja": "Mercado Livre",
            "titulo": titulo,
            "preco": preco
        }
    except Exception as e:
        return {"loja": "Mercado Livre", "erro": str(e)}
    finally:
        driver.quit()
