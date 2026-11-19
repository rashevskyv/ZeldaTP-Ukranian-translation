# Twilit Essentials — українська мова інтерфейсу

Українська локалізація інтерфейсу мода [Twilit Essentials](https://twilitrealm.dev/mods/com.dusklight.twilit_essentials/) (Fimmel) для Dusklight.

## Встановлення

1. Скопіюйте `ua.zeldatp.twilit_essentials_uk.dusk` у `data/mods` поруч із `com.dusklight.twilit_essentials.dusk`.
2. У Twilit Essentials оберіть мову «Українська».

## Файли

- `mod/res/localization/uk/<feature>/<feature>.json` — переклад: 19 розділів, 1937 ключів (усі ключі з README te-service-examples, разом із `quest` і `guide`).
- `mod/` — вихідний код мода: реєструє мову `uk` через сервіс `com.dusklight.twilit_essentials.localization` (fallback `en`).
- `font/remap_font.py` — додає кириличні гліфи шрифту [HyliaSerifCyrillic](https://shedevr.org.ru/zelda64rus/media-fonts.html) у слоти Latin-1, які використовує кодування нашого перекладу гри.

---

# Twilit Essentials — Ukrainian UI

Ukrainian localization of the Twilit Essentials UI. Files for the authors: `mod/res/localization/uk/` (same layout as `res/localization/en/`, 1937 keys, placeholders checked). Copy the `uk` folder next to `en` to ship it built in, or use the `.dusk` add-on that registers the language through the localization service.
