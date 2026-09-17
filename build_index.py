import os

files = {}

html_base = """<!DOCTYPE html>
<html lang="{LANG}" {DIR_ATTR}>
<head>
  <meta charset="UTF-8">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>{TITLE}</title>
  <link rel="icon" type="image/jpeg" href="images/logo_clear.png">
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600&family=Manrope:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css?v=2">
  {EXTRA_HEAD}
</head>
<body>
  <canvas id="gl-canvas"></canvas>
  <div class="grain-overlay"></div>

  <nav class="navbar" id="navbar">
    <a href="{LINK_HOME}" class="nav-logo">
      <img src="images/logo_clear.png" alt="VT Logo" class="logo-img">
      <span class="logo-text">VT VIP</span>
    </a>
    <div class="nav-links">
      <a href="{LINK_HOME}" style="color: var(--gold);">{NAV_HOME}</a>
      <a href="{LINK_FLEET}">{NAV_FLEET}</a>
      <a href="{LINK_DEST}">{NAV_DEST}</a>
    </div>
    <div class="lang-switcher">
      <a href="index.html" class="{LANG_RU_CLASS}">RU</a>
      <a href="en.html" class="{LANG_EN_CLASS}">EN</a>
      <a href="ar.html" class="{LANG_AR_CLASS}">AR</a>
    </div>
  </nav>

  <div id="ui-layer">
    <div class="stage">
      <section class="page is-active" data-index="0" id="hero">
        <div class="content">
          <img src="images/logo_clear.png" alt="VT Logo" class="hero-logo reveal-3d">
          <h1 class="reveal-3d gradient-text">{H1}</h1>
          <p class="hero-subtitle reveal-3d">{HERO_SUB}</p>
          <div class="actions reveal-3d">
            <a href="#contacts" class="btn btn-primary">{BTN_BOOK}</a>
            <a href="#contacts" class="btn btn-outline">{BTN_B2B}</a>
          </div>
        </div>
      </section>

      <section class="page" data-index="1">
        <div class="content">
          <div class="card reveal-3d">
            <h2 class="gradient-text">{S1_H}</h2>
            <p>{S1_P}</p>
          </div>
        </div>
      </section>

      <section class="page" data-index="2">
        <div class="content">
          <div class="card reveal-3d">
            <h2 class="gradient-text">{S2_H}</h2>
            <p>{S2_P}</p>
          </div>
        </div>
      </section>

      <section class="page" data-index="3">
        <div class="content">
          <div class="card reveal-3d">
            <h2 class="gradient-text">{S3_H}</h2>
            <p>{S3_P}</p>
          </div>
        </div>
      </section>

      <section class="page" data-index="4">
        <div class="content">
          <div class="card reveal-3d">
            <h2 class="gradient-text">{S4_H}</h2>
            <p>{S4_P}</p>
          </div>
        </div>
      </section>

      <section class="page" data-index="5">
        <div class="content">
          <div class="card reveal-3d">
            <h2 class="gradient-text">{S5_H}</h2>
            <p>{S5_P}</p>
          </div>
        </div>
      </section>

      <section class="page" data-index="6">
        <div class="content">
          <div class="card reveal-3d">
            <h2 class="gradient-text">{S6_H}</h2>
            <p>{S6_P}</p>
          </div>
        </div>
      </section>

      <section class="page" data-index="7" id="contacts">
        <div class="content">
          <div class="card reveal-3d">
            <h2>{S7_H}</h2>
            <p>{S7_P1}</p>
            <p class="contact-info">Email: info@vt-vip.ru<br>Телефон / WhatsApp: +7 495 000 00 00</p>
            <a href="mailto:info@vt-vip.ru" class="btn btn-primary">{BTN_CONTACT}</a>
          </div>
        </div>
      </section>
    </div>
  </div>

  <div id="loader">
    <img src="images/logo_clear.png" alt="Loading" class="loader-logo">
    <div id="progress-bar-wrap">
      <div id="progress-bar"></div>
    </div>
  </div>

  <a href="https://wa.me/74950000000" class="floating-concierge" target="_blank">
    <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.888-.788-1.487-1.761-1.663-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.052 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
    <span>Personal Concierge</span>
  </a>
  <script src="app.js?v=2"></script>
</body>
</html>"""

ru_data = {
    'LANG': 'ru', 'DIR_ATTR': '', 'EXTRA_HEAD': '',
    'LINK_HOME': 'index.html', 'LINK_FLEET': 'fleet.html', 'LINK_DEST': 'destinations.html',
    'LANG_RU_CLASS': 'active', 'LANG_EN_CLASS': '', 'LANG_AR_CLASS': '',
    'TITLE': 'Визуализированный Трансфер - VIP Сервис в России',
    'NAV_HOME': 'Главная', 'NAV_FLEET': 'Автопарк', 'NAV_DEST': 'Путеводители',
    'H1': 'Визуализированный Трансфер',
    'HERO_SUB': 'Новый стандарт премиального сервиса в России. Исключительный комфорт для взыскательных гостей.',
    'BTN_BOOK': 'Забронировать поездку', 'BTN_B2B': 'B2B Партнерство',
    'S1_H': 'Искусство движения',
    'S1_P': 'Мы предлагаем полностью контролируемый опыт. Ваш личный водитель, безупречный этикет и строгий дресс-код. Автопарк из последних моделей Mercedes-Benz V-Class, S-Class и Maybach.',
    'S2_H': 'Москва',
    'S2_P': 'Столица роскоши и ритма. От трансферов из Внуково-3 до деловых встреч в Москва-Сити и шопинга в ЦУМ с персональным сопровождением.',
    'S3_H': 'Санкт-Петербург',
    'S3_P': 'Погрузитесь в атмосферу имперской столицы. Трансферы из Пулково, поездки по историческому центру и загородным резиденциям в атмосфере абсолютной приватности.',
    'S4_H': 'Сочи и Красная Поляна',
    'S4_P': 'Панорамные поездки вдоль Черного моря и серпантинам Кавказских гор. Автомобили подготовлены к любым условиям для вашего комфорта.',
    'S5_H': 'Казань',
    'S5_P': 'Жемчужина Татарстана с богатым наследием. Идеальные маршруты к Казанскому Кремлю и лучшим халяль-ресторанам города.',
    'S6_H': 'Внимание к каждой детали',
    'S6_P': 'Мы предвосхищаем ваши желания. Халяль-сопровождение, премиальная вода, высокоскоростной Wi-Fi. Полная конфиденциальность маршрутов (NDA) и анонимная оплата в криптовалюте (USDT/BTC).',
    'S7_H': 'Глобальное партнерство',
    'S7_P1': 'Прямая интеграция с туристическими компаниями ОАЭ. Мы предлагаем эксклюзивные B2B условия (Agency Commission) для агентов Дубая и стран Залива.',
    'BTN_CONTACT': 'Связаться с нами'
}

en_data = {
    'LANG': 'en', 'DIR_ATTR': '', 'EXTRA_HEAD': '',
    'LINK_HOME': 'en.html', 'LINK_FLEET': 'fleet-en.html', 'LINK_DEST': 'destinations-en.html',
    'LANG_RU_CLASS': '', 'LANG_EN_CLASS': 'active', 'LANG_AR_CLASS': '',
    'TITLE': 'Visualized Transfer Vip - Premium Transfer in Russia',
    'NAV_HOME': 'Home', 'NAV_FLEET': 'Our Fleet', 'NAV_DEST': 'Tripwires & Concierge',
    'H1': 'Visualized Transfer Vip',
    'HERO_SUB': 'A new standard of premium service in Russia. Exceptional comfort for discerning guests.',
    'BTN_BOOK': 'Book a Ride', 'BTN_B2B': 'B2B Partnership',
    'S1_H': 'The Art of Movement',
    'S1_P': 'We offer a fully controlled, high-end experience. Your personal chauffeur, impeccable etiquette, and strict dress code. Our fleet features only the latest Mercedes-Benz V-Class, S-Class and Maybach models.',
    'S2_H': 'Moscow',
    'S2_P': 'The capital of luxury and rhythm. From Vnukovo-3 transfers to business meetings in Moscow City and premium shopping at TSUM with personal escorts.',
    'S3_H': 'Saint Petersburg',
    'S3_P': 'Immerse yourself in the atmosphere of the imperial capital. Pulkovo airport transfers and journeys through the historic center in absolute privacy.',
    'S4_H': 'Sochi & Krasnaya Polyana',
    'S4_P': 'Panoramic drives along the Black Sea coast and the winding roads of the Caucasus Mountains.',
    'S5_H': 'Kazan',
    'S5_P': 'The pearl of Tatarstan. Ideal routes to the Kazan Kremlin and the best Halal restaurants in the city.',
    'S6_H': 'Attention to Every Detail',
    'S6_P': 'We anticipate your desires. Halal-compliant service, complete confidentiality of your routes (NDA) and anonymous crypto payments (USDT/BTC).',
    'S7_H': 'Global Partnership',
    'S7_P1': 'Direct integration with UAE travel companies. We offer exclusive B2B terms for travel agents in Dubai and the Gulf countries.',
    'BTN_CONTACT': 'Contact Us'
}

ar_data = {
    'LANG': 'ar', 'DIR_ATTR': 'dir="rtl"',
    'EXTRA_HEAD': "<style> body { font-family: 'Cairo', sans-serif; } h1, h2, .logo-text { font-family: 'Cormorant Garamond', serif; } h1 { direction: ltr; display: inline-block; } </style>",
    'LINK_HOME': 'ar.html', 'LINK_FLEET': 'fleet-ar.html', 'LINK_DEST': 'destinations-ar.html',
    'LANG_RU_CLASS': '', 'LANG_EN_CLASS': '', 'LANG_AR_CLASS': 'active',
    'TITLE': 'Visualized Transfer Vip - النقل الفاخر',
    'NAV_HOME': 'الرئيسية', 'NAV_FLEET': 'أسطولنا', 'NAV_DEST': 'الأدلة والكونسيرج',
    'H1': 'Visualized Transfer Vip',
    'HERO_SUB': 'معيار جديد للخدمة المتميزة في روسيا. راحة استثنائية لضيوفنا المميزين.',
    'BTN_BOOK': 'احجز رحلة', 'BTN_B2B': 'شراكة B2B',
    'S1_H': 'فن التنقل',
    'S1_P': 'نحن نقدم تجربة فاخرة خاضعة للرقابة الكاملة. سائقك الشخصي، آداب لا تشوبها شائبة، وقواعد لباس صارمة. يشمل أسطولنا أحدث الموديلات.',
    'S2_H': 'موسكو',
    'S2_P': 'عاصمة الفخامة. من تنقلات فنوكوفو-3 إلى اجتماعات العمل في مدينة موسكو والتسوق الراقي في TSUM مع مرافقين شخصيين.',
    'S3_H': 'سانت بطرسبرغ',
    'S3_P': 'انغمس في أجواء العاصمة الإمبراطورية. خدمة نقل من مطار بولكوفو في خصوصية تامة.',
    'S4_H': 'سوتشي وكراسنيا بوليانا',
    'S4_P': 'رحلات بانورامية على طول ساحل البحر الأسود.',
    'S5_H': 'قازان (كازان)',
    'S5_P': 'لؤلؤة تتارستان. مسارات مثالية إلى كرملين قازان وأفضل المطاعم الحلال.',
    'S6_H': 'الاهتمام بكل التفاصيل',
    'S6_P': 'نحن نتوقع رغباتك. خدمة حلال وسرية تامة لمساراتك ودفع بالعملات المشفرة.',
    'S7_H': 'شراكة عالمية',
    'S7_P1': 'تكامل مباشر مع شركات السفر في الإمارات. نقدم شروط B2B حصرية.',
    'BTN_CONTACT': 'اتصل بنا'
}

files['index.html'] = html_base.format(**ru_data)
files['en.html'] = html_base.format(**en_data)
files['ar.html'] = html_base.format(**ar_data)

for k, v in files.items():
    with open(k, "w", encoding="utf-8") as f:
        f.write(v)
