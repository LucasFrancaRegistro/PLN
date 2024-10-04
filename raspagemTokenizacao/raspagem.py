
import requests
import re
from bs4 import BeautifulSoup
from tokenizacao import tolkenizar

#https://www.amazon.co.uk/Samsung-Smartphone-Unlocked-Manufacturer-Extended/dp/B0D4F814RB/ref=pd_sim_d_sccl_4_3/260-1456759-7020730?pd_rd_w=pxvoJ&content-id=amzn1.sym.c7e2bad4-5f0a-4571-946c-cadf3ebf9cb4&pf_rd_p=c7e2bad4-5f0a-4571-946c-cadf3ebf9cb4&pf_rd_r=BRAWFG5SBQH35KBEMHXZ&pd_rd_wg=fcvZ4&pd_rd_r=a20b2603-9860-480a-b219-858d770b4582&pd_rd_i=B0D4F814RB&th=1

#https://www.amazon.co.uk/dp/B0D4F7CW1N/ref=sspa_dk_detail_0?pd_rd_i=B0D4F7CW1N&pd_rd_w=vJZDP&content-id=amzn1.sym.46187d6a-4306-4bc6-830c-7b2085e0e39f&pf_rd_p=46187d6a-4306-4bc6-830c-7b2085e0e39f&pf_rd_r=N55FYA988VQKQF7R7KKW&pd_rd_wg=fxE0w&pd_rd_r=2d35cd92-72a9-47b2-8b58-533ffbeb8773&s=electronics&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw&th=1

#https://www.amazon.co.uk/dp/B0CGVTJ583/ref=sspa_dk_detail_4?pd_rd_i=B0CGVTJ583&pd_rd_w=j8DH0&content-id=amzn1.sym.6910e71b-a457-4d1b-9885-9ac6dea34603&pf_rd_p=6910e71b-a457-4d1b-9885-9ac6dea34603&pf_rd_r=TD9BS15D1F72TTW87YB5&pd_rd_wg=aOTnF&pd_rd_r=1d4023ee-f894-487e-a3a7-2fbc25172bd0&s=electronics&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWwy&th=1

# a function to get rid of html tags
def get_rid_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    # iframe and script nodes removal from doc tree
    [s.extract() for s in soup(['iframe','script'])]
    stripped_text = soup.get_text()
    stripped_text = re.sub(r'[\r|\n|\r\n]','\n',stripped_text)
    return stripped_text

data = requests.get("https://www.amazon.co.uk/dp/B0CGVTJ583/ref=sspa_dk_detail_4?pd_rd_i=B0CGVTJ583&pd_rd_w=j8DH0&content-id=amzn1.sym.6910e71b-a457-4d1b-9885-9ac6dea34603&pf_rd_p=6910e71b-a457-4d1b-9885-9ac6dea34603&pf_rd_r=TD9BS15D1F72TTW87YB5&pd_rd_wg=aOTnF&pd_rd_r=1d4023ee-f894-487e-a3a7-2fbc25172bd0&s=electronics&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWwy&th=1")
#data = requests.get("#https://www.amazon.co.uk/dp/B0D4F7CW1N/ref=sspa_dk_detail_0?pd_rd_i=B0D4F7CW1N&pd_rd_w=vJZDP&content-id=amzn1.sym.46187d6a-4306-4bc6-830c-7b2085e0e39f&pf_rd_p=46187d6a-4306-4bc6-830c-7b2085e0e39f&pf_rd_r=N55FYA988VQKQF7R7KKW&pd_rd_wg=fxE0w&pd_rd_r=2d35cd92-72a9-47b2-8b58-533ffbeb8773&s=electronics&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw&th=1")
#data = requests.get("https://www.amazon.co.uk/Samsung-Smartphone-Unlocked-Manufacturer-Extended/dp/B0D4F814RB/ref=pd_sim_d_sccl_4_3/260-1456759-7020730?pd_rd_w=pxvoJ&content-id=amzn1.sym.c7e2bad4-5f0a-4571-946c-cadf3ebf9cb4&pf_rd_p=c7e2bad4-5f0a-4571-946c-cadf3ebf9cb4&pf_rd_r=BRAWFG5SBQH35KBEMHXZ&pd_rd_wg=fcvZ4&pd_rd_r=a20b2603-9860-480a-b219-858d770b4582&pd_rd_i=B0D4F814RB&th=1")
content = data.content
soup = BeautifulSoup(content, "html.parser")
clean_content = get_rid_html_tags(soup.get_text())
reviews = clean_content[clean_content.find("Top reviews from United Kingdom"):]
x = reviews.find("Verified Purchase")+17
y = reviews.find("Read more")
print(f"x:{x} y:{y}")
review = reviews[x:y]
print(review)

tolkenizar(review)