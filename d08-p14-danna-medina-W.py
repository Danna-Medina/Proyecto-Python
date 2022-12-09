
def e1(opcion):  # Función principal que llama a las distintas opciones del programa
    import os;

    if opcion == 1:
        os.system("cls");
        alta_Seleccion();

    elif opcion == 2:
        os.system("cls");
        baja_Seleccion();

    elif opcion == 3:
        os.system("cls");
        ventas();

    elif opcion == 4:
        import sys;
        sys.exit();


# SECCIÓN ALTAS
def alta_Seleccion():  # Selecciona qué se quiere dar de alta.
    from colorama import Cursor, Back, Fore, init;
    import msvcrt;
    import os;
    init(autoreset=True);
    ventanas(True);

    opcionA = 1;

    while True:
        print(Cursor.POS(52, 10) + Back.WHITE + Fore.BLACK + "  1. Producto  ");
        print(Cursor.POS(52, 15) + Back.WHITE + Fore.BLACK + "  2. Empleado  ");
        print(Cursor.POS(52, 20) + Back.WHITE + Fore.BLACK + "  3. Datos de la frutería  ");
        print(Cursor.POS(31, 25) + Back.WHITE + Fore.RED + "Presione el número de la opción o seleccione con las flechas");
        print(Cursor.POS(54, 4) + Back.WHITE + Fore.BLUE + ">>> ALTAS <<<");
        print(Cursor.POS(106, 4) + Back.WHITE + Fore.GREEN + "Enter ->");
        print(Cursor.POS(8, 4) + Back.WHITE + Fore.RED + "<- Esc");

        if opcionA == 1:
            print(Cursor.POS(52, 10) + Fore.BLACK + Back.YELLOW + "> 1. Producto <");

        elif opcionA == 2:
            print(Cursor.POS(52, 15) + Fore.BLACK + Back.YELLOW + "> 2. Empleado <");

        elif opcionA == 3:
            print(Cursor.POS(52, 20) + Fore.BLACK + Back.YELLOW + "> 3. Datos de la frutería <");

        tecla = msvcrt.getch();

        if tecla == b'H':
            opcionA -= 1;

        elif tecla == b'P':
            opcionA += 1;

        elif tecla == b'1':
            opcionA = 1;
            break;

        elif tecla == b'2':
            opcionA = 2;
            break;

        elif tecla == b'3':
            opcionA = 3;
            break;

        elif tecla == b'\x1b':
            menu();
            break;

        elif tecla == b'\r':
            break;

        if opcionA < 1:
            opcionA = 3;

        elif opcionA > 3:
            opcionA = 1;

    if opcionA == 1:
        alta_Producto();

    elif opcionA == 2:
        alta_Empleado();

    elif opcionA == 3:
        alta_Datos();


def alta_Producto():  # Alta de productos, validación de existentes.
    from colorama import Cursor, Back, Fore, init;
    import msvcrt;
    import os;

    os.system("cls");
    ventanas(True);
    print(Cursor.POS(51, 4) + Back.WHITE + Fore.BLUE + ">>> ALTA PRODUCTO <<<");
    try:
        a = open("d08-p14-danna-medina-W.txt", mode="r", encoding="utf-8");

        lineas = a.readlines();
        a.close();

        x = 8;
        y = 7;

        for linea in lineas:
            sel = linea.startswith("Producto: ");

            if sel == True:
                producto = linea.replace("Producto: ", "");
                print(Cursor.POS(x, y) + Back.WHITE + Fore.BLACK + producto);
                y += 1;
                if y == 25:
                    y = 7;
                    x += 59;

        nombre = str(input(Cursor.POS(8, 26) + Back.WHITE + Fore.BLUE + "Nombre del producto:" + Back.WHITE + Fore.BLACK + " "));
        unidades = int(input(Cursor.POS(50, 26) + Back.WHITE + Fore.BLUE + "Unidades disponibles:" + Back.WHITE + Fore.BLACK + " "));
        precio = float(input(Cursor.POS(88, 26) + Back.WHITE + Fore.BLUE + "Precio del producto:" + Back.WHITE + Fore.BLACK + " "));

        while True:
            x1 = random(True);
            codigo = str(x1);
            existe = validar_Dato_Existente(codigo, 10);
            if existe == -1:
                break;

        a = open("d08-p14-danna-medina-W.txt", mode="a", encoding="utf-8");

        precioStr = str(precio);
        unidadesStr = str(unidades);

        print(Cursor.POS(8,4) + Back.WHITE + Fore.RED + "<- Esc");
        print(Cursor.POS(106,4) + Back.WHITE + Fore.GREEN + "Enter ->");
        print(Cursor.POS(30,28) + Back.WHITE + Fore.BLUE + "Para guardar el producto presione Enter o presione Esc para cancelar.");

        while True:
            tecla = msvcrt.getch();

            if tecla == b'\x1b':
                a.close();
                print(Cursor.POS(32,28) + Back.WHITE + Fore.RED + "El producto no ha sido añadido, presione Enter para volver al menu.");
                break;

            elif tecla == b'\r':

                nombre = nombre.upper();
                existe = validar_Dato_Existente(nombre,18);  # Se valida si el producto ya existe o no para poder agregarlo.

                if existe == 18:
                    print(Cursor.POS(30,28) + Back.WHITE + Fore.RED + "    Este producto ya existe, presione Enter para volver al menu.     ");
                    a.close();
                    break;

                elif existe == -1:

                    espacioNombre = espacios(nombre, 14);

                    espacioCantidad = espacios(unidadesStr, 5);

                    a.writelines("\n");
                    a.writelines("Producto: " + codigo + ": " + nombre + espacioNombre + "Cantidad: " + unidadesStr + espacioCantidad + "c/u  " + precioStr);
                    a.writelines("\n");
                    a.close();

                    os.system("cls");
                    ventanas(True);
                    print(Cursor.POS(51, 4) + Back.WHITE + Fore.BLUE + ">>> ALTA PRODUCTO <<<");

                    a = open("d08-p14-danna-medina-W.txt", mode="r", encoding="utf-8");

                    lineas = a.readlines();
                    a.close();

                    x = 8;
                    y = 7;

                    for linea in lineas:
                        sel = linea.startswith("Producto: ");

                        if sel == True:
                            producto = linea.replace("Producto: ", "");
                            print(Cursor.POS(x, y) + Back.WHITE + Fore.BLACK + producto);
                            y += 1;
                            if y == 25:
                                y = 7;
                                x += 59;

                    print(Cursor.POS(38, 28) + Back.WHITE + Fore.GREEN + "Producto añadido, presione Enter para volver al menu.");
                    break;

        input();
        menu();

    except:
        print(Cursor.POS(106, 4) + Back.WHITE + Fore.GREEN + "Enter ->");
        print(Cursor.POS(35,28) + Back.WHITE + Fore.RED + "     Datos no válidos, presione Enter para volver al menu.        ");
        input();
        menu();


def alta_Empleado():  # Alta de empleados, validación de existentes.
    from colorama import Cursor, Back, Fore, init;
    import msvcrt;
    import os;

    os.system("cls");
    ventanas(True);
    print(Cursor.POS(51, 4) + Back.WHITE + Fore.BLUE + ">>> ALTA EMPLEADO <<<");
    try:
        print(Cursor.POS(50, 10) + Back.WHITE + Fore.BLACK + "Nombre del empleado: ");
        print(Cursor.POS(50, 14) + Back.WHITE + Fore.BLACK + "Sueldo del empleado: ");
        nombre = str(input(Cursor.POS(50, 10) + Back.WHITE + Fore.BLACK + "Nombre del empleado: "));
        sueldo = float(input(Cursor.POS(50, 14) + Back.WHITE + Fore.BLACK + "Sueldo del empleado: "));

        while True:
            x1 = random(False);
            codigo = str(x1);
            existe = validar_Dato_Existente(codigo, 10);
            if existe == -1:
                break;

        a = open("d08-p14-danna-medina-W.txt", mode="a", encoding="utf-8");

        print(Cursor.POS(8, 4) + Back.WHITE + Fore.RED + "<- Esc");
        print(Cursor.POS(106, 4) + Back.WHITE + Fore.GREEN + "Enter ->");
        print(Cursor.POS(30, 26) + Back.WHITE + Fore.BLUE + "Para guardar los datos presione Enter o presione Esc para cancelar.");

        while True:
            tecla = msvcrt.getch();

            if tecla == b'\x1b':
                a.close();
                print(Cursor.POS(30, 22) + Back.WHITE + Fore.RED + "Los datos no han sido guardados, presione Enter para volver al menu.");
                break;

            elif tecla == b'\r':
                nombre = nombre.upper();
                existe = validar_Dato_Existente(nombre, 15);
                sueldoStr = str(sueldo);

                if existe == 15:
                    a.close();
                    print(Cursor.POS(34, 22) + Back.WHITE + Fore.RED + "El empleado ya existe, presione Enter para volver al menu.");
                    break;

                elif existe == -1:

                    espacioNombre = espacios(nombre, 25);
                    can = len(nombre);

                    a.writelines("\n");
                    a.writelines("Empleado: " + codigo + ": " + nombre + espacioNombre + "Sueldo: $" + sueldoStr);
                    a.writelines("\n");
                    a.close();
                    print(Cursor.POS(31, 22) + Back.WHITE + Fore.GREEN + "Datos del empleado guardados, presione Enter para volver al menu.");
                    break;

        input();
        menu();

    except:
        print(Cursor.POS(106, 4) + Back.WHITE + Fore.GREEN + "Enter ->");
        print(Cursor.POS(38, 22) + Back.WHITE + Fore.RED + "Datos no válidos, presione Enter para continuar.");
        input();
        menu();


def alta_Datos():  # Alta detos de la fruteria, validación de existentes.
    from colorama import Cursor, Back, Fore, init;
    import msvcrt;
    import os;

    os.system("cls");
    ventanas(True);
    print(Cursor.POS(54, 4) + Back.WHITE + Fore.BLUE + ">>> ALTA DATOS <<<");
    print(Cursor.POS(106, 4) + Back.WHITE + Fore.GREEN + "Enter ->");


    for i in ['Nombre', 'Teléfono', 'Correo']:
        existe = validar_Dato_Existente(i, 10);

        if existe == 10:
            print(Cursor.POS(12,16) + Back.WHITE + Fore.RED + "Para añadir nuevos datos primero hay que dar de baja los existentes, presione Enter para continuar.");
            input();
            menu();
            break;

        else:
            print(Cursor.POS(50, 10) + Back.WHITE + Fore.BLACK + "Nombre frutería: ");
            print(Cursor.POS(50, 14) + Back.WHITE + Fore.BLACK + "Teléfono: ");
            print(Cursor.POS(50, 18) + Back.WHITE + Fore.BLACK + "Correo: ");

            try:
                nombre = str(input(Cursor.POS(50, 10) + Back.WHITE + Fore.BLACK + "Nombre frutería: "));
                telefono = int(input(Cursor.POS(50, 14) + Back.WHITE + Fore.BLACK + "Teléfono: "));
                correo = str(input(Cursor.POS(50, 18) + Back.WHITE + Fore.BLACK + "Correo: "));


                if (nombre == '') or (telefono == '') or (correo == ''):
                    print(Cursor.POS(106, 4) + Back.WHITE + Fore.GREEN + "Enter ->");
                    print(Cursor.POS(38, 22) + Back.WHITE + Fore.RED + "Datos no válidos, presione Enter para continuar.");
                    input();
                    menu();

                else:
                    print(Cursor.POS(8, 4) + Back.WHITE + Fore.RED + "<- Esc");
                    print(Cursor.POS(106, 4) + Back.WHITE + Fore.GREEN + "Enter ->");
                    print(Cursor.POS(30, 26) + Back.WHITE + Fore.BLUE + "Para guardar los datos presione Enter o presione Esc para cancelar.");


                    while True:
                        tecla = msvcrt.getch();

                        if tecla == b'\x1b':
                            print(Cursor.POS(32, 22) + Back.WHITE + Fore.RED + "Los datos no han sido guardados, presione enter para continuar.");
                            break;

                        elif tecla == b'\r':
                            a = open("d08-p14-danna-medina-W.txt", mode="a", encoding="utf-8");
                            nombre = nombre.upper();
                            telefono = str(telefono);
                            for i in ['Nombre', 'Teléfono', 'Correo']:
                                existe = validar_Dato_Existente(i, 10);

                            if existe == -1:
                                a.writelines("\n");
                                a.writelines("Frutería: Nombre: " + nombre);
                                a.writelines("\n");
                                a.writelines("Frutería: Teléfono: " + telefono);
                                a.writelines("\n");
                                a.writelines("Frutería: Correo: " + correo);
                                a.writelines("\n");
                                a.close();
                                print(Cursor.POS(33, 22) + Back.WHITE + Fore.GREEN + "Datos de la tienda guardados, presione Enter para continuar.");
                                break;

                    input();
                    menu();
            except:
                print(Cursor.POS(106, 4) + Back.WHITE + Fore.GREEN + "Enter ->");
                print(Cursor.POS(38, 22) + Back.WHITE + Fore.RED + "Datos no válidos, presione Enter para continuar.");
                input();
                menu();


# SECCIÓN BAJAS
def baja_Seleccion():  # Da de baja productos, empleados o los datos de la frutería.
    from colorama import Cursor, Back, Fore, init;
    import msvcrt;
    import os;
    init(autoreset=True);
    ventanas(True);

    opcionB = 1;

    while True:
        print(Cursor.POS(54, 4) + Back.WHITE + Fore.BLUE + ">>> BAJAS <<<")
        print(Cursor.POS(52, 10) + Back.WHITE + Fore.BLACK + "  1. Producto  ");
        print(Cursor.POS(52, 15) + Back.WHITE + Fore.BLACK + "  2. Empleado  ");
        print(Cursor.POS(52, 20) + Back.WHITE + Fore.BLACK + "  3. Datos de la Frutería  ");
        print(Cursor.POS(31, 25) + Back.WHITE + Fore.RED + "Presione el número de la opción o seleccione con las flechas");
        print(Cursor.POS(106, 4) + Back.WHITE + Fore.GREEN + "Enter ->");
        print(Cursor.POS(8, 4) + Back.WHITE + Fore.RED + "<- Esc");

        if opcionB == 1:
            print(Cursor.POS(52, 10) + Fore.BLACK + Back.YELLOW + "> 1. Producto <");

        elif opcionB == 2:
            print(Cursor.POS(52, 15) + Fore.BLACK + Back.YELLOW + "> 2. Empleado <");

        elif opcionB == 3:
            print(Cursor.POS(52, 20) + Fore.BLACK + Back.YELLOW + "> 3. Datos de la Frutería <");

        tecla = msvcrt.getch();

        if tecla == b'H':
            opcionB -= 1;

        elif tecla == b'P':
            opcionB += 1;

        elif tecla == b'1':
            opcionB = 1;
            break;

        elif tecla == b'2':
            opcionB = 2;
            break;

        elif tecla == b'3':
            opcionB = 3;
            break;

        elif tecla == b'\x1b':
            menu();
            break;

        elif tecla == b'\r':
            break;

        if opcionB < 1:
            opcionB = 3;

        elif opcionB > 3:
            opcionB = 1;

    if opcionB == 1:
        baja_Producto();

    elif opcionB == 2:
        baja_Empleado();

    elif opcionB == 3:
        baja_Datos();


def baja_Producto():  # Impresión de inventario y baja de productos.
    from colorama import Cursor, Back, Fore, init;
    import msvcrt;
    import os;
    init(autoreset=True);

    os.system("cls");
    ventanas(True);
    print(Cursor.POS(51, 4) + Back.WHITE + Fore.BLUE + ">>> BAJA PRODUCTO <<<");
    print(Cursor.POS(106, 4) + Back.WHITE + Fore.GREEN + "Enter ->");

    a = open("d08-p14-danna-medina-W.txt", mode="r", encoding="utf-8");

    lineas = a.readlines();
    a.close();

    x = 8;
    y = 7;

    for linea in lineas:
        sel = linea.startswith("Producto: ");

        if sel == True:
            producto = linea.replace("Producto: ", "");
            print(Cursor.POS(x, y) + Back.WHITE + Fore.BLACK + producto);
            y += 1;
            if y == 25:
                y = 7;
                x += 59;
    try:
        codigoBaja = int(input(
            Cursor.POS(8, 26) + Back.WHITE + Fore.BLUE + "Código del producto a dar de baja:" + Fore.BLACK + " "));
        codigoBaja = str(codigoBaja);

    except:
        print(Cursor.POS(26, 28) + Back.WHITE + Fore.RED + "El código introducido no es válido, presione Enter para volver al menu.");
        input();
        menu();

    if codigoBaja == "":
        menu();

    else:
        print(Cursor.POS(35, 28) + Back.WHITE + Fore.BLUE + "Presione Enter para continuar o Esc para cancelar");
        print(Cursor.POS(8, 4) + Back.WHITE + Fore.RED + "<- Esc");

        while True:
            tecla = msvcrt.getch();

            if tecla == b'\x1b':
                menu();
                break;

            elif tecla == b'\r':
                break;

        codigoBaja = str(codigoBaja);

        a = open("d08-p14-danna-medina-W.txt", mode="w", encoding="utf-8");

        for linea in lineas:
            sel = linea.startswith("Producto: " + codigoBaja);

            if sel == False:
                a.write(linea);

        a.close();

        os.system("cls");
        ventanas(True);
        print(Cursor.POS(51, 4) + Back.WHITE + Fore.BLUE + ">>> BAJA PRODUCTO <<<");
        print(Cursor.POS(106, 4) + Back.WHITE + Fore.GREEN + "Enter ->");

        a = open("d08-p14-danna-medina-W.txt", mode="r", encoding="utf-8");

        lineas = a.readlines();
        a.close();

        x = 8;
        y = 7;

        for linea in lineas:
            sel = linea.startswith("Producto: ");

            if sel == True:
                producto = linea.replace("Producto: ", "");
                print(Cursor.POS(x, y) + Back.WHITE + Fore.BLACK + producto);
                y += 1;
                if y == 25:
                    y = 7;
                    x += 59;

        print(Cursor.POS(18,
                         27) + Back.WHITE + Fore.BLUE + "El producto con código " + Back.WHITE + Fore.BLACK + codigoBaja + Back.WHITE + Fore.BLUE + " ha sido dado de baja, presione Enter para volver al menu.");
        input();
        menu();


def baja_Empleado():  # Impresión de empleados y baja de los mismos.
    from colorama import Cursor, Back, Fore, init;
    import msvcrt;
    import os;
    init(autoreset=True);

    os.system("cls");
    ventanas(True);
    print(Cursor.POS(51, 4) + Back.WHITE + Fore.BLUE + ">>> BAJA EMPLEADO <<<");
    print(Cursor.POS(106, 4) + Back.WHITE + Fore.GREEN + "Enter ->");

    a = open("d08-p14-danna-medina-W.txt", mode="r", encoding="utf-8");

    lineas = a.readlines();
    a.close();

    x = 8;
    y = 7;

    for linea in lineas:
        sel = linea.startswith("Empleado: ");

        if sel == True:
            producto = linea.replace("Empleado: ", "");
            print(Cursor.POS(x, y) + Back.WHITE + Fore.BLACK + producto);
            y += 1;
            if y == 25:
                y = 7;
                x += 59;
    try:
        codigoBaja = int(input(
            Cursor.POS(8, 26) + Back.WHITE + Fore.BLUE + "Código del empleado a dar de baja:" + Fore.BLACK + " "));
        codigoBaja = str(codigoBaja);

    except:
        print(Cursor.POS(26, 28) + Back.WHITE + Fore.RED + "El código introducido no es válido, presione Enter para volver al menu.");
        input();
        menu();

    if codigoBaja == "":
        menu();

    else:
        print(Cursor.POS(35, 28) + Back.WHITE + Fore.BLUE + "Presione Enter para continuar o Esc para cancelar");
        print(Cursor.POS(8, 4) + Back.WHITE + Fore.RED + "<- Esc");

        while True:
            tecla = msvcrt.getch();

            if tecla == b'\x1b':
                menu();
                break;

            elif tecla == b'\r':
                break;

        codigoBaja = str(codigoBaja);

        a = open("d08-p14-danna-medina-W.txt", mode="w", encoding="utf-8");

        for linea in lineas:

            sel = linea.startswith("Empleado: " + codigoBaja);

            if sel == False:
                a.write(linea);

        a.close();

        os.system("cls");
        ventanas(True);
        print(Cursor.POS(51, 4) + Back.WHITE + Fore.BLUE + ">>> BAJA EMPLEADO <<<");
        print(Cursor.POS(106, 4) + Back.WHITE + Fore.GREEN + "Enter ->");

        a = open("d08-p14-danna-medina-W.txt", mode="r", encoding="utf-8");

        lineas = a.readlines();
        a.close();

        x = 8;
        y = 7;

        for linea in lineas:
            sel = linea.startswith("Empleado: ");

            if sel == True:
                producto = linea.replace("Empleado: ", "");
                print(Cursor.POS(x, y) + Back.WHITE + Fore.BLACK + producto);
                y += 1;
                if y == 25:
                    y = 7;
                    x += 59;

        print(Cursor.POS(18, 27) + Back.WHITE + Fore.BLUE + "El empleado con código " + Back.WHITE + Fore.BLACK + codigoBaja + Back.WHITE + Fore.BLUE + " ha sido dado de baja, presione Enter para volver al menu.");
        input();
        menu();


def baja_Datos():  # Impresión de los datos y baja de los mismos.
    from colorama import Cursor, Back, Fore, init;
    import msvcrt;
    import os;
    init(autoreset=True);

    ventanas(True);
    print(Cursor.POS(54, 4) + Back.WHITE + Fore.BLUE + ">>> BAJA DATOS <<<");

    a = open("d08-p14-danna-medina-W.txt", mode="r", encoding="utf-8");

    lineas = a.readlines();
    a.close();

    x = 54;
    y = 10;

    datosF = [];

    for linea in lineas:
        sel = linea.startswith("Frutería: ");

        if sel == True:
            producto = linea.replace("Frutería: ", "");
            print(Cursor.POS(x, y) + Back.WHITE + Fore.BLACK + producto);
            y += 1;
            if y == 25:
                y = 7;
                x += 59;
            datosF.append(producto);

    if datosF == []:
        print(Cursor.POS(35,16) + Back.WHITE + Fore.BLUE + "No hay datos guardados, presione Enter para volver al menu.");
        print(Cursor.POS(106, 4) + Back.WHITE + Fore.GREEN + "Enter ->");
        input();
        menu();

    else:
        print(Cursor.POS(18, 25) + Back.WHITE + Fore.BLUE + "Presione Enter para dar de baja los datos o presione Esc para salir sin hacer cambios.");
        print(Cursor.POS(106, 4) + Back.WHITE + Fore.GREEN + "Enter ->");
        print(Cursor.POS(8, 4) + Back.WHITE + Fore.RED + "<- Esc");

        while True:
            tecla = msvcrt.getch();

            if tecla == b'\x1b':
                menu();
                break;

            elif tecla == b'\r':
                break;

        a = open("d08-p14-danna-medina-W.txt", mode="w", encoding="utf-8");

        for linea in lineas:
            nom = linea.startswith("Frutería: Nombre: ");
            tel = linea.startswith("Frutería: Teléfono: ");
            cor = linea.startswith("Frutería: Correo: ");

            if (nom == False) and (tel == False) and (cor == False):
                a.write(linea);

        a.close();

        ventanas(True);
        print(Cursor.POS(54, 4) + Back.WHITE + Fore.BLUE + ">>> BAJA DATOS <<<");
        print(Cursor.POS(106, 4) + Back.WHITE + Fore.GREEN + "Enter ->");
        print(Cursor.POS(30,16) + Back.WHITE + Fore.BLUE + "Los datos han sido dados de baja, presione Enter para volver al menu.");
        input();
        menu();


# SECCIÓN VENTAS
def ventas():  # Genera la venta, cambios en el inventario y el ticket de compra.
    from colorama import Cursor, Back, Fore, init;
    from msvcrt import getch;
    import os

    ventanas(True);
    print(Cursor.POS(55, 4) + Back.WHITE + Fore.BLUE + ">>> VENTAS <<<");
    print(Cursor.POS(106, 4) + Back.WHITE + Fore.GREEN + "Enter ->");

    a = open("d08-p14-danna-medina-W.txt", mode="r", encoding="utf-8");
    lineas = a.readlines();
    a.close();

    mostrarInventario();

    try:
        while True:
            print(Cursor.POS(8, 26) + Back.WHITE + Fore.BLACK + "Código del vendedor:      ");
            vend = int(input(Cursor.POS(8, 26) + Back.WHITE + Fore.BLACK + "Código del vendedor: "));
            vend = str(vend);
            if len(vend) == 3:
                break

        existe = validar_Dato_Existente(vend, 10);  # Se verifica si existe algún empleado registrado con ese código
    except:
        print(Cursor.POS(38,28) + Back.WHITE + Fore.RED + "El código no es correcto, presione Enter para continuar.");
        input();
        menu();

    if existe == -1:  # En caso de que no exista el empleado
        print(Cursor.POS(38,28) + Back.WHITE + Fore.RED + "El código no está registrado, presione Enter para continuar.");
        input();
        menu();

    elif existe == 10:
        for linea in lineas:
            emp = linea.startswith("Empleado: " + vend);
            if emp == True:
                dato = linea.split();
                vendedor = dato[2];  # Nombre del empleado en caja

        lista_Compras = [];
        lista_Precios = [];
        lista_Codigos = [];
        lista_Cantidad = [];
        repe = ["si"];
        for i in repe:
            ventanas(True);
            mostrarInventario();

            print(Cursor.POS(55, 4) + Back.WHITE + Fore.BLUE + ">>> VENTAS <<<");
            print(Cursor.POS(106, 4) + Back.WHITE + Fore.GREEN + "Enter ->");
            print(Cursor.POS(8, 26) + Back.WHITE + Fore.BLACK + ("Atendiendo: " + vendedor + "   "));
            print(Cursor.POS(40, 26) + Back.WHITE + Fore.BLACK + "Código del producto: ");
            print(Cursor.POS(80, 26) + Back.WHITE + Fore.BLACK + "Cantidad a vender: ");

            try:
                while True:
                    print(Cursor.POS(40, 26) + Back.WHITE + Fore.BLACK + "Código del producto:       ");
                    codProd = int(input(Cursor.POS(40, 26) + Back.WHITE + Fore.BLACK + "Código del producto: "));
                    codProd = str(codProd);
                    if len(codProd) == 6:
                        break;

                existe = validar_Dato_Existente(codProd, 10);  # Se verifica que exista el producto registrado


                if existe == -1:

                    while True:
                        print(Cursor.POS(40,28) + Back.WHITE + Fore.RED + "El código no está registrado, presione Enter para continuar.");
                        input();
                        ventanas(True);
                        mostrarInventario();
                        print(Cursor.POS(55, 4) + Back.WHITE + Fore.BLUE + ">>> VENTAS <<<");
                        print(Cursor.POS(106, 4) + Back.WHITE + Fore.GREEN + "Enter ->");
                        print(Cursor.POS(8, 26) + Back.WHITE + Fore.BLACK + ("Atendiendo: " + vendedor + "   "));
                        print(Cursor.POS(40, 26) + Back.WHITE + Fore.BLACK + "Código del producto: ");
                        print(Cursor.POS(80, 26) + Back.WHITE + Fore.BLACK + "Cantidad a vender: ");

                        while True:
                            print(Cursor.POS(40, 26) + Back.WHITE + Fore.BLACK + "Código del producto:       ");
                            codProd = int(input(Cursor.POS(40, 26) + Back.WHITE + Fore.BLACK + "Código del producto: "));
                            codProd = str(codProd);
                            if len(codProd) == 6:
                                break;

                        existe = validar_Dato_Existente(codProd, 10);

                        if existe == 10:
                            break;

                        elif existe == -1:
                            print(Cursor.POS(30,28) + Back.WHITE + Fore.RED + "El código no está registrado, presione Enter para volver al menu.");
                            input();
                            menu();

                if existe == 10:

                    for linea in lineas:
                        sel = linea.startswith("Producto: " + codProd);  # Seleccionamos la línea con el código en específico

                        if sel == True:
                            partes = linea.split();
                            invent = partes[4];  # El valor de "Cantidad: " del producto específico
                            inventInt = int(invent);

                    while  True:
                        print(Cursor.POS(80, 26) + Back.WHITE + Fore.BLACK + "Cantidad a vender:                 ");

                        cant = int(input(Cursor.POS(80, 26) + Back.WHITE + Fore.BLACK + "Cantidad a vender: "));

                        if (cant > 0) and (cant <= inventInt):
                            a = open("d08-p14-danna-medina-W.txt", mode="w", encoding="utf-8");
                            break;


                    for linea in lineas:
                        sel = linea.startswith("Producto: " + codProd);  # Seleccionamos la línea con el código en específico

                        if sel == True:
                            partes = linea.split();
                            invent = partes[4];  # El valor de "Cantidad: " del producto específico
                            inventInt = int(invent);
                            prodNom = partes[2];  # Nombre del producto
                            prodPre = float(partes[6]) * cant;
                            precio = str(prodPre);

                            lista_Compras.append(prodNom);
                            lista_Precios.append(precio);
                            lista_Codigos.append(codProd);
                            lista_Cantidad.append(cant);
                            cantTot = inventInt - cant;  # El resultado de la compra
                            cantTotStr = str(cantTot);
                            producto = linea.replace(invent, cantTotStr);
                            a.write(producto);  # Se reemplaza la línea entera por una con la cantidad nueva.

                        elif (sel == False) and (cant <= inventInt):
                                a.write(linea);  # Se escribe nuevamente el inventario

                a.close();
                ventanas(True);
                print(Cursor.POS(55, 4) + Back.WHITE + Fore.BLUE + ">>> VENTAS <<<");
                print(Cursor.POS(106, 4) + Back.WHITE + Fore.GREEN + "Enter ->");
                print(Cursor.POS(55, 12) + Back.WHITE + Fore.BLACK + "¿Vender algo más? ");
                print(Cursor.POS(55, 14) + Back.WHITE + Fore.BLACK + "1- Sí      2- No");

                import msvcrt;
                while True:
                    nueVent = msvcrt.getch();

                    if nueVent == b'1':
                        repe.append("si");
                        break

                    elif nueVent == b'2':
                        suma = 0;
                        for i in lista_Precios:
                            suma = suma + float(i);
                            break

                        print(Cursor.POS(55, 18) + Back.WHITE + Fore.BLACK + "Total a pagar: " + str(suma));


                        while True:
                            print(Cursor.POS(55, 22) + Back.WHITE + Fore.BLACK + "Monto recibido:                 ");
                            monto = float(input(Cursor.POS(55, 22) + Back.WHITE + Fore.BLACK + "Monto recibido: "));


                            if (monto > 0) and (monto >= suma):
                                break;

                        os.system("cls");
                        print(ticket(lista_Compras, lista_Precios, lista_Codigos, lista_Cantidad, vend,vendedor, monto));

                        menu();
            except:
                print(Cursor.POS(33,28) + Back.WHITE + Fore.RED + "El código no está registrado, presione Enter para volver al menu.");
                input();
                menu();


def ticket(lista_Compras, lista_Precios, lista_Codigos, lista_Cantidad, codigoVend, nombreVend, monto):
    from colorama import Cursor, Back, Fore, init;
    import os;
    init(autoreset=True);
    a = open("d08-p14-danna-medina-W.txt", mode="r", encoding="utf-8");
    lineas = a.readlines();
    a.close();

    nombreFru = "Frutería: ";
    telefonoFru = "Teléfono: ";
    correoFru = "Correo: ";

    for linea in lineas:

        sel = linea.startswith("Frutería: Nombre: ");

        if sel == True:
            nombreFru = linea.replace("Frutería: Nombre: ", "");

    for linea in lineas:

        sel = linea.startswith("Frutería: Teléfono: ");

        if sel == True:
            telefonoFru = linea.replace("Frutería: Teléfono: ", "");

    for linea in lineas:

        sel = linea.startswith("Frutería: Correo: ");

        if sel == True:
            correoFru = linea.replace("Frutería: Correo: ", "");

    ventanaT(True);
    print(Cursor.POS(58, 2) + Back.WHITE + Fore.BLACK + "TICKET");
    print(Cursor.POS(44, 4) + Back.WHITE + Fore.BLACK + nombreFru);
    print(Cursor.POS(44, 5) + Back.WHITE + Fore.BLACK + telefonoFru);
    print(Cursor.POS(44, 6) + Back.WHITE + Fore.BLACK + correoFru);
    print(Cursor.POS(44, 8) + Back.WHITE + Fore.BLACK + "Atendió " + codigoVend + " " + nombreVend);

    lisX = 53;
    lisY = 11;
    preX = 73;
    preY = 11;
    codX = 44;
    codY = 11;
    canX = 65;
    canY = 11;

    for x in lista_Compras:
        print(Cursor.POS(lisX, lisY) + Back.WHITE + Fore.BLACK + x);
        lisY += 1;
    for y in lista_Precios:
        print(Cursor.POS(preX, preY) + Back.WHITE + Fore.BLACK + y);
        preY += 1;

    suma = 0;

    for i in lista_Precios:
        suma = suma + float(i);

    for c in lista_Codigos:
        print(Cursor.POS(codX, codY) + Back.WHITE + Fore.BLACK + c);
        codY += 1;

    for k in lista_Cantidad:
        print(Cursor.POS(canX, canY) + Back.WHITE + Fore.BLACK + str(k));
        canY += 1;

    cambio = monto - suma;
    montoStr = str(monto);
    cambioStr = str(cambio);
    print(Cursor.POS(65, 27) + Back.WHITE + Fore.BLACK + "Total:  " + str(suma));
    print(Cursor.POS(65, 28) + Back.WHITE + Fore.BLACK + "Pago:   " + montoStr);
    print(Cursor.POS(65, 29) + Back.WHITE + Fore.BLACK + "Cambio: " + cambioStr);
    input();
    menu();


# SECCIÓN UTILIDADES
def validar_Dato_Existente(dato, tipo):  # Revisa el archivo txt para saber si hay algun dato duplicado, solicitado por paso de parametros.
    a = open("d08-p14-danna-medina-W.txt", mode="r", encoding="utf-8");
    lineas = a.readlines();
    a.close();

    existe = -1;

    for linea in lineas:
        existe = linea.find(dato);

        if existe == tipo:
            break;

    return existe;


def mostrarInventario():
    from colorama import Back, Fore, Cursor, init;
    init(autoreset=True);
    a = open("d08-p14-danna-medina-W.txt", mode="r", encoding="utf-8");
    lineas = a.readlines();
    a.close();

    x = 8;
    y = 7;

    for linea in lineas:
        sel = linea.startswith("Producto: ");

        if sel == True:
            producto = linea.replace("Producto: ", "");
            print(Cursor.POS(x, y) + Back.WHITE + Fore.BLACK + producto);
            y += 1;
            if y == 24:
                y = 7;
                x += 59;


def random(tipo):  # Genera los códigos de los productos y empleados según el paso de parametros.
    import random;

    if tipo == True:
        x = random.randint(100000, 999999);

    elif tipo == False:
        x = random.randint(100, 999);

    return x;


def espacios(palabra, bucle):  # Crea espacios en blanco para simular una tabla en los datos guardados en el txt.
    letras = len(palabra);
    es = " ";
    if letras < bucle:
        for i in range(bucle):
            es += " ";
            letras += 1;
            if letras == bucle:
                break;
    return es;


def ventanaT(doble):  # Ventanas con paso de parametro.
    from colorama import Cursor, Back, Fore, init;
    from itertools import cycle;
    import os;
    init(autoreset=True);
    os.system("cls");

    xMarco = 41;
    yMarco = 2;
    xInterior = 42;
    yInterior = 2;

    # String con espacios en blanco para optimizar el relleno de la ventana
    espacio = "                                      ";

    for i in range(40):
        print(Cursor.POS(xMarco, 1) + Back.WHITE + " ");
        print(Cursor.POS(xMarco, 29) + Back.WHITE + " ");
        xMarco += 1;

    for i in range(26):
        print(Cursor.POS(41, yMarco) + Back.WHITE + " ");
        print(Cursor.POS(80, yMarco) + Back.WHITE + " ");
        print(Cursor.POS(42, yInterior) + Back.WHITE + espacio);
        yMarco += 1;
        yInterior += 1;

    if doble == True:  # Se valida el parametro pasado para dibujar o no el doble recuadro.
        for i in range(27):
            print(Cursor.POS(42, 3) + Fore.BLACK + espacio);


def ventanas(doble):  # Ventanas con paso de parametro.
    from colorama import Cursor, Back, Fore, init;
    from itertools import cycle;
    import os;
    init(autoreset=True);

    xMarco = 6;
    yMarco = 3;
    xInterior = 7;
    yInterior = 3;

    # String con espacios en blanco para optimizar el relleno de la ventana
    espacio = "                                                                                                            ";

    for i in range(110):
        print(Cursor.POS(xMarco, 2) + Back.CYAN + " ");
        print(Cursor.POS(xMarco, 29) + Back.CYAN + " ");
        xMarco += 1;

    for i in range(26):
        print(Cursor.POS(6, yMarco) + Back.CYAN + " ");
        print(Cursor.POS(115, yMarco) + Back.CYAN + " ");
        print(Cursor.POS(7, yInterior) + Back.WHITE + espacio);
        yMarco += 1;
        yInterior += 1;

    if doble == True:  # Se valida el parametro pasado para dibujar o no el doble recuadro.
        for i in range(26):
            print(Cursor.POS(7, 6) + Back.CYAN + espacio);


def datos():  # Datos de los programadores.
    from colorama import Cursor, Back, Fore;
    print(Cursor.POS(68, 28) + Back.WHITE + Fore.BLACK + "                                Danna Paola");


def menu():  # Menu del programa.
    from colorama import Cursor, Back, Fore, init;
    import msvcrt;
    import os;
    init(autoreset=True);
    os.system("cls");
    ventanas(False);
    datos();

    opcion = 1;

    a = open("d08-p14-danna-medina-W.txt", mode="r", encoding="utf-8");
    lineas = a.readlines();
    a.close();

    nombreFru = "   ABC";

    for linea in lineas:

        sel = linea.startswith("Frutería: Nombre:");

        if sel == True:
            nombreFru = linea.replace("Frutería: Nombre: ", "");
            break;

    while True:
        print(Cursor.POS(57, 4) + Back.WHITE + Fore.BLUE + nombreFru);
        print(Cursor.POS(55, 8) + Back.WHITE + Fore.BLACK + "  1. ALTAS  ");
        print(Cursor.POS(55, 12) + Back.WHITE + Fore.BLACK + "  2. BAJAS  ");
        print(Cursor.POS(55, 16) + Back.WHITE + Fore.BLACK + "  3. VENTA(S)  ");
        print(Cursor.POS(55, 20) + Back.WHITE + Fore.BLACK + "  4. SALIR  ");
        print(Cursor.POS(106, 4) + Back.WHITE + Fore.GREEN + "Enter ->");
        print(Cursor.POS(30,
                         24) + Back.WHITE + Fore.RED + "Presione el número de la opción o seleccione con las flechas");
        if opcion == 1:
            print(Cursor.POS(55, 8) + Fore.BLACK + Back.YELLOW + "> 1. ALTAS <");

        elif opcion == 2:
            print(Cursor.POS(55, 12) + Fore.BLACK + Back.YELLOW + "> 2. BAJAS <");

        elif opcion == 3:
            print(Cursor.POS(55, 16) + Fore.BLACK + Back.YELLOW + "> 3. VENTA(S) <");

        elif opcion == 4:
            print(Cursor.POS(55, 20) + Fore.BLACK + Back.YELLOW + "> 4. SALIR <");

        tecla = msvcrt.getch();

        if tecla == b'H':
            opcion -= 1;

        elif tecla == b'P':
            opcion += 1;

        elif tecla == b'\r':
            break;

        elif tecla == b'1':
            opcion = 1;
            break;

        elif tecla == b'2':
            opcion = 2;
            break;

        elif tecla == b'3':
            opcion = 3;
            break;

        elif tecla == b'4':
            opcion = 4;
            os.system("cls");
            break;

        if opcion < 1:
            opcion = 4;

        elif opcion > 4:
            opcion = 1;


    e1(opcion);


menu();
