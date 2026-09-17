import os

files = {}

files['destinations.html'] = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ÐÐ°Ð¿Ñ€Ð°Ð²Ð»ÐµÐ½Ð¸Ñ Ð¸ ÐŸÑƒÑ‚ÐµÐ²Ð¾Ð´Ð¸Ñ‚ÐµÐ»Ð¸ - VT VIP</title>
  <link rel="icon" type="image/jpeg" href="images/logo_clear.png">
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600&family=Manrope:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body class="standard-page">
  <div class="grain-overlay"></div>
  <nav class="navbar" id="navbar">
    <a href="index.html" class="nav-logo">
      <img src="images/logo_clear.png" alt="VT Logo" class="logo-img"><span class="logo-text">VT VIP</span>
    </a>
    <div class="nav-links">
      <a href="index.html">Ð“Ð»Ð°Ð²Ð½Ð°Ñ</a>
      <a href="fleet.html">ÐÐ²Ñ‚Ð¾Ð¿Ð°Ñ€Ðº</a>
      <a href="destinations.html" style="color: var(--gold);">ÐŸÑƒÑ‚ÐµÐ²Ð¾Ð´Ð¸Ñ‚ÐµÐ»Ð¸</a>
    </div>
    <div class="lang-switcher">
      <a href="destinations.html" class="active">RU</a>
      <a href="destinations-en.html">EN</a>
      <a href="destinations-ar.html">AR</a>
    </div>
  </nav>

  <div class="destinations-hero reveal-3d" style="opacity: 1; transform: none;">
    <h1 class="gradient-text">ÐŸÑƒÑ‚ÐµÐ²Ð¾Ð´Ð¸Ñ‚ÐµÐ»Ð¸ Ð¸ Ð­ÐºÑÐºÐ»ÑŽÐ·Ð¸Ð²</h1>
    <p>Ð”Ð¾Ð±Ð°Ð²ÑŒÑ‚Ðµ Ð°Ð²Ñ‚Ð¾Ñ€ÑÐºÐ¸Ð¹ Ð¿ÑƒÑ‚ÐµÐ²Ð¾Ð´Ð¸Ñ‚ÐµÐ»ÑŒ Ðº Ð²Ð°ÑˆÐµÐ¼Ñƒ VIP-Ñ‚Ñ€Ð°Ð½ÑÑ„ÐµÑ€Ñƒ. ÐœÑ‹ ÑÐ¾Ð±Ñ€Ð°Ð»Ð¸ ÑÐ°Ð¼Ñ‹Ðµ Ð·Ð°ÐºÑ€Ñ‹Ñ‚Ñ‹Ðµ Ð»Ð¾ÐºÐ°Ñ†Ð¸Ð¸, Ð»ÑƒÑ‡ÑˆÐ¸Ðµ Ñ€ÐµÑÑ‚Ð¾Ñ€Ð°Ð½Ñ‹ Ð¸ Ð¿Ñ€ÐµÐ¼Ð¸Ð°Ð»ÑŒÐ½Ñ‹Ðµ Ð°ÐºÑ‚Ð¸Ð²Ð½Ð¾ÑÑ‚Ð¸.</p>
  </div>

  <div class="destinations-grid">
    <div class="destination-card" style="cursor: pointer;" onclick="window.location.href='tripwire-moscow.html'">
      <h3><a href="tripwire-moscow.html" style="color: var(--gold); text-decoration: none;">ÐœÐ¾ÑÐºÐ²Ð°</a></h3>
      <p>Ð¡Ñ‚Ð¾Ð»Ð¸Ñ†Ð° Ñ€Ð¾ÑÐºÐ¾ÑˆÐ¸ Ð¸ Ñ€Ð¸Ñ‚Ð¼Ð°. Ð˜Ð´ÐµÐ°Ð»ÑŒÐ½Ð¾ Ð´Ð»Ñ Ð±Ð¸Ð·Ð½ÐµÑÐ° Ð¸ Ð¿Ñ€ÐµÐ¼Ð¸Ð°Ð»ÑŒÐ½Ð¾Ð³Ð¾ ÑˆÐ¾Ð¿Ð¸Ð½Ð³Ð°.</p>
      <ul><li>Ð—Ð°ÐºÑ€Ñ‹Ñ‚Ñ‹Ðµ VIP-ÐºÐ¾Ð¼Ð½Ð°Ñ‚Ñ‹ Ð¦Ð£Ðœ Ð¸ Ð“Ð£Ðœ</li><li>Ð ÐµÑÑ‚Ð¾Ñ€Ð°Ð½Ñ‹ Ñ Ñ…Ð°Ð»ÑÐ»ÑŒ-Ð¼ÐµÐ½ÑŽ (ÐœÐ¾ÑÐºÐ²Ð°-Ð¡Ð¸Ñ‚Ð¸)</li><li>ÐžÑ…Ñ€Ð°Ð½ÑÐµÐ¼Ñ‹Ðµ Ð¼Ð°Ñ€ÑˆÑ€ÑƒÑ‚Ñ‹</li></ul>
      <div class="price-tag">ÐžÑ‚ $49</div>
      <a href="tripwire-moscow.html" class="btn btn-outline" style="text-align: center;">ÐŸÐ¾Ð´Ñ€Ð¾Ð±Ð½ÐµÐµ Ð¾ Ð¿ÑƒÑ‚ÐµÐ²Ð¾Ð´Ð¸Ñ‚ÐµÐ»Ðµ</a>
    </div>
    <div class="destination-card" style="cursor: pointer;" onclick="window.location.href='tripwire-spb.html'">
      <h3><a href="tripwire-spb.html" style="color: var(--gold); text-decoration: none;">Ð¡Ð°Ð½ÐºÑ‚-ÐŸÐµÑ‚ÐµÑ€Ð±ÑƒÑ€Ð³</a></h3>
      <p>Ð˜Ð¼Ð¿ÐµÑ€ÑÐºÐ°Ñ ÑÑÑ‚ÐµÑ‚Ð¸ÐºÐ° Ð¸ Ð±ÐµÐ»Ñ‹Ðµ Ð½Ð¾Ñ‡Ð¸. Ð¡ÐµÐ²ÐµÑ€Ð½Ð°Ñ ÑÑ‚Ð¾Ð»Ð¸Ñ†Ð° Ð Ð¾ÑÑÐ¸Ð¸.</p>
      <ul><li>Ð˜Ð½Ð´Ð¸Ð²Ð¸Ð´ÑƒÐ°Ð»ÑŒÐ½Ñ‹Ðµ ÑÐºÑÐºÑƒÑ€ÑÐ¸Ð¸ Ð² Ð­Ñ€Ð¼Ð¸Ñ‚Ð°Ð¶</li><li>ÐÑ€ÐµÐ½Ð´Ð° ÑÑ…Ñ‚ Ð¿Ð¾ ÐºÐ°Ð½Ð°Ð»Ð°Ð¼ ÐÐµÐ²Ñ‹</li><li>Ð—Ð°ÐºÑ€Ñ‹Ñ‚Ñ‹Ðµ Ð´Ð²Ð¾Ñ€Ñ†Ñ‹</li></ul>
      <div class="price-tag">ÐžÑ‚ $49</div>
      <a href="tripwire-spb.html" class="btn btn-outline" style="text-align: center;">ÐŸÐ¾Ð´Ñ€Ð¾Ð±Ð½ÐµÐµ Ð¾ Ð¿ÑƒÑ‚ÐµÐ²Ð¾Ð´Ð¸Ñ‚ÐµÐ»Ðµ</a>
    </div>
    <div class="destination-card" style="cursor: pointer;" onclick="window.location.href='tripwire-sochi.html'">
      <h3><a href="tripwire-sochi.html" style="color: var(--gold); text-decoration: none;">Ð¡Ð¾Ñ‡Ð¸ (ÐšÑ€Ð°ÑÐ½Ð°Ñ ÐŸÐ¾Ð»ÑÐ½Ð°)</a></h3>
      <p>Ð ÑƒÑÑÐºÐ°Ñ Ð Ð¸Ð²ÑŒÐµÑ€Ð°. Ð¡Ð¾Ñ‡ÐµÑ‚Ð°Ð½Ð¸Ðµ Ð¼Ð¾Ñ€ÑÐºÐ¾Ð³Ð¾ Ð±Ñ€Ð¸Ð·Ð° Ð¸ Ð³Ð¾Ñ€Ð½Ð¾Ð»Ñ‹Ð¶Ð½Ñ‹Ñ… ÐºÑƒÑ€Ð¾Ñ€Ñ‚Ð¾Ð².</p>
      <ul><li>VIP-ÑˆÐ°Ñ‚Ñ€Ñ‹ Ð½Ð° Ð¿Ð»ÑÐ¶Ðµ Ð¸ ÑÑ…Ñ‚Ñ‹</li><li>Ð’ÐµÑ€Ñ‚Ð¾Ð»ÐµÑ‚Ð½Ñ‹Ðµ Ð¿Ñ€Ð¾Ð³ÑƒÐ»ÐºÐ¸</li><li>ÐšÐ°Ð·Ð¸Ð½Ð¾ Ð¿Ñ€ÐµÐ¼Ð¸ÑƒÐ¼-ÑƒÑ€Ð¾Ð²Ð½Ñ</li></ul>
      <div class="price-tag">ÐžÑ‚ $59</div>
      <a href="tripwire-sochi.html" class="btn btn-outline" style="text-align: center;">ÐŸÐ¾Ð´Ñ€Ð¾Ð±Ð½ÐµÐµ Ð¾ Ð¿ÑƒÑ‚ÐµÐ²Ð¾Ð´Ð¸Ñ‚ÐµÐ»Ðµ</a>
    </div>
    <div class="destination-card" style="cursor: pointer;" onclick="window.location.href='tripwire-kazan.html'">
      <h3><a href="tripwire-kazan.html" style="color: var(--gold); text-decoration: none;">ÐšÐ°Ð·Ð°Ð½ÑŒ</a></h3>
      <p>ÐŸÐµÑ€ÐµÑÐµÑ‡ÐµÐ½Ð¸Ðµ ÐºÑƒÐ»ÑŒÑ‚ÑƒÑ€. Ð–ÐµÐ¼Ñ‡ÑƒÐ¶Ð¸Ð½Ð° Ð¢Ð°Ñ‚Ð°Ñ€ÑÑ‚Ð°Ð½Ð° Ñ Ð±Ð¾Ð³Ð°Ñ‚Ñ‹Ð¼ Ð½Ð°ÑÐ»ÐµÐ´Ð¸ÐµÐ¼.</p>
      <ul><li>Ð­ÐºÑÐºÐ»ÑŽÐ·Ð¸Ð²Ð½Ñ‹Ðµ Ñ‚ÑƒÑ€Ñ‹ Ð² ÐšÑ€ÐµÐ¼Ð»ÑŒ</li><li>Ð›ÑƒÑ‡ÑˆÐ¸Ðµ Ñ…Ð°Ð»ÑÐ»ÑŒ-Ñ€ÐµÑÑ‚Ð¾Ñ€Ð°Ð½Ñ‹</li><li>ÐŸÑ€Ð¾Ð³ÑƒÐ»ÐºÐ¸ Ð¿Ð¾ Ð’Ð¾Ð»Ð³Ðµ</li></ul>
      <div class="price-tag">ÐžÑ‚ $39</div>
      <a href="tripwire-kazan.html" class="btn btn-outline" style="text-align: center;">ÐŸÐ¾Ð´Ñ€Ð¾Ð±Ð½ÐµÐµ Ð¾ Ð¿ÑƒÑ‚ÐµÐ²Ð¾Ð´Ð¸Ñ‚ÐµÐ»Ðµ</a>
    </div>
    <div class="destination-card" style="cursor: pointer;" onclick="window.location.href='tripwire-murmansk.html'">
      <h3><a href="tripwire-murmansk.html" style="color: var(--gold); text-decoration: none;">ÐœÑƒÑ€Ð¼Ð°Ð½ÑÐº</a></h3>
      <p>ÐžÑ…Ð¾Ñ‚Ð° Ð·Ð° Ð¡ÐµÐ²ÐµÑ€Ð½Ñ‹Ð¼ ÑÐ¸ÑÐ½Ð¸ÐµÐ¼ Ð½Ð° ÐºÑ€Ð°ÑŽ ÑÐ²ÐµÑ‚Ð° Ð² Ð°Ð±ÑÐ¾Ð»ÑŽÑ‚Ð½Ð¾Ð¼ ÐºÐ¾Ð¼Ñ„Ð¾Ñ€Ñ‚Ðµ.</p>
      <ul><li>Premium Glamping</li><li>ÐÑ€ÐºÑ‚Ð¸Ñ‡ÐµÑÐºÐ°Ñ Ð³Ð°ÑÑ‚Ñ€Ð¾Ð½Ð¾Ð¼Ð¸Ñ</li><li>Ð­ÐºÑÐ¿ÐµÐ´Ð¸Ñ†Ð¸Ð¸ Ð½Ð° Ð²Ð½ÐµÐ´Ð¾Ñ€Ð¾Ð¶Ð½Ð¸ÐºÐ°Ñ…</li></ul>
      <div class="price-tag">ÐžÑ‚ $79</div>
      <a href="tripwire-murmansk.html" class="btn btn-outline" style="text-align: center;">ÐŸÐ¾Ð´Ñ€Ð¾Ð±Ð½ÐµÐµ Ð¾ Ð¿ÑƒÑ‚ÐµÐ²Ð¾Ð´Ð¸Ñ‚ÐµÐ»Ðµ</a>
    </div>
  </div>
  <a href="https://wa.me/74950000000" class="floating-concierge" target="_blank"><svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.888-.788-1.487-1.761-1.663-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.052 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg><span>Personal Concierge</span></a>
</body>
</html>"""

files['destinations-en.html'] = files['destinations.html'].replace('lang="ru"', 'lang="en"').replace('Ð“Ð»Ð°Ð²Ð½Ð°Ñ', 'Home').replace('ÐÐ²Ñ‚Ð¾Ð¿Ð°Ñ€Ðº', 'Our Fleet').replace('ÐŸÑƒÑ‚ÐµÐ²Ð¾Ð´Ð¸Ñ‚ÐµÐ»Ð¸', 'Tripwires').replace('class="active">RU', '>RU').replace('>EN', 'class="active">EN').replace('ÐŸÑƒÑ‚ÐµÐ²Ð¾Ð´Ð¸Ñ‚ÐµÐ»Ð¸ Ð¸ Ð­ÐºÑÐºÐ»ÑŽÐ·Ð¸Ð²', 'City Guides & Exclusives').replace('Ð”Ð¾Ð±Ð°Ð²ÑŒÑ‚Ðµ Ð°Ð²Ñ‚Ð¾Ñ€ÑÐºÐ¸Ð¹ Ð¿ÑƒÑ‚ÐµÐ²Ð¾Ð´Ð¸Ñ‚ÐµÐ»ÑŒ Ðº Ð²Ð°ÑˆÐµÐ¼Ñƒ VIP-Ñ‚Ñ€Ð°Ð½ÑÑ„ÐµÑ€Ñƒ. ÐœÑ‹ ÑÐ¾Ð±Ñ€Ð°Ð»Ð¸ ÑÐ°Ð¼Ñ‹Ðµ Ð·Ð°ÐºÑ€Ñ‹Ñ‚Ñ‹Ðµ Ð»Ð¾ÐºÐ°Ñ†Ð¸Ð¸, Ð»ÑƒÑ‡ÑˆÐ¸Ðµ Ñ€ÐµÑÑ‚Ð¾Ñ€Ð°Ð½Ñ‹ Ð¸ Ð¿Ñ€ÐµÐ¼Ð¸Ð°Ð»ÑŒÐ½Ñ‹Ðµ Ð°ÐºÑ‚Ð¸Ð²Ð½Ð¾ÑÑ‚Ð¸.', 'Add a premium curated guide to your VIP transfer order. We have gathered the most private locations, top restaurants, and premium activities.').replace('ÐŸÐ¾Ð´Ñ€Ð¾Ð±Ð½ÐµÐµ Ð¾ Ð¿ÑƒÑ‚ÐµÐ²Ð¾Ð´Ð¸Ñ‚ÐµÐ»Ðµ', 'Read More About Guide').replace('ÐœÐ¾ÑÐºÐ²Ð°', 'Moscow').replace('Ð¡Ñ‚Ð¾Ð»Ð¸Ñ†Ð° Ñ€Ð¾ÑÐºÐ¾ÑˆÐ¸ Ð¸ Ñ€Ð¸Ñ‚Ð¼Ð°. Ð˜Ð´ÐµÐ°Ð»ÑŒÐ½Ð¾ Ð´Ð»Ñ Ð±Ð¸Ð·Ð½ÐµÑÐ° Ð¸ Ð¿Ñ€ÐµÐ¼Ð¸Ð°Ð»ÑŒÐ½Ð¾Ð³Ð¾ ÑˆÐ¾Ð¿Ð¸Ð½Ð³Ð°.', 'The capital of luxury and rhythm. Ideal for business and premium shopping.').replace('Ð—Ð°ÐºÑ€Ñ‹Ñ‚Ñ‹Ðµ VIP-ÐºÐ¾Ð¼Ð½Ð°Ñ‚Ñ‹ Ð¦Ð£Ðœ Ð¸ Ð“Ð£Ðœ', 'Private VIP shopping rooms at TSUM and GUM').replace('Ð ÐµÑÑ‚Ð¾Ñ€Ð°Ð½Ñ‹ Ñ Ñ…Ð°Ð»ÑÐ»ÑŒ-Ð¼ÐµÐ½ÑŽ (ÐœÐ¾ÑÐºÐ²Ð°-Ð¡Ð¸Ñ‚Ð¸)', 'Halal-friendly restaurants (Moscow City)').replace('ÐžÑ…Ñ€Ð°Ð½ÑÐµÐ¼Ñ‹Ðµ Ð¼Ð°Ñ€ÑˆÑ€ÑƒÑ‚Ñ‹', 'Secure routes').replace('Ð¡Ð°Ð½ÐºÑ‚-ÐŸÐµÑ‚ÐµÑ€Ð±ÑƒÑ€Ð³', 'Saint Petersburg').replace('Ð˜Ð¼Ð¿ÐµÑ€ÑÐºÐ°Ñ ÑÑÑ‚ÐµÑ‚Ð¸ÐºÐ° Ð¸ Ð±ÐµÐ»Ñ‹Ðµ Ð½Ð¾Ñ‡Ð¸. Ð¡ÐµÐ²ÐµÑ€Ð½Ð°Ñ ÑÑ‚Ð¾Ð»Ð¸Ñ†Ð° Ð Ð¾ÑÑÐ¸Ð¸.', 'Imperial aesthetics and white nights. The northern capital of Russia.').replace('Ð˜Ð½Ð´Ð¸Ð²Ð¸Ð´ÑƒÐ°Ð»ÑŒÐ½Ñ‹Ðµ ÑÐºÑÐºÑƒÑ€ÑÐ¸Ð¸ Ð² Ð­Ñ€Ð¼Ð¸Ñ‚Ð°Ð¶', 'Private tours of the Hermitage').replace('ÐÑ€ÐµÐ½Ð´Ð° ÑÑ…Ñ‚ Ð¿Ð¾ ÐºÐ°Ð½Ð°Ð»Ð°Ð¼ ÐÐµÐ²Ñ‹', 'Yacht rentals along Neva canals').replace('Ð—Ð°ÐºÑ€Ñ‹Ñ‚Ñ‹Ðµ Ð´Ð²Ð¾Ñ€Ñ†Ñ‹', 'Closed palaces').replace('Ð¡Ð¾Ñ‡Ð¸ (ÐšÑ€Ð°ÑÐ½Ð°Ñ ÐŸÐ¾Ð»ÑÐ½Ð°)', 'Sochi (Krasnaya Polyana)').replace('Ð ÑƒÑÑÐºÐ°Ñ Ð Ð¸Ð²ÑŒÐµÑ€Ð°. Ð¡Ð¾Ñ‡ÐµÑ‚Ð°Ð½Ð¸Ðµ Ð¼Ð¾Ñ€ÑÐºÐ¾Ð³Ð¾ Ð±Ñ€Ð¸Ð·Ð° Ð¸ Ð³Ð¾Ñ€Ð½Ð¾Ð»Ñ‹Ð¶Ð½Ñ‹Ñ… ÐºÑƒÑ€Ð¾Ñ€Ñ‚Ð¾Ð².', 'The Russian Riviera. A combination of sea breeze and ski resorts.').replace('VIP-ÑˆÐ°Ñ‚Ñ€Ñ‹ Ð½Ð° Ð¿Ð»ÑÐ¶Ðµ Ð¸ ÑÑ…Ñ‚Ñ‹', 'VIP beach cabanas and yachts').replace('Ð’ÐµÑ€Ñ‚Ð¾Ð»ÐµÑ‚Ð½Ñ‹Ðµ Ð¿Ñ€Ð¾Ð³ÑƒÐ»ÐºÐ¸', 'Helicopter tours').replace('ÐšÐ°Ð·Ð¸Ð½Ð¾ Ð¿Ñ€ÐµÐ¼Ð¸ÑƒÐ¼-ÑƒÑ€Ð¾Ð²Ð½Ñ', 'Premium casinos').replace('ÐšÐ°Ð·Ð°Ð½ÑŒ', 'Kazan').replace('ÐŸÐµÑ€ÐµÑÐµÑ‡ÐµÐ½Ð¸Ðµ ÐºÑƒÐ»ÑŒÑ‚ÑƒÑ€. Ð–ÐµÐ¼Ñ‡ÑƒÐ¶Ð¸Ð½Ð° Ð¢Ð°Ñ‚Ð°Ñ€ÑÑ‚Ð°Ð½Ð° Ñ Ð±Ð¾Ð³Ð°Ñ‚Ñ‹Ð¼ Ð½Ð°ÑÐ»ÐµÐ´Ð¸ÐµÐ¼.', 'Intersection of cultures. The pearl of Tatarstan with a rich heritage.').replace('Ð­ÐºÑÐºÐ»ÑŽÐ·Ð¸Ð²Ð½Ñ‹Ðµ Ñ‚ÑƒÑ€Ñ‹ Ð² ÐšÑ€ÐµÐ¼Ð»ÑŒ', 'Exclusive tours of the Kremlin').replace('Ð›ÑƒÑ‡ÑˆÐ¸Ðµ Ñ…Ð°Ð»ÑÐ»ÑŒ-Ñ€ÐµÑÑ‚Ð¾Ñ€Ð°Ð½Ñ‹', 'Best Halal restaurants').replace('ÐŸÑ€Ð¾Ð³ÑƒÐ»ÐºÐ¸ Ð¿Ð¾ Ð’Ð¾Ð»Ð³Ðµ', 'Volga river cruises').replace('ÐœÑƒÑ€Ð¼Ð°Ð½ÑÐº', 'Murmansk').replace('ÐžÑ…Ð¾Ñ‚Ð° Ð·Ð° Ð¡ÐµÐ²ÐµÑ€Ð½Ñ‹Ð¼ ÑÐ¸ÑÐ½Ð¸ÐµÐ¼ Ð½Ð° ÐºÑ€Ð°ÑŽ ÑÐ²ÐµÑ‚Ð° Ð² Ð°Ð±ÑÐ¾Ð»ÑŽÑ‚Ð½Ð¾Ð¼ ÐºÐ¾Ð¼Ñ„Ð¾Ñ€Ñ‚Ðµ.', 'Hunting for the Northern Lights at the edge of the world in absolute comfort.').replace('ÐÑ€ÐºÑ‚Ð¸Ñ‡ÐµÑÐºÐ°Ñ Ð³Ð°ÑÑ‚Ñ€Ð¾Ð½Ð¾Ð¼Ð¸Ñ', 'Arctic gastronomy').replace('Ð­ÐºÑÐ¿ÐµÐ´Ð¸Ñ†Ð¸Ð¸ Ð½Ð° Ð²Ð½ÐµÐ´Ð¾Ñ€Ð¾Ð¶Ð½Ð¸ÐºÐ°Ñ…', 'SUV expeditions').replace('ÐžÑ‚ $', 'From $')

files['destinations-ar.html'] = files['destinations-en.html'].replace('lang="en"', 'lang="ar" dir="rtl"').replace('<head>', "<head>\n  <style> body { font-family: 'Cairo', sans-serif; } h1, h2, h3, .logo-text { font-family: 'Cormorant Garamond', serif; } h1 { direction: ltr; display: inline-block; } </style>").replace('Home', 'Ø§Ù„Ø±Ø¦ÙŠØ³ÙŠØ©').replace('Our Fleet', 'Ø£Ø³Ø·ÙˆÙ„Ù†Ø§').replace('Tripwires', 'Ø§Ù„Ø£Ø¯Ù„Ø©').replace('class="active">EN', '>EN').replace('>AR', 'class="active">AR').replace('City Guides & Exclusives', 'Ø£Ø¯Ù„Ø© Ø§Ù„Ù…Ø¯Ù† ÙˆØ§Ù„Ø­ØµØ±ÙŠØ§Øª').replace('Add a premium curated guide to your VIP transfer order. We have gathered the most private locations, top restaurants, and premium activities.', 'Ø£Ø¶Ù Ø¯Ù„ÙŠÙ„Ø§Ù‹ Ù…ØªÙ…ÙŠØ²Ù‹Ø§ Ø¥Ù„Ù‰ Ø·Ù„Ø¨ Ø§Ù„Ù†Ù‚Ù„ Ø§Ù„Ø®Ø§Øµ Ø¨Ùƒ. Ù„Ù‚Ø¯ Ø¬Ù…Ø¹Ù†Ø§ Ø£ÙƒØ«Ø± Ø§Ù„Ù…ÙˆØ§Ù‚Ø¹ Ø³Ø±ÙŠØ©ØŒ ÙˆØ£ÙØ¶Ù„ Ø§Ù„Ù…Ø·Ø§Ø¹Ù…ØŒ ÙˆØ§Ù„Ø£Ù†Ø´Ø·Ø© Ø§Ù„ÙØ§Ø®Ø±Ø©.').replace('Read More About Guide', 'Ø§Ù‚Ø±Ø£ Ø§Ù„Ù…Ø²ÙŠØ¯ Ø¹Ù† Ø§Ù„Ø¯Ù„ÙŠÙ„').replace('Moscow', 'Ù…ÙˆØ³ÙƒÙˆ').replace('The capital of luxury and rhythm. Ideal for business and premium shopping.', 'Ø¹Ø§ØµÙ…Ø© Ø§Ù„ÙØ®Ø§Ù…Ø©. Ù…Ø«Ø§Ù„ÙŠØ© Ù„Ù„Ø£Ø¹Ù…Ø§Ù„ ÙˆØ§Ù„ØªØ³ÙˆÙ‚ Ø§Ù„Ø±Ø§Ù‚ÙŠ.').replace('Private VIP shopping rooms at TSUM and GUM', 'ØºØ±Ù ØªØ³ÙˆÙ‚ VIP Ø®Ø§ØµØ© ÙÙŠ TSUM Ùˆ GUM').replace('Halal-friendly restaurants (Moscow City)', 'Ù…Ø·Ø§Ø¹Ù… Ø­Ù„Ø§Ù„ (Ù…Ø¯ÙŠÙ†Ø© Ù…ÙˆØ³ÙƒÙˆ)').replace('Secure routes', 'Ù…Ø³Ø§Ø±Ø§Øª Ø¢Ù…Ù†Ø©').replace('Saint Petersburg', 'Ø³Ø§Ù†Øª Ø¨Ø·Ø±Ø³Ø¨Ø±Øº').replace('Imperial aesthetics and white nights. The northern capital of Russia.', 'Ø§Ù„Ø¬Ù…Ø§Ù„ Ø§Ù„Ø¥Ù…Ø¨Ø±Ø§Ø·ÙˆØ±ÙŠ ÙˆØ§Ù„Ù„ÙŠØ§Ù„ÙŠ Ø§Ù„Ø¨ÙŠØ¶Ø§Ø¡.').replace('Private tours of the Hermitage', 'Ø¬ÙˆÙ„Ø§Øª Ø®Ø§ØµØ© ÙÙŠ Ù…ØªØ­Ù Ø§Ù„Ø¥Ø±Ù…ÙŠØªØ§Ø¬').replace('Yacht rentals along Neva canals', 'ØªØ£Ø¬ÙŠØ± ÙŠØ®ÙˆØª ÙÙŠ Ù‚Ù†ÙˆØ§Øª Ù†ÙŠÙØ§').replace('Closed palaces', 'Ø¯Ø®ÙˆÙ„ Ø§Ù„Ù‚ØµÙˆØ± Ø§Ù„Ù…ØºÙ„Ù‚Ø©').replace('Sochi (Krasnaya Polyana)', 'Ø³ÙˆØªØ´ÙŠ (ÙƒØ±Ø§Ø³Ù†Ø§ÙŠØ§ Ø¨ÙˆÙ„ÙŠØ§Ù†Ø§)').replace('The Russian Riviera. A combination of sea breeze and ski resorts.', 'Ø§Ù„Ø±ÙŠÙÙŠÙŠØ±Ø§ Ø§Ù„Ø±ÙˆØ³ÙŠØ©. Ù…Ø²ÙŠØ¬ Ù…Ù† Ù†Ø³ÙŠÙ… Ø§Ù„Ø¨Ø­Ø± ÙˆÙ…Ù†ØªØ¬Ø¹Ø§Øª Ø§Ù„ØªØ²Ù„Ø¬.').replace('VIP beach cabanas and yachts', 'Ø®ÙŠÙ… Ø´Ø§Ø·Ø¦ÙŠØ© Ù„ÙƒØ¨Ø§Ø± Ø§Ù„Ø´Ø®ØµÙŠØ§Øª ÙˆÙŠØ®ÙˆØª').replace('Helicopter tours', 'Ø¬ÙˆÙ„Ø§Øª Ø¨Ø§Ù„Ø·Ø§Ø¦Ø±Ø© Ø§Ù„Ù…Ø±ÙˆØ­ÙŠØ©').replace('Premium casinos', 'ÙƒØ§Ø²ÙŠÙ†ÙˆÙ‡Ø§Øª ÙØ§Ø®Ø±Ø©').replace('Kazan', 'Ù‚Ø§Ø²Ø§Ù†').replace('Intersection of cultures. The pearl of Tatarstan with a rich heritage.', 'ØªÙ‚Ø§Ø·Ø¹ Ø§Ù„Ø«Ù‚Ø§ÙØ§Øª. Ù„Ø¤Ù„Ø¤Ø© ØªØªØ§Ø±Ø³ØªØ§Ù†.').replace('Exclusive tours of the Kremlin', 'Ø¬ÙˆÙ„Ø§Øª Ø­ØµØ±ÙŠØ© ÙÙŠ Ø§Ù„ÙƒØ±Ù…Ù„ÙŠÙ†').replace('Best Halal restaurants', 'Ø£ÙØ¶Ù„ Ø§Ù„Ù…Ø·Ø§Ø¹Ù… Ø§Ù„Ø­Ù„Ø§Ù„').replace('Volga river cruises', 'Ø±Ø­Ù„Ø§Øª Ù†Ù‡Ø±ÙŠØ© Ø¹Ù„Ù‰ Ø§Ù„ÙÙˆÙ„ØºØ§').replace('Murmansk', 'Ù…ÙˆØ±Ù…Ø§Ù†Ø³Ùƒ').replace('Hunting for the Northern Lights at the edge of the world in absolute comfort.', 'Ù…Ø·Ø§Ø±Ø¯Ø© Ø§Ù„Ø£Ø¶ÙˆØ§Ø¡ Ø§Ù„Ø´Ù…Ø§Ù„ÙŠØ© Ø¹Ù„Ù‰ Ø­Ø§ÙØ© Ø§Ù„Ø¹Ø§Ù„Ù….').replace('Premium Glamping', 'ØªØ®ÙŠÙŠÙ… ÙØ§Ø®Ø±').replace('Arctic gastronomy', 'ÙÙ† Ø§Ù„Ø·Ù‡ÙŠ Ø§Ù„Ù‚Ø·Ø¨ÙŠ').replace('SUV expeditions', 'Ø±Ø­Ù„Ø§Øª Ø§Ø³ØªÙƒØ´Ø§ÙÙŠØ© Ø¨Ø³ÙŠØ§Ø±Ø§Øª Ø§Ù„Ø¯ÙØ¹ Ø§Ù„Ø±Ø¨Ø§Ø¹ÙŠ').replace('From $', 'ØªØ¨Ø¯Ø£ Ù…Ù† $')

for k, v in files.items():
    with open(k, "w", encoding="utf-8") as f:
        f.write(v)

