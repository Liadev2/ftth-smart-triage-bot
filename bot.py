"""
FTTH Smart Triage Bot (Simulación)
---------------------------------
Asistente técnico que simula el diagnóstico real de un ISP FTTH.

⚠️ Proyecto educativo.
No usa datos reales ni se conecta a sistemas reales.
"""

# ==============================
# BASE DE DATOS SIMULADA (CRM + OLT)
# ==============================

clientes = {
    "1234V": {
        "dni": "1234V",
        "nombre": "Juan",
        "optical_power": -28,      # dBm
        "averia_masiva": False,
        "wifi_enabled": False
    },
    "5678X": {
        "dni": "5678X",
        "nombre": "Marta",
        "optical_power": -19,      # dBm
        "averia_masiva": True,
        "wifi_enabled": True
    }
}

# ==============================
# FUNCIONES PRINCIPALES
# ==============================

def identificar_cliente():
    print("\n--- BIENVENIDO AL ASISTENTE TÉCNICO ISP ---")
    dni = input("Introduce tu DNI o ID de cliente: ").upper()

    if dni not in clientes:
        print("❌ Cliente no encontrado. Derivando a un agente humano.")
        return None

    cliente = clientes[dni]

    if cliente["averia_masiva"]:
        print("⚠️ Detectamos una avería general en tu zona.")
        print("Nuestros técnicos ya están trabajando. Tiempo estimado: 3 horas.")
        return None

    return cliente


def diagnostico_optico(cliente):
    print(f"\n[Analizando señal óptica para {cliente['nombre']}]")

    if cliente["optical_power"] < -26:
        print(
            "🆘 Señal óptica fuera de margen.\n"
            "Revisa que el latiguillo de fibra no esté doblado, presionado o suelto.\n"
            "Si está desconectado, fíjate en la pequeña marca del conector e introdúcelo hasta oír 'click'."
        )

        respuesta = input("¿Has podido revisarlo? (SI/NO): ").upper()

        if respuesta == "SI":
            # Simulación de corrección
            cliente["optical_power"] = -22
            print("✅ Señal recuperada. Valores dentro de rango.")
            print("Tu conexión debería restablecerse en unos instantes.")
        else:
            print("📅 No es posible acceder al equipo.")
            print("Se programa visita técnica (problema Capa 1).")
    else:
        print("✅ Señal óptica correcta. No se detectan problemas físicos.")


def diagnostico_wifi(cliente):
    print("\n[Analizando configuración WiFi del router]")

    if not cliente["wifi_enabled"]:
        print("💡 El WiFi estaba desactivado en el router.")
        print("Activándolo remotamente...")
        cliente["wifi_enabled"] = True

    respuesta = input("¿Ahora ves tu red WiFi? (SI/NO): ").upper()

    if respuesta == "SI":
        print("✅ WiFi operativo.")
        ayuda_extra = input("¿Puedo ayudarte en algo más? (SI/NO): ").upper()

        if ayuda_extra == "SI":
            print(
                "\nPuedo ayudarte con:\n"
                "- WiFi lento\n"
                "- Poco alcance\n"
                "- Colocación del router y antenas"
            )
        else:
            print("Gracias por contactar. ¡Buen día!")
    else:
        print("❌ El WiFi sigue sin estar disponible.")
        print("Se programa revisión técnica del equipo.")


def diagnostico_velocidad(cliente):
    print("\n--- ANALIZADOR DE VELOCIDAD POR CABLE ETHERNET ---")

    # Simulación de lectura de puerto LAN
    puerto_link = 100  # Mbps

    if puerto_link < 1000:
        print(f"⚠️ El enlace Ethernet está negociando a {puerto_link} Mbps.")
        print("Esto limita la velocidad de tu fibra.")

        info_cables = {
            "Cat 5": "❌ Máximo 100 Mbps (obsoleto)",
            "Cat 5e": "✅ Hasta 1 Gbps (mínimo recomendado)",
            "Cat 6 / 6a": "🚀 Hasta 10 Gbps (ideal)"
        }

        print("\nTipos de cable Ethernet:")
        for cat, desc in info_cables.items():
            print(f"- {cat}: {desc}")

        print("\n💡 Consejo técnico:")
        print("Si el conector solo tiene 4 hilos, nunca superará los 100 Mbps.")
    else:
        print("✅ Enlace Gigabit detectado.")
        print("La lentitud podría deberse al dispositivo o saturación local.")


# ==============================
# FLUJO PRINCIPAL
# ==============================

cliente = identificar_cliente()

if cliente:
    print(f"\nHola {cliente['nombre']}, ¿en qué puedo ayudarte hoy?")

    opcion = input(
        "\n1. No tengo Internet\n"
        "2. No tengo WiFi\n"
        "3. Internet lento por cable\n"
        "Selecciona una opción: "
    )

    if opcion == "1":
        diagnostico_optico(cliente)
    elif opcion == "2":
        diagnostico_wifi(cliente)
    elif opcion == "3":
        diagnostico_velocidad(cliente)
    else:
        print("Opción no válida.")
