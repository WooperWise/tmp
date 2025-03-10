import requests
import csv

api_key = "AIzaSyAqpctoUlx_X6uNRxRDpiSA3mPM2RODYjA"
cx = "e665012fba77d4cf4"
queries = [
    "В каком году был основан Университет ИТМО?",
    "Сколько факультетов в Университете ИТМО?",
    "В каком городе находится главный кампус Университета ИТМО?",
    "Какие научные направления являются приоритетными для Университета ИТМО?",
    "В каком рейтинге Университет ИТМО впервые вошёл в топ-400 мировых университетов?",
    "Какой факультет Университета ИТМО специализируется на фотонике?",
    "Сколько студентов обучается в Университете ИТМО?",
    "Какие программы магистратуры предлагает Университет ИТМО?",
    "Какой год считается годом основания факультета информационных технологий и программирования?",
    "Какие международные партнёры есть у Университета ИТМО?",
    "В каком году Университет ИТМО получил статус Национального исследовательского университета?",
    "Какие научные центры работают при Университете ИТМО?",
    "Какой факультет Университета ИТМО занимается робототехникой?",
    "Какие языки программирования изучают студенты Университета ИТМО?",
    "Сколько лабораторий работает в Университете ИТМО?",
    "Какие достижения Университета ИТМО в области искусственного интеллекта?",
    "Какой факультет Университета ИТМО занимается биотехнологиями?",
    "Какие программы бакалавриата предлагает Университет ИТМО?",
    "Сколько научных публикаций ежегодно выпускает Университет ИТМО?",
    "Какие международные рейтинги включают Университет ИТМО?",
    "Какой факультет Университета ИТМО занимается квантовыми технологиями?",
    "Какие программы аспирантуры предлагает Университет ИТМО?",
    "Сколько иностранных студентов обучается в Университете ИТМО?",
    "Какие научные гранты доступны для студентов Университета ИТМО?",
    "Какой факультет Университета ИТМО занимается наукой о данных?",
    "Какие программы обмена доступны для студентов Университета ИТМО?",
    "Сколько преподавателей работает в Университете ИТМО?",
    "Какие инновационные проекты реализует Университет ИТМО?",
    "Какой факультет Университета ИТМО занимается компьютерной безопасностью?",
    "Какие программы дополнительного образования предлагает Университет ИТМО?",
    "Сколько научных конференций ежегодно проводит Университет ИТМО?",
    "Какие стартапы были созданы выпускниками Университета ИТМО?",
    "Какой факультет Университета ИТМО занимается нанотехнологиями?",
    "Какие программы PhD предлагает Университет ИТМО?",
    "Сколько патентов зарегистрировано Университетом ИТМО?",
    "Какие научные журналы издаёт Университет ИТМО?",
    "Какой факультет Университета ИТМО занимается искусственным интеллектом?",
    "Какие программы стажировок доступны для студентов Университета ИТМО?",
    "Сколько выпускников Университета ИТМО работают в IT-компаниях?",
    "Какие научные премии получили сотрудники Университета ИТМО?",
    "Какой факультет Университета ИТМО занимается машинным обучением?",
    "Какие программы поддержки стартапов предлагает Университет ИТМО?",
    "Сколько научных партнёров у Университета ИТМО?",
    "Какие образовательные технологии использует Университет ИТМО?",
    "Какой факультет Университета ИТМО занимается разработкой игр?",
    "Какие программы для школьников предлагает Университет ИТМО?",
    "Сколько научных статей опубликовано сотрудниками Университета ИТМО за последний год?",
    "Какие международные конференции организует Университет ИТМО?",
    "Какой факультет Университета ИТМО занимается виртуальной реальностью?",
    "Какие программы поддержки молодых учёных предлагает Университет ИТМО?",
    "В каком году был основан Университет ИТМО? 1900 1920 1945 1960",
    "Какой город является местом расположения главного кампуса Университета ИТМО? Москва Санкт-Петербург Новосибирск Казань",
    "В каком году Университет ИТМО получил статус Национального исследовательского университета? 2007 2009 2011 2015",
    "Какое место занял Университет ИТМО в рейтинге QS World University Rankings в 2023 году? Топ-100 Топ-200 Топ-300 Топ-400",
    "Сколько факультетов в Университете ИТМО? 5 7 10 12",
    "Какой факультет Университета ИТМО специализируется на информационных технологиях? Факультет программной инженерии Факультет компьютерных технологий Факультет фотоники Факультет управления технологиями",
    "Какой рейтинг впервые включил Университет ИТМО в топ-400 в 2021 году? ARWU (Shanghai Ranking) Times Higher Education (THE) QS World University Rankings U.S. News & World Report",
    "Какой год считается годом основания факультета фотоники в Университете ИТМО? 1990 2000 2010 2015",
    "Какой язык программирования чаще всего изучают студенты Университета ИТМО? Python Java C++ JavaScript",
    "Сколько студентов обучается в Университете ИТМО? 5000 10000 15000 20000",
    "Какой факультет Университета ИТМО занимается исследованиями в области искусственного интеллекта? Факультет компьютерных технологий Факультет программной инженерии Факультет фотоники Факультет управления технологиями",
    "Какой год стал годом основания факультета программной инженерии? 2005 2010 2015 2020",
    "Какой рейтинг впервые включил Университет ИТМО в топ-1000? ARWU (Shanghai Ranking) Times Higher Education (THE) QS World University Rankings U.S. News & World Report",
    "Какой факультет Университета ИТМО занимается исследованиями в области квантовых технологий? Факультет фотоники Факультет компьютерных технологий Факультет программной инженерии Факультет управления технологиями",
    "Какой год стал годом основания факультета управления технологиями? 2000 2005 2010 2015",
    "Какой язык программирования используется для обучения на факультете программной инженерии? Python Java C++ JavaScript",
    "Сколько преподавателей работает в Университете ИТМО? 500 1000 1500 2000",
    "Какой факультет Университета ИТМО занимается исследованиями в области робототехники? Факультет компьютерных технологий Факультет программной инженерии Факультет фотоники Факультет управления технологиями",
    "Какой год стал годом основания факультета компьютерных технологий? 1990 2000 2010 2015",
    "Какой рейтинг впервые включил Университет ИТМО в топ-500? ARWU (Shanghai Ranking) Times Higher Education (THE) QS World University Rankings U.S. News & World Report",
    "Какой факультет Университета ИТМО занимается исследованиями в области больших данных? Факультет компьютерных технологий Факультет программной инженерии Факультет фотоники Факультет управления технологиями",
    "Какой год стал годом основания факультета фотоники? 1990 2000 2010 2015",
    "Какой язык программирования используется для обучения на факультете компьютерных технологий? Python Java C++ JavaScript",
    "Сколько научных лабораторий в Университете ИТМО? 50 100 150 200",
    "Какой факультет Университета ИТМО занимается исследованиями в области машинного обучения? Факультет компьютерных технологий Факультет программной инженерии Факультет фотоники Факультет управления технологиями",
    "Какой год стал годом основания факультета управления технологиями? 2000 2005 2010 2015",
    "Какой рейтинг впервые включил Университет ИТМО в топ-300? ARWU (Shanghai Ranking) Times Higher Education (THE) QS World University Rankings U.S. News & World Report",
    "Какой факультет Университета ИТМО занимается исследованиями в области интернета вещей? Факультет компьютерных технологий Факультет программной инженерии Факультет фотоники Факультет управления технологиями",
    "Какой год стал годом основания факультета программной инженерии? 2005 2010 2015 2020",
    "Какой язык программирования используется для обучения на факультете фотоники? Python Java C++ JavaScript",
    "Сколько международных партнёров у Университета ИТМО? 100 200 300 400",
    "Какой факультет Университета ИТМО занимается исследованиями в области кибербезопасности? Факультет компьютерных технологий Факультет программной инженерии Факультет фотоники Факультет управления технологиями",
    "Какой год стал годом основания факультета компьютерных технологий? 1990 2000 2010 2015",
    "Какой рейтинг впервые включил Университет ИТМО в топ-200? ARWU (Shanghai Ranking) Times Higher Education (THE) QS World University Rankings U.S. News & World Report",
    "Какой факультет Университета ИТМО занимается исследованиями в области искусственного интеллекта? Факультет компьютерных технологий Факультет программной инженерии Факультет фотоники Факультет управления технологиями",
    "Какой год стал годом основания факультета фотоники? 1990 2000 2010 2015",
    "Какой язык программирования используется для обучения на факультете управления технологиями? Python Java C++ JavaScript",
    "Сколько научных публикаций ежегодно выпускает Университет ИТМО? 1000 2000 3000 4000",
    "Какой факультет Университета ИТМО занимается исследованиями в области робототехники? Факультет компьютерных технологий Факультет программной инженерии Факультет фотоники Факультет управления технологиями",
    "Какой год стал годом основания факультета программной инженерии? 2005 2010 2015 2020",
    "Какой рейтинг впервые включил Университет ИТМО в топ-100? ARWU (Shanghai Ranking) Times Higher Education (THE) QS World University Rankings U.S. News & World Report",
    "Какой факультет Университета ИТМО занимается исследованиями в области больших данных? Факультет компьютерных технологий Факультет программной инженерии Факультет фотоники Факультет управления технологиями",
    "Какой год стал годом основания факультета управления технологиями? 2000 2005 2010 2015",
    "Какой язык программирования используется для обучения на факультете компьютерных технологий? Python Java C++ JavaScript",
    "Сколько студентов из других стран обучается в Университете ИТМО? 500 1000 1500 2000",
    "Какой факультет Университета ИТМО занимается исследованиями в области машинного обучения? Факультет компьютерных технологий Факультет программной инженерии Факультет фотоники Факультет управления технологиями",
    "Какой год стал годом основания факультета фотоники? 1990 2000 2010 2015",
    "Какой рейтинг впервые включил Университет ИТМО в топ-50? ARWU (Shanghai Ranking) Times Higher Education (THE) QS World University Rankings U.S. News & World Report",
    "Какой факультет Университета ИТМО занимается исследованиями в области интернета вещей? Факультет компьютерных технологий Факультет программной инженерии Факультет фотоники Факультет управления технологиями",
    "Какой год стал годом основания факультета программной инженерии? 2005 2010 2015 2020"
]  # Ваши 100 запросов

with open('results.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Записываем заголовки

    for query in queries:
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}&num=3"
        response = requests.get(url)
        data = response.json()
        
        # Извлекаем ссылки
        links = [item["link"] for item in data.get("items", [])]
        # Если ссылок меньше 3, дополняем пустыми значениями
        links.extend(["NULL"] * (3 - len(links)))
        
        # Записываем запрос и ссылки в CSV
        writer.writerow(links)

print("Результаты сохранены в файл results.csv")