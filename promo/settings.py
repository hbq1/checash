
BASE_URL = 'https://dixy.ru'
BASE_DISCOUNT_URL = '{}{}'.format(BASE_URL, '/akcii')
PATH_WHOLE_CONTENT = '//div[@class="product"]/div/div/img/@alt'
PATH_NAME = '//div[@class="product"]/div/div/img/@alt'
PATH_PHOTO = '//div[@class="product"]/div/div/img/@src'
PATH_CATEGORY = '//div[@class="product-info-container"]/div/a/text()'
PATH_FRACT_NEW = '//div[@class="fract"]/text()'
PATH_PRICE_NEW = '//div[@class="price" or @class="price hundred"]/text()'
PATH_PRICE_OLD = '//div[@class="old-price"]/text()'
PATH_FRACT_OLD = '//div[@class="old-price"]/span/text()'
PATH_TITLE = '//div[@class="product-day" or @class="product-title"]//text()'
PATH_PROMO = '//div[@class="discount  " or @class="value"]/text()'

BASE_DISCOUNT_URL_DIXY_SKIDKI_NEDELI = '{}{}'.format(
    BASE_URL, '/akcii/skidki-nedeli/?PAGEN_1='
)

PATH_WHOLE_CONTENT_DIXY_SKIDKI_NEDELI = (
    '//div[contains(@class, "elem-badge-cornered")]/text()'
)

PATH_NAME_DIXY_SKIDKI_NEDELI = '//div[@class="elem-product__image"]/img/@alt'
PATH_PHOTO_DIXY_SKIDKI_NEDELI = '//div[@class="elem-product__image"]/img/@src'
PATH_CATEGORY_DIXY_SKIDKI_NEDELI = '//div[@class="product-category"]/text()'

PATH_PRICE_NEW_DIXY_SKIDKI_NEDELI = (
    '//span[@class="price-discount__integer"]/text()'
)

PATH_PRICE_OLD_DIXY_SKIDKI_NEDELI = (
    '//div[@class="elem-product__price-container"]/'
    'div[@class="just-now"]/text()|//span[@class="price-full__integer"]/text()'
)
PATH_TITLE_DIXY_SKIDKI_NEDELI = (
    '//div[contains(@class, "elem-badge-cornered")]/text()'
)

PATH_ACTIVE_PAGE_NUMBER = '//li[@class="active"]/a[@href="#"]/text()'


PATH_LAST_PAGE_ID = '//div/nav/ul/li[7]/a/text()'
