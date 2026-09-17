import os

files = {}

# ----------------- FLEET PAGES -----------------
files['fleet.html'] = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Автопарк - VT VIP</title>
  <link rel="icon" type="image/jpeg" href="images/logo.png">
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600&family=Manrope:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body class="standard-page">
  <div class="grain-overlay"></div>
  <nav class="navbar" id="navbar">
    <a href="index.html" class="nav-logo">
      <img src="images/logo.png" alt="VT Logo" class="logo-img">
      <span class="logo-text">VT VIP</span>
    </a>
    <div class="nav-links">
      <a href="index.html">Главная</a>
      <a href="fleet.html" style="color: var(--gold);">Автопарк</a>
      <a href="destinations.html">Путеводители</a>
    </div>
    <div class="lang-switcher">
      <a href="fleet.html" class="active">RU</a>
      <a href="fleet-en.html">EN</a>
      <a href="fleet-ar.html">AR</a>
    </div>
  </nav>

  <div class="destinations-hero reveal-3d" style="opacity: 1; transform: none;">
    <h1 class="gradient-text">Наш Премиальный Автопарк</h1>
    <p>Безупречные автомобили, прошедшие строгий контроль. Бронированные версии и сопровождение охраны доступны по запросу.</p>
  </div>
  <div class="destinations-grid">
    <div class="destination-card">
      <h3>Mercedes-Benz Maybach S-Class</h3>
      <p>Абсолютный эталон роскоши для первых лиц и топ-менеджмента.</p>
      <ul><li>Сиденья Executive с массажем</li><li>Идеальная шумоизоляция</li><li>Только модели 2023-2025 года</li></ul>
      <a href="mailto:info@vt-vip.ru?subject=Book Maybach" class="btn btn-outline" style="text-align: center;">Забронировать</a>
    </div>
    <div class="destination-card">
      <h3>Mercedes-Benz V-Class VIP</h3>
      <p>Простор и комфорт. Идеально для делегаций и семейных путешествий.</p>
      <ul><li>Перегородка от водителя (Full Privacy)</li><li>Apple TV, PS5 и премиальный звук</li><li>Капитанские кресла с оттоманкой</li></ul>
      <a href="mailto:info@vt-vip.ru?subject=Book V-Class" class="btn btn-outline" style="text-align: center;">Забронировать</a>
    </div>
    <div class="destination-card">
      <h3>Mercedes-Benz G-Class (Escort)</h3>
      <p>Статус и безопасность. Сопровождение в любых условиях.</p>
      <ul><li>Вооруженная охрана (опционально)</li><li>Высший уровень защиты</li><li>Сопровождение кортежей</li></ul>
      <a href="mailto:info@vt-vip.ru?subject=Book G-Class" class="btn btn-outline" style="text-align: center;">Забронировать</a>
    </div>
  </div>
  <a href="https://wa.me/74950000000" class="floating-concierge" target="_blank"><svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.888-.788-1.487-1.761-1.663-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.052 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg><span>Personal Concierge</span></a>
</body>
</html>"""

files['fleet-en.html'] = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Our Fleet - VT VIP</title>
  <link rel="icon" type="image/jpeg" href="images/logo.png">
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600&family=Manrope:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body class="standard-page">
  <div class="grain-overlay"></div>
  <nav class="navbar" id="navbar">
    <a href="en.html" class="nav-logo">
      <img src="images/logo.png" alt="VT Logo" class="logo-img">
      <span class="logo-text">VT VIP</span>
    </a>
    <div class="nav-links">
      <a href="en.html">Home</a>
      <a href="fleet-en.html" style="color: var(--gold);">Our Fleet</a>
      <a href="destinations-en.html">Tripwires & Concierge</a>
    </div>
    <div class="lang-switcher">
      <a href="fleet.html">RU</a>
      <a href="fleet-en.html" class="active">EN</a>
      <a href="fleet-ar.html">AR</a>
    </div>
  </nav>

  <div class="destinations-hero reveal-3d" style="opacity: 1; transform: none;">
    <h1 class="gradient-text">Our Premium Fleet</h1>
    <p>Impeccable vehicles that have passed strict quality control. Armored versions and armed escorts available upon request.</p>
  </div>
  <div class="destinations-grid">
    <div class="destination-card">
      <h3>Mercedes-Benz Maybach S-Class</h3>
      <p>The absolute standard of luxury for VIPs and top management.</p>
      <ul><li>Executive seats with massage</li><li>Perfect sound insulation</li><li>Only 2023-2025 models</li></ul>
      <a href="mailto:info@vt-vip.ru?subject=Book Maybach" class="btn btn-outline" style="text-align: center;">Book Now</a>
    </div>
    <div class="destination-card">
      <h3>Mercedes-Benz V-Class VIP</h3>
      <p>Space and comfort. Ideal for delegations and family trips.</p>
      <ul><li>Chauffeur partition (Full Privacy)</li><li>Apple TV, PS5 & premium sound</li><li>Captain chairs with ottoman</li></ul>
      <a href="mailto:info@vt-vip.ru?subject=Book V-Class" class="btn btn-outline" style="text-align: center;">Book Now</a>
    </div>
    <div class="destination-card">
      <h3>Mercedes-Benz G-Class (Escort)</h3>
      <p>Status and security. Escort in all conditions.</p>
      <ul><li>Armed security (optional)</li><li>Highest security level</li><li>Motorcade escort</li></ul>
      <a href="mailto:info@vt-vip.ru?subject=Book G-Class" class="btn btn-outline" style="text-align: center;">Book Now</a>
    </div>
  </div>
  <a href="https://wa.me/74950000000" class="floating-concierge" target="_blank"><svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.888-.788-1.487-1.761-1.663-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.052 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg><span>Personal Concierge</span></a>
</body>
</html>"""

files['fleet-ar.html'] = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>أسطولنا - VT VIP</title>
  <link rel="icon" type="image/jpeg" href="images/logo.png">
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600&family=Cairo:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
  <style> body { font-family: 'Cairo', sans-serif; } h1, h2, h3, .logo-text { font-family: 'Cormorant Garamond', serif; } h1 { direction: ltr; display: inline-block; } </style>
</head>
<body class="standard-page">
  <div class="grain-overlay"></div>
  <nav class="navbar" id="navbar">
    <a href="ar.html" class="nav-logo">
      <img src="images/logo.png" alt="VT Logo" class="logo-img">
      <span class="logo-text">VT VIP</span>
    </a>
    <div class="nav-links">
      <a href="ar.html">الرئيسية</a>
      <a href="fleet-ar.html" style="color: var(--gold);">أسطولنا</a>
      <a href="destinations-ar.html">الأدلة والكونسيرج</a>
    </div>
    <div class="lang-switcher">
      <a href="fleet.html">RU</a>
      <a href="fleet-en.html">EN</a>
      <a href="fleet-ar.html" class="active">AR</a>
    </div>
  </nav>

  <div class="destinations-hero reveal-3d" style="opacity: 1; transform: none;">
    <h1 class="gradient-text">أسطولنا الفاخر</h1>
    <p>سيارات خالية من العيوب اجتازت مراقبة الجودة الصارمة. تتوفر إصدارات مصفحة ومرافقون مسلحون عند الطلب.</p>
  </div>
  <div class="destinations-grid">
    <div class="destination-card">
      <h3>Mercedes-Benz Maybach S-Class</h3>
      <p>المعيار المطلق للرفاهية لكبار الشخصيات.</p>
      <ul><li>مقاعد تنفيذية مع تدليك</li><li>عزل صوتي مثالي</li><li>موديلات 2023-2025 فقط</li></ul>
      <a href="mailto:info@vt-vip.ru?subject=Book Maybach" class="btn btn-outline" style="text-align: center;">احجز الآن</a>
    </div>
    <div class="destination-card">
      <h3>Mercedes-Benz V-Class VIP</h3>
      <p>مساحة وراحة. مثالية للوفود والرحلات العائلية.</p>
      <ul><li>فاصل للسائق (خصوصية تامة)</li><li>Apple TV, PS5 وصوت فاخر</li><li>مقاعد كابتن مع مسند قدم</li></ul>
      <a href="mailto:info@vt-vip.ru?subject=Book V-Class" class="btn btn-outline" style="text-align: center;">احجز الآن</a>
    </div>
    <div class="destination-card">
      <h3>Mercedes-Benz G-Class (Escort)</h3>
      <p>المكانة والأمن. مرافقة في جميع الظروف.</p>
      <ul><li>حراسة مسلحة (اختياري)</li><li>أعلى مستوى أمان</li><li>مرافقة المواكب</li></ul>
      <a href="mailto:info@vt-vip.ru?subject=Book G-Class" class="btn btn-outline" style="text-align: center;">احجز الآن</a>
    </div>
  </div>
  <a href="https://wa.me/74950000000" class="floating-concierge" target="_blank"><svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.888-.788-1.487-1.761-1.663-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.052 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg><span>Personal Concierge</span></a>
</body>
</html>"""

# Write files securely
for k, v in files.items():
    with open(k, "w", encoding="utf-8") as f:
        f.write(v)
