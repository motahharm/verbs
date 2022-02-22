"""
This is MaziVerbPersion generator.
"""

def get_shenaseh_mazi(shakhs, mofrad):
    """
    this is ShenasehMazi generator.
    examples:
    دادم = داد + م(شناسه ماضی)
    """
    if shakhs == 1 and mofrad == True:
        return 'م'
    if shakhs == 2 and mofrad == True:
        return 'ی'
    if shakhs == 3 and mofrad == True:
        return ''
    if shakhs == 1 and mofrad == False:
        return 'یم'
    if shakhs == 2 and mofrad == False:
        return 'ید'
    if shakhs == 3 and mofrad == False:
        return 'ند'

def get_gozashteh_naghly(shakhs, mofrad):
    """
    this is GozashtehNaghly generator.
    examples:
    بوده ام = بوده + ام(شناسه گذشته نقلی(ماضی نقلی))
    """
    if shakhs == 1 and mofrad == True:
        return 'ام'
    if shakhs == 2 and mofrad == True:
        return 'ای'
    if shakhs == 3 and mofrad == True:
        return 'است'
    if shakhs == 1 and mofrad == False:
        return 'ایم'
    if shakhs == 2 and mofrad == False:
        return 'اید'
    if shakhs == 3 and mofrad == False:
        return 'اند'

def get_gozashteh_mostamar(shakhs, mofrad):
    """
    this is GozashtehMostamar generator.
    examples:
    داشتم می رفتم = داشتم(شناسه گذشته مستمر) + می رفتم
    """
    if shakhs == 1 and mofrad == True:
        return 'داشتم'
    if shakhs == 2 and mofrad == True:
        return 'داشتی'
    if shakhs == 3 and mofrad == True:
        return 'داشت'
    if shakhs == 1 and mofrad == False:
        return 'داشتیم'
    if shakhs == 2 and mofrad == False:
        return 'داشتید'
    if shakhs == 3 and mofrad == False:
        return 'داشتند'

def get_gozashteh_eltezamy(shakhs, mofrad):
    """
    this is GozashtehEltezamy generator.
    examples:
    خورده باشم = خورده + باشم(شناسه گذشته التزامی)
    """
    if shakhs == 1 and mofrad == True:
        return 'باشم'
    if shakhs == 2 and mofrad == True:
        return 'باشی'
    if shakhs == 3 and mofrad == True:
        return 'باشد'
    if shakhs == 1 and mofrad == False:
        return 'باشیم'
    if shakhs == 2 and mofrad == False:
        return 'باشید'
    if shakhs == 3 and mofrad == False:
        return 'باشند'

def get_gozashteh_baid(shakhs, mofrad):
    """
    this is GozashtehBaid generator.
    examples:
    گرفته بودند = گرفته + بودند(شناسه گذشته بعید)
    """
    if shakhs == 1 and mofrad == True:
        return 'بودم'
    if shakhs == 2 and mofrad == True:
        return 'بودی'
    if shakhs == 3 and mofrad == True:
        return 'بود'
    if shakhs == 1 and mofrad == False:
        return 'بودیم'
    if shakhs == 2 and mofrad == False:
        return 'بودید'
    if shakhs == 3 and mofrad == False:
        return 'بودند'

def get_bon_mozare(masdar):
    """
    this is BonMozare generator.
    examples:
    گرفتن(مصدر) - ن(در آخر مصدر) = بن ماضی
    """
    return masdar[:-1]

class MaziVerb:
    """
    this is a class for create Mazi verbs.
    """
    def __init__(self, shakhs, masdar, mofrad):
        self.shakhs = shakhs
        self.masdar = masdar
        self.mofrad = mofrad
        self.bon_mozare = get_bon_mozare(masdar)

    def sadeh(self):
        """
        فعل گذشته ساده:
        مثال ها:
        رفتم
        دیدم
        """
        result = ''
        result += self.bon_mozare
        result += get_shenaseh_mazi(self.shakhs, self.mofrad)
        return result

    def estemrary(self):
        """
        فعل گذشته التزامی:
        مثال ها:
        می رفتم
        می دیدی
        """
        result = ''
        result += 'می '
        result += self.sadeh()
        return result

    def mostamar(self):
        """
        فعل گذشته مستمر:
        مثال ها:
        داشتم می رفتم
        داشتم می دیدی
        """
        result = ''
        result += get_gozashteh_mostamar(self.shakhs, self.mofrad)
        result += ' '
        result += self.estemrary()
        return result

    def naghly(self):
        """
        فعل گذشته نقلی:
        مثال ها:
        رفته اند
        دیده است
        """
        result = ''
        result += self.bon_mozare
        result += 'ه'
        result += ' '
        result += get_gozashteh_naghly(self.shakhs, self.mofrad)
        return result

    def eltezamy(self):
        """
        فعل گذشته التزامی:
        مثال ها:
        رفته بودی
        دیده بود
        """
        result = ''
        result += self.bon_mozare
        result += 'ه'
        result += ' '
        result += get_gozashteh_eltezamy(self.shakhs, self.mofrad)
        return result

    def baid(self):
        """
        فعل گذشته التزامی:
        مثال ها:
        رفته بودم
        دیده بودید
        """
        result = ''
        result += self.bon_mozare
        result += 'ه'
        result += ' '
        result += get_gozashteh_baid(self.shakhs, self.mofrad)
        return result

def get_zamir(shakhs, mofrad):
    """
    this is Zamir generator.
    examples:
    من(ضمیر) داشتم می رفتم.
    آنها(ضمیر) داشتند می رفتند
    """
    if shakhs == 1 and mofrad == True:
        return 'من'
    if shakhs == 2 and mofrad == True:
        return 'تو'
    if shakhs == 3 and mofrad == True:
        return 'او'
    if shakhs == 1 and mofrad == False:
        return 'ما'
    if shakhs == 2 and mofrad == False:
        return 'شما'
    if shakhs == 3 and mofrad == False:
        return 'آنها'
