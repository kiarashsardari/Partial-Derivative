# Partial Derivative

اسکریپت ساده‌ای برای محاسبه مشتقات جزئی یک عبارت ریاضی با استفاده از کتابخانه **SymPy** در پایتون.

## نصب پیش‌نیاز

```bash
pip install sympy
```

## معرفی

این پروژه شامل یک تابع به نام `d` است که یک عبارت SymPy و چند نام متغیر را دریافت می‌کند و مشتق جزئی عبارت را نسبت به هر متغیر برمی‌گرداند.

```python
def d(f, *sympols_list):
    sympols_list = [sp.Symbol(s) for s in sympols_list]
    return [sp.diff(f, x) for x in sympols_list]
```

### پارامترها

- `f`: عبارت ریاضی مورد نظر (از نوع SymPy)
- `*sympols_list`: نام متغیرها به صورت رشته (`str`)

### خروجی

یک لیست از مشتقات جزئی، به ترتیب متغیرهای ورودی.

## مثال استفاده

```python
import sympy as sp
from Partial_Derivative import d

x = sp.Symbol('x')
y = sp.Symbol('y')

f = x**3 + 3*x - 4 + y

result = d(f, "x", "y", "g")
sp.pprint(result)
```

خروجی:

```text
⎡   2       ⎤
⎣3⋅x  + 3, 1, 0⎦
```

توضیح:

- مشتق نسبت به `x`: `3*x**2 + 3`
- مشتق نسبت به `y`: `1`
- مشتق نسبت به `g`: `0` (چون `g` در عبارت وجود ندارد)

## اجرای مستقیم

```bash
python Partial_Derivative.py
```

## نکات

- اگر متغیری در عبارت وجود نداشته باشد، مشتق آن صفر می‌شود.
- در کد اصلی، نام `sympols_list` یک غلط املایی است؛ شکل صحیح آن `symbols_list` است.
- بهتر است به جای رشته، خود `Symbol`ها به تابع پاس داده شوند تا از ساخت مجدد آن‌ها جلوگیری شود.
- می‌توان خروجی را به صورت دیکشنری نیز برگرداند تا نگاشت متغیر به مشتق مشخص باشد:

```python
def d(f, *symbols):
    symbols = [sp.Symbol(s) if isinstance(s, str) else s for s in symbols]
    return {s: sp.diff(f, s) for s in symbols}
```
