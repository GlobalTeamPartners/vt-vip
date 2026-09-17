import os

files = {}

files['destinations.html'] = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Направления и Путеводители - VT VIP</title>
  <link rel="icon" type="image/jpeg" href="images/logo.png">
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600&family=Manrope:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body class="standard-page">
  <div class="grain-overlay"></div>
  <nav class="navbar" id="navbar">
    <a href="index.html" class="nav-logo">
      <img src="images/logo.png" alt="VT Logo" class="logo-img"><span class="logo-text">VT VIP</span>
    </a>
    <div class="nav-links">
      <a href="index.html">Главная</a>
      <a href="fleet.html">Автопарк</a>
      <a href="destinations.html" style="color: var(--gold);">Путеводители</a>
    </div>
    <div class="lang-switcher">
      <a href="destinations.html" class="active">RU</a>
      <a href="destinations-en.html">EN</a>
      <a href="destinations-ar.html">AR</a>
    </div>
  </nav>

  <div class="destinations-hero reveal-3d" style="opacity: 1; transform: none;">
    <h1 class="gradient-text">Путеводители и Эксклюзив</h1>
    <p>Добавьте авторский путеводитель к вашему VIP-трансферу. Мы собрали самые закрытые локации, лучшие рестораны и премиальные активности.</p>
  </div>

  <div class="destinations-grid">
    <div class="destination-card" style="cursor: pointer;" onclick="window.location.href='tripwire-moscow.html'">
      <h3><a href="tripwire-moscow.html" style="color: var(--gold); text-decoration: none;">Москва</a></h3>
      <p>Столица роскоши и ритма. Идеально для бизнеса и премиального шопинга.</p>
      <ul><li>Закрытые VIP-комнаты ЦУМ и ГУМ</li><li>Рестораны с халяль-меню (Москва-Сити)</li><li>Охраняемые маршруты</li></ul>
      <div class="price-tag">От $49</div>
      <a href="tripwire-moscow.html" class="btn btn-outline" style="text-align: center;">Подробнее о путеводителе</a>
    </div>
    <div class="destination-card" style="cursor: pointer;" onclick="window.location.href='tripwire-spb.html'">
      <h3><a href="tripwire-spb.html" style="color: var(--gold); text-decoration: none;">Санкт-Петербург</a></h3>
      <p>Имперская эстетика и белые ночи. Северная столица России.</p>
      <ul><li>Индивидуальные экскурсии в Эрмитаж</li><li>Аренда яхт по каналам Невы</li><li>Закрытые дворцы</li></ul>
      <div class="price-tag">От $49</div>
      <a href="tripwire-spb.html" class="btn btn-outline" style="text-align: center;">Подробнее о путеводителе</a>
    </div>
    <div class="destination-card" style="cursor: pointer;" onclick="window.location.href='tripwire-sochi.html'">
      <h3><a href="tripwire-sochi.html" style="color: var(--gold); text-decoration: none;">Сочи (Красная Поляна)</a></h3>
      <p>Русская Ривьера. Сочетание морского бриза и горнолыжных курортов.</p>
      <ul><li>VIP-шатры на пляже и яхты</li><li>Вертолетные прогулки</li><li>Казино премиум-уровня</li></ul>
      <div class="price-tag">От $59</div>
      <a href="tripwire-sochi.html" class="btn btn-outline" style="text-align: center;">Подробнее о путеводителе</a>
    </div>
    <div class="destination-card" style="cursor: pointer;" onclick="window.location.href='tripwire-kazan.html'">
      <h3><a href="tripwire-kazan.html" style="color: var(--gold); text-decoration: none;">Казань</a></h3>
      <p>Пересечение культур. Жемчужина Татарстана с богатым наследием.</p>
      <ul><li>Эксклюзивные туры в Кремль</li><li>Лучшие халяль-рестораны</li><li>Прогулки по Волге</li></ul>
      <div class="price-tag">От $39</div>
      <a href="tripwire-kazan.html" class="btn btn-outline" style="text-align: center;">Подробнее о путеводителе</a>
    </div>
    <div class="destination-card" style="cursor: pointer;" onclick="window.location.href='tripwire-murmansk.html'">
      <h3><a href="tripwire-murmansk.html" style="color: var(--gold); text-decoration: none;">Мурманск</a></h3>
      <p>Охота за Северным сиянием на краю света в абсолютном комфорте.</p>
      <ul><li>Premium Glamping</li><li>Арктическая гастрономия</li><li>Экспедиции на внедорожниках</li></ul>
      <div class="price-tag">От $79</div>
      <a href="tripwire-murmansk.html" class="btn btn-outline" style="text-align: center;">Подробнее о путеводителе</a>
    </div>
  </div>
  <a href="https://wa.me/74950000000" class="floating-concierge" target="_blank"><svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.888-.788-1.487-1.761-1.663-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.052 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg><span>Personal Concierge</span></a>
</body>
</html>"""

files['destinations-en.html'] = files['destinations.html'].replace('lang="ru"', 'lang="en"').replace('Главная', 'Home').replace('Автопарк', 'Our Fleet').replace('Путеводители', 'Tripwires').replace('class="active">RU', '>RU').replace('>EN', 'class="active">EN').replace('Путеводители и Эксклюзив', 'City Guides & Exclusives').replace('Добавьте авторский путеводитель к вашему VIP-трансферу. Мы собрали самые закрытые локации, лучшие рестораны и премиальные активности.', 'Add a premium curated guide to your VIP transfer order. We have gathered the most private locations, top restaurants, and premium activities.').replace('Подробнее о путеводителе', 'Read More About Guide').replace('Москва', 'Moscow').replace('Столица роскоши и ритма. Идеально для бизнеса и премиального шопинга.', 'The capital of luxury and rhythm. Ideal for business and premium shopping.').replace('Закрытые VIP-комнаты ЦУМ и ГУМ', 'Private VIP shopping rooms at TSUM and GUM').replace('Рестораны с халяль-меню (Москва-Сити)', 'Halal-friendly restaurants (Moscow City)').replace('Охраняемые маршруты', 'Secure routes').replace('Санкт-Петербург', 'Saint Petersburg').replace('Имперская эстетика и белые ночи. Северная столица России.', 'Imperial aesthetics and white nights. The northern capital of Russia.').replace('Индивидуальные экскурсии в Эрмитаж', 'Private tours of the Hermitage').replace('Аренда яхт по каналам Невы', 'Yacht rentals along Neva canals').replace('Закрытые дворцы', 'Closed palaces').replace('Сочи (Красная Поляна)', 'Sochi (Krasnaya Polyana)').replace('Русская Ривьера. Сочетание морского бриза и горнолыжных курортов.', 'The Russian Riviera. A combination of sea breeze and ski resorts.').replace('VIP-шатры на пляже и яхты', 'VIP beach cabanas and yachts').replace('Вертолетные прогулки', 'Helicopter tours').replace('Казино премиум-уровня', 'Premium casinos').replace('Казань', 'Kazan').replace('Пересечение культур. Жемчужина Татарстана с богатым наследием.', 'Intersection of cultures. The pearl of Tatarstan with a rich heritage.').replace('Эксклюзивные туры в Кремль', 'Exclusive tours of the Kremlin').replace('Лучшие халяль-рестораны', 'Best Halal restaurants').replace('Прогулки по Волге', 'Volga river cruises').replace('Мурманск', 'Murmansk').replace('Охота за Северным сиянием на краю света в абсолютном комфорте.', 'Hunting for the Northern Lights at the edge of the world in absolute comfort.').replace('Арктическая гастрономия', 'Arctic gastronomy').replace('Экспедиции на внедорожниках', 'SUV expeditions').replace('От $', 'From $')

files['destinations-ar.html'] = files['destinations-en.html'].replace('lang="en"', 'lang="ar" dir="rtl"').replace('<head>', "<head>\n  <style> body { font-family: 'Cairo', sans-serif; } h1, h2, h3, .logo-text { font-family: 'Cormorant Garamond', serif; } h1 { direction: ltr; display: inline-block; } </style>").replace('Home', 'الرئيسية').replace('Our Fleet', 'أسطولنا').replace('Tripwires', 'الأدلة').replace('class="active">EN', '>EN').replace('>AR', 'class="active">AR').replace('City Guides & Exclusives', 'أدلة المدن والحصريات').replace('Add a premium curated guide to your VIP transfer order. We have gathered the most private locations, top restaurants, and premium activities.', 'أضف دليلاً متميزًا إلى طلب النقل الخاص بك. لقد جمعنا أكثر المواقع سرية، وأفضل المطاعم، والأنشطة الفاخرة.').replace('Read More About Guide', 'اقرأ المزيد عن الدليل').replace('Moscow', 'موسكو').replace('The capital of luxury and rhythm. Ideal for business and premium shopping.', 'عاصمة الفخامة. مثالية للأعمال والتسوق الراقي.').replace('Private VIP shopping rooms at TSUM and GUM', 'غرف تسوق VIP خاصة في TSUM و GUM').replace('Halal-friendly restaurants (Moscow City)', 'مطاعم حلال (مدينة موسكو)').replace('Secure routes', 'مسارات آمنة').replace('Saint Petersburg', 'سانت بطرسبرغ').replace('Imperial aesthetics and white nights. The northern capital of Russia.', 'الجمال الإمبراطوري والليالي البيضاء.').replace('Private tours of the Hermitage', 'جولات خاصة في متحف الإرميتاج').replace('Yacht rentals along Neva canals', 'تأجير يخوت في قنوات نيفا').replace('Closed palaces', 'دخول القصور المغلقة').replace('Sochi (Krasnaya Polyana)', 'سوتشي (كراسنايا بوليانا)').replace('The Russian Riviera. A combination of sea breeze and ski resorts.', 'الريفييرا الروسية. مزيج من نسيم البحر ومنتجعات التزلج.').replace('VIP beach cabanas and yachts', 'خيم شاطئية لكبار الشخصيات ويخوت').replace('Helicopter tours', 'جولات بالطائرة المروحية').replace('Premium casinos', 'كازينوهات فاخرة').replace('Kazan', 'قازان').replace('Intersection of cultures. The pearl of Tatarstan with a rich heritage.', 'تقاطع الثقافات. لؤلؤة تتارستان.').replace('Exclusive tours of the Kremlin', 'جولات حصرية في الكرملين').replace('Best Halal restaurants', 'أفضل المطاعم الحلال').replace('Volga river cruises', 'رحلات نهرية على الفولغا').replace('Murmansk', 'مورمانسك').replace('Hunting for the Northern Lights at the edge of the world in absolute comfort.', 'مطاردة الأضواء الشمالية على حافة العالم.').replace('Premium Glamping', 'تخييم فاخر').replace('Arctic gastronomy', 'فن الطهي القطبي').replace('SUV expeditions', 'رحلات استكشافية بسيارات الدفع الرباعي').replace('From $', 'تبدأ من $')

for k, v in files.items():
    with open(k, "w", encoding="utf-8") as f:
        f.write(v)
