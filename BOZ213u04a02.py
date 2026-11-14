def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if year < 1 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

yr = int(input("Bir yıl giriniz: "))
mo = int(input("Bir ay giriniz (1-12): "))
beklenen = int(input("Beklenen gün sayısını giriniz: "))

result = days_in_month(yr, mo)
print("Sonuç:", result)

print(yr, mo, "->", end="")
if result == beklenen:
    print("OK")
else:
    print("Failed")
