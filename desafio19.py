a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

if a > b > c:
    print(f'maior {a} | menor {c}')
if a > c > b:
    print(f'maior {a} | menor {b}')
if b > a > c:
    print(f'maior {b} | menor {c}')
if b > c > a:
    print(f'maior {b} | menor {a}')
if c > b > a:
    print(f'maior {c} | menor {a}')
if c > a > b:
    print(f'maior {c} | menor {b}')
