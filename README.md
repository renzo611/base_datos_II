# 🥜 Sistema de Monitoreo y Control de Secado de Nueces - Base de Datos II

El proceso de secado de nueces requiere un control preciso de variables como temperatura, humedad, peso y consumo de gas para asegurar la calidad del producto final. Este sistema permite optimizar dicho proceso mediante monitoreo en tiempo real y automatización inteligente.

---

## 🚀 Objetivos del Sistema

- 📈 **Control en tiempo real** de temperatura, humedad, peso y gas.
- 💧 **Monitoreo de la pérdida de humedad** durante el proceso.
- 🚨 **Alertas automáticas** ante desvíos en parámetros ideales.
- 🧠 **Análisis histórico** para mejorar la eficiencia del proceso.
- 🔥 **Control del consumo de gas** por lote de secado.

---

## 🧱 Arquitectura del Sistema

### 🔸 Bases de Datos NoSQL
- **MongoDB**: Registra los lotes, historial de secado, tipo de nuez, etc.
- **Redis**: Almacena datos en tiempo real (temperatura, humedad, peso).

### 🔸 Dispositivos y Sensores

| Tipo de Sensor      | Función                                        | Ejemplo / Costo Aprox.               |
|---------------------|----------------------------------------------- |--------------------------------------|
| Temperatura         | Controla el aire del horno                     | DHT22 (~15 USD)                      |
| Humedad             | Mide humedad ambiental e interna de la nuez    | DHT22                                |
| Peso                | Determina la pérdida de humedad                | Celdas de carga + HX711 (~20 USD)    |
| Gas                 | Mide el caudal de gas consumido                | YF-S401 (~6000 ARS)                  |

---

## 🌐 Comunicación y Transmisión de Datos

- **Redes LoRaWAN/Bluetooth**: Comunicación de sensores al gateway central.
- **IoT Gateway (Raspberry Pi 4)**: Centraliza y envía datos a la nube vía 4G LTE o Wi-Fi.

---
![ChatGPT Image 24 may 2025, 07_47_09 a m](https://github.com/user-attachments/assets/f9805dba-9b64-465d-807f-a2258cf96d08)


## 🔄 Proceso de Secado

1. **Inicio del Secado**
   - Registro de lote: tipo de nuez, peso inicial, humedad inicial, horno asignado.
   - Almacenado en MongoDB.

2. **Monitoreo Continuo**
   - Sensores miden temperatura, humedad, peso y consumo de gas.
   - Datos enviados a Redis para acceso inmediato.

3. **Ajustes Automáticos**
   - El sistema regula automáticamente resistencias, ventiladores, etc., según las condiciones actuales.

4. **Alerta de Secado Completo**
   - Basado en la pérdida de peso.
   - Generación de alertas automáticas.

5. **Historial de Secado**
   - Datos completos almacenados en MongoDB.
   - Útil para análisis, auditorías y mejoras del proceso.

---

## 📊 Beneficios del Sistema

- ⚡ **Eficiencia Energética**: Reducción del consumo de gas y electricidad.
- 🌰 **Calidad del Producto**: Mejor control = mejor nuez.
- 📉 **Optimización del Proceso**: Reducción de errores y desperdicio.
- 🤖 **Automatización**: Menor intervención manual.

---

## 🧠 Tecnologías Utilizadas

- 🐍 Python
- 📦 MongoDB (NoSQL)
- 🔁 Redis
- 📡 LoRaWAN / Bluetooth
- 🖥️ Raspberry Pi (IoT Gateway)
- 📶 Módulo 4G LTE
- ⚙️ Sensores DHT22, HX711, YF-S401


## 🧪 Proceso de Ejecución

Para poner en marcha el entorno y comenzar a trabajar con este proyecto, seguí estos pasos:

### 0. Crea y activa un entorno virtual
```bash
python -m venv venv
source venv/bin/activate    # En Linux/Mac
venv\Scripts\activate       # En Windows
```     

### 1. Instala las dependencias necesarias
```bash
pip install -r requirements.txt
```
O
```bash
pip3 install -r requirements.txt
```

### 2. Crear un archivo `.env` y copiar las variables de entorno del archivo `.env.template`

### 3. Levantar los servicios con Docker Compose

Asegurate de estar ubicado en el mismo directorio donde se encuentra el archivo `docker-compose.yml`. Luego ejecutá el siguiente comando en la terminal:

```bash
docker-compose up -d
```

### 4. Ejecutar el script de carga de datos

```bash
python insert_fields.py
```

### 5. Ejecutar el análisis desde Jupyter Notebook

Abrí el archivo `dao_nuts.ipynb` usando Jupyter Notebook o algún entorno como VS Code con soporte para notebooks. Ejecutá las celdas para interactuar con los datos y analizar la información procesada.
