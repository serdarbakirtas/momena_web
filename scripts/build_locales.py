#!/usr/bin/env python3
"""One-off helpers to build de/ and tr/ locale pages from English sources."""
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]


def fix_assets(text: str, depth: int) -> str:
    prefix = "../" * depth
    for attr in ('href="', 'src="'):
        text = text.replace(attr + "assets/", attr + prefix + "assets/")
    return text


def patch_de_index():
    src = ROOT / "index.html"
    p = ROOT / "de/index.html"
    t = src.read_text(encoding="utf-8")
    t = fix_assets(t, 1)
    t = t.replace('<html lang="en">', '<html lang="de">')
    t = re.sub(
        r'<link rel="canonical" href="https://momena\.app/"',
        '<link rel="canonical" href="https://momena.app/de/"',
        t,
        count=1,
    )
    t = t.replace('<meta property="og:locale" content="en_US" />', '<meta property="og:locale" content="de_DE" />')
    t = t.replace(
        '<meta property="og:url" content="https://momena.app/"',
        '<meta property="og:url" content="https://momena.app/de/"',
        1,
    )
    t = t.replace('"inLanguage": "en"', '"inLanguage": "de"')
    t = t.replace(
        "<title>Momena – Family memories, calendar &amp; health in one app</title>",
        "<title>Momena – Familienerinnerungen, Kalender &amp; Gesundheit in einer App</title>",
    )
    t = t.replace(
        '<meta name="description" content="Momena helps families organize memories, events, and health records in one simple, private iOS app. Encrypted on-device; optional iCloud backup." />',
        '<meta name="description" content="Momena hilft Familien, Erinnerungen, Termine und Gesundheitsdaten in einer einfachen, privaten iOS-App zu organisieren. Verschlüsselt auf dem Gerät; optionales iCloud-Backup." />',
    )
    t = t.replace(">Pricing<", ">Preise<", 4)
    t = t.replace(">Our story<", ">Unsere Geschichte<", 4)
    t = t.replace('aria-label="Download Momena on the App Store"', 'aria-label="Momena im App Store laden"')
    t = t.replace(">App Download<", ">App-Download<")
    t = t.replace(
        "<h1>Stop missing family moments.<br />Start organizing like a pro.</h1>",
        "<h1>Verpassen Sie keine Familienmomente mehr.<br />Organisieren Sie wie ein Profi.</h1>",
    )
    t = t.replace(
        "Memories, events, and health records in one place. Track growth, sleep, and appointments—all designed for families.",
        "Erinnerungen, Termine und Gesundheitsdaten an einem Ort. Wachstum, Schlaf und Arzttermine im Blick—für Familien gemacht.",
    )
    t = t.replace(">Download on the App Store<", ">Im App Store laden<")
    t = t.replace("<h2>Your family, one app</h2>", "<h2>Ihre Familie, eine App</h2>")
    t = t.replace(
        "<p class=\"subtitle\">Memories, calendar, health—everything in sync.</p>",
        "<p class=\"subtitle\">Erinnerungen, Kalender, Gesundheit—alles im Einklang.</p>",
    )
    t = t.replace("<h2>Built for families</h2>", "<h2>Für Familien gebaut</h2>")
    t = t.replace("<h3>Memories</h3>", "<h3>Erinnerungen</h3>")
    t = t.replace(
        "Store photos, videos, and notes. Build a timeline of your family's best moments.",
        "Fotos, Videos und Notizen speichern. Die schönsten Momente als Zeitleiste.",
    )
    t = t.replace("<h3>Events & Calendar</h3>", "<h3>Termine &amp; Kalender</h3>")
    t = t.replace(
        "Birthdays, appointments, vaccinations—never miss an important date again.",
        "Geburtstage, Arzttermine, Impfungen—wichtige Daten nicht mehr verpassen.",
    )
    t = t.replace("<h3>Health Tracking</h3>", "<h3>Gesundheit</h3>")
    t = t.replace(
        "Height, weight, sleep, symptoms. Keep essential records in one secure place.",
        "Größe, Gewicht, Schlaf, Symptome. Wichtige Daten an einem sicheren Ort.",
    )
    t = t.replace("<h2>Security first</h2>", "<h2>Sicherheit zuerst</h2>")
    t = t.replace(
        "<p class=\"subtitle\">Your family data stays private and protected.</p>",
        "<p class=\"subtitle\">Ihre Familiendaten bleiben privat und geschützt.</p>",
    )
    t = t.replace("<h3>AES-256 encryption</h3>", "<h3>AES-256-Verschlüsselung</h3>")
    t = t.replace(
        "All sensitive data is encrypted at rest using industry-standard AES-256-GCM. Keys are stored in iOS Keychain.",
        "Sensible Daten werden mit AES-256-GCM verschlüsselt. Schlüssel liegen im iOS-Schlüsselbund.",
    )
    t = t.replace("<h3>On-device by default</h3>", "<h3>Standardmäßig auf dem Gerät</h3>")
    t = t.replace(
        "Data stays on your device. No cloud required unless you enable optional iCloud Backup with a subscription.",
        "Daten bleiben auf Ihrem Gerät. Keine Cloud nötig, außer Sie aktivieren optional iCloud-Backup.",
    )
    t = t.replace("<h3>Encrypted iCloud backup</h3>", "<h3>Verschlüsseltes iCloud-Backup</h3>")
    t = t.replace(
        "When enabled, backups are stored encrypted in your private iCloud database—we never see your data.",
        "Aktiviert werden Backups verschlüsselt in Ihrer iCloud gespeichert—wir sehen Ihre Daten nicht.",
    )
    t = t.replace("<h2>Frequently Asked Questions</h2>", "<h2>Häufige Fragen</h2>")
    t = t.replace(
        'Have a different question? Reach out to us at <a href="mailto:serdarbakirtas@pm.me">serdarbakirtas@pm.me</a>.',
        'Andere Frage? Schreiben Sie uns an <a href="mailto:serdarbakirtas@pm.me">serdarbakirtas@pm.me</a>.',
    )
    # FAQ items
    reps = [
        (
            "What makes Momena different from other family organizers?",
            "Was unterscheidet Momena von anderen Familien-Apps?",
        ),
        (
            "Momena combines memories, calendar events, and health tracking in one app. Your data stays on your device by default with AES-256 encryption—no cloud required unless you choose optional iCloud Backup. We don't share, sell, or use your data for advertising.",
            "Momena vereint Erinnerungen, Kalender und Gesundheit in einer App. Ihre Daten bleiben standardmäßig auf dem Gerät mit AES-256—ohne Cloud, außer Sie aktivieren optional iCloud-Backup. Wir verkaufen Ihre Daten nicht und nutzen sie nicht für Werbung.",
        ),
        ("Do I need to pay to use Momena?", "Muss ich für Momena bezahlen?"),
        (
            "Local storage and on-device usage are free. iCloud Backup is an optional subscription feature—you only pay if you want your data backed up to your iCloud account for restore when you change devices.",
            "Lokale Speicherung ist kostenlos. iCloud-Backup ist optional kostenpflichtig—Sie zahlen nur, wenn Sie Daten in Ihrer iCloud sichern möchten.",
        ),
        ("Can I use Momena offline?", "Funktioniert Momena offline?"),
        (
            "Yes. All your data is stored locally on your device. The app works fully offline. iCloud Backup (if enabled) syncs when you're connected, but core features don't require internet.",
            "Ja. Alle Daten liegen lokal auf Ihrem Gerät. Die App funktioniert offline. iCloud-Backup synchronisiert bei Verbindung; Kernfunktionen brauchen kein Internet.",
        ),
        ("How secure is my family's data?", "Wie sicher sind unsere Daten?"),
        (
            "All sensitive data is encrypted at rest using AES-256-GCM. Encryption keys are stored in iOS Keychain, and data is protected by the iOS Data Protection API. We don't operate our own servers—your data stays on your device or in your private iCloud account when you enable backup.",
            "Sensible Daten sind mit AES-256-GCM verschlüsselt. Schlüssel liegen im iOS-Schlüsselbund. Wir betreiben keine eigenen Server—Ihre Daten bleiben auf dem Gerät oder in Ihrer iCloud.",
        ),
        ("Can I export or delete my data?", "Kann ich Daten exportieren oder löschen?"),
        (
            "Yes. You can export your data at any time, delete all data through app settings, and control backup and restore operations. You own your data.",
            "Ja. Export jederzeit, Löschen in den App-Einstellungen, volle Kontrolle über Backup und Wiederherstellung.",
        ),
        ("What devices does Momena work on?", "Auf welchen Geräten läuft Momena?"),
        (
            "Momena is available on iPhone and iPad via the App Store. It's designed for iOS and uses Apple's security features including Keychain and Data Protection.",
            "Momena gibt es für iPhone und iPad im App Store. Nutzt Apples Sicherheitsfunktionen wie Schlüsselbund und Data Protection.",
        ),
    ]
    for a, b in reps:
        t = t.replace(a, b)
    t = t.replace("<h3>Navigate</h3>", "<h3>Navigation</h3>")
    t = t.replace('<li><a href="./">Home</a></li>', '<li><a href="./">Start</a></li>')
    t = t.replace("<h3>Legal</h3>", "<h3>Rechtliches</h3>")
    t = t.replace(">Privacy Policy<", ">Datenschutz<")
    t = t.replace(">Terms of Service<", ">Nutzungsbedingungen<")
    old_lang = """    <div class="footer-lang-row">
      <div class="footer-lang-block">
        <span class="footer-lang-label" id="footer-lang-label">Language</span>
        <details class="lang-select">
          <summary class="lang-select-summary">
            <span class="lang-flag" aria-hidden="true">🇬🇧</span>
            <span>English</span>
            <span class="lang-chevron" aria-hidden="true">▾</span>
          </summary>
          <ul class="lang-select-list" role="list">
            <li><a class="lang-select-link" href="./" hreflang="en" aria-current="page"><span class="lang-flag" aria-hidden="true">🇬🇧</span> English</a></li>
            <li><a class="lang-select-link" href="de/" hreflang="de"><span class="lang-flag" aria-hidden="true">🇩🇪</span> Deutsch</a></li>
            <li><a class="lang-select-link" href="tr/" hreflang="tr"><span class="lang-flag" aria-hidden="true">🇹🇷</span> Türkçe</a></li>
          </ul>
        </details>
      </div>
    </div>"""
    new_lang = """    <div class="footer-lang-row">
      <div class="footer-lang-block">
        <span class="footer-lang-label" id="footer-lang-label">Sprache</span>
        <details class="lang-select">
          <summary class="lang-select-summary">
            <span class="lang-flag" aria-hidden="true">🇩🇪</span>
            <span>Deutsch</span>
            <span class="lang-chevron" aria-hidden="true">▾</span>
          </summary>
          <ul class="lang-select-list" role="list">
            <li><a class="lang-select-link" href="../" hreflang="en"><span class="lang-flag" aria-hidden="true">🇬🇧</span> English</a></li>
            <li><a class="lang-select-link" href="./" hreflang="de" aria-current="page"><span class="lang-flag" aria-hidden="true">🇩🇪</span> Deutsch</a></li>
            <li><a class="lang-select-link" href="../tr/" hreflang="tr"><span class="lang-flag" aria-hidden="true">🇹🇷</span> Türkçe</a></li>
          </ul>
        </details>
      </div>
    </div>"""
    t = t.replace(old_lang, new_lang)
    t = t.replace(">Cookie Policy<", ">Cookie-Richtlinie<")
    t = t.replace(">Cookie preferences<", ">Cookie-Einstellungen<")
    t = t.replace("All rights reserved.", "Alle Rechte vorbehalten.")
    t = t.replace('aria-label="Cookie consent"', 'aria-label="Cookie-Einwilligung"')
    t = t.replace(
        "We use cookies and local storage to remember your preferences. By continuing, you accept our use of cookies.",
        "Wir verwenden Cookies und lokalen Speicher für Ihre Einstellungen. Mit Fortfahren akzeptieren Sie die Nutzung von Cookies.",
    )
    t = t.replace(">Accept<", ">Akzeptieren<")
    t = t.replace(">Reject<", ">Ablehnen<")
    p.write_text(t, encoding="utf-8")
    print("Wrote", p)


def patch_tr_index():
    src = ROOT / "index.html"
    p = ROOT / "tr/index.html"
    t = src.read_text(encoding="utf-8")
    t = fix_assets(t, 1)
    t = t.replace('<html lang="en">', '<html lang="tr">')
    t = re.sub(
        r'<link rel="canonical" href="https://momena\.app/"',
        '<link rel="canonical" href="https://momena.app/tr/"',
        t,
        count=1,
    )
    t = t.replace('<meta property="og:locale" content="en_US" />', '<meta property="og:locale" content="tr_TR" />')
    t = t.replace(
        '<meta property="og:url" content="https://momena.app/"',
        '<meta property="og:url" content="https://momena.app/tr/"',
        1,
    )
    t = t.replace('"inLanguage": "en"', '"inLanguage": "tr"')
    t = t.replace(
        "<title>Momena – Family memories, calendar &amp; health in one app</title>",
        "<title>Momena – Aile anıları, takvim ve sağlık tek uygulamada</title>",
    )
    t = t.replace(
        '<meta name="description" content="Momena helps families organize memories, events, and health records in one simple, private iOS app. Encrypted on-device; optional iCloud backup." />',
        '<meta name="description" content="Momena, ailelerin anıları, etkinlikleri ve sağlık kayıtlarını basit ve gizli bir iOS uygulamasında düzenlemesine yardımcı olur. Şifreli, isteğe bağlı iCloud yedekleme." />',
    )
    t = t.replace(">Pricing<", ">Fiyatlandırma<", 4)
    t = t.replace(">Our story<", ">Hikayemiz<", 4)
    t = t.replace('aria-label="Download Momena on the App Store"', 'aria-label="Momena’yı App Store’dan indir"')
    t = t.replace(">App Download<", ">Uygulama indir<")
    t = t.replace(
        "<h1>Stop missing family moments.<br />Start organizing like a pro.</h1>",
        "<h1>Aile anılarını kaçırmayın.<br />Profesyonel gibi düzenleyin.</h1>",
    )
    t = t.replace(
        "Memories, events, and health records in one place. Track growth, sleep, and appointments—all designed for families.",
        "Anılar, etkinlikler ve sağlık kayıtları tek yerde. Büyüme, uyku ve randevular—aileler için.",
    )
    t = t.replace(">Download on the App Store<", ">App Store’dan indir<")
    t = t.replace("<h2>Your family, one app</h2>", "<h2>Aileniz, tek uygulama</h2>")
    t = t.replace(
        "<p class=\"subtitle\">Memories, calendar, health—everything in sync.</p>",
        "<p class=\"subtitle\">Anılar, takvim, sağlık—hepsi uyum içinde.</p>",
    )
    t = t.replace("<h2>Built for families</h2>", "<h2>Aileler için</h2>")
    t = t.replace("<h3>Memories</h3>", "<h3>Anılar</h3>")
    t = t.replace(
        "Store photos, videos, and notes. Build a timeline of your family's best moments.",
        "Fotoğraf, video ve notlar. En güzel anları zaman çizelgesinde toplayın.",
    )
    t = t.replace("<h3>Events & Calendar</h3>", "<h3>Etkinlikler ve takvim</h3>")
    t = t.replace(
        "Birthdays, appointments, vaccinations—never miss an important date again.",
        "Doğum günleri, randevular, aşılar—önemli tarihleri kaçırmayın.",
    )
    t = t.replace("<h3>Health Tracking</h3>", "<h3>Sağlık takibi</h3>")
    t = t.replace(
        "Height, weight, sleep, symptoms. Keep essential records in one secure place.",
        "Boy, kilo, uyku, semptomlar. Kayıtlar güvenli bir yerde.",
    )
    t = t.replace("<h2>Security first</h2>", "<h2>Önce güvenlik</h2>")
    t = t.replace(
        "<p class=\"subtitle\">Your family data stays private and protected.</p>",
        "<p class=\"subtitle\">Aile verileriniz gizli ve korunur.</p>",
    )
    t = t.replace("<h3>AES-256 encryption</h3>", "<h3>AES-256 şifreleme</h3>")
    t = t.replace(
        "All sensitive data is encrypted at rest using industry-standard AES-256-GCM. Keys are stored in iOS Keychain.",
        "Hassas veriler AES-256-GCM ile şifrelenir. Anahtarlar iOS Anahtarlık’ta saklanır.",
    )
    t = t.replace("<h3>On-device by default</h3>", "<h3>Varsayılan olarak cihazda</h3>")
    t = t.replace(
        "Data stays on your device. No cloud required unless you enable optional iCloud Backup with a subscription.",
        "Veriler cihazınızda kalır. İsteğe bağlı iCloud Yedekleme dışında bulut gerekmez.",
    )
    t = t.replace("<h3>Encrypted iCloud backup</h3>", "<h3>Şifreli iCloud yedekleme</h3>")
    t = t.replace(
        "When enabled, backups are stored encrypted in your private iCloud database—we never see your data.",
        "Etkinleştirildiğinde yedekler iCloud’unuzda şifreli saklanır—verilerinizi görmeyiz.",
    )
    t = t.replace("<h2>Frequently Asked Questions</h2>", "<h2>Sıkça sorulan sorular</h2>")
    t = t.replace(
        'Have a different question? Reach out to us at <a href="mailto:serdarbakirtas@pm.me">serdarbakirtas@pm.me</a>.',
        'Başka sorunuz mu var? <a href="mailto:serdarbakirtas@pm.me">serdarbakirtas@pm.me</a> adresine yazın.',
    )
    trep = [
        (
            "What makes Momena different from other family organizers?",
            "Momena’yı diğer aile uygulamalarından ayıran nedir?",
        ),
        (
            "Momena combines memories, calendar events, and health tracking in one app. Your data stays on your device by default with AES-256 encryption—no cloud required unless you choose optional iCloud Backup. We don't share, sell, or use your data for advertising.",
            "Momena anıları, takvimi ve sağlığı tek uygulamada birleştirir. Verileriniz varsayılan olarak AES-256 ile cihazınızda kalır—isteğe bağlı iCloud Yedekleme hariç bulut gerekmez. Verilerinizi satmıyor veya reklam için kullanmıyoruz.",
        ),
        ("Do I need to pay to use Momena?", "Momena için ödeme yapmam gerekir mi?"),
        (
            "Local storage and on-device usage are free. iCloud Backup is an optional subscription feature—you only pay if you want your data backed up to your iCloud account for restore when you change devices.",
            "Yerel kullanım ücretsizdir. iCloud Yedekleme isteğe bağlıdır—yalnızca cihaz değişiminde yedek isterseniz ödersiniz.",
        ),
        ("Can I use Momena offline?", "Momena çevrimdışı çalışır mı?"),
        (
            "Yes. All your data is stored locally on your device. The app works fully offline. iCloud Backup (if enabled) syncs when you're connected, but core features don't require internet.",
            "Evet. Tüm veriler cihazınızda. Uygulama çevrimdışı çalışır. iCloud etkinse bağlantıda senkron olur; temel özellikler internet istemez.",
        ),
        ("How secure is my family's data?", "Verilerim ne kadar güvenli?"),
        (
            "All sensitive data is encrypted at rest using AES-256-GCM. Encryption keys are stored in iOS Keychain, and data is protected by the iOS Data Protection API. We don't operate our own servers—your data stays on your device or in your private iCloud account when you enable backup.",
            "Hassas veriler AES-256-GCM ile şifrelenir. Anahtarlar iOS Anahtarlık’tadır. Kendi sunucularımız yok—veriler cihazda veya iCloud’unuzda kalır.",
        ),
        ("Can I export or delete my data?", "Verilerimi dışa aktarabilir veya silebilir miyim?"),
        (
            "Yes. You can export your data at any time, delete all data through app settings, and control backup and restore operations. You own your data.",
            "Evet. İstediğiniz zaman dışa aktarın, ayarlardan silin, yedeklemeyi yönetin.",
        ),
        ("What devices does Momena work on?", "Hangi cihazlarda çalışır?"),
        (
            "Momena is available on iPhone and iPad via the App Store. It's designed for iOS and uses Apple's security features including Keychain and Data Protection.",
            "Momena iPhone ve iPad için App Store’da. iOS güvenlik özelliklerini kullanır.",
        ),
    ]
    for a, b in trep:
        t = t.replace(a, b)
    t = t.replace("<h3>Navigate</h3>", "<h3>Gezinme</h3>")
    t = t.replace('<li><a href="./">Home</a></li>', '<li><a href="./">Ana sayfa</a></li>')
    t = t.replace("<h3>Legal</h3>", "<h3>Yasal</h3>")
    t = t.replace(">Privacy Policy<", ">Gizlilik politikası<")
    t = t.replace(">Terms of Service<", ">Kullanım şartları<")
    old_lang = """    <div class="footer-lang-row">
      <div class="footer-lang-block">
        <span class="footer-lang-label" id="footer-lang-label">Language</span>
        <details class="lang-select">
          <summary class="lang-select-summary">
            <span class="lang-flag" aria-hidden="true">🇬🇧</span>
            <span>English</span>
            <span class="lang-chevron" aria-hidden="true">▾</span>
          </summary>
          <ul class="lang-select-list" role="list">
            <li><a class="lang-select-link" href="./" hreflang="en" aria-current="page"><span class="lang-flag" aria-hidden="true">🇬🇧</span> English</a></li>
            <li><a class="lang-select-link" href="de/" hreflang="de"><span class="lang-flag" aria-hidden="true">🇩🇪</span> Deutsch</a></li>
            <li><a class="lang-select-link" href="tr/" hreflang="tr"><span class="lang-flag" aria-hidden="true">🇹🇷</span> Türkçe</a></li>
          </ul>
        </details>
      </div>
    </div>"""
    new_lang = """    <div class="footer-lang-row">
      <div class="footer-lang-block">
        <span class="footer-lang-label" id="footer-lang-label">Dil</span>
        <details class="lang-select">
          <summary class="lang-select-summary">
            <span class="lang-flag" aria-hidden="true">🇹🇷</span>
            <span>Türkçe</span>
            <span class="lang-chevron" aria-hidden="true">▾</span>
          </summary>
          <ul class="lang-select-list" role="list">
            <li><a class="lang-select-link" href="../" hreflang="en"><span class="lang-flag" aria-hidden="true">🇬🇧</span> English</a></li>
            <li><a class="lang-select-link" href="../de/" hreflang="de"><span class="lang-flag" aria-hidden="true">🇩🇪</span> Deutsch</a></li>
            <li><a class="lang-select-link" href="./" hreflang="tr" aria-current="page"><span class="lang-flag" aria-hidden="true">🇹🇷</span> Türkçe</a></li>
          </ul>
        </details>
      </div>
    </div>"""
    t = t.replace(old_lang, new_lang)
    t = t.replace(">Cookie Policy<", ">Çerez politikası<")
    t = t.replace(">Cookie preferences<", ">Çerez tercihleri<")
    t = t.replace("All rights reserved.", "Tüm hakları saklıdır.")
    t = t.replace('aria-label="Cookie consent"', 'aria-label="Çerez onayı"')
    t = t.replace(
        "We use cookies and local storage to remember your preferences. By continuing, you accept our use of cookies.",
        "Tercihlerinizi hatırlamak için çerez ve yerel depolama kullanıyoruz. Devam ederek çerez kullanımını kabul edersiniz.",
    )
    t = t.replace(">Accept<", ">Kabul et<")
    t = t.replace(">Reject<", ">Reddet<")
    p.write_text(t, encoding="utf-8")
    print("Wrote", p)


def patch_locale_subpage(locale: str, slug: str):
    """Copy EN subpage; set lang selector + canonical for de/ or tr/. Body stays English until translated."""
    en_path = ROOT / slug / "index.html"
    out = ROOT / locale / slug / "index.html"
    t = en_path.read_text(encoding="utf-8")
    t = t.replace('<html lang="en">', f'<html lang="{locale}">')
    if locale == "de":
        t = t.replace('<meta property="og:locale" content="en_US" />', '<meta property="og:locale" content="de_DE" />')
    else:
        t = t.replace('<meta property="og:locale" content="en_US" />', '<meta property="og:locale" content="tr_TR" />')
    pat = re.compile(
        r'<div class="footer-lang-row">.*?</div>\s*<div class="footer-bottom">',
        re.DOTALL,
    )
    en_url = f"https://momena.app/{slug}/"
    de_url = f"https://momena.app/de/{slug}/"
    tr_url = f"https://momena.app/tr/{slug}/"
    canon = de_url if locale == "de" else tr_url
    t = re.sub(
        r'<link rel="canonical" href="https://momena\.app/' + re.escape(slug) + r'/"',
        f'<link rel="canonical" href="{canon}"',
        t,
        count=1,
    )
    t = t.replace(f'<meta property="og:url" content="{en_url}"', f'<meta property="og:url" content="{canon}"', 1)
    if locale == "de":
        new_block = f"""      <div class="footer-lang-row">
        <div class="footer-lang-block">
          <span class="footer-lang-label" id="footer-lang-label">Sprache</span>
          <details class="lang-select">
            <summary class="lang-select-summary">
              <span class="lang-flag" aria-hidden="true">🇩🇪</span>
              <span>Deutsch</span>
              <span class="lang-chevron" aria-hidden="true">▾</span>
            </summary>
            <ul class="lang-select-list" role="list">
              <li><a class="lang-select-link" href="../../{slug}/" hreflang="en"><span class="lang-flag" aria-hidden="true">🇬🇧</span> English</a></li>
              <li><a class="lang-select-link" href="./" hreflang="de" aria-current="page"><span class="lang-flag" aria-hidden="true">🇩🇪</span> Deutsch</a></li>
              <li><a class="lang-select-link" href="../../tr/{slug}/" hreflang="tr"><span class="lang-flag" aria-hidden="true">🇹🇷</span> Türkçe</a></li>
            </ul>
          </details>
        </div>
      </div>
      <div class="footer-bottom">"""
    else:
        new_block = f"""      <div class="footer-lang-row">
        <div class="footer-lang-block">
          <span class="footer-lang-label" id="footer-lang-label">Dil</span>
          <details class="lang-select">
            <summary class="lang-select-summary">
              <span class="lang-flag" aria-hidden="true">🇹🇷</span>
              <span>Türkçe</span>
              <span class="lang-chevron" aria-hidden="true">▾</span>
            </summary>
            <ul class="lang-select-list" role="list">
              <li><a class="lang-select-link" href="../../{slug}/" hreflang="en"><span class="lang-flag" aria-hidden="true">🇬🇧</span> English</a></li>
              <li><a class="lang-select-link" href="../../de/{slug}/" hreflang="de"><span class="lang-flag" aria-hidden="true">🇩🇪</span> Deutsch</a></li>
              <li><a class="lang-select-link" href="./" hreflang="tr" aria-current="page"><span class="lang-flag" aria-hidden="true">🇹🇷</span> Türkçe</a></li>
            </ul>
          </details>
        </div>
      </div>
      <div class="footer-bottom">"""
    t = pat.sub(new_block, t, count=1)
    out.write_text(t, encoding="utf-8")
    print("Wrote", out)


if __name__ == "__main__":
    patch_de_index()
    patch_tr_index()
    for slug in (
        "pricing",
        "our-story",
        "blog",
        "support",
        "terms-of-service",
        "privacy-policy",
        "cookies-policy",
    ):
        patch_locale_subpage("de", slug)
        patch_locale_subpage("tr", slug)
