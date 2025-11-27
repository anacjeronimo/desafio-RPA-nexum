from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def buscar_preco_casas_bahia():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.casasbahia.com.br/xbox-series-s/b")
        driver.implicitly_wait(5)

        item = driver.find_element(By.CSS_SELECTOR, ".ProductCard__Card-sc-1hlrxcw-0")
        titulo = item.find_element(By.CSS_SELECTOR, ".ProductCard__Title-sc-1hlrxcw-4").text
        preco = item.find_element(By.CSS_SELECTOR, ".ProductPrice__PriceValue-sc-1hlrxcw-7").text
        preco = preco.replace("R$", "").replace(".", "").replace(",", ".").strip()
        preco = float(preco)

        return {
            "loja": "Casas Bahia",
            "titulo": titulo,
            "preco": preco
        }
    except Exception as e:
        return {"loja": "Casas Bahia", "erro": str(e)}
    finally:
        driver.quit()
