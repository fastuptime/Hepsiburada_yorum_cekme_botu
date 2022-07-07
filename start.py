import time
from selenium import webdriver

def log(log_text):
    log_text = str(time.strftime("%Y.%m.%d %H:%M:%S")) + " ➾ " + log_text
    print(log_text)
    log_file = open("log.txt", "a", encoding='utf-8')
    log_file.write(log_text + "\n")
    log_file.close()

global_delay = 0.5
driver = webdriver.Chrome()
log('Bu program Can Tarafından Yapılmıştır.')
log('https://fastuptime.com ve https://speedsmm.com üzerinden bize ulaşabilirsiniz.')
log('Program başlatıldı')

urun_url = 'https://www.hepsiburada.com/blu-navy-elbise-blunavy-viscon-cicek-detayli-elbise-p-HBCV000028SDAW' # Ürün URL HEPSİBURADA

try:
    driver.get(urun_url)
    time.sleep(5)
    log('Ürün sayfasına gidildi')
    driver.find_element_by_xpath('/html/body/div[2]/main/div[3]/section[3]/div/div/table/tbody/tr/td[3]/a').click()
    log('Ürünün yorum sayfasına gidildi')
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    kac_yorum_var = driver.find_element_by_xpath('/html/body/div[2]/main/div[3]/section[3]/div/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/div/div[4]/div[1]/div[2]/div/div[2]').text
    kac_yorum_var = kac_yorum_var.replace("Bu ürün ile ilgili ", "")
    kac_yorum_var = kac_yorum_var.replace(" değerlendirme var.", "")
    log('Toplam ' + kac_yorum_var + ' yorum var.')
    for i in range(int(kac_yorum_var)):
        try:
            yorum = driver.find_element_by_xpath('/html/body/div[2]/main/div[3]/section[3]/div/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/div/div[4]/div[3]/div/div[' + str(i) + ']/div[2]/div[2]/span').text
            yorum_tarih = driver.find_element_by_xpath('/html/body/div[2]/main/div[3]/section[3]/div/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/div/div[4]/div[3]/div/div[' + str(i) + ']/div[2]/div[1]/div[2]/div/div/span[1]').text
            yorum_sahibi = driver.find_element_by_xpath('/html/body/div[2]/main/div[3]/section[3]/div/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/div/div[4]/div[3]/div/div[' + str(i) + ']/div[2]/div[1]/div[2]/div/div/div/span[1]').text
            yorum_il = driver.find_element_by_xpath('/html/body/div[2]/main/div[3]/section[3]/div/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/div/div[4]/div[3]/div/div[' + str(i) + ']/div[2]/div[1]/div[2]/div/div/div/span[3]').text
            log('Yorum Tarihi: ' + yorum_tarih + ' Yorum Sahibi: ' + yorum_sahibi + ' Yorum İl: ' + yorum_il + ' Yorum: ' + yorum)
            yorum_file = open("yorumlar.txt", "a", encoding='utf-8')
            yorum_file.write(yorum_tarih + ' ' + yorum_sahibi + ' ' + yorum_il + ' ' + yorum + '\n')
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(global_delay)
        except:
            continue
except Exception as e:
    log('Hata: ' + str(e))
    log('Program sonlandı')
    driver.quit()
    exit()