def recursiva(n):
    try:
        if not isinstance(n, int):
            print("recursiva: n debe ser un entero")
            return None
        if n < 0:
            print("recursiva: n no puede ser negativo")
            return None
        # BASE CASE
        if n == 0:
            return "Done!"
        else:
            print(n)
            return recursiva(n - 1)
    except RecursionError:
        print("recursiva: se alcanzó el límite de recursión")
        return None


def fibonacci(n):
    try:
        if not isinstance(n, int):
            print("fibonacci: n debe ser un entero")
            return None
        if n < 0:
            print("fibonacci: n no puede ser negativo")
            return None
        if (n == 0) or (n == 1):
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    except RecursionError:
        print("fibonacci: se alcanzó el límite de recursión")
        return None


def factorial(n):
    try:
        if not isinstance(n, int):
            print("factorial: n debe ser un entero")
            return None
        if n < 0:
            print("factorial: n no puede ser negativo")
            return None
        if (n == 0) or (n == 1):
            return 1
        else:
            return factorial(n - 1) * n
    except RecursionError:
        print("factorial: se alcanzó el límite de recursión")
        return None


def multiplicacion_recursiva(n, m):
    try:
        if not isinstance(m, int):
            print("multiplicacion_recursiva: m debe ser un entero")
            return None
        if m < 0:
            print("multiplicacion_recursiva: m no puede ser negativo")
            return None
        if m == 0:
            return 0
        else:
            return multiplicacion_recursiva(n, m - 1) + n
    except RecursionError:
        print("multiplicacion_recursiva: se alcanzó el límite de recursión")
        return None


def division_entera_recursiva(dividendo, divisor):
    try:
        if not isinstance(dividendo, (int, float)) or not isinstance(divisor, (int, float)):
            print("division_entera_recursiva: dividendo y divisor deben ser numéricos")
            return None
        if divisor == 0:
            print("division_entera_recursiva: no se puede dividir entre cero")
            return None
        if dividendo - divisor < 0:
            return 0
        else:
            return division_entera_recursiva(dividendo - divisor, divisor) + 1
    except RecursionError:
        print("division_entera_recursiva: se alcanzó el límite de recursión")
        return None


def potencia_recursiva(base, exponente):
    try:
        if not isinstance(exponente, int):
            print("potencia_recursiva: exponente debe ser un entero")
            return None
        if exponente < 0:
            print("potencia_recursiva: exponente no puede ser negativo")
            return None
        if exponente == 0:
            return 1
        else:
            return potencia_recursiva(base, exponente - 1) * base
    except RecursionError:
        print("potencia_recursiva: se alcanzó el límite de recursión")
        return None


def serie_collatz(n):
    try:
        if not isinstance(n, int):
            print("serie_collatz: n debe ser un entero")
            return None
        if n < 1:
            print("serie_collatz: n debe ser mayor o igual a 1")
            return None
        if n == 1:
            print("END!")
            return 0
        else:
            if n % 2 == 0:
                print(n // 2)
                return serie_collatz(n // 2)
            else:
                print(3 * n + 1)
                return serie_collatz(3 * n + 1)
    except RecursionError:
        print("serie_collatz: se alcanzó el límite de recursión")
        return None


def aplanar_json(diccionario, clave_padre='', separador='.'):
    try:
        elementos = []
        for key, value in diccionario.items():
            nueva_llave = f"{clave_padre}{separador}{key}" if clave_padre else key
            if isinstance(value, dict):
                elementos.extend(aplanar_json(value, nueva_llave, separador).items())
            else:
                elementos.append((nueva_llave, value))
        return dict(elementos)
    except AttributeError:
        print("aplanar_json: se esperaba un diccionario")
        return None


if __name__ == "__main__":
    print("--- recursiva ---")
    print(recursiva(5))
    recursiva(-3)
    recursiva(3.5)
    recursiva("5")

    print("\n--- fibonacci ---")
    print(fibonacci(7))
    fibonacci(-1)

    print("\n--- factorial ---")
    print(factorial(5))
    factorial(-2)
    factorial(1.5)

    print("\n--- multiplicacion_recursiva ---")
    print(multiplicacion_recursiva(4, 3))
    multiplicacion_recursiva(4, -3)

    print("\n--- division_entera_recursiva ---")
    print(division_entera_recursiva(17, 5))
    division_entera_recursiva(10, 0)
    print(division_entera_recursiva(-10, 3))

    print("\n--- potencia_recursiva ---")
    print(potencia_recursiva(2, 5))
    potencia_recursiva(2, -2)

    print("\n--- serie_collatz ---")
    serie_collatz(6)
    serie_collatz(0)
    serie_collatz(-6)

    print("\n--- aplanar_json ---")
    print(aplanar_json({"a": 1, "b": {"c": 2}}))
    print(aplanar_json({"a": {"b": {"c": 1}}}))
    aplanar_json(["a", "b", "c"])

    json_prueba = {
        "a": 1,
        "b": {
            "c": 2,
            "d": {
                "e": 3
            }
        },
        "f": [1, 2, 3],
        "g": [
            {"h": 4},
            {"i": 5}
        ],
        "j": {
            "k": [6, 7, {"l": 8}]
        },
        "m": None,
        "n": True,
        "o": []
    }
    print(aplanar_json(json_prueba))
