import os

files = {}

files['index.html'] = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Ð’Ð¸Ð·ÑƒÐ°Ð»Ð¸Ð·Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð½Ñ‹Ð¹ Ð¢Ñ€Ð°Ð½ÑÑ„ÐµÑ€ - VIP Ð¡ÐµÑ€Ð²Ð¸Ñ Ð² Ð Ð¾ÑÑÐ¸Ð¸</title>
  <link rel="icon" type="image/jpeg" href="images/logo_clear.png">
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600&family=Manrope:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <canvas id="gl-canvas"></canvas>
  <div class="grain-overlay"></div>

  <nav class="navbar" id="navbar">
    <a href="#" class="nav-logo">
      <img src="images/logo_clear.png" alt="VT Logo" class="logo-img">
      <span class="logo-text">VT VIP</span>
    </a>
    <div class="nav-links">
      <a href="index.html" style="color: var(--gold);">Ð“Ð»Ð°Ð²Ð½Ð°Ñ</a>
      <a href="fleet.html">ÐÐ²Ñ‚Ð¾Ð¿Ð°Ñ€Ðº</a>
      <a href="destinations.html">ÐŸÑƒÑ‚ÐµÐ²Ð¾Ð´Ð¸Ñ‚ÐµÐ»Ð¸</a>
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
          <img src="images/logo_clear.png" alt="VT Logo" class="hero-logo reveal-3d">
          <h1 class="reveal-3d gradient-text">Ð’Ð¸Ð·ÑƒÐ°Ð»Ð¸Ð·Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð½Ñ‹Ð¹ Ð¢Ñ€Ð°Ð½ÑÑ„ÐµÑ€</h1>
          <p class="hero-subtitle reveal-3d">ÐÐ¾Ð²Ñ‹Ð¹ ÑÑ‚Ð°Ð½Ð´Ð°Ñ€Ñ‚ Ð¿Ñ€ÐµÐ¼Ð¸Ð°Ð»ÑŒÐ½Ð¾Ð³Ð¾ ÑÐµÑ€Ð²Ð¸ÑÐ° Ð² Ð Ð¾ÑÑÐ¸Ð¸. Ð˜ÑÐºÐ»ÑŽÑ‡Ð¸Ñ‚ÐµÐ»ÑŒÐ½Ñ‹Ð¹ ÐºÐ¾Ð¼Ñ„Ð¾Ñ€Ñ‚ Ð´Ð»Ñ Ð²Ð·Ñ‹ÑÐºÐ°Ñ‚ÐµÐ»ÑŒÐ½Ñ‹Ñ… Ð³Ð¾ÑÑ‚ÐµÐ¹.</p>
          <div class="actions reveal-3d">
            <a href="#contacts" class="btn btn-primary">Ð—Ð°Ð±Ñ€Ð¾Ð½Ð¸Ñ€Ð¾Ð²Ð°Ñ‚ÑŒ Ð¿Ð¾ÐµÐ·Ð´ÐºÑƒ</a>
            <a href="#contacts" class="btn btn-outline">B2B ÐŸÐ°Ñ€Ñ‚Ð½ÐµÑ€ÑÑ‚Ð²Ð¾</a>
          </div>
        </div>
      </section>

      <section class="page" data-index="1">
        <div class="content">
          <div class="card reveal-3d">
            <h2 class="gradient-text">Ð˜ÑÐºÑƒÑÑÑ‚Ð²Ð¾ Ð´Ð²Ð¸Ð¶ÐµÐ½Ð¸Ñ</h2>
            <p>ÐœÑ‹ Ð¿Ñ€ÐµÐ´Ð»Ð°Ð³Ð°ÐµÐ¼ Ð¿Ð¾Ð»Ð½Ð¾ÑÑ‚ÑŒÑŽ ÐºÐ¾Ð½Ñ‚Ñ€Ð¾Ð»Ð¸Ñ€ÑƒÐµÐ¼Ñ‹Ð¹ Ð¾Ð¿Ñ‹Ñ‚. Ð’Ð°Ñˆ Ð»Ð¸Ñ‡Ð½Ñ‹Ð¹ Ð²Ð¾Ð´Ð¸Ñ‚ÐµÐ»ÑŒ, Ð±ÐµÐ·ÑƒÐ¿Ñ€ÐµÑ‡Ð½Ñ‹Ð¹ ÑÑ‚Ð¸ÐºÐµÑ‚ Ð¸ ÑÑ‚Ñ€Ð¾Ð³Ð¸Ð¹ Ð´Ñ€ÐµÑÑ-ÐºÐ¾Ð´. ÐÐ²Ñ‚Ð¾Ð¿Ð°Ñ€Ðº Ð¸Ð· Ð¿Ð¾ÑÐ»ÐµÐ´Ð½Ð¸Ñ… Ð¼Ð¾Ð´ÐµÐ»ÐµÐ¹ Mercedes-Benz V-Class, S-Class Ð¸ Maybach.</p>
          </div>
        </div>
      </section>

      <section class="page" data-index="2">
        <div class="content">
          <div class="card reveal-3d">
            <h2 class="gradient-text">ÐœÐ¾ÑÐºÐ²Ð°</h2>
            <p>Ð¡Ñ‚Ð¾Ð»Ð¸Ñ†Ð° Ñ€Ð¾ÑÐºÐ¾ÑˆÐ¸ Ð¸ Ñ€Ð¸Ñ‚Ð¼Ð°. ÐžÑ‚ Ñ‚Ñ€Ð°Ð½ÑÑ„ÐµÑ€Ð¾Ð² Ð¸Ð· Ð’Ð½ÑƒÐºÐ¾Ð²Ð¾-3 Ð´Ð¾ Ð´ÐµÐ»Ð¾Ð²Ñ‹Ñ… Ð²ÑÑ‚Ñ€ÐµÑ‡ Ð² ÐœÐ¾ÑÐºÐ²Ð°-Ð¡Ð¸Ñ‚Ð¸ Ð¸ ÑˆÐ¾Ð¿Ð¸Ð½Ð³Ð° Ð² Ð¦Ð£Ðœ Ñ Ð¿ÐµÑ€ÑÐ¾Ð½Ð°Ð»ÑŒÐ½Ñ‹Ð¼ ÑÐ¾Ð¿Ñ€Ð¾Ð²Ð¾Ð¶Ð´ÐµÐ½Ð¸ÐµÐ¼.</p>
          </div>
        </div>
      </section>

      <section class="page" data-index="3">
        <div class="content">
          <div class="card reveal-3d">
            <h2 class="gradient-text">Ð¡Ð°Ð½ÐºÑ‚-ÐŸÐµÑ‚ÐµÑ€Ð±ÑƒÑ€Ð³</h2>
            <p>ÐŸÐ¾Ð³Ñ€ÑƒÐ·Ð¸Ñ‚ÐµÑÑŒ Ð² Ð°Ñ‚Ð¼Ð¾ÑÑ„ÐµÑ€Ñƒ Ð¸Ð¼Ð¿ÐµÑ€ÑÐºÐ¾Ð¹ ÑÑ‚Ð¾Ð»Ð¸Ñ†Ñ‹. Ð¢Ñ€Ð°Ð½ÑÑ„ÐµÑ€Ñ‹ Ð¸Ð· ÐŸÑƒÐ»ÐºÐ¾Ð²Ð¾, Ð¿Ð¾ÐµÐ·Ð´ÐºÐ¸ Ð¿Ð¾ Ð¸ÑÑ‚Ð¾Ñ€Ð¸Ñ‡ÐµÑÐºÐ¾Ð¼Ñƒ Ñ†ÐµÐ½Ñ‚Ñ€Ñƒ Ð¸ Ð·Ð°Ð³Ð¾Ñ€Ð¾Ð´Ð½Ñ‹Ð¼ Ñ€ÐµÐ·Ð¸Ð´ÐµÐ½Ñ†Ð¸ÑÐ¼ Ð² Ð°Ñ‚Ð¼Ð¾ÑÑ„ÐµÑ€Ðµ Ð°Ð±ÑÐ¾Ð»ÑŽÑ‚Ð½Ð¾Ð¹ Ð¿Ñ€Ð¸Ð²Ð°Ñ‚Ð½Ð¾ÑÑ‚Ð¸.</p>
          </div>
        </div>
      </section>

      <section class="page" data-index="4">
        <div class="content">
          <div class="card reveal-3d">
            <h2 class="gradient-text">Ð¡Ð¾Ñ‡Ð¸ Ð¸ ÐšÑ€Ð°ÑÐ½Ð°Ñ ÐŸÐ¾Ð»ÑÐ½Ð°</h2>
            <p>ÐŸÐ°Ð½Ð¾Ñ€Ð°Ð¼Ð½Ñ‹Ðµ Ð¿Ð¾ÐµÐ·Ð´ÐºÐ¸ Ð²Ð´Ð¾Ð»ÑŒ Ð§ÐµÑ€Ð½Ð¾Ð³Ð¾ Ð¼Ð¾Ñ€Ñ Ð¸ ÑÐµÑ€Ð¿Ð°Ð½Ñ‚Ð¸Ð½Ð°Ð¼ ÐšÐ°Ð²ÐºÐ°Ð·ÑÐºÐ¸Ñ… Ð³Ð¾Ñ€. ÐÐ²Ñ‚Ð¾Ð¼Ð¾Ð±Ð¸Ð»Ð¸ Ð¿Ð¾Ð´Ð³Ð¾Ñ‚Ð¾Ð²Ð»ÐµÐ½Ñ‹ Ðº Ð»ÑŽÐ±Ñ‹Ð¼ ÑƒÑÐ»Ð¾Ð²Ð¸ÑÐ¼ Ð´Ð»Ñ Ð²Ð°ÑˆÐµÐ³Ð¾ ÐºÐ¾Ð¼Ñ„Ð¾Ñ€Ñ‚Ð°.</p>
          </div>
        </div>
      </section>

      <section class="page" data-index="5">
        <div class="content">
          <div class="card reveal-3d">
            <h2 class="gradient-text">ÐšÐ°Ð·Ð°Ð½ÑŒ</h2>
            <p>Ð–ÐµÐ¼Ñ‡ÑƒÐ¶Ð¸Ð½Ð° Ð¢Ð°Ñ‚Ð°Ñ€ÑÑ‚Ð°Ð½Ð° Ñ Ð±Ð¾Ð³Ð°Ñ‚Ñ‹Ð¼ Ð½Ð°ÑÐ»ÐµÐ´Ð¸ÐµÐ¼. Ð˜Ð´ÐµÐ°Ð»ÑŒÐ½Ñ‹Ðµ Ð¼Ð°Ñ€ÑˆÑ€ÑƒÑ‚Ñ‹ Ðº ÐšÐ°Ð·Ð°Ð½ÑÐºÐ¾Ð¼Ñƒ ÐšÑ€ÐµÐ¼Ð»ÑŽ Ð¸ Ð»ÑƒÑ‡ÑˆÐ¸Ð¼ Ñ…Ð°Ð»ÑÐ»ÑŒ-Ñ€ÐµÑÑ‚Ð¾Ñ€Ð°Ð½Ð°Ð¼ Ð³Ð¾Ñ€Ð¾Ð´Ð°.</p>
          </div>
        </div>
      </section>

      <section class="page" data-index="6">
        <div class="content">
          <div class="card reveal-3d">
            <h2 class="gradient-text">Ð’Ð½Ð¸Ð¼Ð°Ð½Ð¸Ðµ Ðº ÐºÐ°Ð¶Ð´Ð¾Ð¹ Ð´ÐµÑ‚Ð°Ð»Ð¸</h2>
            <p>ÐœÑ‹ Ð¿Ñ€ÐµÐ´Ð²Ð¾ÑÑ…Ð¸Ñ‰Ð°ÐµÐ¼ Ð²Ð°ÑˆÐ¸ Ð¶ÐµÐ»Ð°Ð½Ð¸Ñ. Ð¥Ð°Ð»ÑÐ»ÑŒ-ÑÐ¾Ð¿Ñ€Ð¾Ð²Ð¾Ð¶Ð´ÐµÐ½Ð¸Ðµ, Ð¿Ñ€ÐµÐ¼Ð¸Ð°Ð»ÑŒÐ½Ð°Ñ Ð²Ð¾Ð´Ð°, Ð²Ñ‹ÑÐ¾ÐºÐ¾ÑÐºÐ¾Ñ€Ð¾ÑÑ‚Ð½Ð¾Ð¹ Wi-Fi. ÐŸÐ¾Ð»Ð½Ð°Ñ ÐºÐ¾Ð½Ñ„Ð¸Ð´ÐµÐ½Ñ†Ð¸Ð°Ð»ÑŒÐ½Ð¾ÑÑ‚ÑŒ Ð¼Ð°Ñ€ÑˆÑ€ÑƒÑ‚Ð¾Ð² (NDA) Ð¸ Ð°Ð½Ð¾Ð½Ð¸Ð¼Ð½Ð°Ñ Ð¾Ð¿Ð»Ð°Ñ‚Ð° Ð² ÐºÑ€Ð¸Ð¿Ñ‚Ð¾Ð²Ð°Ð»ÑŽÑ‚Ðµ (USDT/BTC).</p>
          </div>
        </div>
      </section>

      <section class="page" data-index="7" id="contacts">
        <div class="content">
          <div class="card reveal-3d">
            <h2>Ð“Ð»Ð¾Ð±Ð°Ð»ÑŒÐ½Ð¾Ðµ Ð¿Ð°Ñ€Ñ‚Ð½ÐµÑ€ÑÑ‚Ð²Ð¾</h2>
            <p>ÐŸÑ€ÑÐ¼Ð°Ñ Ð¸Ð½Ñ‚ÐµÐ³Ñ€Ð°Ñ†Ð¸Ñ Ñ Ñ‚ÑƒÑ€Ð¸ÑÑ‚Ð¸Ñ‡ÐµÑÐºÐ¸Ð¼Ð¸ ÐºÐ¾Ð¼Ð¿Ð°Ð½Ð¸ÑÐ¼Ð¸ ÐžÐÐ­. ÐœÑ‹ Ð¿Ñ€ÐµÐ´Ð»Ð°Ð³Ð°ÐµÐ¼ ÑÐºÑÐºÐ»ÑŽÐ·Ð¸Ð²Ð½Ñ‹Ðµ B2B ÑƒÑÐ»Ð¾Ð²Ð¸Ñ (Agency Commission) Ð´Ð»Ñ Ð°Ð³ÐµÐ½Ñ‚Ð¾Ð² Ð”ÑƒÐ±Ð°Ñ Ð¸ ÑÑ‚Ñ€Ð°Ð½ Ð—Ð°Ð»Ð¸Ð²Ð°.</p>
            <p class="contact-info">Email: info@vt-vip.ru<br>Ð¢ÐµÐ»ÐµÑ„Ð¾Ð½ / WhatsApp: +7 495 000 00 00</p>
            <a href="mailto:info@vt-vip.ru" class="btn btn-primary">Ð¡Ð²ÑÐ·Ð°Ñ‚ÑŒÑÑ Ñ Ð½Ð°Ð¼Ð¸</a>
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
  <script src="app.js"></script>
</body>
</html>"""

files['en.html'] = files['index.html'].replace('lang="ru"', 'lang="en"').replace('Ð’Ð¸Ð·ÑƒÐ°Ð»Ð¸Ð·Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð½Ñ‹Ð¹ Ð¢Ñ€Ð°Ð½ÑÑ„ÐµÑ€ - VIP Ð¡ÐµÑ€Ð²Ð¸Ñ Ð² Ð Ð¾ÑÑÐ¸Ð¸', 'Visualized Transfer Vip - Premium Transfer in Russia').replace('Ð“Ð»Ð°Ð²Ð½Ð°Ñ', 'Home').replace('ÐÐ²Ñ‚Ð¾Ð¿Ð°Ñ€Ðº', 'Our Fleet').replace('ÐŸÑƒÑ‚ÐµÐ²Ð¾Ð´Ð¸Ñ‚ÐµÐ»Ð¸', 'Tripwires & Concierge').replace('class="active">RU', '>RU').replace('>EN', 'class="active">EN').replace('ÐÐ¾Ð²Ñ‹Ð¹ ÑÑ‚Ð°Ð½Ð´Ð°Ñ€Ñ‚ Ð¿Ñ€ÐµÐ¼Ð¸Ð°Ð»ÑŒÐ½Ð¾Ð³Ð¾ ÑÐµÑ€Ð²Ð¸ÑÐ° Ð² Ð Ð¾ÑÑÐ¸Ð¸. Ð˜ÑÐºÐ»ÑŽÑ‡Ð¸Ñ‚ÐµÐ»ÑŒÐ½Ñ‹Ð¹ ÐºÐ¾Ð¼Ñ„Ð¾Ñ€Ñ‚ Ð´Ð»Ñ Ð²Ð·Ñ‹ÑÐºÐ°Ñ‚ÐµÐ»ÑŒÐ½Ñ‹Ñ… Ð³Ð¾ÑÑ‚ÐµÐ¹.', 'A new standard of premium service in Russia. Exceptional comfort for discerning guests.').replace('Ð—Ð°Ð±Ñ€Ð¾Ð½Ð¸Ñ€Ð¾Ð²Ð°Ñ‚ÑŒ Ð¿Ð¾ÐµÐ·Ð´ÐºÑƒ', 'Book a Ride').replace('B2B ÐŸÐ°Ñ€Ñ‚Ð½ÐµÑ€ÑÑ‚Ð²Ð¾', 'B2B Partnership').replace('Ð˜ÑÐºÑƒÑÑÑ‚Ð²Ð¾ Ð´Ð²Ð¸Ð¶ÐµÐ½Ð¸Ñ', 'The Art of Movement').replace('ÐœÑ‹ Ð¿Ñ€ÐµÐ´Ð»Ð°Ð³Ð°ÐµÐ¼ Ð¿Ð¾Ð»Ð½Ð¾ÑÑ‚ÑŒÑŽ ÐºÐ¾Ð½Ñ‚Ñ€Ð¾Ð»Ð¸Ñ€ÑƒÐµÐ¼Ñ‹Ð¹ Ð¾Ð¿Ñ‹Ñ‚. Ð’Ð°Ñˆ Ð»Ð¸Ñ‡Ð½Ñ‹Ð¹ Ð²Ð¾Ð´Ð¸Ñ‚ÐµÐ»ÑŒ, Ð±ÐµÐ·ÑƒÐ¿Ñ€ÐµÑ‡Ð½Ñ‹Ð¹ ÑÑ‚Ð¸ÐºÐµÑ‚ Ð¸ ÑÑ‚Ñ€Ð¾Ð³Ð¸Ð¹ Ð´Ñ€ÐµÑÑ-ÐºÐ¾Ð´. ÐÐ²Ñ‚Ð¾Ð¿Ð°Ñ€Ðº Ð¸Ð· Ð¿Ð¾ÑÐ»ÐµÐ´Ð½Ð¸Ñ… Ð¼Ð¾Ð´ÐµÐ»ÐµÐ¹ Mercedes-Benz V-Class, S-Class Ð¸ Maybach.', 'We offer a fully controlled, high-end experience. Your personal chauffeur, impeccable etiquette, and strict dress code. Our fleet features only the latest Mercedes-Benz models.').replace('ÐœÐ¾ÑÐºÐ²Ð°', 'Moscow').replace('Ð¡Ñ‚Ð¾Ð»Ð¸Ñ†Ð° Ñ€Ð¾ÑÐºÐ¾ÑˆÐ¸ Ð¸ Ñ€Ð¸Ñ‚Ð¼Ð°. ÐžÑ‚ Ñ‚Ñ€Ð°Ð½ÑÑ„ÐµÑ€Ð¾Ð² Ð¸Ð· Ð’Ð½ÑƒÐºÐ¾Ð²Ð¾-3 Ð´Ð¾ Ð´ÐµÐ»Ð¾Ð²Ñ‹Ñ… Ð²ÑÑ‚Ñ€ÐµÑ‡ Ð² ÐœÐ¾ÑÐºÐ²Ð°-Ð¡Ð¸Ñ‚Ð¸ Ð¸ ÑˆÐ¾Ð¿Ð¸Ð½Ð³Ð° Ð² Ð¦Ð£Ðœ Ñ Ð¿ÐµÑ€ÑÐ¾Ð½Ð°Ð»ÑŒÐ½Ñ‹Ð¼ ÑÐ¾Ð¿Ñ€Ð¾Ð²Ð¾Ð¶Ð´ÐµÐ½Ð¸ÐµÐ¼.', 'The capital of luxury and rhythm. Ideal for business meetings and premium shopping with personal escorts.').replace('Ð¡Ð°Ð½ÐºÑ‚-ÐŸÐµÑ‚ÐµÑ€Ð±ÑƒÑ€Ð³', 'Saint Petersburg').replace('ÐŸÐ¾Ð³Ñ€ÑƒÐ·Ð¸Ñ‚ÐµÑÑŒ Ð² Ð°Ñ‚Ð¼Ð¾ÑÑ„ÐµÑ€Ñƒ Ð¸Ð¼Ð¿ÐµÑ€ÑÐºÐ¾Ð¹ ÑÑ‚Ð¾Ð»Ð¸Ñ†Ñ‹. Ð¢Ñ€Ð°Ð½ÑÑ„ÐµÑ€Ñ‹ Ð¸Ð· ÐŸÑƒÐ»ÐºÐ¾Ð²Ð¾, Ð¿Ð¾ÐµÐ·Ð´ÐºÐ¸ Ð¿Ð¾ Ð¸ÑÑ‚Ð¾Ñ€Ð¸Ñ‡ÐµÑÐºÐ¾Ð¼Ñƒ Ñ†ÐµÐ½Ñ‚Ñ€Ñƒ Ð¸ Ð·Ð°Ð³Ð¾Ñ€Ð¾Ð´Ð½Ñ‹Ð¼ Ñ€ÐµÐ·Ð¸Ð´ÐµÐ½Ñ†Ð¸ÑÐ¼ Ð² Ð°Ñ‚Ð¼Ð¾ÑÑ„ÐµÑ€Ðµ Ð°Ð±ÑÐ¾Ð»ÑŽÑ‚Ð½Ð¾Ð¹ Ð¿Ñ€Ð¸Ð²Ð°Ñ‚Ð½Ð¾ÑÑ‚Ð¸.', 'Immerse yourself in the atmosphere of the imperial capital. Pulkovo airport transfers and journeys through the historic center in absolute privacy.').replace('Ð¡Ð¾Ñ‡Ð¸ Ð¸ ÐšÑ€Ð°ÑÐ½Ð°Ñ ÐŸÐ¾Ð»ÑÐ½Ð°', 'Sochi & Krasnaya Polyana').replace('ÐŸÐ°Ð½Ð¾Ñ€Ð°Ð¼Ð½Ñ‹Ðµ Ð¿Ð¾ÐµÐ·Ð´ÐºÐ¸ Ð²Ð´Ð¾Ð»ÑŒ Ð§ÐµÑ€Ð½Ð¾Ð³Ð¾ Ð¼Ð¾Ñ€Ñ Ð¸ ÑÐµÑ€Ð¿Ð°Ð½Ñ‚Ð¸Ð½Ð°Ð¼ ÐšÐ°Ð²ÐºÐ°Ð·ÑÐºÐ¸Ñ… Ð³Ð¾Ñ€. ÐÐ²Ñ‚Ð¾Ð¼Ð¾Ð±Ð¸Ð»Ð¸ Ð¿Ð¾Ð´Ð³Ð¾Ñ‚Ð¾Ð²Ð»ÐµÐ½Ñ‹ Ðº Ð»ÑŽÐ±Ñ‹Ð¼ ÑƒÑÐ»Ð¾Ð²Ð¸ÑÐ¼ Ð´Ð»Ñ Ð²Ð°ÑˆÐµÐ³Ð¾ ÐºÐ¾Ð¼Ñ„Ð¾Ñ€Ñ‚Ð°.', 'Panoramic drives along the Black Sea coast and the winding roads of the Caucasus Mountains.').replace('ÐšÐ°Ð·Ð°Ð½ÑŒ', 'Kazan').replace('Ð–ÐµÐ¼Ñ‡ÑƒÐ¶Ð¸Ð½Ð° Ð¢Ð°Ñ‚Ð°Ñ€ÑÑ‚Ð°Ð½Ð° Ñ Ð±Ð¾Ð³Ð°Ñ‚Ñ‹Ð¼ Ð½Ð°ÑÐ»ÐµÐ´Ð¸ÐµÐ¼. Ð˜Ð´ÐµÐ°Ð»ÑŒÐ½Ñ‹Ðµ Ð¼Ð°Ñ€ÑˆÑ€ÑƒÑ‚Ñ‹ Ðº ÐšÐ°Ð·Ð°Ð½ÑÐºÐ¾Ð¼Ñƒ ÐšÑ€ÐµÐ¼Ð»ÑŽ Ð¸ Ð»ÑƒÑ‡ÑˆÐ¸Ð¼ Ñ…Ð°Ð»ÑÐ»ÑŒ-Ñ€ÐµÑÑ‚Ð¾Ñ€Ð°Ð½Ð°Ð¼ Ð³Ð¾Ñ€Ð¾Ð´Ð°.', 'The pearl of Tatarstan. Ideal routes to the Kazan Kremlin and the best Halal restaurants in the city.').replace('Ð’Ð½Ð¸Ð¼Ð°Ð½Ð¸Ðµ Ðº ÐºÐ°Ð¶Ð´Ð¾Ð¹ Ð´ÐµÑ‚Ð°Ð»Ð¸', 'Attention to Every Detail').replace('ÐœÑ‹ Ð¿Ñ€ÐµÐ´Ð²Ð¾ÑÑ…Ð¸Ñ‰Ð°ÐµÐ¼ Ð²Ð°ÑˆÐ¸ Ð¶ÐµÐ»Ð°Ð½Ð¸Ñ. Ð¥Ð°Ð»ÑÐ»ÑŒ-ÑÐ¾Ð¿Ñ€Ð¾Ð²Ð¾Ð¶Ð´ÐµÐ½Ð¸Ðµ, Ð¿Ñ€ÐµÐ¼Ð¸Ð°Ð»ÑŒÐ½Ð°Ñ Ð²Ð¾Ð´Ð°, Ð²Ñ‹ÑÐ¾ÐºÐ¾ÑÐºÐ¾Ñ€Ð¾ÑÑ‚Ð½Ð¾Ð¹ Wi-Fi. ÐŸÐ¾Ð»Ð½Ð°Ñ ÐºÐ¾Ð½Ñ„Ð¸Ð´ÐµÐ½Ñ†Ð¸Ð°Ð»ÑŒÐ½Ð¾ÑÑ‚ÑŒ Ð¼Ð°Ñ€ÑˆÑ€ÑƒÑ‚Ð¾Ð² (NDA) Ð¸ Ð°Ð½Ð¾Ð½Ð¸Ð¼Ð½Ð°Ñ Ð¾Ð¿Ð»Ð°Ñ‚Ð° Ð² ÐºÑ€Ð¸Ð¿Ñ‚Ð¾Ð²Ð°Ð»ÑŽÑ‚Ðµ (USDT/BTC).', 'We anticipate your desires. Halal-compliant service, complete confidentiality of your routes (NDA) and anonymous crypto payments (USDT/BTC).').replace('Ð“Ð»Ð¾Ð±Ð°Ð»ÑŒÐ½Ð¾Ðµ Ð¿Ð°Ñ€Ñ‚Ð½ÐµÑ€ÑÑ‚Ð²Ð¾', 'Global Partnership').replace('ÐŸÑ€ÑÐ¼Ð°Ñ Ð¸Ð½Ñ‚ÐµÐ³Ñ€Ð°Ñ†Ð¸Ñ Ñ Ñ‚ÑƒÑ€Ð¸ÑÑ‚Ð¸Ñ‡ÐµÑÐºÐ¸Ð¼Ð¸ ÐºÐ¾Ð¼Ð¿Ð°Ð½Ð¸ÑÐ¼Ð¸ ÐžÐÐ­. ÐœÑ‹ Ð¿Ñ€ÐµÐ´Ð»Ð°Ð³Ð°ÐµÐ¼ ÑÐºÑÐºÐ»ÑŽÐ·Ð¸Ð²Ð½Ñ‹Ðµ B2B ÑƒÑÐ»Ð¾Ð²Ð¸Ñ (Agency Commission) Ð´Ð»Ñ Ð°Ð³ÐµÐ½Ñ‚Ð¾Ð² Ð”ÑƒÐ±Ð°Ñ Ð¸ ÑÑ‚Ñ€Ð°Ð½ Ð—Ð°Ð»Ð¸Ð²Ð°.', 'Direct integration with UAE travel companies. We offer exclusive B2B terms for travel agents in Dubai and the Gulf countries.').replace('Ð¡Ð²ÑÐ·Ð°Ñ‚ÑŒÑÑ Ñ Ð½Ð°Ð¼Ð¸', 'Contact Us').replace('Ð’Ð¸Ð·ÑƒÐ°Ð»Ð¸Ð·Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð½Ñ‹Ð¹ Ð¢Ñ€Ð°Ð½ÑÑ„ÐµÑ€', 'Visualized Transfer Vip')

files['ar.html'] = files['en.html'].replace('lang="en"', 'lang="ar" dir="rtl"').replace('<head>', "<head>\n  <style> body { font-family: 'Cairo', sans-serif; } h1, h2, .logo-text { font-family: 'Cormorant Garamond', serif; } h1 { direction: ltr; display: inline-block; } </style>").replace('Home', 'Ø§Ù„Ø±Ø¦ÙŠØ³ÙŠØ©').replace('Our Fleet', 'Ø£Ø³Ø·ÙˆÙ„Ù†Ø§').replace('Tripwires & Concierge', 'Ø§Ù„Ø£Ø¯Ù„Ø© ÙˆØ§Ù„ÙƒÙˆÙ†Ø³ÙŠØ±Ø¬').replace('A new standard of premium service in Russia. Exceptional comfort for discerning guests.', 'Ù…Ø¹ÙŠØ§Ø± Ø¬Ø¯ÙŠØ¯ Ù„Ù„Ø®Ø¯Ù…Ø© Ø§Ù„Ù…ØªÙ…ÙŠØ²Ø© ÙÙŠ Ø±ÙˆØ³ÙŠØ§. Ø±Ø§Ø­Ø© Ø§Ø³ØªØ«Ù†Ø§Ø¦ÙŠØ© Ù„Ø¶ÙŠÙˆÙÙ†Ø§ Ø§Ù„Ù…Ù…ÙŠØ²ÙŠÙ†.').replace('Book a Ride', 'Ø§Ø­Ø¬Ø² Ø±Ø­Ù„Ø©').replace('B2B Partnership', 'Ø´Ø±Ø§ÙƒØ© B2B').replace('The Art of Movement', 'ÙÙ† Ø§Ù„ØªÙ†Ù‚Ù„').replace('We offer a fully controlled, high-end experience. Your personal chauffeur, impeccable etiquette, and strict dress code. Our fleet features only the latest Mercedes-Benz models.', 'Ù†Ø­Ù† Ù†Ù‚Ø¯Ù… ØªØ¬Ø±Ø¨Ø© ÙØ§Ø®Ø±Ø© Ø®Ø§Ø¶Ø¹Ø© Ù„Ù„Ø±Ù‚Ø§Ø¨Ø© Ø§Ù„ÙƒØ§Ù…Ù„Ø©. Ø³Ø§Ø¦Ù‚Ùƒ Ø§Ù„Ø´Ø®ØµÙŠØŒ Ø¢Ø¯Ø§Ø¨ Ù„Ø§ ØªØ´ÙˆØ¨Ù‡Ø§ Ø´Ø§Ø¦Ø¨Ø©ØŒ ÙˆÙ‚ÙˆØ§Ø¹Ø¯ Ù„Ø¨Ø§Ø³ ØµØ§Ø±Ù…Ø©.').replace('Moscow', 'Ù…ÙˆØ³ÙƒÙˆ').replace('The capital of luxury and rhythm. Ideal for business meetings and premium shopping with personal escorts.', 'Ø¹Ø§ØµÙ…Ø© Ø§Ù„ÙØ®Ø§Ù…Ø©. Ù…Ø«Ø§Ù„ÙŠØ© Ù„Ø§Ø¬ØªÙ…Ø§Ø¹Ø§Øª Ø§Ù„Ø£Ø¹Ù…Ø§Ù„ ÙˆØ§Ù„ØªØ³ÙˆÙ‚ Ø§Ù„Ø±Ø§Ù‚ÙŠ.').replace('Saint Petersburg', 'Ø³Ø§Ù†Øª Ø¨Ø·Ø±Ø³Ø¨Ø±Øº').replace('Immerse yourself in the atmosphere of the imperial capital. Pulkovo airport transfers and journeys through the historic center in absolute privacy.', 'Ø§Ù†ØºÙ…Ø³ ÙÙŠ Ø£Ø¬ÙˆØ§Ø¡ Ø§Ù„Ø¹Ø§ØµÙ…Ø© Ø§Ù„Ø¥Ù…Ø¨Ø±Ø§Ø·ÙˆØ±ÙŠØ© ÙÙŠ Ø®ØµÙˆØµÙŠØ© ØªØ§Ù…Ø©.').replace('Sochi & Krasnaya Polyana', 'Ø³ÙˆØªØ´ÙŠ ÙˆÙƒØ±Ø§Ø³Ù†ÙŠØ§ Ø¨ÙˆÙ„ÙŠØ§Ù†Ø§').replace('Panoramic drives along the Black Sea coast and the winding roads of the Caucasus Mountains.', 'Ø±Ø­Ù„Ø§Øª Ø¨Ø§Ù†ÙˆØ±Ø§Ù…ÙŠØ© Ø¹Ù„Ù‰ Ø·ÙˆÙ„ Ø³Ø§Ø­Ù„ Ø§Ù„Ø¨Ø­Ø± Ø§Ù„Ø£Ø³ÙˆØ¯.').replace('Kazan', 'Ù‚Ø§Ø²Ø§Ù† (ÙƒØ§Ø²Ø§Ù†)').replace('The pearl of Tatarstan. Ideal routes to the Kazan Kremlin and the best Halal restaurants in the city.', 'Ù„Ø¤Ù„Ø¤Ø© ØªØªØ§Ø±Ø³ØªØ§Ù†. Ù…Ø³Ø§Ø±Ø§Øª Ù…Ø«Ø§Ù„ÙŠØ© Ø¥Ù„Ù‰ ÙƒØ±Ù…Ù„ÙŠÙ† Ù‚Ø§Ø²Ø§Ù† ÙˆØ£ÙØ¶Ù„ Ø§Ù„Ù…Ø·Ø§Ø¹Ù… Ø§Ù„Ø­Ù„Ø§Ù„.').replace('Attention to Every Detail', 'Ø§Ù„Ø§Ù‡ØªÙ…Ø§Ù… Ø¨ÙƒÙ„ Ø§Ù„ØªÙØ§ØµÙŠÙ„').replace('We anticipate your desires. Halal-compliant service, complete confidentiality of your routes (NDA) and anonymous crypto payments (USDT/BTC).', 'Ù†Ø­Ù† Ù†ØªÙˆÙ‚Ø¹ Ø±ØºØ¨Ø§ØªÙƒ. Ø®Ø¯Ù…Ø© Ø­Ù„Ø§Ù„ ÙˆØ³Ø±ÙŠØ© ØªØ§Ù…Ø© Ù„Ù…Ø³Ø§Ø±Ø§ØªÙƒ ÙˆØ¯ÙØ¹ Ø¨Ø§Ù„Ø¹Ù…Ù„Ø§Øª Ø§Ù„Ù…Ø´ÙØ±Ø©.').replace('Global Partnership', 'Ø´Ø±Ø§ÙƒØ© Ø¹Ø§Ù„Ù…ÙŠØ©').replace('Direct integration with UAE travel companies. We offer exclusive B2B terms for travel agents in Dubai and the Gulf countries.', 'ØªÙƒØ§Ù…Ù„ Ù…Ø¨Ø§Ø´Ø± Ù…Ø¹ Ø´Ø±ÙƒØ§Øª Ø§Ù„Ø³ÙØ± ÙÙŠ Ø§Ù„Ø¥Ù…Ø§Ø±Ø§Øª. Ù†Ù‚Ø¯Ù… Ø´Ø±ÙˆØ· B2B Ø­ØµØ±ÙŠØ©.').replace('Contact Us', 'Ø§ØªØµÙ„ Ø¨Ù†Ø§').replace('class="active">EN', '>EN').replace('>AR', 'class="active">AR')

for k, v in files.items():
    with open(k, "w", encoding="utf-8") as f:
        f.write(v)

