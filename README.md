# 🎯 OfferHunter

OfferHunter is a lightweight Python tool that helps job seekers explore junior-level opportunities from two popular platforms: Djinni and DOU. Just choose your keywords and get curated listings with key info in your terminal.

---

## ⚙️ Features

- 🔍 Scrape jobs by technology or role (e.g., Python, Android, QA)  
- 🌐 Supports two sources: Djinni and DOU  
- 🧵 Multi-keyword selection for broader search  
- 📦 Output includes job title, company, location, optional description, and direct link  

---

## 📚 Technologies Used

- `requests` — for HTTP communication  
- `BeautifulSoup` — for parsing HTML  
- Python 3.7+  

---

## 📥 Installation

~~~bash
git clone https://github.com/yourusername/OfferHunter.git
cd OfferHunter
pip install -r requirements.txt
~~~

Content of `requirements.txt`:

~~~
requests
beautifulsoup4
~~~

---

## 🧪 How to Use

Run the script and follow the terminal prompts:

~~~bash
python main.py
~~~

1. Choose the data source:  
   - 1 – Djinni  
   - 2 – DOU  
   - 3 – Both  

2. Select job categories by number or enter a custom keyword (Latin letters, max 20 characters)  

Example categories include:

~~~
1 - Android  
2 - iOS  
3 - Python  
...
~~~

---

## 🔎 Sample Output

~~~
========== DJINNI — Python ==========
1. 📌 Junior Python Developer
   🏢 TechNova
   🌍 Remote
   🔗 https://djinni.co/jobs/123456/

========== DOU — Python =========
   🏢 CoolSoft
   🌍 Kyiv
   📝 Assist in developing internal tools for data analysis...
   🔗 https://jobs.dou.ua/vacancies/987654/
~~~

---

## 📌 Notes

- Use a VPN if access to sites is restricted  
- You can expand the script with CSV export, filters, or even connect it to a Telegram bot  
- Perfect for aspiring developers looking to land their first tech job  

---

## 📄 License

MIT — free for personal and commercial use.

---

Made with ❤️ by olegnck404
