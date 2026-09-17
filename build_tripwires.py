import os

template = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Путеводитель: {{CITY_NAME}} - VT VIP</title>
  <link rel="icon" type="image/jpeg" href="images/logo_clear.png">
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600&family=Manrope:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
  <style>
    .tripwire-header { padding: 150px 10% 80px; text-align: center; }
    .tripwire-header h1 { font-size: 48px; margin-bottom: 20px; color: var(--gold); }
    .tripwire-content { max-width: 900px; margin: 0 auto; padding: 0 20px 100px; line-height: 1.8; color: #ccc; }
    .tripwire-content img { width: 100%; border-radius: 12px; margin: 40px 0; border: 1px solid rgba(212, 168, 67, 0.3); }
    .tripwire-content h2 { font-family: 'Cormorant Garamond', serif; font-size: 32px; color: #fff; margin-top: 50px; margin-bottom: 20px; }
    .cta-box { background: rgba(20,15,25,0.8); border: 1px solid var(--gold); border-radius: 12px; padding: 40px; text-align: center; margin-top: 60px; }
    .cta-box h3 { color: var(--gold); font-size: 28px; margin-bottom: 15px; }
  </style>
</head>
<body class="standard-page">
  <div class="grain-overlay"></div>
  <nav class="navbar" id="navbar">
    <a href="index.html" class="nav-logo"><img src="images/logo_clear.png" alt="VT Logo" class="logo-img"><span class="logo-text">VT VIP</span></a>
    <div class="nav-links"><a href="index.html">Главная</a><a href="fleet.html">Автопарк</a><a href="destinations.html" style="color: var(--gold);">Путеводители</a></div>
    <div class="lang-switcher"><a href="#" class="active">RU</a></div>
  </nav>

  <div class="tripwire-header reveal-3d" style="opacity: 1; transform: none;">
    <h1>{{CITY_NAME}}: Эксклюзивный Путеводитель</h1>
    <p style="font-size: 20px; color: #fff;">{{SUBTITLE}}</p>
  </div>

  <div class="tripwire-content">
    <img src="images/placeholder_{{CITY_EN}}.jpg" alt="{{CITY_NAME}}" onerror="this.style.display='none'">
    <p>{{INTRO}}</p>
    <h2>Главные достопримечательности (VIP)</h2>
    <ul>{{FEATURES}}</ul>
    <h2>Рестораны и Гастрономия (Halal & Fine Dining)</h2>
    <p>{{FOOD}}</p>
    <div class="cta-box">
      <h3>Добавить этот путеводитель к заказу</h3>
      <p>Полный гайд с контактами закрытых заведений, прямыми бронями и рекомендациями по безопасности.</p>
      <div style="font-size: 32px; font-weight: bold; margin: 20px 0; font-family: 'Cormorant Garamond', serif;">Стоимость: {{PRICE}}</div>
      <a href="mailto:info@vt-vip.ru?subject=Buy {{CITY_EN}} Tripwire" class="btn btn-primary">Заказать путеводитель</a>
    </div>
  </div>
  
  <a href="https://wa.me/74950000000" class="floating-concierge" target="_blank"><svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.888-.788-1.487-1.761-1.663-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.052 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg><span>Personal Concierge</span></a>
</body>
</html>"""

cities = [
    {
        "file": "tripwire-moscow.html",
        "CITY_NAME": "Москва",
        "CITY_EN": "Moscow",
        "SUBTITLE": "Столица роскоши, бизнеса и премиального шопинга.",
        "INTRO": "Москва — это мегаполис, который никогда не спит. Для VIP-гостей мы подготовили маршруты, исключающие толпы туристов: закрытые залы, персональные менеджеры в бутиках и столы в лучших ресторанах с панорамным видом на город.",
        "FEATURES": "<li><strong>Красная Площадь и Кремль:</strong> Индивидуальные экскурсии после закрытия для обычных посетителей.</li><li><strong>ЦУМ и ГУМ (VIP Shopping):</strong> Доступ в секретные комнаты для примерки (VIP Lounge) с личным стилистом и шампанским.</li><li><strong>Большой Театр:</strong> Бронирование правительственных и директорских лож на балет.</li>",
        "FOOD": "В гиде собраны лучшие рестораны Москва-Сити (Ruski, Sixty) и Патриарших прудов. Отдельный акцент сделан на заведения с премиальным халяль-меню (сертификация Halal), где подают изысканные блюда ближневосточной и русской кухни.",
        "PRICE": "$49"
    },
    {
        "file": "tripwire-spb.html",
        "CITY_NAME": "Санкт-Петербург",
        "CITY_EN": "SPB",
        "SUBTITLE": "Имперская эстетика, белые ночи и дворцы.",
        "INTRO": "Северная Венеция предлагает аристократический отдых. Мы организуем для вас доступ к закрытым коллекциям императоров и прогулки на премиальных яхтах по рекам и каналам.",
        "FEATURES": "<li><strong>Эрмитаж и Зимний Дворец:</strong> Проход через закрытые VIP-входы, экскурсии с главными кураторами музея.</li><li><strong>Петергоф и Царское Село:</strong> Поездка на премиум-трансфере или вертолете, ужин в дворцовых интерьерах.</li><li><strong>Аренда Яхт:</strong> Прогулки по Неве под разводными мостами с личным шеф-поваром на борту.</li>",
        "FOOD": "Гастрономическая столица России. В путеводителе указаны рестораны высокой кухни с видом на Исаакиевский собор и Финский залив, а также лучшие заведения с соблюдением стандартов Halal.",
        "PRICE": "$49"
    },
    {
        "file": "tripwire-sochi.html",
        "CITY_NAME": "Сочи",
        "CITY_EN": "Sochi",
        "SUBTITLE": "Русская Ривьера и вершины Кавказских гор.",
        "INTRO": "Сочи объединяет субтропический климат у Черного моря и горнолыжные курорты мирового класса. Идеальное место для релаксации, спа-отдыха и приватных развлечений.",
        "FEATURES": "<li><strong>Красная Поляна:</strong> VIP-ски-пассы, аренда закрытых шале с личным поваром и банщиком.</li><li><strong>Вертолетные туры:</strong> Полет над Кавказским хребтом с посадкой на диких ледниках для пикника.</li><li><strong>Казино Сочи:</strong> Доступ в закрытые VIP-залы для высоких ставок с абсолютной конфиденциальностью.</li>",
        "FOOD": "Свежайшие морепродукты и кавказская кухня. В путеводителе — закрытые рестораны яхт-портов и горные террасы с халяльным мясом и лучшим сервисом.",
        "PRICE": "$59"
    },
    {
        "file": "tripwire-kazan.html",
        "CITY_NAME": "Казань",
        "CITY_EN": "Kazan",
        "SUBTITLE": "Пересечение культур и исламских традиций.",
        "INTRO": "Столица Татарстана — один из самых комфортных городов для гостей из арабских стран. Здесь исламская архитектура гармонично сочетается с современным сервисом.",
        "FEATURES": "<li><strong>Казанский Кремль и Мечеть Кул-Шариф:</strong> Эксклюзивные экскурсии с погружением в историю татарских ханов.</li><li><strong>Свияжск и Болгар:</strong> Индивидуальные туры на премиум-катерах по реке Волге.</li><li><strong>Premium Spa & Wellness:</strong> Лучшие национальные спа-комплексы и закрытые бани.</li>",
        "FOOD": "Казань — центр халяльной гастрономии. Мы собрали рестораны, где можно попробовать аутентичную татарскую кухню (эчпочмаки, конина) в люксовом исполнении и строгом соответствии с канонами Ислама.",
        "PRICE": "$39"
    },
    {
        "file": "tripwire-murmansk.html",
        "CITY_NAME": "Мурманск",
        "CITY_EN": "Murmansk",
        "SUBTITLE": "Охота за Северным сиянием на краю света.",
        "INTRO": "Уникальное направление, набирающее огромную популярность. Мы предлагаем увидеть Арктику, не отказываясь от роскоши и абсолютного комфорта.",
        "FEATURES": "<li><strong>Premium Glamping:</strong> Проживание в стеклянных иглу посреди тундры, чтобы наблюдать за сиянием прямо из теплой постели.</li><li><strong>Териберка и Ледовитый океан:</strong> Индивидуальные экспедиции на заряженных VIP-внедорожниках (G-Class).</li><li><strong>Морские прогулки:</strong> Выход в море на современных яхтах для наблюдения за китами.</li>",
        "FOOD": "Арктическая кухня — деликатесы из оленины, крабы и морские ежи. В нашем гиде собраны только те места, где могут организовать специальное халяль-меню даже на краю земли.",
        "PRICE": "$79"
    }
]

for c in cities:
    out = template
    for k, v in c.items():
        out = out.replace("{{" + k + "}}", v)
    with open(c["file"], "w", encoding="utf-8") as f:
        f.write(out)
