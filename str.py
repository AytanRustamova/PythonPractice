str='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'
# - str daxilində neçə xarakter olduğunu ekrana yazdırın
count = len(str)
print(count)


# - str daxilində neçə hərf olduğunu ekrana yazdırın 

words = str.split()
count = len(words)
print(count)

# - str daxilindəki sözləri ayrı bir massiv içərisində toplayın

words = str.split()
newArray = []
newArray.append(words)
print(newArray)


# - str daxilində son iki sözü silən metod yazın

words = str.rsplit(' ', 2)[0]
print(words)


# - str ni vergülə görə ayırıb iki string halına gətirin

words1 = str.split(',')[0]
words2 = str.split(',')[1]



 # - stringSearch(word) adında bir metod yazın. daxil edilən sözün mətnin içində olub olmadığını ekrana çap edən metod yazın 

def stringSearchWord():
    a= input("Soz axtarin:")
    if(a in str):
        print(a)
    else:
        print("Axtardiginiz soz metnde tapilmadi")
    
    
stringSearchWord()



 # - str daxilində neçə sait və neçə samit olduğunu ekrana çap edin
str='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'
cleanStr = str.lower() # butun herfleri kicildir.

saitler = ['a', 'e', 'i', 'o', 'u', 'ə' ,'ü', 'ö' ,'ı' ] # yalniz saitlerle edib if else'le de ede bilerdik, o zaman replace methodu ile whitespaceleri temizlemek lazim olacaqdi, ona gore samitler arrayinden istifade etdim.

samitler = ['q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'ç', 'ş', 'ğ']
saitSayi = 0
samitSayi = 0 

for i in cleanStr:
    if i in saitler:
        saitSayi = saitSayi + 1
    elif i in samitler:
        samitSayi = samitSayi + 1 
print(saitSayi)
print(samitSayi)