import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options 

# driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeuWBmADFr1VWUUaMR0A6YAUMMXaoR8f512JWs1OiP0_3dfTQ/viewform')

def waitAndClickRandomText(textForWait, randomValue):
  # vertical choice
  waitFor = '//span[text()="%s"]' % textForWait
  WebDriverWait(driver,15).until(
      EC.presence_of_element_located((By.XPATH,waitFor))
  )
  elementForClick = '//span[text()="%s"]' % randomValue
  element = driver.find_element_by_xpath(elementForClick)
  print("%s = %s" % (textForWait ,element.get_attribute('innerHTML')))
  WebDriverWait(driver,3)
  driver.find_element_by_xpath(elementForClick).click()

def waitAndClickRandomValue(textForWait):
  # horizon choice
  waitFor = '//div[text()="%s"]' % textForWait
  WebDriverWait(driver,15).until(
      EC.presence_of_element_located((By.XPATH,waitFor))
  )
  randomRate = random.choice(["5","4","3","2"])
  ariaLabel = "//div[@aria-label='%s เป็นคำตอบสำหรับ %s']" % (randomRate, textForWait)

  getPath=driver.find_element_by_xpath(".%s" % waitFor)
  getRow = getPath.find_element(By.XPATH,"..")
  getRow.find_element_by_xpath(ariaLabel).click()
  # print('test = '+ str(getRow.get_attribute('innerHTML')))
  # 322
count = 1
while count < (346):
  age = random.choice(["ต่ำกว่า 20 ปี","20 – 30 ปี","31 – 40 ปี","มากกว่า 40 ปี"])
  married = ""
  education = ""
  job = ""
  salary = ""

  if age == "ต่ำกว่า 20 ปี":
    married = "โสด"
    job = random.choice(["ธุรกิจส่วนตัว / อาชีพอิสระ","นักเรียน / นักศึกษา"])
    education = "ต่ำกว่าปริญญาตรี"
  elif age == "มากกว่า 40 ปี":
    married = random.choice(["โสด","สมรส","หม้าย/หย่าร้าง/แยกกันอยู่"])
    job = random.choice(["ข้าราชการ / พนักงานรัฐวิสาหกิจ","พนักงานบริษัทเอกชน / ลูกจ้าง","ธุรกิจส่วนตัว / อาชีพอิสระ"])
    education = random.choice(["ต่ำกว่าปริญญาตรี","ปริญญาตรี","สูงกว่าปริญญาตรี"])
  else:
    married = random.choice(["โสด","สมรส","หม้าย/หย่าร้าง/แยกกันอยู่"])
    job = random.choice(["ข้าราชการ / พนักงานรัฐวิสาหกิจ","พนักงานบริษัทเอกชน / ลูกจ้าง","ธุรกิจส่วนตัว / อาชีพอิสระ","นักเรียน / นักศึกษา"])
    education = random.choice(["ต่ำกว่าปริญญาตรี","ปริญญาตรี","สูงกว่าปริญญาตรี"])

  if education == "ต่ำกว่าปริญญาตรี":
    salary = random.choice(["ต่ำกว่า 15,000 บาท","15,000 – 30,000 บาท"])
  elif education =="ปริญญาตรี":
    salary = random.choice(["ต่ำกว่า 15,000 บาท","15,000 – 30,000 บาท","30,001 – 45,000 บาท","45,001 – 60,000 บาท"])
  elif education =="สูงกว่าปริญญาตรี":
    salary = random.choice(["45,001 – 60,000 บาท","มากกว่า 60,000 บาท"])

  waitAndClickRandomText("ชาย",random.choice(["ชาย","หญิง"]))
  waitAndClickRandomText("มากกว่า 40 ปี", age)
  waitAndClickRandomText("หม้าย/หย่าร้าง/แยกกันอยู่",married)
  waitAndClickRandomText("สูงกว่าปริญญาตรี",education)
  waitAndClickRandomText("นักเรียน / นักศึกษา" ,job)
  waitAndClickRandomText("มากกว่า 60,000 บาท" ,salary)

  waitAndClickRandomValue("1. ท่านคิดว่าร้านค้าที่จำหน่ายเครื่องเขียนผ่านแอปพลิเคชั่น Shopee สามารถตอบสนองความจำเป็น และความต้องการการของท่านได้")
  waitAndClickRandomValue("2. ท่านคิดว่าร้านค้าที่จำหน่ายเครื่องเขียนผ่านแอปพลิเคชั่น Shopee มีความหลากหลายรูปแบบ")
  waitAndClickRandomValue("3. ท่านได้รับข้อมูลเครื่องเขียนของแต่ละอย่างชัดเจนเกี่ยวกับ เช่น ตัวผลิตภัณฑ์ ชื่อผลิตภัณฑ์ การบรรจุหีบห่อ")
  waitAndClickRandomValue("1. ท่านคิดว่าราคาของเครื่องเขียนที่จำหน่ายในแอปพลิเคชั่น Shopee มีความคุ้มค่ากว่าในตลาด")
  waitAndClickRandomValue("2. ท่านได้รับข้อมูลในเรื่องราคา ส่วนลด และเงื่อนไขการได้รับส่วนลดของแต่ละร้านอย่างชัดเจนก่อนตัดสินใจซื้อ")
  waitAndClickRandomValue("3. ท่านคิดว่าผู้ขายมีการกำหนดราคาไว้อย่างชัดเจน เข้าใจง่ายโดยไม่ต้องถามถึงรายละเอียดก่อนการตัดสินใจซื้อ")
  waitAndClickRandomValue("1. ท่านสามารถเข้าถึง แอปพลิเคชั่น Shopee ได้ง่ายและสะดวก")
  waitAndClickRandomValue("2. ท่านสามารถค้นหาเครื่องเขียนที่ท่านต้องการได้ง่ายและสะดวก")
  waitAndClickRandomValue("3. ท่านสับสนในขั้นตอนต่าง ๆในการใช้ แอปพลิเคชั่น Shopee")
  waitAndClickRandomValue("4. ท่านคิดว่า แอปพลิเคชั่น Shopee มีบริการส่งสินค้าที่รวดเร็ว")
  waitAndClickRandomValue("5. ท่านได้รับการอำนวยความสะดวกในเรื่องต่าง ๆ เช่นช่องทางในการชำระเงิน")
  waitAndClickRandomValue("1. ท่านชื่นชอบโปรโมชั่นส่วนลดที่ทางแอปพลิเคชั่น Shopee ให้ในการซื้อสินค้าในแต่ละเดือน และเทศกาลต่าง ๆ")
  waitAndClickRandomValue("2. ร้านค้ามีโปรโมชั่นที่ทำให้ท่านกลับไปซื้อซ้ำในร้านค้าเดิม")
  waitAndClickRandomValue("1. ท่านซื้อเครื่องเขียนผ่านแอปพลิเคชั่น Shopee เป็นประจำ")
  waitAndClickRandomValue("2. ท่านซื้อเครื่องเขียนจากแอปพลิเคชั่น Shopee ในช่วงเวลาที่ท่านต้องการทันที")
  waitAndClickRandomValue("3. ท่านซื้อเครื่องเขียนจากแอปพลิเคชั่น Shopee ทันทีที่ทราบว่ามีส่วนลดในช่วงเวลาต่าง ๆ")
  waitAndClickRandomValue("4. ท่านซื้อเครื่องเขียนผ่านแอปพลิเคชั่น Shopee เพื่อเป็นของขวัญในช่วงเวลาพิเศษ")
  waitAndClickRandomValue("5. ท่านซื้อเครื่องเขียนจากหลายๆ ร้าน มีความหลากหลายในการเลือกร้านค้า")
  waitAndClickRandomValue("6. ท่านเปรียบเทียบราคาจากหลาย ๆ ร้านค้าก่อนซื้อ")

  time.sleep(3)
  driver.find_element_by_xpath("//span[text()='ส่ง']").click()

  try:
    driver.find_element_by_xpath("//div[text()='จำเป็นต้องตอบคำถามนี้']")
    print('except')
  except:
    """ถ้าไม่เจอคำว่า "จำเป็นต้องตอบคำถาม แสดงว่าถูกแล้ว ให้ทำต่อ"
    ปกติ block except คือเอาไว้แจ้ง error นะจ๊ะ"""
    success = driver.find_element_by_xpath("//div[text()='เราได้บันทึกคำตอบของคุณไว้แล้ว']")
    
    print(success.get_attribute('innerHTML'))
    WebDriverWait(driver,15).until(
      EC.presence_of_element_located((By.XPATH,"//a[text()='ส่งคำตอบเพิ่มอีก']"))
    )
    driver.find_element_by_xpath("//a[text()='ส่งคำตอบเพิ่มอีก']").click()
    print("count = %d" % count)
    count+=1
    continue