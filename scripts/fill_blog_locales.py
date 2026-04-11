#!/usr/bin/env python3
"""Fill de/ and tr/ blog HTML for the six April 2026 posts."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Shared chrome strings
CHROME = {
    "de": {
        "nav_aria": "Hauptnavigation",
        "blog_back_aria": "Blog-Navigation",
        "nav_home": "Start",
        "nav_pricing": "Preise",
        "nav_story": "Unsere Geschichte",
        "nav_blog": "Blog",
        "nav_support": "Support",
        "header_qr": "Momena im App Store laden",
        "qr_label": "App-Download",
        "back": "← Alle Beiträge",
        "newsletter_h": "Bleiben Sie auf dem Laufenden",
        "newsletter_p": "Neue Beiträge, Produktupdates und Hinweise zum Datenschutz — direkt in Ihr Postfach. Kein Spam, niemals.",
        "placeholder": "Ihre E-Mail-Adresse",
        "subscribe": "Abonnieren",
        "disclaimer": "Kein Spam. Jederzeit abbestellbar.",
        "footer_nav_h": "Navigation",
        "footer_legal_h": "Rechtliches",
        "privacy": "Datenschutz",
        "terms": "Nutzungsbedingungen",
        "footer_lang": "Sprache",
        "cookie_aria": "Cookie-Einwilligung",
        "cookie_p": "Wir verwenden Cookies und lokalen Speicher, um Ihre Einstellungen zu speichern. Wenn Sie fortfahren, akzeptieren Sie unsere Cookies. ",
        "learn": "Mehr erfahren",
        "accept": "Akzeptieren",
        "reject": "Ablehnen",
        "cookie_link": "Cookie-Richtlinie",
        "footer_cookie_policy": "Cookie-Richtlinie",
        "footer_cookie_prefs": "Cookie-Einstellungen",
        "html_lang": "de",
        "og_locale": "de_DE",
    },
    "tr": {
        "nav_aria": "Ana gezinme",
        "blog_back_aria": "Blog gezintisi",
        "nav_home": "Ana sayfa",
        "nav_pricing": "Fiyatlandırma",
        "nav_story": "Hikayemiz",
        "nav_blog": "Blog",
        "nav_support": "Support",
        "header_qr": "Momena’yı App Store’dan indir",
        "qr_label": "Uygulama indir",
        "back": "← Tüm yazılar",
        "newsletter_h": "Haberdar olun",
        "newsletter_p": "Yeni yazılar, ürün güncellemeleri ve gizlilik notları — doğrudan gelen kutunuza. Asla spam yok.",
        "placeholder": "E-posta adresiniz",
        "subscribe": "Abone ol",
        "disclaimer": "Spam yok. İstediğiniz zaman çıkın.",
        "footer_nav_h": "Gezinme",
        "footer_legal_h": "Yasal",
        "privacy": "Gizlilik Politikası",
        "terms": "Hizmet Şartları",
        "footer_lang": "Dil",
        "cookie_aria": "Çerez onayı",
        "cookie_p": "Tercihlerinizi hatırlamak için çerezler ve yerel depolama kullanıyoruz. Devam ederek çerez kullanımımızı kabul etmiş olursunuz. ",
        "learn": "Daha fazla bilgi",
        "accept": "Kabul et",
        "reject": "Reddet",
        "cookie_link": "Çerez Politikası",
        "footer_cookie_policy": "Çerez Politikası",
        "footer_cookie_prefs": "Çerez tercihleri",
        "html_lang": "tr",
        "og_locale": "tr_TR",
    },
}

POSTS: dict[str, dict[str, dict[str, str]]] = {
    "capture-your-family-story": {
        "de": {
            "title": "Warum Sie die Geschichte Ihrer Familie festhalten sollten – Momena",
            "meta": "Fotos zeigen einen Moment, nicht die Geschichte dahinter. Warum Kontext zählt – und wie Momena Erinnerungen privat hält.",
            "canonical": "https://momena.app/de/blog/capture-your-family-story.html",
            "headline": "Warum Sie die Geschichte Ihrer Familie festhalten sollten",
            "badge_class": "blog-card__badge--family-tips",
            "badge": "Elternschaft",
            "date": "12. April 2026",
            "read": "3 Min. Lesezeit",
            "hero_alt": "Eine mehrgenerationen Familie lacht gemeinsam auf einer Holzbrücke in der Natur.",
            "body": """<p>Lassen Sie uns eine Frage stellen: Erinnern Sie sich an den Tag, an dem Ihr Kind zum ersten Mal gelacht hat?</p>
<p>Wahrscheinlich ja — denn dieser Moment hat sich in Ihr Gedächtnis eingebrannt. Aber was ist mit drei Monaten später, als es zum ersten Mal in die Hände geklatscht hat? Oder dem Tag, an dem es zum ersten Mal „Nein" gesagt hat?</p>
<p>Diese Momente verblassen. Nicht alle, aber die meisten.</p>
<h2>Fotos reichen nicht aus</h2>
<p>Auf Ihrem Telefon befinden sich wahrscheinlich Tausende von Fotos. Aber ein Foto fängt nur einen Moment ein — nicht die Geschichte dahinter. „Wo waren Sie auf diesem Foto? Was ist an diesem Tag passiert? Warum sehen Sie so glücklich aus?"</p>
<p>In ein paar Jahren, wenn Sie sich diese Fragen stellen, werden die Antworten nicht immer da sein.</p>
<h2>Kontext vervollständigt die Erinnerung</h2>
<p>„14. März 2025, 9:42 Uhr — Als Papa nach draußen ging, weinte sie, schaute dann aus dem Fenster und beruhigte sich."</p>
<p>Das ist ein Satz. Aber dieser Satz bewahrt diesen Moment für immer. Selbst wenn Sie kein Foto machen oder kein Video aufnehmen können, bewahren Worte den Moment.</p>
<h2>Wenn Ihr Kind aufwächst</h2>
<p>Stellen Sie sich vor: Wenn Ihr Kind 20 Jahre alt wird, wie wird es sich an seine frühen Jahre erinnern? Von alleine wird es sich an nichts erinnern. Aber wenn Sie Aufzeichnungen geführt haben — Notizen, Daten, kleine Momente — helfen diese Aufzeichnungen ihm, seine eigene Geschichte zu verstehen.</p>
<p>Deshalb haben wir Momena gebaut. Um Momente festzuhalten, zu organisieren und zu bewahren. Vollständig privat, vollständig Ihres.</p>""",
        },
        "tr": {
            "title": "Ailenizin Hikayesini Neden Kaydetmelisiniz? – Momena",
            "meta": "Fotoğraf bir anı yakalar, arkasındaki hikayeyi değil. Bağlamın neden önemli olduğu ve Momena’nın anıları nasıl gizli tuttuğu.",
            "canonical": "https://momena.app/tr/blog/capture-your-family-story.html",
            "headline": "Ailenizin Hikayesini Neden Kaydetmelisiniz?",
            "badge_class": "blog-card__badge--family-tips",
            "badge": "Ebeveynlik",
            "date": "12 Nisan 2026",
            "read": "3 dk okuma",
            "hero_alt": "Doğada ahşap köprüde birlikte gülümseyen çok nesilli bir aile.",
            "body": """<p>Bir soru soralım: Çocuğunuzun ilk güldüğü günü hatırlıyor musunuz?</p>
<p>Muhtemelen evet — çünkü o gün aklınıza kazındı. Peki ya üç ay sonra ilk kez ellerini birbirine vurduğu anı? Ya da ilk kez "hayır" dediği günü?</p>
<p>Bunlar kaybolur. Hepsi değil, ama çoğu.</p>
<h2>Fotoğraf Yetmez</h2>
<p>Telefonunuzda binlerce fotoğraf var muhtemelen. Ama fotoğraf sadece bir an yakalar — arkasındaki hikayeyi değil. "Bu fotoğrafta neredeydiniz? O gün ne olmuştu? Neden bu kadar mutlu görünüyorsunuz?"</p>
<p>Birkaç yıl sonra bu soruları kendinize sorduğunuzda cevap her zaman hazır olmaz.</p>
<h2>Bağlam Anıyı Tamamlar</h2>
<p>"14 Mart 2025, 09.42 — Baba ilk kez dışarı çıkınca ağladı, sonra pencereden bakıp sakinleşti."</p>
<p>Bu bir cümle. Ama bu cümle o anı sonsuza kadar yakalar. Fotoğraf çekemediğiniz, video kaydedemediğiniz anlarda bile yazı o anı korur.</p>
<h2>Çocuğunuz Büyüdüğünde</h2>
<p>Düşünün: Çocuğunuz 20 yaşına geldiğinde, ilk yıllarını nasıl hatırlayacak? Kendi başına hiçbir şey hatırlamayacak. Ama sizin tuttuğunuz kayıtlar varsa — notlar, tarihleri, küçük anlar — o kayıtlar onun kendi hikayesini anlamasına yardımcı olur.</p>
<p>Bu yüzden Momena'yı yaptık. Anları kaydetmek, düzenlemek ve korumak için. Tamamen gizli, tamamen sizin.</p>""",
        },
    },
    "where-child-data-lives": {
        "de": {
            "title": "Wo leben die Daten Ihres Kindes wirklich? – Momena",
            "meta": "Die meisten Baby-Apps laden Daten standardmäßig in die Cloud. Was das bedeutet – und warum Momena Gesundheitsdaten auf Ihrem Gerät lässt.",
            "canonical": "https://momena.app/de/blog/where-child-data-lives.html",
            "headline": "Wo leben die Daten Ihres Kindes wirklich?",
            "badge_class": "blog-card__badge--privacy-philosophy",
            "badge": "Datenschutz",
            "date": "12. April 2026",
            "read": "4 Min. Lesezeit",
            "hero_alt": "Buchstabenplättchen bilden die Wörter Family Activities auf grauem Stoff.",
            "body": """<p>Sie haben eine beliebte Baby-Tracking-App heruntergeladen. Sie erfassen den Schlafrhythmus, Fütterungszeiten, Größe und Gewicht Ihres Kindes. Die App funktioniert hervorragend.</p>
<p>Aber wo sind diese Daten?</p>
<h2>Die meisten Apps laden standardmäßig hoch</h2>
<p>Die überwiegende Mehrheit der großen App-Unternehmen lädt Ihre Daten auf ihre eigenen Cloud-Server hoch. Das erwähnen sie meist tief in der Datenschutzrichtlinie — wo niemand liest.</p>
<p>Was bedeutet das?</p>
<ul>
<li>Die Wachstumsdaten Ihres Kindes liegen auf einem Server irgendwo</li>
<li>Ihre Schlafprotokolle werden analysiert</li>
<li>Einige Apps teilen diese Daten mit Dritten — Werbenetzwerke, Forschungsunternehmen</li>
</ul>
<p>Die Gesundheitsdaten Ihres Kindes. Für Werbezwecke.</p>
<h2>Reicht „Anonym"?</h2>
<p>Manche Unternehmen sagen „Ihre Daten werden anonymisiert." Aber Forschungen zeigen, dass „anonyme" Datensätze viel einfacher re-identifiziert werden können als Sie denken — besonders wenn Geburtsdatum, Standort und Wachstumsdaten kombiniert werden.</p>
<h2>Was macht Momena anders?</h2>
<p>In Momena <strong>bleiben Ihre Daten standardmäßig auf Ihrem Gerät.</strong> Nichts wird automatisch in die Cloud gesendet.</p>
<ul>
<li>Geschützt mit AES-256-Verschlüsselung</li>
<li>Kein Tracking, keine Analysen</li>
<li>Keine Werbenetzwerke</li>
<li>Wir sehen, teilen oder verkaufen Ihre Daten nicht</li>
</ul>
<p>Wenn Sie iCloud Backup aktivieren (mit Familya Plus), gehen Ihre Backups verschlüsselt auf Ihr eigenes iCloud-Konto — nicht auf unsere Server.</p>
<h2>Warum ist das wichtig?</h2>
<p>Weil die Gesundheits- und Entwicklungsdaten Ihres Kindes sensible Informationen sind. Sie haben das Recht zu wissen, wo sie liegen und wer darauf zugreifen kann.</p>
<p>Momena bezieht eine klare Position: <strong>Ihre Daten, auf Ihrem Gerät.</strong></p>""",
        },
        "tr": {
            "title": "Çocuğunuzun Verileri Nerede Saklıyor? – Momena",
            "meta": "Çoğu bebek uygulaması verileri varsayılan olarak buluta yükler. Bu ne anlama geliyor ve Momena sağlık verilerini cihazınızda nasıl tutuyor?",
            "canonical": "https://momena.app/tr/blog/where-child-data-lives.html",
            "headline": "Çocuğunuzun Verileri Nerede Saklıyor?",
            "badge_class": "blog-card__badge--privacy-philosophy",
            "badge": "Gizlilik",
            "date": "12 Nisan 2026",
            "read": "4 dk okuma",
            "hero_alt": "Gri kumaş üzerinde Family Activities yazan harf plakaları.",
            "body": """<p>Popüler bir bebek takip uygulaması indirdiniz. Çocuğunuzun uyku düzenini, beslenme saatlerini, boy ve kilosunu giriyorsunuz. Uygulama harika çalışıyor.</p>
<p>Peki bu veriler nerede?</p>
<h2>Çoğu Uygulama Varsayılan Olarak Yükler</h2>
<p>Büyük uygulama şirketlerinin büyük çoğunluğu, verilerinizi kendi bulut sunucularına yükler. Bunu genellikle gizlilik politikasının derinliklerinde belirtirler — kimsenin okumadığı yerde.</p>
<p>Bu ne anlama gelir?</p>
<ul>
<li>Çocuğunuzun büyüme verileri bir sunucuda duruyor</li>
<li>Uyku düzeni kayıtlarınız analiz ediliyor</li>
<li>Bazı uygulamalar bu verileri üçüncü taraflarla paylaşıyor — reklam ağları, araştırma şirketleri</li>
</ul>
<p>Çocuğunuzun sağlık verisi. Reklam amacıyla.</p>
<h2>"Anonim" Yeterli mi?</h2>
<p>Bazı şirketler "verileriniz anonimleştirilir" der. Ama araştırmalar gösteriyor ki "anonim" veri seti düşündüğünüzden çok daha kolay yeniden tanımlanabiliyor — özellikle doğum tarihi, konum ve büyüme verisi bir arada olunca.</p>
<h2>Momena Farklı Nedir?</h2>
<p>Momena'da verileriniz <strong>varsayılan olarak cihazınızda kalır.</strong> Hiçbir şey otomatik olarak buluta gönderilmez.</p>
<ul>
<li>AES-256 şifreleme ile korunur</li>
<li>İzleme yok, analitik yok</li>
<li>Reklam ağları yok</li>
<li>Verilerinizi görmüyoruz, paylaşmıyoruz, satmıyoruz</li>
</ul>
<p>iCloud Yedekleme özelliğini (Familya Plus ile) etkinleştirirseniz, yedekleriniz şifreli olarak kendi iCloud hesabınıza gider — bizim sunucularımıza değil.</p>
<h2>Bu Neden Önemli?</h2>
<p>Çünkü çocuğunuzun sağlık ve gelişim verileri hassas bilgidir. Bu verilerin nerede durduğunu, kimin erişebildiğini bilmek hakkınızdır.</p>
<p>Momena bu konuda net bir tutum alıyor: <strong>Sizin veriniz, sizin cihazınızda.</strong></p>""",
        },
    },
    "what-is-momena": {
        "de": {
            "title": "Was ist Momena? Warum haben wir es gebaut? – Momena",
            "meta": "Erinnerungen, Gesundheit und Meilensteine an einem Ort — lokal, verschlüsselt und so gebaut, dass Eltern immer wissen, wo Daten liegen.",
            "canonical": "https://momena.app/de/blog/what-is-momena.html",
            "headline": "Was ist Momena? Warum haben wir es gebaut?",
            "badge_class": "blog-card__badge--product-updates",
            "badge": "Produkt",
            "date": "12. April 2026",
            "read": "4 Min. Lesezeit",
            "hero_alt": "Ein Neugeborenes wird behutsam über einer medizinischen Waage gehalten.",
            "body": """<p>Jede App beginnt mit einer Frage. Momenas Frage war: Gibt es einen Ort, an dem Sie die wertvollsten Momente Ihrer Familie sicher aufbewahren können — einen Ort, der wirklich Ihnen gehört?</p>
<p>Die Antwort war nein. Also haben wir ihn gebaut.</p>
<h2>Das Problem: Alles ist verstreut</h2>
<p>Denken Sie an den Tag, an dem Ihr Kind geboren wurde. Fotos auf dem Telefon, Arztnotizen auf Papier, der Impfplan in einer separaten App und Erinnerungen nur in Ihrem Kopf. Nichts ist an einem Ort.</p>
<p>Mit dem Wachstum wächst das Chaos. Eine App für Größe und Gewicht, eine andere für Schlaf, eine andere für den Kalender. Jede mit eigenem Konto, eigenem Login, eigener Datenschutzrichtlinie.</p>
<p>Und die meisten dieser Apps laden Ihre Daten auf ihre Server hoch.</p>
<h2>Die Lösung: Alles in einem, vollständig privat</h2>
<p>Beim Entwurf von Momena haben wir ein Prinzip festgelegt: <strong>Eltern sollten sich keine Gedanken darüber machen müssen, wo ihre Daten sind.</strong></p>
<p>Jede Entscheidung kam aus diesem Prinzip:</p>
<p><strong>Lokale Speicherung:</strong> Ihre Daten bleiben standardmäßig auf Ihrem Gerät. Kein automatischer Cloud-Upload.</p>
<p><strong>Verschlüsselung:</strong> Sensible Daten werden mit AES-256 geschützt. Selbst wir können sie nicht sehen.</p>
<p><strong>Alles in einem:</strong> Erinnerungen, Gesundheitsverfolgung, Entwicklungsmeilensteine, Kalender — in einer einzigen App, einer einzigen Oberfläche.</p>
<p><strong>Keine Werbung:</strong> Wir verwenden Ihre Daten nicht für Werbezwecke. Niemals.</p>
<h2>Was können Sie tun?</h2>
<ul>
<li>Familienerinnerungen mit Fotos und Videos erstellen</li>
<li>Größe, Gewicht, Schlaf und Symptome verfolgen</li>
<li>Die Wachstumskurve basierend auf WHO-Daten verfolgen</li>
<li>50 Meilensteine basierend auf dem Alter Ihres Kindes verfolgen</li>
<li>Wichtige Familienereignisse im Kalender hinzufügen</li>
<li>Daten verschlüsselt sichern</li>
</ul>
<h2>Wir bauen weiter</h2>
<p>Momena entwickelt sich noch weiter. Alle zwei Wochen veröffentlichen wir eine neue Version. Artikel, tiefere Entwicklungsverfolgung, intelligentere Erinnerungen — alles kommt.</p>
<p>Aber das Fundament wird sich nicht ändern: <strong>Ihre Daten, auf Ihrem Gerät, vollständig unter Ihrer Kontrolle.</strong></p>""",
        },
        "tr": {
            "title": "Momena Nedir? Neden Yaptık? – Momena",
            "meta": "Anılar, sağlık takibi ve kilometre taşları tek yerde — yerel, şifreli ve ebeveynlerin verinin nerede olduğunu bilmesi için tasarlandı.",
            "canonical": "https://momena.app/tr/blog/what-is-momena.html",
            "headline": "Momena Nedir? Neden Yaptık?",
            "badge_class": "blog-card__badge--product-updates",
            "badge": "Ürün",
            "date": "12 Nisan 2026",
            "read": "4 dk okuma",
            "hero_alt": "Klinik ortamında tıbbi bir tartının üzerinde nazikçe tutulan yenidoğan bebek.",
            "body": """<p>Her uygulama bir sorudan doğar. Momena'nın sorusu şuydu: Ailenizin en değerli anlarını güvenle saklayabileceğiniz, tamamen size ait bir yer var mı?</p>
<p>Cevap "hayır"dı. Bu yüzden yaptık.</p>
<h2>Sorun: Her Şey Dağınık</h2>
<p>Çocuğunuzun doğduğu gün düşünün. Fotoğraflar telefonda, doktor notları kağıtta, aşı takvimi ayrı bir uygulamada, anılar ise sadece kafanızda. Hiçbir şey bir arada değil.</p>
<p>Büyüdükçe bu dağınıklık artıyor. Boy-kilo takibi için bir uygulama, uyku için başka bir uygulama, takvim için başka bir uygulama. Her biri ayrı bir hesap, ayrı bir giriş, ayrı bir veri politikası.</p>
<p>Ve bu uygulamaların çoğu verilerinizi sunucularına yüklüyor.</p>
<h2>Çözüm: Hepsi Bir Arada, Tamamen Gizli</h2>
<p>Momena'yı tasarlarken tek bir ilke belirledik: <strong>Ebeveynler verilerinin nerede olduğunu merak etmemeli.</strong></p>
<p>Bu ilkeden her karar çıktı:</p>
<p><strong>Yerel depolama:</strong> Verileriniz varsayılan olarak cihazınızda. Buluta otomatik gönderim yok.</p>
<p><strong>Şifreleme:</strong> Hassas veriler AES-256 ile şifrelenir. Biz de göremeyiz.</p>
<p><strong>Hepsi bir arada:</strong> Anılar, sağlık takibi, gelişim kilometre taşları, takvim — tek bir uygulamada, tek bir arayüzde.</p>
<p><strong>Reklam yok:</strong> Verilerinizi reklam amacıyla kullanmıyoruz. Hiçbir zaman.</p>
<h2>Neler Yapabilirsiniz?</h2>
<ul>
<li>Fotoğraf ve videolarla aile anıları oluşturun</li>
<li>Boy, kilo, uyku, semptom takip edin</li>
<li>WHO verilerine dayanan büyüme eğrisini izleyin</li>
<li>50 kilometre taşını çocuğunuzun yaşına göre takip edin</li>
<li>Önemli aile etkinliklerini takvime ekleyin</li>
<li>Verilerinizi şifreli olarak yedekleyin</li>
</ul>
<h2>Devam Ediyoruz</h2>
<p>Momena hâlâ gelişiyor. Her iki haftada bir yeni sürüm yayınlıyoruz. Makaleler, daha derin gelişim takibi, daha akıllı hatırlatıcılar — hepsi geliyor.</p>
<p>Ama temel değişmeyecek: <strong>Sizin veriniz, sizin cihazınızda, tamamen sizin kontrolünüzde.</strong></p>""",
        },
    },
    "read-child-growth-chart": {
        "de": {
            "title": "Wie liest man die Wachstumskurve Ihres Kindes? – Momena",
            "meta": "Perzentile, WHO-Wachstumsstandards und warum der Verlauf über Zeit wichtiger ist als ein einzelner Messwert.",
            "canonical": "https://momena.app/de/blog/read-child-growth-chart.html",
            "headline": "Wie liest man die Wachstumskurve Ihres Kindes?",
            "badge_class": "blog-card__badge--child-development",
            "badge": "Elternschaft",
            "date": "12. April 2026",
            "read": "4 Min. Lesezeit",
            "hero_alt": "Ein Neugeborenes wird behutsam über einer digitalen medizinischen Waage gehalten.",
            "body": """<p>Sie haben die Arztpraxis mit einem Zettel verlassen: „Ihr Kind liegt beim Gewicht auf der 45. Perzentile und bei der Körpergröße auf der 60." Was bedeutet das? Sollten Sie sich Sorgen machen?</p>
<h2>Was ist eine Perzentile?</h2>
<p>Eine Perzentile zeigt, wie Ihr Kind im Vergleich zu anderen Kindern desselben Alters und Geschlechts dasteht. Auf der 60. Perzentile zu liegen bedeutet, dass 59 von 100 Kindern kleiner und 40 größer sind.</p>
<p>Der entscheidende Punkt: <strong>Die 50. Perzentile ist nicht „ideal".</strong> Jeder Wert zwischen der 3. und 97. Perzentile gilt als normal.</p>
<h2>WHO-Wachstumsstandards</h2>
<p>Die Weltgesundheitsorganisation (WHO) untersuchte mehr als 8.000 Kinder aus 6 Ländern, um internationale Wachstumsstandards zu entwickeln. Diese Standards sind unabhängig von Rasse oder Geographie — sie beschreiben, wie gesunde Kinder unter optimalen Bedingungen wachsen.</p>
<p>Die WHO-Wachstumskurve hat 5 Hauptbereiche:</p>
<ul>
<li><strong>Unter der 3. Perzentile:</strong> Konsultieren Sie Ihren Arzt</li>
<li><strong>3. – 15. Perzentile:</strong> Niedriger Bereich, beobachten</li>
<li><strong>15. – 85. Perzentile:</strong> Normaler Bereich</li>
<li><strong>85. – 97. Perzentile:</strong> Hoher Bereich, beobachten</li>
<li><strong>Über der 97. Perzentile:</strong> Konsultieren Sie Ihren Arzt</li>
</ul>
<h2>Die Kurve ist wichtiger als ein einzelner Messwert</h2>
<p>Die beste Methode, das Wachstum eines Kindes zu beurteilen, ist nicht ein einzelner Datenpunkt, sondern die Entwicklung über die Zeit. Wenn Ihr Kind konstant auf der 30. Perzentile liegt, ist das völlig normal. Aber ein Abfall von der 70. auf die 20. Perzentile innerhalb weniger Monate ist ein Signal, das untersucht werden sollte.</p>
<p>Deshalb ist <strong>regelmäßiges Messen entscheidend:</strong></p>
<ul>
<li>0–6 Monate: Monatlich</li>
<li>6–12 Monate: Alle 45 Tage</li>
<li>1–2 Jahre: Alle 3 Monate</li>
<li>2–5 Jahre: Alle 6 Monate</li>
</ul>
<h2>Wachstumsverfolgung in Momena</h2>
<p>Wenn Sie in Momena Größe und Gewicht eingeben, vergleicht die App diese automatisch mit der WHO-Wachstumskurve. Sie sehen, auf welcher Perzentile Ihr Kind liegt, und können die Entwicklung von der Geburt bis zum 60. Monat verfolgen.</p>
<p>Wenn Sie längere Zeit keine Messung eingetragen haben, erinnert Sie die App — mit einem dynamischen Intervall je nach Alter Ihres Kindes.</p>
<p><strong>Ihre Daten bleiben auf Ihrem Gerät. Sie werden niemals an einen Cloud-Server gesendet.</strong></p>""",
        },
        "tr": {
            "title": "Çocuğunuzun Büyüme Eğrisini Nasıl Yorumlarsınız? – Momena",
            "meta": "Yüzdelikler, WHO büyüme standartları ve tek ölçümden çok zaman içindeki eğrinin neden önemli olduğu.",
            "canonical": "https://momena.app/tr/blog/read-child-growth-chart.html",
            "headline": "Çocuğunuzun Büyüme Eğrisini Nasıl Yorumlarsınız?",
            "badge_class": "blog-card__badge--child-development",
            "badge": "Ebeveynlik",
            "date": "12 Nisan 2026",
            "read": "4 dk okuma",
            "hero_alt": "Hastanede dijital tıbbi tartının üzerinde nazikçe tutulan yenidoğan bebek.",
            "body": """<p>Doktor ziyaretinden çıktınızda elinizde bir kağıt var: "Çocuğunuz boy için 60. yüzdelikte, kilo için 45. yüzdelikte." Bu rakamlar ne anlama geliyor? Endişelenmeli misiniz?</p>
<h2>Yüzdelik Nedir?</h2>
<p>Yüzdelik (percentile), çocuğunuzun aynı yaş ve cinsiyetteki diğer çocuklarla nasıl karşılaştırıldığını gösterir. 60. yüzdelikte olmak, 100 çocuktan 59'unun daha kısa, 40'ının daha uzun olduğu anlamına gelir.</p>
<p>Önemli olan nokta şu: <strong>50. yüzdelik "ideal" değildir.</strong> 3. ile 97. yüzdelik arasındaki herhangi bir değer normal kabul edilir.</p>
<h2>WHO Büyüme Standartları</h2>
<p>Dünya Sağlık Örgütü (WHO), 6 farklı ülkeden 8.000'den fazla çocuğu inceleyerek uluslararası büyüme standartları oluşturdu. Bu standartlar ırk veya coğrafyadan bağımsız — optimal koşullarda büyüyen sağlıklı çocukların nasıl geliştiğini gösteriyor.</p>
<p>WHO büyüme eğrisi 5 ana bant içerir:</p>
<ul>
<li><strong>3. yüzdeliğin altı:</strong> Doktorunuzla görüşün</li>
<li><strong>3. – 15. yüzdelik:</strong> Düşük aralık, izlenmeli</li>
<li><strong>15. – 85. yüzdelik:</strong> Normal aralık</li>
<li><strong>85. – 97. yüzdelik:</strong> Yüksek aralık, izlenmeli</li>
<li><strong>97. yüzdeliğin üstü:</strong> Doktorunuzla görüşün</li>
</ul>
<h2>Tek Ölçümden Çok, Eğri Önemlidir</h2>
<p>Bir çocuğun büyümesini değerlendirmenin en doğru yolu tek bir noktaya bakmak değil, zaman içindeki eğriyi takip etmektir. Çocuğunuz tutarlı olarak 30. yüzdelikte gidiyorsa bu tamamen normaldir. Ama 70. yüzdelikten birkaç ayda 20. yüzdeliğe düşüş varsa bu bir sinyaldir.</p>
<p>Bu yüzden <strong>düzenli ölçüm kritiktir:</strong></p>
<ul>
<li>0–6 ay: Her ay</li>
<li>6–12 ay: Her 45 günde bir</li>
<li>1–2 yaş: Her 3 ayda bir</li>
<li>2–5 yaş: Her 6 ayda bir</li>
</ul>
<h2>Momena'da Büyüme Takibi</h2>
<p>Momena'da boy ve kilo ölçümlerinizi girdiğinizde, uygulama bunları WHO büyüme eğrisiyle otomatik olarak karşılaştırır. Çocuğunuzun hangi yüzdelikte olduğunu görür, eğriyi 0–60 ay boyunca izleyebilirsiniz.</p>
<p>Uzun süre ölçüm girmedinizse, uygulama sizi hatırlatır — çocuğunuzun yaşına göre dinamik bir aralıkta.</p>
<p><strong>Verileriniz cihazınızda kalır. Hiçbir bulut sunucusuna gönderilmez.</strong></p>""",
        },
    },
    "baby-health-tracking-what-to-record": {
        "de": {
            "title": "Baby-Gesundheitsverfolgung: Was Sie aufzeichnen sollten und wie oft – Momena",
            "meta": "Praktischer Leitfaden nach Alter: was Sie von der Geburt bis 5 Jahren protokollieren, warum Schlaf zählt und warum datierte Symptome beim Kinderarzt helfen.",
            "canonical": "https://momena.app/de/blog/baby-health-tracking-what-to-record.html",
            "headline": "Baby-Gesundheitsverfolgung: Was Sie aufzeichnen sollten und wie oft",
            "badge_class": "blog-card__badge--child-development",
            "badge": "Gesundheit",
            "date": "12. April 2026",
            "read": "5 Min. Lesezeit",
            "hero_alt": "Kinderärztin untersucht ein Baby mit einem Stethoskop in einer freundlichen Praxis.",
            "body": """<p>Als frischgebackene Eltern möchten Sie alles festhalten — und das sollten Sie auch. Aber was, wann und wie? Ohne ein System wird es schnell chaotisch.</p>
<p>Hier ist ein praktischer Leitfaden nach Altersgruppen.</p>
<h2>0–6 Monate: Die intensivste Phase</h2>
<p>Ihr Baby verändert sich in dieser Phase rasant. Arztbesuche sind häufig, Beobachtungen sind entscheidend.</p>
<p><strong>Monatlich aufzeichnen:</strong></p>
<ul>
<li>Körpergröße und Gewicht — zur Verfolgung der Wachstumskurve</li>
<li>Schlafdauer und -muster — bildet sich ein Tag-/Nachtrhythmus?</li>
<li>Fieber und Symptome — jedes Zeichen mit Datum</li>
</ul>
<p><strong>Warum das wichtig ist:</strong> Ihr Kinderarzt bewertet das Wachstum bei jedem Besuch. Mit Aufzeichnungen wird Ihr Termin viel produktiver. „Letzten Monat wog sie 5,2 kg, jetzt 6,1" ist sehr anders als „Ich glaube, sie hat etwas zugenommen."</p>
<h2>6–12 Monate: Beikost und Schlafwende</h2>
<p>Ihr Baby beginnt, die Welt zu erkunden, Schlafmuster festigen sich, und die ersten Zähne erscheinen.</p>
<p><strong>Alle 45 Tage aufzeichnen:</strong></p>
<ul>
<li>Größe und Gewicht</li>
<li>Schlafstunden — nimmt der Tagesschlaf ab?</li>
<li>Neue Symptome — Zahnen, erste Erkältung</li>
</ul>
<p><strong>Achten Sie auf:</strong> Beikost beginnt normalerweise um den 6. Monat. Die Gewichtszunahme kann sich in dieser Phase verlangsamen — das ist normal. Bei großen Abweichungen von der Wachstumskurve sollten Sie Ihren Arzt aufsuchen.</p>
<h2>1–2 Jahre: Beweglichkeit und Unabhängigkeit</h2>
<p>Laufen, alles anfassen, alles in den Mund stecken.</p>
<p><strong>Alle 3 Monate aufzeichnen:</strong></p>
<ul>
<li>Größe und Gewicht</li>
<li>Schlafmuster — wie viele Stunden schläft das Kind nachts?</li>
<li>Wiederkehrende Symptome — Ohrenschmerzen, Allergiezeichen</li>
</ul>
<h2>2–5 Jahre: Routinemäßige Überwachung</h2>
<p>Das Wachstum verlangsamt sich, aber hören Sie nicht auf, es zu verfolgen.</p>
<p><strong>Alle 6 Monate aufzeichnen:</strong></p>
<ul>
<li>Größe und Gewicht</li>
<li>Schlafstunden</li>
<li>Saisonale Symptome</li>
</ul>
<h2>Warum ist Schlafverfolgung so wichtig?</h2>
<p>Schlaf ist entscheidend für die Gehirnentwicklung. Bei Kindern von 0–3 Jahren können Schlafmuster ein Indikator für die neurologische Entwicklung sein. Verfolgen Sie „wie oft sind sie letzte Nacht aufgewacht?" bevor Ihr Arzt überhaupt fragt.</p>
<p>In Momena können Sie jede Schlafsitzung mit dem Schlaf-Timer aufzeichnen und Muster in Diagrammen sehen. Live-Activity-Unterstützung ist für iOS 16.1 und später verfügbar.</p>
<h2>Praktischer Tipp: Symptome mit Datum aufzeichnen</h2>
<p>„Sie hatten letzte Woche Fieber" ist sehr anders als „38,2 °C am 14. März" — und dieser Unterschied ist wichtig für die Diagnose Ihres Arztes. In Momena enthalten Symptomeinträge sowohl Datum als auch Wert, sodass Sie jederzeit zurückblicken können.</p>
<p><strong>Alle Ihre Daten werden verschlüsselt und nur auf Ihrem Gerät gespeichert.</strong></p>""",
        },
        "tr": {
            "title": "Bebek Sağlık Takibi: Neyi, Ne Sıklıkla Kaydetmelisiniz? – Momena",
            "meta": "Yaşa göre pratik rehber: doğumdan 5 yaşa kadar neyi kaydetmeli, uyku neden önemli ve tarihli semptomlar pediatriste nasıl yardımcı olur.",
            "canonical": "https://momena.app/tr/blog/baby-health-tracking-what-to-record.html",
            "headline": "Bebek Sağlık Takibi: Neyi, Ne Sıklıkla Kaydetmelisiniz?",
            "badge_class": "blog-card__badge--child-development",
            "badge": "Sağlık",
            "date": "12 Nisan 2026",
            "read": "5 dk okuma",
            "hero_alt": "Aydınlık muayene odasında stetoskopla bebeğini muayene eden çocuk doktoru.",
            "body": """<p>Yeni ebeveyn olduğunuzda her şeyi kaydetmek istersiniz — ve kaydetmelisiniz. Ama neyi, ne zaman, nasıl? Bir sistem olmadan bu kaos haline gelir.</p>
<p>İşte yaşa göre pratik bir rehber.</p>
<h2>0–6 Ay: En Yoğun Dönem</h2>
<p>Bu dönemde bebeğiniz hızla değişir. Doktor ziyaretleri sık, gözlemler kritiktir.</p>
<p><strong>Her ay kaydetmeniz gerekenler:</strong></p>
<ul>
<li>Boy ve kilo — büyüme eğrisini takip için</li>
<li>Uyku süresi ve düzeni — gece/gündüz ayrımı oluşuyor mu?</li>
<li>Ateş ve semptomlar — her belirti tarihiyle birlikte</li>
</ul>
<p><strong>Neden önemli?</strong> Pediatristiniz her ziyarette büyümeyi değerlendirir. Elinizde kayıt varsa doktorunuzla çok daha verimli bir görüşme yaparsınız. "Geçen ay 5,2 kg'dı, şimdi 6,1" demek ile "sanırım biraz arttı" demek arasındaki fark büyük.</p>
<h2>6–12 Ay: Katı Gıda ve Uyku Dönüşümü</h2>
<p>Bu dönem bebeğinizin dünyayı keşfetmeye başladığı, uyku düzeninin oturduğu ve ilk dişlerin çıktığı dönemdir.</p>
<p><strong>Her 45 günde bir kaydetmeniz gerekenler:</strong></p>
<ul>
<li>Boy ve kilo</li>
<li>Uyku saatleri — gündüz uykusu azalıyor mu?</li>
<li>Yeni semptomlar — diş çıkarma, ilk soğuk algınlığı</li>
</ul>
<p><strong>Dikkat edilmesi gereken:</strong> Katı gıdaya geçiş genellikle 6. ayda başlar. Bu dönemde kilo artışı yavaşlayabilir — bu normal. Ama büyüme eğrisinden büyük sapma varsa doktorunuza danışın.</p>
<h2>1–2 Yaş: Hareketlilik ve Bağımsızlık</h2>
<p>Yürümeye başlayan, her şeye dokunan, her şeyi ağzına götüren dönem.</p>
<p><strong>Her 3 ayda bir kaydetmeniz gerekenler:</strong></p>
<ul>
<li>Boy ve kilo</li>
<li>Uyku düzeni — gece uykusu kaç saat?</li>
<li>Tekrarlayan semptomlar — kulak ağrısı, alerji belirtileri</li>
</ul>
<h2>2–5 Yaş: Rutin Takip</h2>
<p>Bu dönemde büyüme yavaşlar, ama izlemeyi bırakmayın.</p>
<p><strong>Her 6 ayda bir kaydetmeniz gerekenler:</strong></p>
<ul>
<li>Boy ve kilo</li>
<li>Uyku saatleri</li>
<li>Mevsimsel semptomlar</li>
</ul>
<h2>Uyku Takibi Neden Bu Kadar Önemli?</h2>
<p>Uyku, beyin gelişimi için kritiktir. 0–3 yaş arasındaki çocuklarda uyku örüntüleri nörolojik gelişimin göstergesi olabilir. "Geceleri kaç kez uyandı?" sorusunu doktorunuz sormadan siz kendiniz takip edin.</p>
<p>Momena'da uyku zamanlayıcısı ile her uyku seansını kaydedebilir, grafiklerde düzeni görebilirsiniz. iOS 16.1 ve sonrası için Canlı Aktivite desteği de mevcut — kilidi açmadan ekranınızdan takip edin.</p>
<h2>Pratik İpucu: Semptomu Tarihiyle Kaydedin</h2>
<p>"Geçen hafta ateşi vardı" yerine "14 Mart'ta 38.2 derece ateş" — bu fark doktorunuzun teşhisini kolaylaştırır. Momena'da semptom kaydı yaparken tarih ve değer birlikte girilir, böylece geçmişe her zaman bakabilirsiniz.</p>
<p><strong>Tüm verileriniz şifreli olarak yalnızca cihazınızda saklanır.</strong></p>""",
        },
    },
    "tracking-child-milestones": {
        "de": {
            "title": "Warum die Meilensteine Ihres Kindes zu verfolgen wichtig ist – Momena",
            "meta": "Was Meilensteine sind, was die WHO zu Grobmotorik sagt und wie Momena 1.5 hilft, Daten und Notizen privat auf dem Gerät zu speichern.",
            "canonical": "https://momena.app/de/blog/tracking-child-milestones.html",
            "headline": "Warum die Meilensteine Ihres Kindes zu verfolgen wichtig ist",
            "badge_class": "blog-card__badge--child-development",
            "badge": "Entwicklung",
            "date": "12. April 2026",
            "read": "4 Min. Lesezeit",
            "hero_alt": "Kleinkind macht am Strand mit Hilfe eines Erwachsenen die ersten Schritte.",
            "body": """<p>Das erste Lächeln. Das erste Wort. Der erste Schritt. Diese Momente sind nicht nur emotional bedeutsam — sie sind wichtige Indikatoren für die Entwicklung Ihres Kindes.</p>
<p>Aber die meisten Eltern lassen diese Momente vergehen, indem sie sich auf ihr Gedächtnis verlassen. „Ich glaube, es war ungefähr im 10. Monat" oder „Ich kann mich nicht genau erinnern." Dabei können diese Informationen sowohl für Eltern als auch für Ärzte entscheidend sein.</p>
<h2>Was ist ein Meilenstein?</h2>
<p>Meilensteine sind Fähigkeiten, die Kinder in bestimmten Altersbereichen erwerben. Sie fallen in vier Hauptkategorien:</p>
<p><strong>Grobmotorik:</strong> Sitzen, Krabbeln, Laufen, Hüpfen<br />
<strong>Feinmotorik:</strong> Pinzettengriff, Löffel benutzen, Zeichnen<br />
<strong>Sprache:</strong> Gurren, Plappern, erstes Wort, Sätze<br />
<strong>Kognition:</strong> Objektpermanenz, Farben erkennen, Zählen</p>
<p>Und zwei Kategorien, die oft übersehen werden: <strong>soziale Entwicklung</strong> (Fremdeln, Teilen) und <strong>Ernährung</strong> (Beikost, Entwöhnung von der Flasche).</p>
<h2>Was sagt die WHO?</h2>
<p>Die Weltgesundheitsorganisation hat offizielle Daten zu 6 wichtigen grobmotorischen Meilensteinen veröffentlicht. Diese Daten zeigen, wann gesunde Kinder diese Fähigkeiten typischerweise in drei Phasen erwerben: <strong>frühestens</strong>, <strong>typisch</strong> und <strong>spätestens</strong>.</p>
<p>Beim alleinigen Laufen zum Beispiel:</p>
<ul>
<li>Frühestens: 8. Monat</li>
<li>Typisch: 12. Monat</li>
<li>Spätestens: 18. Monat</li>
</ul>
<p>Wenn ein Kind mit 18 Monaten noch nicht laufen kann — das ist ein Signal, einen Arzt aufzusuchen. Aber für ein Kind, das mit 14 Monaten noch nicht läuft, besteht noch kein Grund zur Sorge.</p>
<h2>Ist „Früh" immer gut?</h2>
<p>Nein — und das ist ein wichtiger Punkt. Wenn ein Kind einen Meilenstein wirklich früh erreicht (vor dem erwarteten Fenster), ist das wunderbar. Aber manche Eltern erzeugen unter dem Druck von „früh" unnötige Vergleiche.</p>
<p>Wenn ein Meilenstein in Momena eingetragen wird, zeigt die App:</p>
<ul>
<li>🌟 <strong>Früh</strong> — vor dem erwarteten Fenster</li>
<li>✓ <strong>Normal</strong> — innerhalb des erwarteten Fensters</li>
<li>⚠️ <strong>Spät</strong> — nach dem erwarteten Fenster (Arzt aufsuchen)</li>
</ul>
<h2>Warum Aufzeichnungen führen?</h2>
<p><strong>Für Arztbesuche:</strong> Ihr Kinderarzt wird fragen „wann hat er angefangen zu laufen?" Ein genaues Datum macht den Termin viel produktiver.</p>
<p><strong>Für Geschwister:</strong> Wenn Ihr zweites Kind kommt, können Sie mit dem ersten vergleichen — rein aus Neugier.</p>
<p><strong>Für Erinnerungen:</strong> „Ihr erstes Wort war nicht 'Mama', sondern 'Auto', gesagt mit 11 Monaten" — solche Details werden in späteren Jahren kostbar.</p>
<h2>Entwicklungsverfolgung in Momena 1.5</h2>
<p>In dieser Version haben wir <strong>50 Meilensteine</strong> basierend auf WHO- und AAP-Daten hinzugefügt. In den Kategorien Grobmotorik, Feinmotorik, Sprache, Kognition, Soziales und Ernährung.</p>
<p>Basierend auf dem Alter Ihres Kindes zeigt die App automatisch:</p>
<ul>
<li><strong>Überfällig</strong> — noch nicht erreicht, erwartetes Alter überschritten</li>
<li><strong>Aktuell</strong> — wird jetzt erwartet</li>
<li><strong>Demnächst</strong> — wird in den nächsten 4 Monaten erwartet</li>
<li><strong>Abgeschlossen</strong> — mit Datum und Notiz eingetragen</li>
</ul>
<p>Sie können jedem Meilenstein eine Notiz hinzufügen. Ein Detail wie „hat die ersten Schritte bei der Oma gemacht" wird Jahre später unbezahlbar.</p>
<p><strong>Alle Ihre Daten werden verschlüsselt und nur auf Ihrem Gerät gespeichert.</strong></p>""",
        },
        "tr": {
            "title": "Çocuğunuzun Kilometre Taşlarını Takip Etmek Neden Önemli? – Momena",
            "meta": "Kilometre taşları nedir, WHO kaba motor verileri ne diyor ve Momena 1.5 tarihleri ve notları cihazda nasıl tutuyor.",
            "canonical": "https://momena.app/tr/blog/tracking-child-milestones.html",
            "headline": "Çocuğunuzun Kilometre Taşlarını Takip Etmek Neden Önemli?",
            "badge_class": "blog-card__badge--child-development",
            "badge": "Gelişim",
            "date": "12 Nisan 2026",
            "read": "4 dk okuma",
            "hero_alt": "Sahilde bir yetişkinin yardımıyla ilk adımlarını atan küçük çocuk.",
            "body": """<p>İlk gülümseme. İlk söylenen kelime. İlk adım. Bu anlar sadece duygusal değil — aynı zamanda çocuğunuzun gelişiminin önemli göstergeleridir.</p>
<p>Ama çoğu ebeveyn bu anları hafızaya güvenerek geçirir. "Herhalde 10. aydaydı" ya da "tam olarak hatırlamıyorum." Oysa bu bilgiler hem ebeveyn hem de doktor için kritik olabilir.</p>
<h2>Kilometre Taşı Nedir?</h2>
<p>Kilometre taşları (milestones), çocukların belirli yaş aralıklarında kazandığı becerilerdir. Dört ana kategoride değerlendirilir:</p>
<p><strong>Kaba motor:</strong> Oturma, emekleme, yürüme, zıplama<br />
<strong>İnce motor:</strong> Pinse tutuş, kaşık kullanma, çizim<br />
<strong>Dil:</strong> Agulama, heceleme, ilk kelime, cümleler<br />
<strong>Bilişsel:</strong> Nesne kalıcılığı, renk tanıma, sayma</p>
<p>Bir de sıkça gözden kaçan kategoriler var: <strong>sosyal gelişim</strong> (yabancı kaygısı, paylaşma) ve <strong>beslenme</strong> (katı gıda, biberondan kesilme).</p>
<h2>WHO Neyi Söylüyor?</h2>
<p>Dünya Sağlık Örgütü 6 temel kaba motor kilometre taşı için resmi veriler yayımlamıştır. Bu veriler, sağlıklı çocukların bu becerileri ne zaman kazandığını üç aşamada gösterir: <strong>en erken</strong>, <strong>tipik</strong> ve <strong>en geç</strong>.</p>
<p>Örneğin yalnız yürüme için:</p>
<ul>
<li>En erken: 8. ay</li>
<li>Tipik: 12. ay</li>
<li>En geç: 18. ay</li>
</ul>
<p>18. ayda hâlâ yürüyemiyorsa — bu doktora başvurma sinyalidir. Ama 14. ayda yürüyemeyen bir çocuk için henüz endişelenmeye gerek yoktur.</p>
<h2>"Erken" Her Zaman İyi mi?</h2>
<p>Hayır — ve bu önemli bir nokta. Erken gerçekten erken ise (beklenen aralığın öncesinde) bu harika. Ama bazı ebeveynler "erken" baskısıyla çocuklar arasında gereksiz karşılaştırma yapar.</p>
<p>Momena'da bir kilometre taşı kaydedildiğinde uygulama şunları gösterir:</p>
<ul>
<li>🌟 <strong>Erken</strong> — beklenen aralığın öncesinde</li>
<li>✓ <strong>Normal</strong> — beklenen pencere içinde</li>
<li>⚠️ <strong>Geç</strong> — beklenen aralığın sonrasında (doktorla görüşün)</li>
</ul>
<h2>Neden Kayıt Tutmalısınız?</h2>
<p><strong>Doktor ziyaretleri için:</strong> Pediatristiniz gelişimi değerlendirirken "ne zaman yürümeye başladı?" diye sorar. Kesin bir tarih vermek muayeneyi çok daha verimli kılar.</p>
<p><strong>Kardeşler için:</strong> İkinci çocuğunuz olduğunda ilk çocuğunuzla karşılaştırma yapabilirsiniz — tamamen meraktan.</p>
<p><strong>Anılar için:</strong> "İlk kelimesi 'anne' değil 'araba'ydı, 11. ayda söyledi" — bu detaylar ilerleyen yıllarda çok değerli hale gelir.</p>
<h2>Momena 1.5 ile Gelişim Takibi</h2>
<p>Bu sürümde WHO ve Amerikan Pediatri Akademisi (AAP) verilerine dayanan <strong>50 kilometre taşı</strong> ekledik. Kaba motor, ince motor, dil, bilişsel, sosyal ve beslenme kategorilerinde.</p>
<p>Çocuğunuzun yaşına göre uygulama otomatik olarak şunları gösterir:</p>
<ul>
<li><strong>Gecikmiş</strong> — henüz kazanılmamış, beklenen yaş geçmiş</li>
<li><strong>Bu dönem</strong> — şu an kazanılması beklenen</li>
<li><strong>Yakında</strong> — önümüzdeki 4 ayda beklenen</li>
<li><strong>Tamamlanan</strong> — tarih ve notla birlikte kaydedilmiş</li>
</ul>
<p>Her kilometre taşı için bir not ekleyebilirsiniz. "İlk adımını büyükannesinin evinde attı" gibi bir detay, yıllar sonra çok değerli.</p>
<p><strong>Tüm verileriniz şifreli olarak yalnızca cihazınızda saklanır.</strong></p>""",
        },
    },
}


def replace_body(html: str, new_body: str) -> str:
    return re.sub(
        r'(<div class="blog-article-body"[^>]*>)(.*?)(</div>\s*</article>)',
        r"\1\n          " + new_body + r"\n        \3",
        html,
        count=1,
        flags=re.DOTALL,
    )


def fill_chrome(html: str, loc: str, slug: str) -> str:
    c = CHROME[loc]
    html = html.replace('<html lang="en">', f'<html lang="{c["html_lang"]}">')
    html = html.replace('aria-label="Primary"', f'aria-label="{c["nav_aria"]}"')
    html = html.replace('aria-label="Blog navigation"', f'aria-label="{c["blog_back_aria"]}"')
    html = html.replace(">Home<", f'>{c["nav_home"]}<')
    html = html.replace(">Pricing<", f'>{c["nav_pricing"]}<')
    html = html.replace(">Our story<", f'>{c["nav_story"]}<')
    html = re.sub(r'(<a href="\./">)Blog(</a>)', rf'\1{c["nav_blog"]}\2', html, count=1)
    html = html.replace(">Support<", f'>{c["nav_support"]}<')
    html = html.replace('aria-label="Download Momena on the App Store"', f'aria-label="{c["header_qr"]}"')
    html = html.replace(">App Download<", f'>{c["qr_label"]}<')
    html = html.replace(">← All posts<", f'>{c["back"]}<')
    html = re.sub(r'<h2 id="newsletter-heading">[^<]+</h2>', f'<h2 id="newsletter-heading">{c["newsletter_h"]}</h2>', html)
    html = re.sub(
        r'<p>New posts, product updates, and privacy notes — straight to your inbox\. No spam, ever\.</p>',
        f'<p>{c["newsletter_p"]}</p>',
        html,
        count=1,
    )
    html = re.sub(r'placeholder="Your email address"', f'placeholder="{c["placeholder"]}"', html, count=1)
    html = html.replace(">Subscribe<", f'>{c["subscribe"]}<', 1)
    html = html.replace(">No spam. Unsubscribe anytime.<", f'>{c["disclaimer"]}<', 1)
    html = html.replace("<h3>Navigate</h3>", f'<h3>{c["footer_nav_h"]}</h3>')
    html = html.replace("<h3>Legal</h3>", f'<h3>{c["footer_legal_h"]}</h3>')
    html = html.replace(">Privacy Policy<", f'>{c["privacy"]}<', 1)
    html = html.replace(">Terms of Service<", f'>{c["terms"]}<', 1)
    html = html.replace('id="footer-lang-label">Language<', f'id="footer-lang-label">{c["footer_lang"]}<')
    html = html.replace('aria-label="Cookie consent"', f'aria-label="{c["cookie_aria"]}"')
    html = re.sub(
        r'<p class="cookie-banner-text">We use cookies and local storage to remember your preferences\. By continuing, you accept our use of cookies\. ',
        f'<p class="cookie-banner-text">{c["cookie_p"]}',
        html,
        count=1,
    )
    html = html.replace(">Learn more<", f'>{c["learn"]}<', 1)
    html = html.replace(">Accept<", f'>{c["accept"]}<', 1)
    html = html.replace(">Reject<", f'>{c["reject"]}<', 1)
    html = re.sub(r'(<a href="../#cookies-policy" class="cookie-link">)[^<]+(</a>)', rf'\1{c["cookie_link"]}\2', html, count=1)
    html = html.replace(
        '<a href="../#cookies-policy">Cookie Policy</a>',
        f'<a href="../#cookies-policy">{c["footer_cookie_policy"]}</a>',
        1,
    )
    html = html.replace(
        '<a href="#" id="cookie-prefs">Cookie preferences</a>',
        f'<a href="#" id="cookie-prefs">{c["footer_cookie_prefs"]}</a>',
        1,
    )

    en = f"https://momena.app/blog/{slug}.html"
    de = f"https://momena.app/de/blog/{slug}.html"
    tr = f"https://momena.app/tr/blog/{slug}.html"
    if loc == "de":
        lang_block = f"""            <ul class="lang-select-list" role="list">
              <li><a class="lang-select-link" href="../../blog/{slug}.html" hreflang="en"><span class="lang-flag" aria-hidden="true">🇬🇧</span> English</a></li>
              <li><a class="lang-select-link" href="./{slug}.html" hreflang="de" aria-current="page"><span class="lang-flag" aria-hidden="true">🇩🇪</span> Deutsch</a></li>
              <li><a class="lang-select-link" href="../../tr/blog/{slug}.html" hreflang="tr"><span class="lang-flag" aria-hidden="true">🇹🇷</span> Türkçe</a></li>
            </ul>"""
    else:
        lang_block = f"""            <ul class="lang-select-list" role="list">
              <li><a class="lang-select-link" href="../../blog/{slug}.html" hreflang="en"><span class="lang-flag" aria-hidden="true">🇬🇧</span> English</a></li>
              <li><a class="lang-select-link" href="../../de/blog/{slug}.html" hreflang="de"><span class="lang-flag" aria-hidden="true">🇩🇪</span> Deutsch</a></li>
              <li><a class="lang-select-link" href="./{slug}.html" hreflang="tr" aria-current="page"><span class="lang-flag" aria-hidden="true">🇹🇷</span> Türkçe</a></li>
            </ul>"""
    html = re.sub(
        r'<ul class="lang-select-list" role="list">.*?</ul>',
        lang_block,
        html,
        count=1,
        flags=re.DOTALL,
    )
    # Summary line for lang dropdown (optional - keep flag from current)
    if loc == "de":
        html = re.sub(
            r'<summary class="lang-select-summary">\s*<span class="lang-flag"[^>]*>[^<]+</span>\s*<span>[^<]+</span>',
            '<summary class="lang-select-summary">\n              <span class="lang-flag" aria-hidden="true">🇩🇪</span>\n              <span>Deutsch</span>',
            html,
            count=1,
        )
    else:
        html = re.sub(
            r'<summary class="lang-select-summary">\s*<span class="lang-flag"[^>]*>[^<]+</span>\s*<span>[^<]+</span>',
            '<summary class="lang-select-summary">\n              <span class="lang-flag" aria-hidden="true">🇹🇷</span>\n              <span>Türkçe</span>',
            html,
            count=1,
        )
    return html


def localize_article(html: str, loc: str, slug: str, d: dict[str, str]) -> str:
    html = re.sub(r"<title>.*?</title>", f"<title>{d['title']}</title>", html, count=1)
    html = re.sub(
        r'<meta name="description" content="[^"]*"',
        f'<meta name="description" content="{d["meta"]}"',
        html,
        count=1,
    )
    html = re.sub(r'<link rel="canonical" href="[^"]*"', f'<link rel="canonical" href="{d["canonical"]}"', html, count=1)
    html = re.sub(r'<meta property="og:locale" content="[^"]*"', f'<meta property="og:locale" content="{CHROME[loc]["og_locale"]}"', html, count=1)
    html = re.sub(r'<meta property="og:title" content="[^"]*"', f'<meta property="og:title" content="{d["headline"]}"', html, count=1)
    html = re.sub(r'<meta property="og:description" content="[^"]*"', f'<meta property="og:description" content="{d["meta"]}"', html, count=1)
    html = re.sub(r'<meta property="og:url" content="[^"]*"', f'<meta property="og:url" content="{d["canonical"]}"', html, count=1)
    html = re.sub(r'"headline": "[^"]*"', f'"headline": "{d["headline"]}"', html, count=1)
    html = re.sub(r'"@id": "[^"]+"', f'"@id": "{d["canonical"]}"', html, count=1)
    html = re.sub(
        rf'<span class="blog-card__badge {re.escape(d["badge_class"])}">[^<]+</span>',
        f'<span class="blog-card__badge {d["badge_class"]}">{d["badge"]}</span>',
        html,
        count=1,
    )
    html = re.sub(r"<h1[^>]*>.*?</h1>", f'<h1 itemprop="headline">{d["headline"]}</h1>', html, count=1)
    html = re.sub(
        r'<time datetime="2026-04-12"[^>]*>.*?</time>',
        f'<time datetime="2026-04-12" itemprop="datePublished">{d["date"]}</time>',
        html,
        count=1,
    )
    html = re.sub(
        r'(<time datetime="2026-04-12"[^>]*>.*?</time>\s*<span aria-hidden="true">·</span>\s*)<span>[^<]+</span>',
        rf'\1<span>{d["read"]}</span>',
        html,
        count=1,
    )
    html = re.sub(
        r'(<img src="../../assets/images/blog/[^"]+" width="\d+" height="\d+" alt=")[^"]*(")',
        rf'\1{d["hero_alt"]}\2',
        html,
        count=1,
    )
    html = replace_body(html, d["body"])
    html = fill_chrome(html, loc, slug)
    return html


def main() -> None:
    for slug, locales in POSTS.items():
        en_path = ROOT / "blog" / f"{slug}.html"
        en_html = en_path.read_text(encoding="utf-8")
        # de/tr from broken copy: rebuild from EN with correct asset paths
        base = en_html.replace('href="../assets/', 'href="../../assets/')
        base = base.replace('src="../assets/', 'src="../../assets/')
        base = base.replace('src="../assets/js/', 'src="../../assets/js/')
        for loc in ("de", "tr"):
            out = ROOT / loc / "blog" / f"{slug}.html"
            html = localize_article(base, loc, slug, locales[loc])
            out.write_text(html, encoding="utf-8")
            print("Wrote", out)


if __name__ == "__main__":
    main()
