import os

with open('build_index.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace missing translations
content = content.replace(
    "'Столица роскоши и ритма. От трансферов из Внуково-3 до деловых встреч в Москва-Сити и шопинга в ЦУМ с персональным сопровождением.', 'The capital of luxury and rhythm. Ideal for business meetings and premium shopping with personal escorts.'",
    "'Столица роскоши и ритма. От трансферов из Внуково-3 до деловых встреч в Москва-Сити и шопинга в ЦУМ с персональным сопровождением.', 'The capital of luxury and rhythm. From Vnukovo-3 transfers to business meetings in Moscow City and premium shopping at TSUM with personal escorts.'"
)

# Arabic translations
content = content.replace(
    "'Столица роскоши и ритма. От трансферов из Внуково-3 до деловых встреч в Москва-Сити и шопинга в ЦУМ с персональным сопровождением.', 'عاصمة الفخامة. مثالية لاجتماعات الأعمال والتسوق الراقي.'",
    "'Столица роскоши и ритма. От трансферов из Внуково-3 до деловых встреч в Москва-Сити и шопинга в ЦУМ с персональным сопровождением.', 'عاصمة الفخامة والإيقاع. من تنقلات فنوكوفو-3 إلى اجتماعات العمل في مدينة موسكو والتسوق الراقي في TSUM مع مرافقين شخصيين.'"
)

# Insert cache busting meta
meta = '''<meta charset="UTF-8">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">'''
content = content.replace('<meta charset="UTF-8">', meta)

with open('build_index.py', 'w', encoding='utf-8') as f:
    f.write(content)
