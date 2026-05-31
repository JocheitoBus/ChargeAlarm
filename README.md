# 🔋 Power Alarm - Alarma de Carga Móvil

Aplicación móvil diseñada con **Python** y el framework **Flet**, estructurada bajo los principios de **Arquitectura Limpia (Clean Architecture)**. Su función principal es emitir una alerta sonora en tiempo real en el momento exacto en que el dispositivo móvil se conecta a una fuente de energía eléctrica.

---

## 🎯 1. Objetivo del Proyecto

El propósito de este proyecto es construir una aplicación móvil funcional, mantenible y escalable utilizando un ecosistema puramente basado en Python. Al aplicar Arquitectura Limpia, se busca desacoplar por completo las reglas del negocio de los componentes volátiles como la interfaz gráfica (UI) y las librerías de hardware del sistema operativo.

### Funcionalidades Clave:
*   **Monitoreo de Energía:** Conocer el estado de carga actual del dispositivo (conectado/desconectado).
*   **Eventos Reactivos:** Reaccionar inmediatamente ante el evento físico de inicio de carga.
*   **Personalización de Alertas:** Acceder al almacenamiento local del teléfono para seleccionar archivos de audio personalizados (`.mp3` o similares).
*   **Control del Estado:** Permitir al usuario programar, activar o desactivar la alarma a través de un panel interactivo.
*   **Desacoplamiento:** Simular o integrar el estado del hardware mediante servicios independientes de la interfaz de usuario.

---

## 🛠️ 2. Stack Tecnológico

*   **Lenguaje Core:** Python 3.10+
*   **Framework de Interfaz de Usuario:** Flet (motor UI basado en Flutter adaptado a Python)
*   **Gestión de Audio:** Componente nativo `flet.Audio`
*   **Monitoreo del Sistema:** Servicios nativos/librerías de sensores (según la abstracción de la capa de datos)
*   **Entorno de Desarrollo (IDE):** Visual Studio Code
*   **Compilación y Despliegue:** GitHub Actions (automatización de compilación de archivos `.apk` en la nube)

---

## 📂 3. Estructura del Proyecto (Clean Architecture)

El código fuente se organiza de forma modular en capas independientes dentro del directorio `src/`. Cada capa tiene una única responsabilidad y la dependencia de datos siempre fluye de afuera hacia adentro (hacia el Dominio):

```text
power_alarm/
│
├── .github/
│   └── workflows/
│       └── build.yml          # Configuración de compilación automatizada en la nube
│
├── src/
│   ├── __init__.py
│   │
│   ├── domain/                # Capa 1: Lógica de Negocio Pura (Independiente)
│   │   ├── __init__.py
│   │   ├── entities.py        # Modelos de datos de negocio (ej. Alarma, EstadoBateria)
│   │   ├── interfaces.py      # Contratos/Interfaces abstractas de repositorios
│   │   └── use_cases.py       # Casos de uso de la app (ej. ActivarAlarma, VerificarCarga)
│   │
│   ├── data/                  # Capa 2: Repositorios, Hardware e Infraestructura
│   │   ├── __init__.py
│   │   ├── battery_service.py # Monitoreo físico o simulado de la corriente eléctrica
│   │   ├── audio_service.py   # Selector de archivos y reproductor de sonido
│   │   └── repositories.py    # Implementación concreta de los contratos del dominio
│   │
│   ├── presentation/          # Capa 3: Interfaz Gráfica de Usuario (Flet UI)
│   │   ├── __init__.py
│   │   ├── views.py           # Vistas, pantallas y diseño visual interactivo
│   │   └── view_models.py     # Manejadores de estado y controladores de eventos de la UI
│   │
│   └── main.py                # Punto de entrada de la aplicación e Inyección de Dependencias
│
├── README.md                  # Este archivo informativo
└── requirements.txt           # Dependencias y paquetes del proyecto