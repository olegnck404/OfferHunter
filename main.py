import requests
from bs4 import BeautifulSoup

def get_djinni_vacancies(keyword):
    url = f"https://djinni.co/jobs/?primary_keyword={keyword}&exp_level=no_exp"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"[❌] Djinni: ошибка {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    job_items = soup.find_all('li', class_='mb-4')

    vacancies = []
    for job in job_items:
        title_tag = job.find('a', class_='job-item__title-link')
        company_tag = job.find('a', class_='text-body js-analytics-event')
        location_tag = job.find('span', class_='location-text')

        if title_tag and company_tag:
            vacancies.append({
                'title': title_tag.text.strip(),
                'company': company_tag.text.strip(),
                'location': location_tag.text.strip() if location_tag else 'Location not specified',
                'link': 'https://djinni.co' + title_tag['href']
            })
    return vacancies

def get_dou_vacancies(keyword):
    url = f"https://jobs.dou.ua/vacancies/?category={keyword}&exp=0-1"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"[❌] DOU: ошибка {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    job_items = soup.find_all('li', class_='l-vacancy')

    vacancies = []
    for job in job_items:
        title_tag = job.find('a', class_='vt')
        company_tag = job.find('a', class_='company')
        location_tag = job.find('span', class_='cities')
        description_tag = job.find('div', class_='sh-info')

        if title_tag and company_tag:
            vacancies.append({
                'title': title_tag.text.strip(),
                'company': company_tag.text.strip(),
                'location': location_tag.text.strip() if location_tag else 'Location not specified',
                'description': description_tag.text.strip() if description_tag else '',
                'link': title_tag['href']
            })
    return vacancies

def print_vacancies(source, keyword, vacancies):
    print(f"\n{'='*10} {source.upper()} — {keyword} {'='*10}\n")

    if not vacancies:
        print("⚠️ Вакансий не найдено.\n")
        return

    for idx, vacancy in enumerate(vacancies, 1):
        print(f"{idx}. 📌 {vacancy['title']}")
        print(f"   🏢 {vacancy['company']}")
        print(f"   🌍 {vacancy['location']}")
        if 'description' in vacancy:
            print(f"   📝 {vacancy['description'][:150]}...")
        print(f"   🔗 {vacancy['link']}\n")

# --- Основной блок ---
sources = input("Выберите источник для парсинга:\n1 - Djinni\n2 - DOU\n3 - Оба\nВведите номер: ").strip()

print("\nВыберите категории по номерам через запятую или введите свои (только латиница, макс 20 символов):")
popular_keywords = ["Android", "iOS", "Python", "JavaScript", "Java", "QA", "DevOps", "Project Manager", "Product Manager"]
for idx, kw in enumerate(popular_keywords, 1):
    print(f"{idx} - {kw}")

user_input = input("Ваш выбор: ").strip()
if user_input.isdigit() or ',' in user_input:
    selected_nums = [int(num.strip()) for num in user_input.split(',') if num.strip().isdigit()]
    keywords = [popular_keywords[num - 1] for num in selected_nums if 0 < num <= len(popular_keywords)]
else:
    if user_input.isalpha() and len(user_input) <= 20:
        keywords = [user_input]
    else:
        print("❌ Неверный ввод ключевых слов.")
        exit()

for keyword in keywords:
    if sources in ['1', '3']:
        djinni_vacancies = get_djinni_vacancies(keyword)
        print_vacancies("Djinni", keyword, djinni_vacancies)

    if sources in ['2', '3']:
        dou_vacancies = get_dou_vacancies(keyword)
        print_vacancies("DOU", keyword, dou_vacancies)
