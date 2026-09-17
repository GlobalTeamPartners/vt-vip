import os

files = {}

files['index.html'] = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Визуализированный Трансфер - VIP Сервис в России</title>
  <link rel="icon" type="image/jpeg" href="images/logo.png">
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600&family=Manrope:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <canvas id="gl-canvas"></canvas>
  <div class="grain-overlay"></div>

  <nav class="navbar" id="navbar">
    <a href="#" class="nav-logo">
      <img src="images/logo.png" alt="VT Logo" class="logo-img">
      <span class="logo-text">VT VIP</span>
    </a>
    <div class="nav-links">
      <a href="index.html" style="color: var(--gold);">Главная</a>
      <a href="fleet.html">Автопарк</a>
      <a href="destinations.html">Путеводители</a>
    </div>
    <div class="lang-switcher">
      <a href="index.html" class="active">RU</a>
      <a href="en.html">EN</a>
      <a href="ar.html">AR</a>
    </div>
  </nav>

  <div id="ui-layer">
    <div class="stage">
      <section class="page is-active" data-index="0" id="hero">
        <div class="content">
          <img src="images/logo.png" alt="VT Logo" class="hero-logo reveal-3d">
          <h1 class="reveal-3d gradient-text">Визуализированный Трансфер</h1>
          <p class="hero-subtitle reveal-3d">Новый стандарт премиального сервиса в России. Исключительный комфорт для взыскательных гостей.</p>
          <div class="actions reveal-3d">
            <a href="#contacts" class="btn btn-primary">Забронировать поездку</a>
            <a href="#contacts" class="btn btn-outline">B2B Партнерство</a>
          </div>
        </div>
      </section>

      <section class="page" data-index="1">
        <div class="content">
          <div class="card reveal-3d">
            <h2 class="gradient-text">Искусство движения</h2>
            <p>Мы предлагаем полностью контролируемый опыт. Ваш личный водитель, безупречный этикет и строгий дресс-код. Автопарк из последних моделей Mercedes-Benz V-Class, S-Class и Maybach.</p>
          </div>
        </div>
      </section>

      <section class="page" data-index="2">
        <div class="content">
          <div class="card reveal-3d">
            <h2 class="gradient-text">Москва</h2>
            <p>Столица роскоши и ритма. От трансферов из Внуково-3 до деловых встреч в Москва-Сити и шопинга в ЦУМ с персональным сопровождением.</p>
          </div>
        </div>
      </section>

      <section class="page" data-index="3">
        <div class="content">
          <div class="card reveal-3d">
            <h2 class="gradient-text">Санкт-Петербург</h2>
            <p>Погрузитесь в атмосферу имперской столицы. Трансферы из Пулково, поездки по историческому центру и загородным резиденциям в атмосфере абсолютной приватности.</p>
          </div>
        </div>
      </section>

      <section class="page" data-index="4">
        <div class="content">
          <div class="card reveal-3d">
            <h2 class="gradient-text">Сочи и Красная Поляна</h2>
            <p>Панорамные поездки вдоль Черного моря и серпантинам Кавказских гор. Автомобили подготовлены к любым условиям для вашего комфорта.</p>
          </div>
        </div>
      </section>

      <section class="page" data-index="5">
        <div class="content">
          <div class="card reveal-3d">
            <h2 class="gradient-text">Казань</h2>
            <p>Жемчужина Татарстана с богатым наследием. Идеальные маршруты к Казанскому Кремлю и лучшим халяль-ресторанам города.</p>
          </div>
        </div>
      </section>

      <section class="page" data-index="6">
        <div class="content">
          <div class="card reveal-3d">
            <h2 class="gradient-text">Внимание к каждой детали</h2>
            <p>Мы предвосхищаем ваши желания. Халяль-сопровождение, премиальная вода, высокоскоростной Wi-Fi. Полная конфиденциальность маршрутов (NDA) и анонимная оплата в криптовалюте (USDT/BTC).</p>
          </div>
        </div>
      </section>

      <section class="page" data-index="7" id="contacts">
        <div class="content">
          <div class="card reveal-3d">
            <h2>Глобальное партнерство</h2>
            <p>Прямая интеграция с туристическими компаниями ОАЭ. Мы предлагаем эксклюзивные B2B условия (Agency Commission) для агентов Дубая и стран Залива.</p>
            <p class="contact-info">Email: info@vt-vip.ru<br>Телефон / WhatsApp: +7 495 000 00 00</p>
            <a href="mailto:info@vt-vip.ru" class="btn btn-primary">Связаться с нами</a>
          </div>
        </div>
      </section>
    </div>
  </div>

  <div id="loader">
    <img src="images/logo.png" alt="Loading" class="loader-logo">
    <div id="progress-bar-wrap">
      <div id="progress-bar"></div>
    </div>
  </div>

  <a href="https://wa.me/74950000000" class="floating-concierge" target="_blank">
    <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.888-.788-1.487-1.761-1.663-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.052 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
    <span>Personal Concierge</span>
  </a>
  <script src="app.js"></script>
</body>
</html>"""

files['en.html'] = files['index.html'].replace('lang="ru"', 'lang="en"').replace('Визуализированный Трансфер - VIP Сервис в России', 'Visualized Transfer Vip - Premium Transfer in Russia').replace('Главная', 'Home').replace('Автопарк', 'Our Fleet').replace('Путеводители', 'Tripwires & Concierge').replace('class="active">RU', '>RU').replace('>EN', 'class="active">EN').replace('Новый стандарт премиального сервиса в России. Исключительный комфорт для взыскательных гостей.', 'A new standard of premium service in Russia. Exceptional comfort for discerning guests.').replace('Забронировать поездку', 'Book a Ride').replace('B2B Партнерство', 'B2B Partnership').replace('Искусство движения', 'The Art of Movement').replace('Мы предлагаем полностью контролируемый опыт. Ваш личный водитель, безупречный этикет и строгий дресс-код. Автопарк из последних моделей Mercedes-Benz V-Class, S-Class и Maybach.', 'We offer a fully controlled, high-end experience. Your personal chauffeur, impeccable etiquette, and strict dress code. Our fleet features only the latest Mercedes-Benz models.').replace('Москва', 'Moscow').replace('Столица роскоши и ритма. От трансферов из Внуково-3 до деловых встреч в Москва-Сити и шопинга в ЦУМ с персональным сопровождением.', 'The capital of luxury and rhythm. Ideal for business meetings and premium shopping with personal escorts.').replace('Санкт-Петербург', 'Saint Petersburg').replace('Погрузитесь в атмосферу имперской столицы. Трансферы из Пулково, поездки по историческому центру и загородным резиденциям в атмосфере абсолютной приватности.', 'Immerse yourself in the atmosphere of the imperial capital. Pulkovo airport transfers and journeys through the historic center in absolute privacy.').replace('Сочи и Красная Поляна', 'Sochi & Krasnaya Polyana').replace('Панорамные поездки вдоль Черного моря и серпантинам Кавказских гор. Автомобили подготовлены к любым условиям для вашего комфорта.', 'Panoramic drives along the Black Sea coast and the winding roads of the Caucasus Mountains.').replace('Казань', 'Kazan').replace('Жемчужина Татарстана с богатым наследием. Идеальные маршруты к Казанскому Кремлю и лучшим халяль-ресторанам города.', 'The pearl of Tatarstan. Ideal routes to the Kazan Kremlin and the best Halal restaurants in the city.').replace('Внимание к каждой детали', 'Attention to Every Detail').replace('Мы предвосхищаем ваши желания. Халяль-сопровождение, премиальная вода, высокоскоростной Wi-Fi. Полная конфиденциальность маршрутов (NDA) и анонимная оплата в криптовалюте (USDT/BTC).', 'We anticipate your desires. Halal-compliant service, complete confidentiality of your routes (NDA) and anonymous crypto payments (USDT/BTC).').replace('Глобальное партнерство', 'Global Partnership').replace('Прямая интеграция с туристическими компаниями ОАЭ. Мы предлагаем эксклюзивные B2B условия (Agency Commission) для агентов Дубая и стран Залива.', 'Direct integration with UAE travel companies. We offer exclusive B2B terms for travel agents in Dubai and the Gulf countries.').replace('Связаться с нами', 'Contact Us').replace('Визуализированный Трансфер', 'Visualized Transfer Vip')

files['ar.html'] = files['en.html'].replace('lang="en"', 'lang="ar" dir="rtl"').replace('<head>', "<head>\n  <style> body { font-family: 'Cairo', sans-serif; } h1, h2, .logo-text { font-family: 'Cormorant Garamond', serif; } h1 { direction: ltr; display: inline-block; } </style>").replace('Home', 'الرئيسية').replace('Our Fleet', 'أسطولنا').replace('Tripwires & Concierge', 'الأدلة والكونسيرج').replace('A new standard of premium service in Russia. Exceptional comfort for discerning guests.', 'معيار جديد للخدمة المتميزة في روسيا. راحة استثنائية لضيوفنا المميزين.').replace('Book a Ride', 'احجز رحلة').replace('B2B Partnership', 'شراكة B2B').replace('The Art of Movement', 'فن التنقل').replace('We offer a fully controlled, high-end experience. Your personal chauffeur, impeccable etiquette, and strict dress code. Our fleet features only the latest Mercedes-Benz models.', 'نحن نقدم تجربة فاخرة خاضعة للرقابة الكاملة. سائقك الشخصي، آداب لا تشوبها شائبة، وقواعد لباس صارمة.').replace('Moscow', 'موسكو').replace('The capital of luxury and rhythm. Ideal for business meetings and premium shopping with personal escorts.', 'عاصمة الفخامة. مثالية لاجتماعات الأعمال والتسوق الراقي.').replace('Saint Petersburg', 'سانت بطرسبرغ').replace('Immerse yourself in the atmosphere of the imperial capital. Pulkovo airport transfers and journeys through the historic center in absolute privacy.', 'انغمس في أجواء العاصمة الإمبراطورية في خصوصية تامة.').replace('Sochi & Krasnaya Polyana', 'سوتشي وكراسنيا بوليانا').replace('Panoramic drives along the Black Sea coast and the winding roads of the Caucasus Mountains.', 'رحلات بانورامية على طول ساحل البحر الأسود.').replace('Kazan', 'قازان (كازان)').replace('The pearl of Tatarstan. Ideal routes to the Kazan Kremlin and the best Halal restaurants in the city.', 'لؤلؤة تتارستان. مسارات مثالية إلى كرملين قازان وأفضل المطاعم الحلال.').replace('Attention to Every Detail', 'الاهتمام بكل التفاصيل').replace('We anticipate your desires. Halal-compliant service, complete confidentiality of your routes (NDA) and anonymous crypto payments (USDT/BTC).', 'نحن نتوقع رغباتك. خدمة حلال وسرية تامة لمساراتك ودفع بالعملات المشفرة.').replace('Global Partnership', 'شراكة عالمية').replace('Direct integration with UAE travel companies. We offer exclusive B2B terms for travel agents in Dubai and the Gulf countries.', 'تكامل مباشر مع شركات السفر في الإمارات. نقدم شروط B2B حصرية.').replace('Contact Us', 'اتصل بنا').replace('class="active">EN', '>EN').replace('>AR', 'class="active">AR')

for k, v in files.items():
    with open(k, "w", encoding="utf-8") as f:
        f.write(v)
