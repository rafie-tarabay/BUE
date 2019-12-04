from bs4 import BeautifulSoup
import requests

Sources=[
            {
                "URL":"https://k-tb.com/books/disc/تاريخ?page=",
                "Pages":100,
                "FT_URL":"https://archive.org/download/history", #'https://archive.org/download/history10000/history09907.zip'
                "start":7,
                "end":9
            },

            {
                "URL":"https://k-tb.com/books/disc/الزهد-والرقائق?page=",
                "Pages":27,
                "FT_URL":"https://archive.org/download/tarbyah", #'https://archive.org/download/tarbyah3000/tarbyah02693.zip'
                "start":7,
                "end":9
            },

            {
                "URL":"https://k-tb.com/books/disc/الحديث-وعلومه?page=",
                "Pages":87,
                "FT_URL":"https://archive.org/download/hadeeth", #'https://archive.org/download/hadeeth9000/hadeeth8697.zip'
                "start":7,
                "end":8
            },
            {
                "URL":"https://k-tb.com/books/disc/التفسير-وعلوم-القرآن?page=",
                "Pages":120,
                "FT_URL":"https://archive.org/download/Quran", #'https://archive.org/download/Quran12000/Quraan11975.zip'
                "start":6,
                "end":8
            },
            {
                "URL":"https://k-tb.com/books/disc/العقيدة-والمذاهب-والأديان?page=",
                "Pages":92,
                "FT_URL":"https://archive.org/download/aqidah01/" #https://archive.org/download/aqidah01/Aqidah09200.zip
            },

            {
                "URL":"https://k-tb.com/books/disc/الدعوة-والاحتساب?page=",
                "Pages":10,
                "FT_URL":"https://archive.org/download/dawah1000/" #https://archive.org/download/dawah1000/dawah00927.zip
            },
            {
                "URL":"https://k-tb.com/books/disc/الثقافة-الإسلامية-?page=",
                "Pages":6,
                "FT_URL":"https://archive.org/download/Th2000/" #'https://archive.org/download/Th2000/Th1898.zip'
            },
            {
                "URL":"https://k-tb.com/books/disc/السيرة-النبوية?page=",
                "Pages":11,
                "FT_URL":"https://archive.org/download/serah1000/" #https://archive.org/download/serah1000/serah01055.zip
            },
            {
                "URL":"https://k-tb.com/books/disc/دوريات-ومجلات?page=",
                "Pages":4,
                "FT_URL":"https://archive.org/download/magazine1000/" #https://archive.org/download/magazine1000/magazine0003.zip
            },
        ]
for item in Sources 
    for i in range(1,item["Pages"])
        r  = requests.get(item["URL"] + str(i))
        html =  r.text
        soup = BeautifulSoup(html, "lxml")
        table = soup.find("table",{"class":"table-hover"})
        rows = table.find_all('tr', recursive=False)                  
        for row in rows:
            cell = row.find_all(['td'], recursive=False)         
            if cell:
                ID= cell[0].string
                Title= cell[1].string
                Author=cell[2].string
                OriginalURL=cell[3].find('a').get('href')
                if item["FT_URL"][-1]=="/":
                    FT=item["FT_URL"]+""+ID+".zip"
                else
                    FT=item["FT_URL"]+str(int(ID[item["start"]:end["start"]])+1)+"000/"+ID+".zip"




"""
for tag in filtered:
    print (tag.get_text())
    


for link in soup.find_all('a'):
    print(link.get('href'))



history09804
مواقف الأشراف السعديين بالمغرب من مسألة الخلافة العثمانية
فهد بن محمد السويكت
https://k-tb.com/book/history09804-%D9%85%D9%88%D8%A7%D9%82%D9%81-%D8%A7%D9%84%D8%A3%D8%B4%D8%B1%D8%A7%D9%81-%D8%A7%D9%84%D8%B3%D8%B9%D8%AF%D9%8A%D9%8A%D9%86-%D8%A8%D8%A7%D9%84%D9%85%D8%BA%D8%B1%D8%A8-%D9%85%D9%86-%D9%85%D8%B3%D8%A3%D9%84%D8%A9-%D8%A7%D9%84%D8%AE%D9%84%D8%A7%D9%81%D8%A9-%D8%A7%D9%84%D8%B9%D8%AB%D9%85%D8%A7%D9%86%D9%8A%D8%A9
history09803
FT = https://archive.org/download/history10000/history09803.zip
"""     