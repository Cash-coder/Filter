import random

def color_detector(ebay_title):
    # oredring all colors in the same order, the using index, if the first match in iatlina, you know it's negro, second mattch= azul
    spanish_colors = ['negro',  'azul',  'marrón',  'gris',  'verde',   'naranja',  ' rosa',    'violeta',  'rojo', 'blanco',    'amarillo', 'oro', 'plata']
    english_colors = ['black',  'blue',  'brown',   'grey',   'verde',   'orange',   'pink',    'purple',   'red',  'white',    'yellow',   'gold', 'silver']
    italian_colors = ['nero',   'blu',   'marrone', 'grigio', 'verde',  'arancione', 'rosa',    'viola',    'rosso', 'bianco',   'giallo'   'oro',  'argento'] 
    german_colors  = ['schwarz', 'blau', 'braun',    'grau',  'verde',   'orange',  'rosa',     'lila',     'rot',   'weiß',    'gelb',     'gold', 'silber']
    french_colors  = [ 'noir',    'bleu', 'brun',   'gris',   'vert',   'orange',  'rose',       'pourpre', 'rouge', 'blanc',   'jaune',   '----',  'argent'] #mising golden in french because it's 'or', will make a lot of false postives
    #spanish
    n_colors = 0
    for color in spanish_colors:
        if color in ebay_title:
            detected_color = color
            return detected_color
    #english
    for color in english_colors:
        if color in ebay_title:
            i = english_colors.index(color)
            detected_color = spanish_colors[i]
            return detected_color
    #italian
    for color in italian_colors:
        if color in ebay_title:
            i = italian_colors.index(color)
            detected_color = spanish_colors[i]
            return detected_color
    #german
    for color in german_colors:
        if color in ebay_title:
            i = german_colors.index(color)
            detected_color = spanish_colors[i]
    #french
    for color in french_colors:
        if color in ebay_title:
            i = french_colors.index(color)
            detected_color = spanish_colors[i]

    return None

def warranty_detector(subtitle, description):
    '30 días', '1 mes', 'un mes'
    '60 días', '2 mes', 'dos meses'

    german_year = '12 Monate Gewährleistung'
    '24 Monate Gewährleistung'
    '12 Monate Garantie'
    'GARANZIA'
    '6 MESI'
    '1 ANNO di garanzia!'
    '12 mesi di garanzia'

    year = ['1 year warranty', 'one year warranty', '12 months']
    # 90 días, = 3 meses de reembolso

    # lower and search phrases.

# ebay_title = 'iphone 12 schwarz max'
# color = color_detector(ebay_title)
# print(color)

def warr1(description):
    description = description.lower()

    one_year  = ['12 monate gewährleistung' , '12 monate herstellergarantie', '1 jahr gewährleistung' , '1 jahr herstellergarantie', '12 mesi garanzia', 'garanzia 12 mesi' , 'garanzia 1 anni']
    half_year = ['6 monate gewährleistung' , '6 monate herstellergarantie', '6 mesi garanzia', 'garanzia 6 mesi']
    two_years = ['24 monate gewährleistung' , '24 monate herstellergarantie', '2 jahr gewährleistung' , '2 jahr herstellergarantie', '24 mesi garanzia', 'garanzia 24 mesi' , 'garanzia 1 anni']
    two_years = ['24 mesi garanzia', 'garanzia 24 mesi' , 'garanzia 2 anni']

    for item in one_year:
        if item in description:
            return '12 months'
    for item in half_year:
        if item in description:
            return '6 months'
    for item in two_years:
        if item in description:
            return '24 months'
    
    # if german_year in description:
    #     return '1 year'
    
    



def warr2(description):
    pass

t1 = ''' "<div id=\"ds_div\">\n\t\t\t\t\t\t\t<!-- powered by plentymarkets www.plentymarkets.eu  //-->\n\n\n<title>Corona</title>\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n<meta content=\"YES\" name=\"apple-touch-fullscreen\">\n<meta content=\"telephone=no\" name=\"format-detection\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n<link href=\"https://fonts.googleapis.com/css?family=Open+Sans\" rel=\"stylesheet\" type=\"text/css\">\n<link href=\"https://content.kontramobile.de/media/files/ebayshop-kontra/css/style.css\" rel=\"stylesheet\" type=\"text/css\"><link href=\"https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css\" rel=\"stylesheet\">\n\n\t\n<div style=\"display: none;\" typeof=\"Product\" vocab=\"https://schema.org/\">\n\t<span property=\"description\">5,4\" Super Retina XDR Display (13,7 cm Diagonale)\nCeramic Shield, der mehr aushält als jedes Smartphone Glas\n5G für superschnelle Downloads und Streaming in höchster Qualität\nA14 Bionic, der schnellste Chip in einem Smartphone\nFortschrittliches Zwei‐Kamera-System mit 12 MP Ultraweitwinkel‐ und Weitwinkelobjektiv, Nachtmodus, Deep Fusion, Smart HDR 3, 4K Dolby Vision HDR Aufnahme\n12 MP TrueDepth Frontkamera mit Nachtmodus, 4K Dolby Vision HDR Aufnahme\nBranchenführender IP68 Wasserschutz</span>\n</div>\n\t\n<div id=\"shop\">\n<!------------------------------BODY------------------------------------->\n\n\t<div class=\"wrapper-grey\">\n\t\t<div class=\"wrapper-white\">\n        \t<div class=\"content-box\">\n          \t\t<div class=\"links\">\n            \t\t<div class=\"galerie\">\n\t\t\t\t\t\t<input class=\"btn-checkbox\" id=\"bild-1\" type=\"radio\" name=\"image-view\" checked>\n\t\t\t\t\t\t<input class=\"btn-checkbox\" id=\"bild-2\" type=\"radio\" name=\"image-view\">\n\t\t\t\t\t\t<input class=\"btn-checkbox\" id=\"bild-3\" type=\"radio\" name=\"image-view\">\n\t\t\t\t\t\t<input class=\"btn-checkbox\" id=\"bild-4\" type=\"radio\" name=\"image-view\">\n\t\t\t\t\t\t<input class=\"btn-checkbox\" id=\"bild-5\" type=\"radio\" name=\"image-view\">\n\t\t\t\t\t\t<input class=\"btn-checkbox\" id=\"bild-6\" type=\"radio\" name=\"image-view\">\n\t\t\t\t\t\t<input class=\"btn-checkbox\" id=\"bild-7\" type=\"radio\" name=\"image-view\">\n\t\t\t\t\t\t<input class=\"btn-checkbox\" id=\"bild-8\" type=\"radio\" name=\"image-view\">\n\t\t\t\t\t\t<input class=\"btn-checkbox\" id=\"bild-9\" type=\"radio\" name=\"image-view\">\n\t\t\t\t\t\t<input class=\"btn-checkbox\" id=\"bild-10\" type=\"radio\" name=\"image-view\">\n\t\t\t\t\t\t<div class=\"bild-gross\">  \n                                              \n\t\t\t\t\t\t\t<div id=\"bild-gross-1\" class=\"bild-gross-position\">\n\t\t\t\t\t\t\t\t<a href=\"#lightbox-1\"><img src=\"https://cdn02.plentymarkets.com/xzddf5zqcnd7/item/images/1240002/middle/Iph12minigalerie.jpg\"></a>                                     \n\t\t\t\t\t\t\t\t<div class=\"lightbox\" id=\"lightbox-1\">                                    \n\t\t\t\t\t\t\t\t\t<div class=\"lightbox-popup\">\n\t\t\t\t\t\t\t\t\t\t<img src=\"https://cdn02.plentymarkets.com/xzddf5zqcnd7/item/images/1240002/middle/Iph12minigalerie.jpg\">   \n\t\t\t\t\t\t\t\t\t\t<a class=\"btn-close\" href=\"#\"></a>\n\t\t\t\t\t\t\t\t\t</div>                                  \n\t\t\t\t\t\t\t\t</div>                                \n\t\t\t\t\t\t\t</div>   \n\n\t\t\t\t\t\t\t<div id=\"bild-gross-2\" class=\"bild-gross-position\">\n\t\t\t\t\t\t\t\t<a href=\"#lightbox-2\"><img src=\"https://cdn02.plentymarkets.com/xzddf5zqcnd7/item/images/1240002/middle/iph12minirot.jpg\"></a>                                     \n\t\t\t\t\t\t\t\t<div class=\"lightbox\" id=\"lightbox-2\">                                    \n\t\t\t\t\t\t\t\t\t<div class=\"lightbox-popup\">\n\t\t\t\t\t\t\t\t\t\t<img src=\"https://cdn02.plentymarkets.com/xzddf5zqcnd7/item/images/1240002/middle/iph12minirot.jpg\">   \n\t\t\t\t\t\t\t\t\t\t<a class=\"btn-close\" href=\"#\"></a>\n\t\t\t\t\t\t\t\t\t</div>                                  \n\t\t\t\t\t\t\t\t</div>                                \n\t\t\t\t\t\t\t</div>  \n\n\t\t\t\t\t\t\t<div id=\"bild-gross-3\" class=\"bild-gross-position\">\n\t\t\t\t\t\t\t\t<a href=\"#lightbox-3\"><img src=\"https://cdn02.plentymarkets.com/xzddf5zqcnd7/item/images/1240002/middle/iph12minirot2.jpg\"></a>                                     \n\t\t\t\t\t\t\t\t<div class=\"lightbox\" id=\"lightbox-3\">                                    \n\t\t\t\t\t\t\t\t\t<div class=\"lightbox-popup\">\n\t\t\t\t\t\t\t\t\t\t<img src=\"https://cdn02.plentymarkets.com/xzddf5zqcnd7/item/images/1240002/middle/iph12minirot2.jpg\">   \n\t\t\t\t\t\t\t\t\t\t<a class=\"btn-close\" href=\"#\"></a>\n\t\t\t\t\t\t\t\t\t</div>                                  \n\t\t\t\t\t\t\t\t</div>                                \n\t\t\t\t\t\t\t</div>  \n\n\t\t\t\t\t\t\t<div id=\"bild-gross-4\" class=\"bild-gross-position\">\n\t\t\t\t\t\t\t\t<a href=\"#lightbox-4\"><img src=\"https://cdn02.plentymarkets.com/xzddf5zqcnd7/item/images/1240002/middle/iph12minirot3.jpg\"></a>                                     \n\t\t\t\t\t\t\t\t<div class=\"lightbox\" id=\"lightbox-4\">                                    \n\t\t\t\t\t\t\t\t\t<div class=\"lightbox-popup\">\n\t\t\t\t\t\t\t\t\t\t<img src=\"https://cdn02.plentymarkets.com/xzddf5zqcnd7/item/images/1240002/middle/iph12minirot3.jpg\">   \n\t\t\t\t\t\t\t\t\t\t<a class=\"btn-close\" href=\"#\"></a>\n\t\t\t\t\t\t\t\t\t</div>                                  \n\t\t\t\t\t\t\t\t</div>                                \n\t\t\t\t\t\t\t</div>  \n\n\t\t\t\t\t\t\t<div id=\"bild-gross-5\" class=\"bild-gross-position\">\n\t\t\t\t\t\t\t\t<a href=\"#lightbox-5\"><img src=\"https://cdn02.plentymarkets.com/xzddf5zqcnd7/item/images/1240002/middle/iph12miniblau.jpg\"></a>                                     \n\t\t\t\t\t\t\t\t<div class=\"lightbox\" id=\"lightbox-5\">                                    \n\t\t\t\t\t\t\t\t\t<div class=\"lightbox-popup\">\n\t\t\t\t\t\t\t\t\t    <img src=\"https://cdn02.plentymarkets.com/xzddf5zqcnd7/item/images/1240002/middle/iph12miniblau.jpg\">   \n\t\t\t\t\t\t\t\t\t\t<a class=\"btn-close\" href=\"#\"></a>\n\t\t\t\t\t\t\t\t\t</div>                                  \n\t\t\t\t\t\t\t\t</div>                                \n\t\t\t\t\t\t\t</div>   \n\n\t\t\t\t\t\t\t<div id=\"bild-gross-6\" class=\"bild-gross-position\">\n\t\t\t\t\t\t\t\t<a href=\"#lightbox-6\"><img src=\"https://cdn02.plentymarkets.com/xzddf5zqcnd7/item/images/1240002/middle/iph12miniblau2.jpg\"></a>                                     \n\t\t\t\t\t\t\t\t<div class=\"lightbox\" id=\"lightbox-6\">                                    \n\t\t\t\t\t\t\t\t\t<div class=\"lightbox-popup\">\n\t\t\t\t\t\t\t\t\t\t<img src=\"https://cdn02.plentymarkets.com/xzddf5zqcnd7/item/images/1240002/middle/iph12miniblau2.jpg\">   \n\t\t\t\t\t\t\t\t\t\t<a class=\"btn-close\" href=\"#\"></a> \n\t\t\t\t\t\t\t\t\t</div>                                  \n\t\t\t\t\t\t\t\t</div>                                \n\t\t\t\t\t\t\t</div> \n\n\t\t\t\t\t\t\t<div id=\"bild-gross-7\" class=\"bild-gross-position\">\n\t\t\t\t\t\t\t\t<a href=\"#lightbox-7\"><img src=\"https://cdn02.plentymarkets.com/xzddf5zqcnd7/item/images/1240002/middle/iph12miniblau3.jpg\"></a>                                     \n\t\t\t\t\t\t\t\t<div class=\"lightbox\" id=\"lightbox-7\">                                    \n\t\t\t\t\t\t\t\t\t<div class=\"lightbox-popup\">\n\t\t\t\t\t\t\t\t\t\t<img src=\"https://cdn02.plentymarkets.com/xzddf5zqcnd7/item/images/1240002/middle/iph12miniblau3.jpg\">   \n\t\t\t\t\t\t\t\t\t\t<a class=\"btn-close\" href=\"#\"></a> \n\t\t\t\t\t\t\t\t\t</div>                                  \n\t\t\t\t\t\t\t\t</div>                                \n\t\t\t\t\t\t\t</div>  \n\n\t\t\t\t\t\t\t<div id=\"bild-gross-8\" class=\"bild-gross-position\">\n\t\t\t\t\t\t\t\t<a href=\"#lightbox-8\"><img src=\"https://cdn02.plentymarkets.com/xzddf5zqcnd7/item/images/1240002/middle/iph12miniblau4.jpg\"></a>                                     \n\t\t\t\t\t\t\t\t<div class=\"lightbox\" id=\"lightbox-8\">                                    \n\t\t\t\t\t\t\t\t\t<div class=\"lightbox-popup\">\n\t\t\t\t\t\t\t\t\t\t<img src=\"https://cdn02.plentymarkets.com/xzddf5zqcnd7/item/images/1240002/middle/iph12miniblau4.jpg\">   \n\t\t\t\t\t\t\t\t\t\t<a class=\"btn-close\" href=\"#\"></a> \n\t\t\t\t\t\t\t\t\t</div>                                  \n\t\t\t\t\t\t\t\t</div>                                \n\t\t\t\t\t\t\t</div>  \n\n\t\t\t\t\t\t\t<div id=\"bild-gross-9\" class=\"bild-gross-position\">\n\t\t\t\t\t\t\t\t<a href=\"#lightbox-9\"><img src=\"https://cdn02.plentymarkets.com/xzddf5zqcnd7/item/images/1240002/middle/iph12minigruen.jpg\"></a>                                     \n\t\t\t\t\t\t\t\t<div class=\"lightbox\" id=\"lightbox-9\">                                    \n\t\t\t\t\t\t\t\t\t<div class=\"lightbox-popup\">\n\t\t\t\t\t\t\t\t\t\t<img src=\"https://cdn02.plentymarkets.com/xzddf5zqcnd7/item/images/1240002/middle/iph12minigruen.jpg\">   \n\t\t\t\t\t\t\t\t\t\t<a class=\"btn-close\" href=\"#\"></a> \n\t\t\t\t\t\t\t\t\t</div>                                  \n\t\t\t\t\t\t\t\t</div>                                \n\t\t\t\t\t\t\t</div>  \n\n\t\t\t\t\t\t\t<div id=\"bild-gross-10\" class=\"bild-gross-position\">\n\t\t\t\t\t\t\t\t<a href=\"#lightbox-10\"><img src=\"https://cdn02.plentymarkets.com/xzddf5zqcnd7/item/images/1240002/middle/iph12minigruen2.jpg\"></a>                                     \n\t\t\t\t\t\t\t\t<div class=\"lightbox\" id=\"lightbox-10\">                                    \n\t\t\t\t\t\t\t\t\t<div class=\"lightbox-popup\">\n\t\t\t\t\t\t\t\t\t\t<img src=\"https://cdn02.plentymarkets.com/xzddf5zqcnd7/item/images/1240002/middle/iph12minigruen2.jpg\">   \n\t\t\t\t\t\t\t\t\t\t<a class=\"btn-close\" href=\"#\"></a> \n\t\t\t\t\t\t\t\t\t</div>                                  \n\t\t\t\t\t\t\t\t</div> '''
t2 = '''"<div id=\"ds_div\">\n\t\t\t\t\t\t\t <meta charset=\"UTF-8\"> <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"> <link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/font-awesome/4.6.2/css/font-awesome.min.css\"> <link rel=\"stylesheet\" href=\"https://media.wirkaufens.org/vertrieb/ebay/template/new/css/base.css\"> <title>asgoodasnew eBay</title><div class=\"template\"> <div class=\"template__outer\"> <div class=\"template__inner\"> <div style=\"color:#FFFFFF\">AN560294</div> <div class=\"template__header container hidden-sm-down\"> <div class=\"template__header--teaser row flex-items-xs-around mt-2\"> <div class=\"template__header--teaser-box col-sm-12 col-md-6\"> <div class=\"teaser mb-2\"><a href=\"https://stores.ebay.de/asgoodasnew-premium/Handys-Smartphones-/_i.html?_fsub=1084297419&amp;_sid=1380752719\" target=\"_blank\"><img src=\"https://media.wirkaufens.org/vertrieb/ebay/template/new/bilder/ebay_banner_handy.jpg\" class=\"img-fluid\" alt=\"\"></a></div> </div> <div class=\"template__header--teaser-box col-sm-12 col-md-6\"> <div class=\"teaser mb-2\"><a href=\"https://stores.ebay.de/asgoodasnew-premium\" target=\"_blank\"><img src=\"https://media.wirkaufens.org/vertrieb/ebay/template/new/bilder/ebay_banner_shop.jpg\" class=\"img-fluid\" alt=\"\"></a></div> </div> </div> </div> <div class=\"template__navigation\"> <div class=\"template__navigation--inner container-fluid\"> <div class=\"template__navigation--inner-logo text-sm-center text-xs-center text-md-left w-100\"> <p><strong>asgoodasnew</strong> <span>/ Premium</span></p> </div> <div class=\"row\"> <div class=\"template__navigation--inner-menu col-md-12 col-lg-9 hidden-sm-down\"> <ul class=\"list-unstyled mb-0\"> <li><a href=\"https://stores.ebay.de/asgoodasnew-premium\" class=\"d-block\" target=\"_blank\">Shop</a></li> <li> <a href=\"https://stores.ebay.de/asgoodasnew-premium\" class=\"d-block\" target=\"_blank\">Shop-Kategorien</a> <ul class=\"list-unstyled text-xs-center\"> <li><a href=\"https://stores.ebay.de/asgoodasnew-premium/Handys-Smartphones-/_i.html?_fsub=1084297419&amp;_sid=1380752719\" class=\"d-block w-100\" target=\"_blank\">Handys &amp; Smartphones</a></li> <li> <a href=\"https://stores.ebay.de/asgoodasnew-premium/Tablets-/_i.html?_fsub=1084297519&amp;_sid=1380752719\" class=\"d-block w-100\" target=\"_blank\">Tablets</a></li> <li><a href=\"https://stores.ebay.de/asgoodasnew-premium/Smartwatches-/_i.html?_fsub=1084334019&amp;_sid=1380752719\" class=\"d-block w-100\" target=\"_blank\">Smartwatches</a></li> <li><a href=\"https://stores.ebay.de/asgoodasnew-premium/Objektive-/_i.html?_fsub=1084297719&amp;_sid=1380752719\" class=\"d-block w-100\" target=\"_blank\">Objektive</a></li> <li> <a href=\"https://stores.ebay.de/asgoodasnew-premium/Kameras-/_i.html?_fsub=1084297619&amp;_sid=1380752719\" class=\"d-block w-100\" target=\"_blank\">Kameras</a></li> </ul> </li> <li><a href=\"https://stores.ebay.de/asgoodasnew-premium/Zahlung.html\" class=\"d-block\" target=\"_blank\">Zahlung</a></li> <li><a href=\"https://stores.ebay.de/asgoodasnew-premium/Versand-und-Retoure.html\" class=\"d-block\" target=\"_blank\">Versand &amp; Retoure</a></li> <li><a href=\"https://stores.ebay.de/asgoodasnew-premium/Kundenservice.html\" class=\"d-block\" target=\"_blank\">Kundenservice</a></li> <li><a href=\"https://stores.ebay.de/asgoodasnew-premium/AGB.html\" class=\"d-block\" target=\"_blank\">AGB</a></li> <li><a href=\"https://stores.ebay.de/asgoodasnew-premium/Impressum.html\" class=\"d-block\" target=\"_blank\">Impressum</a></li> </ul> </div> <div class=\"template__navigation--inner-search col-sm-12 col-lg-3 flex-md-first flex-lg-last hidden-sm-down\"></div> </div> </div> </div> <div class=\"template__breadcrumb container\"> <div class=\"row\"> <div class=\"col-xs\"><span>handys &gt; Apple &gt; <strong>Apple iPhone 12 mini 64GB rot</strong></span></div> </div> </div> <div class=\"template__product container\"> <div class=\"row\"> <div class=\"template__product--gallery col-lg-6\"> <div class=\"row\"> <div class=\"col-xs-12 col-md-10 flex-xs-first flex-md-last\"> <div class=\"stage\"> <ul> <li> <input type=\"radio\" name=\"agan-gallery\" checked id=\"pic1\"> <div style=\"background-image: url(https://imageservice.asgoodasnew.com/1024/17880/38/title-0000.jpg);\">  </div> </li> </ul> </div> <p class=\"text-xs-center\"> <small class=\"text-muted\">Standardbilder. Abbildung Ähnlich (Farbe und Zustand können abweichen), bitte beachten Sie die Detailbeschreibung. </small> </p> </div> </div> </div> <div class=\"template__product--description col-lg-6\"> <div class=\"template__product--description-producer\"></div> <h1 class=\"h2\">Apple iPhone 12 mini 64GB rot</h1> <p>Zustand: Wie neu</p> <p><span style=\"font-size:14px;\">Gerät professionell aufbereitet in Deutschland</span></p> <ul class=\"list-unstyled\"> <li class=\"text-success\">• Bis zu <strong>30% günstiger</strong> als Neuware*</li> <li class=\"text-success\">• <strong>Kostenloser DHL-Versand</strong> innerhalb Deutschlands </li> <li class=\"text-success\">• <strong>Schnelle Lieferung</strong> innerhalb von 2 Werktagen</li> <li class=\"text-success\">• <strong>30 Tage Rückgaberecht</strong></li> <li class=\"text-success\">• <strong>12 Monate Gewährleistung</strong></li> </ul> <div class=\"template__product--description-box mb-3\"> <p class=\"h5\"> <strong>Produkteigenschaften</strong></p> <div><p><span>SIM-Lock</span>kein SIM-Lock</p> <p><span>Farbe</span>rot</p> <p><span>Speicher</span>64GB</p></div> <div><p><span>Lieferumfang</span></p> <p> &gt; Ladekabel</p> <p> &gt; Akku</p> <p> &gt; USB-Datenkabel</p> <p> &gt; asgoodasnew Verpackung</p></div> <div> <p><strong>** Preisangabe/Rechnung</strong></p> <p>Der angegebene Preis enthält die Umsatzsteuer. Die von uns angebotenen Artikel unterliegen der Differenzbesteuerung nach § 25a UStG, so dass die enthaltene Umsatzsteuer nicht separat auf der Rechnung ausgewiesen wird.</p> </div> </div> <div class=\"template__product--description-condition mb-\"> <p><strong>Wie neu - Was bedeutet das?</strong></p> <div class=\"condition-box\"> <div class=\"row flex-items-xs-bottom\"> <div class=\"col-xs-4 selected\"> <p>Wie neu</p> <div><img src=\"https://media.wirkaufens.org/vertrieb/ebay/template/new/bilder/zustand_wie_neu.jpg\" class=\"img-fluid\" alt=\"\"></div> </div> <div class=\"col-xs-4 \"> <p>Sehr gut</p> <div><img src=\"https://media.wirkaufens.org/vertrieb/ebay/template/new/bilder/zustand_sehr_gut.jpg\" class=\"img-fluid\" alt=\"\"></div> </div> <div class=\"col-xs-4 \"> <p> Gut </p> <div><img src=\"https://media.wirkaufens.org/vertrieb/ebay/template/new/bilder/zustand_gut.jpg\" class=\"img-fluid\" alt=\"\"></div> </div> <br><br> <div class=\"col-xs-4 selected\"> <div><span class=\"mt-2 mb-1\">Optischer Zustand: Ohne Gebrauchsspuren oder Beschädigungen<br><br>Technischer Zustand:<br>einwandfrei</span></div> </div> <div class=\"col-xs-4 \"> <div><span class=\"mt-2 mb-1\">Optischer Zustand: Einzelne, leichte und oberflächliche Kratzer oder Abnutzungen möglich.<br><br>Technischer Zustand:<br>einwandfrei</span></div> </div> <div class=\"col-xs-4 \"> <div><span class=\"mt-2 mb-1\">Optischer Zustand: Mehrere leichte Gebrauchsspuren oder maximal 3 schwere Gebrauchsspuren (z.B. tiefe Kratzer, Abnutzungen, Kerben).<br><br>Technischer Zustand:<br>einwandfrei</span></div> </div> </div> </div> </div> <div class=\"template__product--description-disclaimer mb-\"> <p><br><br><strong>Über asgoodasnew:</strong></p> <ul class=\"list-unstyled mb-2\"> <li>&amp;bullet; Ihre Nummer eins in Deutschland für refurbished Elektronik.</li> <li>&amp;bullet; Seit 2008, mit mittlerweile über 120 Mitarbeitern für Sie da.</li> <li>&amp;bullet; Große Auswahl von generalüberholten und neuen Geräten, wie Smartphones, Tablets, Kameras, Objektive und vieles mehr.</li> <li>&amp;bullet; Professionell aufbereitet von Technik-Spezialisten, unter strengen Qualitätskontrollen.</li> <li>&amp;bullet; Bereits über hundertausend zufriedene Kunden.</li> </ul> <img src=\"https://media.wirkaufens.org/vertrieb/ebay/template/new/bilder/mitarbeiter.jpg\" class=\"img-fluid mb-2\" alt=\"\"> <p class=\"mb-2\">Hier geht es zu unserem Shop &gt; <a href=\"https://stores.ebay.de/asgoodasnew-premium\" target=\"_blank\"><u>eBay Shop</u></a></p> <p> <small>*im Vergleich zu Neuware. (Unverbindliche Preisempfehlung des Herstellers) </small> </p> </div> </div> </div> </div> </div> </div></div></div>" '''
t3 = '''"<div id=\"ds_div\">\n\t\t\t\t\t\t\t\n\n\n<meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\">\n<meta http-equiv=\"X-UA-Compatible\" content=\"IE=Edge\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, user-scalable=yes\">\n<title>Apple iPhone 12 mini (64GB) (PRODUCT)RED rot Super Retina XDR Display A14 Bionic</title>\n<link href=\"https://commerce.price-guard.net/templates/simplebay/00/pg17rsp/css/banner_slider.css\" rel=\"stylesheet\">\n<link rel=\"stylesheet\" type=\"text/css\" href=\"https://commerce.price-guard.net/templates/simplebay/00/pg17rsp/css/slider-widget-structure.css\">\n<link rel=\"stylesheet\" type=\"text/css\" href=\"https://commerce.price-guard.net/templates/simplebay/00/pg17rsp/css/themes/default/slider-widget-settings.css\">\n<link rel=\"stylesheet\" type=\"text/css\" href=\"https://commerce.price-guard.net/templates/simplebay/00/pg17rsp/css/themes/default/slider-widget-theme.css\">\n<link rel=\"stylesheet\" type=\"text/css\" href=\"https://commerce.price-guard.net/templates/simplebay/00/pg17rsp/css/themes/default/slider-widget-animations.css\">\n<link rel=\"stylesheet\" type=\"text/css\" href=\"https://commerce.price-guard.net/templates/simplebay/00/pg17rsp/css/slider-widget-responsive.css\">\n<link rel=\"stylesheet\" type=\"text/css\" href=\"https://fonts.googleapis.com/css?family=Open+Sans:400,400italic,600,600italic,700,700italic,800,800italic%7CSource+Sans+Pro:400,300,300italic,400italic,600,600italic,700,700italic,900,900italic%7CAlegreya+Sans:400,300,300italic,400italic,500,500italic,700,700italic,800,800italic,900,900italic%7CPoiret+One%7CDosis:400,500,300,600,700,800%7CLobster+Two:400,400italic,700,700italic%7CRaleway:400,300,300italic,400italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic%7CRoboto+Condensed:400,300italic,300,400italic,700,700italic%7CRoboto:400,300,300italic,400italic,500,500italic,700,700italic,900,900italic%7CCourgette\">\n<link href=\"https://commerce.price-guard.net/templates/simplebay/00/pg17rsp/css/bootstrap.min.css\" rel=\"stylesheet\">\n<link href=\"https://commerce.price-guard.net/templates/simplebay/00/pg17rsp/css/pg17rsp.css\" rel=\"stylesheet\">\n\n\n<style>\n        #SiMPLEKS-v2-data, #SiMPLEKS-v2-meta {\n            display: none;\n        }\n    </style>\n<div id=\"SiMPLEKS-v2-meta\">\n<div id=\"SiMPLEKS-v2-meta-generated-at\" class=\"simpleks-v2-meta\">27.11.2021 02:37:35</div>\n<div id=\"SiMPLEKS-v2-meta-account\" class=\"simpleks-v2-meta\">price-guard</div>\n<div id=\"SiMPLEKS-v2-meta-template\" class=\"simpleks-v2-meta\">Price Guard</div>\n<div id=\"SiMPLEKS-v2-meta-template-id\" class=\"simpleks-v2-meta\">2</div>\n<div id=\"SiMPLEKS-v2-meta-last-template-deploy\" class=\"simpleks-v2-meta\">27.07.2020 10:58:21</div>\n<div id=\"SiMPLEKS-v2-meta-template-deployed-version\" class=\"simpleks-v2-meta\">1d3382aa8992</div>\n<div id=\"SiMPLEKS-v2-meta-description-version\" class=\"simpleks-v2-meta\">182</div>\n</div>\n<div id=\"SiMPLEKS-v2-data\">\n<div id=\"SiMPLEKS-v2-data-title\" class=\"simpleks-v2-data\">Apple iPhone 12 mini (64GB) (PRODUCT)RED rot Super Retina XDR Display A14 Bionic</div>\n<div id=\"SiMPLEKS-v2-data-sku\" class=\"simpleks-v2-data\">appi12m_64rede</div>\n<div id=\"SiMPLEKS-v2-data-ebayplus\" class=\"simpleks-v2-data\">0</div>\n<div id=\"SiMPLEKS-v2-data-weight\" class=\"simpleks-v2-data\">0.0000</div>\n<div id=\"SiMPLEKS-v2-data-manufacturerImage\" class=\"simpleks-v2-data\">https://commerce.price-guard.net/img/manufacturers/00/14.jpg</div>\n<div id=\"SiMPLEKS-v2-data-headline\" class=\"simpleks-v2-data\">Ein Modell mit brillanter Kameraauflösung und großer Speicherkapazität!</div>\n<div id=\"SiMPLEKS-v2-data-shortdescription\" class=\"simpleks-v2-data\"><div><ul>\n<li><font size=\"2\">5,4\" Super Retina XDR Display (13,7 cm Diagonale)</font></li>\n<li><font size=\"2\">Ceramic Shield, der mehr aushält als jedes Smartphone Glas</font></li>\n<li><font size=\"2\">5G für superschnelle Downloads und Streaming in höchster Qualität</font></li>\n<li><font size=\"2\">A14 Bionic, der schnellste Chip in einem Smartphone</font></li>\n<li><font size=\"2\">Fortschrittliches Zwei‑Kamera-System mit 12 MP Ultraweitwinkel‑ und Weitwinkelobjektiv, Nachtmodus, Deep Fusion, Smart HDR 3, 4K Dolby Vision HDR Aufnahme</font></li>\n<li><font size=\"2\">12 MP TrueDepth Frontkamera mit Nachtmodus, 4K Dolby Vision HDR Aufnahme</font></li>\n<li><font size=\"2\">Branchenführender IP68 Wasserschutz</font></li>\n<li><font size=\"2\">Unterstützt MagSafe Zubehör zum einfachen Andocken und schnelleren kabellosen Laden, iOS 14 mit neuen Widgets auf dem Homescreen, der neuen App Mediathek, App Clips und mehr</font></li>\n</ul></div></div>\n<div id=\"SiMPLEKS-v2-data-acondition\" class=\"simpleks-v2-data\"> <li>NEUWARE</li>\n<li>mit Originalverpackung</li>\n<li>12 Monate Herstellergarantie 2)</li>\n<li>ohne Branding! EU-Ware 3)<br>\n</li>\n<li>ohne Vertrag! ohne Simlock!<br>\n</li>\n<li>EAN kann u.U. abweichen!</li>\n</div>\n<div id=\"SiMPLEKS-v2-data-productLegalInformation\" class=\"simpleks-v2-data\"><font color=\"#ff0000\"><b>Achtung! Aus Umweltschutzgründen werden alle neuen iPhone und Apple Watch Modelle ohne Netzteil und EarPods ausgeliefert. Im Lieferumfang befindet sich ein USB-C auf Lightning Kabel (bei iPhones) oder ein magnetisches Ladekabel (bei Watches) das schnelles Aufladen unterstützt und mit USB-C Netzteilen und Computeranschlüssen kompatibel ist.</b></font> </div>\n<div id=\"SiMPLEKS-v2-data-delivery\" class=\"simpleks-v2-data\"><ul><li><font size=\"2\">Apple iPhone 12 mini (64GB) (PRODUCT)RED rot</font></li></ul>\n<div><span style=\"font-size: small;\">Als Teil der Bemühungen von Apple, seine Umweltziele zu erreichen, kommt das iPhone 12 mini ohne Netzteil und EarPods. Verwende bitte ein vorhandenes Apple Netzteil und vorhandene Kopfhörer oder kaufe dieses Zubehör separat.</span></div></div>\n<div id=\"SiMPLEKS-v2-data-description\" class=\"simpleks-v2-data\"><div><font size=\"2\"><br></font></div>\n<div>\n<div><font size=\"2\"><b>Apple iPhone 12 mini (64GB) (PRODUCT)RED Smartphone</b></font></div>\n<div><font size=\"2\">Mit einem Gewicht von 133 g und den Maßen 13,15 x 6,42 x 0,74 cm zählt das Smartphone Apple iPhone 12 mini (64GB) (PRODUCT)RED zu den mittelgroßen Modellen. Für eine übersichtliche Anzeige der Bildschirminhalte sorgt das 5,4 Zoll Multitouch-Display, das 1080 x 2340 Pixel abbilden kann. Eine Besonderheit: Das Apple iPhone 12 mini (64GB) (PRODUCT)RED ist wasserdicht.</font></div>\n<div><font size=\"2\"><br></font></div>\n<div><font size=\"2\"><b>Die Schnittstellen des Apple iPhone 12 mini (64GB) (PRODUCT)RED</b></font></div>\n<div><font size=\"2\">Mittels WLAN und UMTS haben Sie mit Ihrem Apple iPhone 12 mini (64GB) (PRODUCT)RED jederzeit Zugang zum Internet, ob zu Hause oder unterwegs. Dank Bluetooth lässt sich das Smartphone mit Headsets, Fitness-Trackern und anderen Geräten verbinden. NFC ermöglicht eine sichere Übertragung von Daten sowie mobiles Payment. Eine Lightning-Schnittstelle ist zusätzlich eingebaut, um Daten via Kabel zu übertragen.</font></div>\n<div><font size=\"2\"><br></font></div>\n<div><font size=\"2\"><b>Sonstige Eigenschaften dieses Smartphones</b></font></div>\n<div><font size=\"2\">Mit einer hochauflösenden 12 Megapixel-Kamera und einer 12 Megapixel-Frontkamera können Sie schöne Momente auf Fotos und Videos einfangen. Mit dem bemerkenswerten Speichervolumen von 64 GB hat das Apple iPhone 12 mini (64GB) (PRODUCT)RED neben Ihren Bildern auch für viele Filme, Apps und andere Dateien Platz. Beim Apple iPhone 12 mini (64GB) (PRODUCT)RED besonders praktisch ist die kabellose Ladefunktion.</font></div>\n</div></div>\n<div id=\"SiMPLEKS-v2-data-downloads\" class=\"simpleks-v2-data\"><a target=\"_blank\" class=\"download\" href=\"https://commerce.price-guard.net/attachments/download/875/pg_root_op.html\">Herstellergarantiebedingungen Apple.pdf</a></div>\n<div id=\"SiMPLEKS-v2-data-technicalData\" class=\"simpleks-v2-data\"><div><b><font size=\"2\">Netz-Standard</font></b></div>\n<div><ul>\n<li><font size=\"2\">5G-Standard: ja  </font></li>\n<li><font size=\"2\">UMTS (3G): ja  </font></li>\n<li><font size=\"2\">LTE-Advanced (Cat. 16): ja  </font></li>\n<li><font size=\"2\">5G Band 78 (3500 MHz): ja  </font></li>\n<li><font size=\"2\">LTE Band 1 (2100 MHz): ja  </font></li>\n<li><font size=\"2\">LTE Band 3 (1800 MHz): ja  </font></li>\n<li><font size=\"2\">LTE Band 5 (850 MHz): ja  </font></li>\n<li><font size=\"2\">LTE Band 7 (2600 MHz): ja  </font></li>\n<li><font size=\"2\">LTE Band 8 (900 MHz): ja  </font></li>\n<li><font size=\"2\">LTE Band 20 (800 MHz): ja  </font></li>\n<li><font size=\"2\">1800 MHz/900 MHz Betrieb: ja  </font></li>\n<li><font size=\"2\">850 MHz/1900 MHz (USA-Netz) Betrieb: ja  </font></li>\n<li><font size=\"2\">800 MHz Betrieb: ja  </font></li>\n<li><font size=\"2\">1700 MHz Betrieb: ja  </font></li>\n<li><font size=\"2\">2100 MHz Betrieb: ja  </font></li>\n<li><font size=\"2\">HSDPA: ja  </font></li>\n<li><font size=\"2\">HSUPA: ja</font></li>\n</ul></div>\n<div><b><font size=\"2\">Netz-Zusatzdienste</font></b></div>\n<div><ul><li><font size=\"2\">E-Mail fähig: ja</font></li></ul></div>\n<div><b><font size=\"2\">Bedienung</font></b></div>\n<div><ul>\n<li><font size=\"2\">Beschleunigungssensor: ja  </font></li>\n<li><font size=\"2\">Gyro-Sensor: ja  </font></li>\n<li><font size=\"2\">Näherungssensor: ja  </font></li>\n<li><font size=\"2\">Barometer: ja  </font></li>\n<li><font size=\"2\">Sprachsteuerung möglich: ja</font></li>\n</ul></div>\n<div><b><font size=\"2\">Display/Anzeigen</font></b></div>\n<div><ul>\n<li><font size=\"2\">Display-Diagonale (cm): 13.7  </font></li>\n<li><font size=\"2\">Display-Diagonale (zoll): 5.4  </font></li>\n<li><font size=\"2\">Display-Typ: Farb-Grafik Touchscreen Display  </font></li>\n<li><font size=\"2\">Retina-Display: ja  </font></li>\n<li><font size=\"2\">kapazitiver Touch-Screen: ja  </font></li>'''

warr = warr1(t2)
warr = warr1(t1)
warr = warr1(t3)
print(warr)


response= ''
from bs4 import BeautifulSoup



divs = response.xpath('//div[@class="ux-layout-section__row"]')#.extract()
des = ''
for div in divs:
    labels = div.xpath('.//div[@class="ux-labels-values__labels"]').extract()
    values = div.xpath('.//div[@class="ux-labels-values__values-content"]').extract()

    labels_soup = BeautifulSoup(str(labels), features="html.parser")
    values_soup = BeautifulSoup(str(values), features="html.parser")

    print(labels_soup, '\n', values_soup)

    entry1 = labels_soup[0] + ' ' + values_soup[0] + '\n'
    entry2 = labels_soup[1] + ' ' + values_soup[1] + '\n'

    des += entry1
    des += entry2

print(des)

labels_text = labels_soup.get_text()
values_text = values_soup.get_text()
# print(labels_text, '\n', values_text)
print(labels_text)
# print(type(labels_text))

# zipped = list(zip(labels_text, values_text))
# print(zipped)

soup = BeautifulSoup(str(div), features="html.parser")
text = soup.get_text()
print(text)


divs = response.xpath('//div[@class="ux-layout-section__row"]').extract()
description = ''
for div in divs:
    div_text = BeautifulSoup(str(div), features="html.parser").get_text()
    description += div_text + '\n'
print(description)



divs = response.xpath('//div[@class="ux-layout-section__row"]')#.extract()
des = ''
# for div in divs:
# label1 = xpath(label)[0]
# label2 = xpath(label)[1]

#value1 = xpath(value)[0]
#value2 = xpath(value)[1]

# entry1 = label1 + ' ' + value1 + '\n'
# entry2 = label2 + ' ' + value2 + '\n'

# des += entry1
# des += entry2


divs = response.xpath('//div[@class="ux-layout-section__row"]')#.extract()
des = ''
flag = 0
for div in divs:
    # labels = div.xpath('.//div[@class="ux-labels-values__labels"]/text()').get()
    # values = div.xpath('.//div[@class="ux-labels-values__values-content"]/text()').get()
    labels = div.xpath('.//div[@class="ux-labels-values__labels"]/div/div/span/text()').getall()
    value_state = div.xpath('.//div[@class="ux-labels-values__values-content"]/div/span/span/span/text()').get()
    values = div.xpath('.//div[@class="ux-labels-values__values-content"]/div/span/text()').getall()

    # print(type(labels))
    print(labels)
    print(values)
    print('-----------')



divs = response.xpath('//div[@class="ux-layout-section__row"]')#.extract()
des = ''
flag = 0
for div in divs:
    labels = div.xpath('.//div[@class="ux-labels-values__labels"]/div/div/span/text()').getall()
    value_state = div.xpath('.//div[@class="ux-labels-values__values-content"]/div/span/span/span/text()').get()
    values = div.xpath('.//div[@class="ux-labels-values__values-content"]/div/span/text()').getall()

    if flag == 0:
        entry1 = labels[0] + value_state + '\n'+ '\n'
        entry2 = labels[1] + values[0] + '\n'+ '\n'
        
        des += entry1
        des += entry2
        flag += 1
    else:
        try:
            entry1 = labels[0] + values[0] + '\n' + '\n'
            entry2 = labels[1] + values[1] + '\n' + '\n'
            des += entry1
            des += entry2
        except: pass
print(des)

#     if flag == 0:
#         entry1 = labels[0] + ' ' + value_state + '\n'
#         entry2 = labels[1] + ' ' + values[0] + '\n'
#     else:
#         entry1 = labels[0] + ' ' + values[0] + '\n'
#         entry2 = labels[1] + ' ' + values[1] + '\n'

#     des += entry1
#     des += entry2
# print(des)