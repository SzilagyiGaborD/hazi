import pytest
from bs4 import BeautifulSoup

# Teszt fájl betöltése
def load_html():
    with open("hpux.html", "r", encoding="utf-8") as file:
        return file.read()

# Teszt a HP-UX tartalomra
def test_hpux_txt_content():
    html_content = load_html()
    soup = BeautifulSoup(html_content, "html.parser")
    
    hpux_txt_content = soup.find("p").text.strip()
    with open("hpux.txt", "r", encoding="utf-8") as file:
        expected_content = file.read().strip()
    
    assert hpux_txt_content == expected_content, "A hpux.txt tartalma nem egyezik."

# Teszt a magyar nyelv beállításra
def test_language_setting():
    html_content = load_html()
    soup = BeautifulSoup(html_content, "html.parser")
    
    lang_attr = soup.html.get("lang")
    assert lang_attr == "hu", "A nyelv nincs magyarra állítva."

# Teszt a böngészőfülön megjelenő címre
def test_browser_tab_title():
    html_content = load_html()
    soup = BeautifulSoup(html_content, "html.parser")
    
    title = soup.title.string.strip()
    assert title == "HP-UX", "A böngészőfülön nem a megfelelő cím jelenik meg."

# Teszt az első szintű fejezetcímre
def test_main_header():
    html_content = load_html()
    soup = BeautifulSoup(html_content, "html.parser")
    
    h1 = soup.h1.string.strip()
    assert h1 == "HP-UX", "Az első szintű fejezetcím nem megfelelő."

# Teszt a második szintű fejezetcímre
def test_support_header():
    html_content = load_html()
    soup = BeautifulSoup(html_content, "html.parser")
    
    h2 = soup.h2.string.strip()
    assert h2 == "Támogatás", "A második szintű fejezetcím nem megfelelő."

# Teszt a Támogatott platformok bekezdésére
def test_supported_platforms():
    html_content = load_html()
    soup = BeautifulSoup(html_content, "html.parser")
    
    p = soup.find_all("p")[1].text.strip()
    assert "Támogatott platformok:" in p, "A 'Támogatott platformok:' nem szerepel a bekezdésben."
    
    platforms = p.split(":")[1].strip()
    assert "HP 9000" in platforms, "A HP 9000 nincs benne a platformok között."
    assert "HP Integral PC" in platforms, "A HP Integral PC nincs benne a platformok között."

# Teszt a rövidítés és kiemelés helyes használatára
def test_abbr_and_mark():
    html_content = load_html()
    soup = BeautifulSoup(html_content, "html.parser")
    
    abbr = soup.find("abbr")
    mark = soup.find("mark")
    
    assert abbr and abbr["title"] == "HP 9000", "A HP 9000 rövidítés nem megfelelő."
    assert mark and mark.string == "HP Integral PC", "A HP Integral PC kiemelés nem megfelelő."

#tesztek futtatása
if __name__ == "__main__":
    create_html()
    pytest.main()
