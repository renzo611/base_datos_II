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


