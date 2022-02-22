"""
This is a example of how to use the persion_verbs module.
"""
import mazi

verb = mazi.MaziVerb(2, 'خوردن', False)
zamir = mazi.get_zamir(2, False)

print('-'*20)
print(f'{zamir} '+verb.sadeh())
print(f'{zamir} '+verb.estemrary())
print(f'{zamir} '+verb.mostamar())
print(f'{zamir} '+verb.naghly())
print(f'شاید {zamir} '+verb.eltezamy())
print(f'{zamir} '+verb.baid())

verb = mazi.MaziVerb(1, 'دادن', False)
zamir = mazi.get_zamir(1, False)

print('-'*20)
print(f'{zamir} '+verb.sadeh())
print(f'{zamir} '+verb.estemrary())
print(f'{zamir} '+verb.mostamar())
print(f'{zamir} '+verb.naghly())
print(f'شاید {zamir} '+verb.eltezamy())
print(f'{zamir} '+verb.baid())