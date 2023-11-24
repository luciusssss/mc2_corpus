'''
Author: luciusssss (https://github.com/luciusssss)
Date: 2023-10-20

# reference:
https://en.wikipedia.org/wiki/Kazakh_alphabets
https://doc.wikimedia.org/mediawiki-core/1.34.4/php/classLanguageKk.html
http://www.transliteration.kpr.eu/kk-en/
https://en.wikipedia.org/wiki/Hamza#Kazakh_alphabet
'''

import re

KK_C_UC = "АӘБВГҒДЕЁЖЗИЙКҚЛМНҢОӨПРСТУҰҮФХҺЦЧШЩЪЫІЬЭЮЯ" # Kazakh Cyrillic uppercase
KK_C_LC = "аәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя" # Kazakh Cyrillic lowercase
KK_L_UC = "AÄBCÇDEÉFGĞHIİÏJKLMNÑOÖPQRSŞTUÜVWXYÝZ" # Kazakh Latin uppercase
KK_L_LC = "aäbcçdeéfgğhıiïjklmnñoöpqrsştuüvwxyýz" # Kazakh Latin lowercase
H_HAMZA = 'ء' # U+0674 ARABIC LETTER HIGH HAMZA


mCyLa2Arab = {
    ## Punctuation -> Arabic
    r'#|№|No\.': '؀', # U+0600;
    r',': '،', # U+060C;
    r';': '؛', # U+061B;
    r'\?': '؟', # U+061F;
    r'%': '٪', # U+066A;
    r'\*': '٭', # U+066D;
    ## Digits -> Arabic
    r'0': '۰', # U+06F0;
    r'1': '۱', # U+06F1;
    r'2': '۲', # U+06F2;
    r'3': '۳', # U+06F3;
    r'4': '۴', # U+06F4;
    r'5': '۵', # U+06F5;
    r'6': '۶', # U+06F6;
    r'7': '۷', # U+06F7;
    r'8': '۸', # U+06F8;
    r'9': '۹', # U+06F9;
    ## Cyrillic -> Arabic
    r'Аллаһ': 'ﷲ',
    # r'([АӘЕЁИОӨҰҮЭЮЯЪЬ])е': r'\1يە',
    # ZRUSIT IE 
    r'[е]': 'ە',
    r'([АӘЕЁОӨҰҮЭЮЯЪЬ])е': r'\1يە',
    # Cyrillic -> Arabic MOJE UPRAVY - upravil som yya = ya
    r'ия': 'يا',
    r'[еэ]': 'ە', r'[ъь]': '',
    r'[аә]': 'ا', r'[оө]': 'و', r'[ұү]': 'ۇ', r'[ыі]': 'ى',
    r'[и]': 'ي', r'ё': 'يو', r'ю': 'يۋ', r'я': 'يا', r'[й]': 'ي',
    r'ц': 'تس', r'щ': 'شش',
    r'һ': 'ح', r'ч': 'چ',
    # r'һ': 'ھ', r'ч': 'چ',
    r'б': 'ب', r'в': 'ۆ', r'г': 'گ', r'ғ': 'ع',
    r'д': 'د', r'ж': 'ج', r'з': 'ز', r'к': 'ك',
    r'қ': 'ق', r'л': 'ل', r'м': 'م', r'н': 'ن',
    r'ң': 'ڭ', r'п': 'پ', r'р': 'ر', r'с': 'س',
    r'т': 'ت', r'у': 'ۋ', r'ф': 'ف', r'х': 'ح',
    r'ш': 'ش',
    # punctuation
    r'»': '"',
    r'«': '"'
}

def split(split_pattern, text):
    matches = [(match.start(), match.end()) for match in re.finditer(split_pattern, text)]

    start = 0
    result = []
    for match in matches:
        end = match[0]
        result.append([text[start:end], start, end])
        start = match[1]
    result.append([text[start:], start, len(text)])
    
    return result

def regsConverter(text, toVariant):
    if text == '':
        return text
    
    pat = []
    rep = []
    if toVariant in ['kk-arab']:
        letters = KK_C_LC + KK_C_UC
        front = 'әөүіӘӨҮІ'
        excludes = 'еэгғкқЕЭГҒКҚ'
        matches = split('[\b\s\-\.:]+', text)
        mstart = 0
        ret = ''
        for m in matches:
            ret += text[mstart:m[1]]
            
            '''
            In the Kazakh Arabic alphabet, the hamza is used only at the beginning of words, and the only form is high hamza. It is not used to denote any sound, but used to indicate vowels in the word will be the four front vowels: ⟨ٵ⟩ (ä), ⟨ٸ⟩ (ı), ⟨ٶ⟩ (ö), ⟨ٷ⟩ (ü). However, it doesn't used for words contains the front vowel ⟨ە⟩ (e) or words contains four consonants ⟨گ⟩ (g), ⟨غ⟩ (ğ), ⟨ك⟩ (k), ⟨ق⟩ (q).
            '''
            if re.search('[' + front + ']', m[0]) and not re.search('[' + excludes + ']', m[0]):
                ret += re.sub('[' + letters + ']+', H_HAMZA + '\\g<0>', m[0])
            else:
                ret += m[0]
            mstart = m[2]

        text = ret
        for pat, rep in mCyLa2Arab.items():
            text = re.sub(pat, rep, text)

        return text
    
    elif toVariant in ['kk-latn']:
        raise NotImplementedError
    elif toVariant in ['kk-cyrl']:
        raise NotImplementedError
    else:
        return text

def translate(text, toVariant):
    # only lower the cyrillic character in the text, without affecting the latin characters
    result = ''
    for char in text:
        if char in KK_C_UC:
            result += char.lower()
        else:
            result += char
    text = result

    letters = ''
    if toVariant in ['kk-cyrl']:
        letters = KK_L_UC + KK_L_LC + 'ʺʹ#0123456789'
        raise Exception('Not implemented')
    elif toVariant in ['kk-arab']:
        letters = KK_C_UC + KK_C_LC + ',;\?%\*№0123456789'
    else:
        raise Exception('Not implemented')
        return text

    varsfix = '\$[0-9]'
    matches = split(varsfix + '[^' + letters + ']+', text)
    mstart = 0
    ret = ''
    for m in matches:
        ret += text[mstart:m[1]]
        ret += regsConverter(m[0], toVariant)
        mstart = m[2]

    return ret

# for testing
if __name__ == '__main__':
    text = "Барлық адамдар тумасынан азат және қадыр-қасиеті мен құқтары тең болып дүниеге келеді. Адамдарға ақыл-парасат, ар-ождан берілген, сондықтан олар бір-бірімен туыстық, бауырмалдық қарым-қатынас жасаулары тиіс."

    output = translate(text, 'kk-arab')
    print(output)


    text = "Қазақстан ( ), толық атауы Қазақстан Республикасы () — Шығыс Еуропа мен Орталық Азияда орналасқан мемлекет. Батысында Еділдің төменгі ағысынан, шығысында Алтай тауларына дейін 3 000 км-ге, солтүстіктегі Батыс Сібір жазығынан, оңтүстіктегі Қызылқұм шөлі мен Тянь-Шань тау жүйесіне 1 600 км-ге созылып жатыр. http://www.kazakhstan.kz"
    
    output = translate(text, 'kk-arab')
    print(output)
