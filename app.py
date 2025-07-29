print("AI Doktor Assistentga xush kelibsiz!")

# Foydalanuvchidan simptomlarni olish
simptom = input("\nSizda qanday alomatlar bor? (masalan: bosh og'rig'i, isitma, yo'tal): ")

javob = ""

if "isitma" in simptom.lower():
    javob += "- Sizda ehtimoliy virusli infeksiya bor. Suv iching va shifokorga murojaat qiling.\n"
if "yo'tal" in simptom.lower():
    javob += "- Sizda nafas yo'llari kasalligi bo'lishi mumkin. Iloji bo'lsa, rentgen tekshiruvi qiling.\n"
if "bosh og'rig'i" in simptom.lower():
    javob += "- Siz charchagandirsiz yoki stressdasiz. Dam oling, agar davom etsa, shifokorga boring.\n"

if not javob:
    javob = "Kechirasiz, siz kiritgan alomatlar bo‘yicha maslahat bera olmadim. Iltimos, batafsilroq yozing."

print("\nTavsiyalar:")
print(javob)