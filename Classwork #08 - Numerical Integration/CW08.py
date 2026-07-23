import math

# INPUT
a_str = input("write the left endpoint of the interval: ")
b_str = input("write the right endpoint of the interval: ")
f_x = input("write the function f(x) to integrate: ")
method = input("write the integration method to use (LRM/RRM/MPM/TM): ")

# PROCESS
a = None
try:
    if "pi" in a_str:
        a = eval(a_str.replace("pi", str(math.pi)))
    else:
        a = float(a_str)
except (ValueError, SyntaxError, NameError, TypeError):
    print("El límite inferior debe ser numérico")

if a is not None:
    b = None
    try:
        if "pi" in b_str:
            b = eval(b_str.replace("pi", str(math.pi)))
        else:
            b = float(b_str)
    except (ValueError, SyntaxError, NameError, TypeError):
        print("El límite superior debe ser numérico")

    if b is not None:
        f_valida = True
        if f_x.strip() == "":
            print("La función ingresada no es válida")
            f_valida = False
        elif "x" not in f_x:
            print("La función debe estar escrita en términos de x")
            f_valida = False

        if f_valida:
            if a >= b:
                print("El límite inferior debe ser menor que el límite superior")
            elif method not in ("LRM", "RRM", "MPM", "TM"):
                print("El método de integración no es válido. Usa LRM, RRM, MPM o TM")
            else:
                n = 1000
                h = (b - a) / n
                area = 0.0
                constant = 0
                shift = 0

                if method == "RRM":
                    shift = 1
                if method == "MPM":
                    constant = h / 2

                try:
                    if method == "TM":
                        f_0 = f_x.replace("x", str(a))
                        area += (h / 2) * eval(f_0)
                        for i in range(1, n):
                            xi = a + i * h
                            f_xi = f_x.replace("x", str(xi))
                            area += h / 2 * 2 * eval(f_xi)
                        f_xn = f_x.replace("x", str(b))
                        area += (h / 2) * eval(f_xn)
                    else:
                        for i in range(shift, n + shift):
                            xi = a + i * h
                            height = f_x.replace("x", str(xi + constant))
                            area += h * eval(height)

                    # OUTPUT
                    print(f"The integration of {f_x} is {area:.3f}")

                except ZeroDivisionError:
                    print("La función no está definida en algún punto del intervalo")
                except Exception:
                    print("La función ingresada no es válida")
