# Zoom Recordings Downloader

Este script descarga automáticamente las grabaciones de Zoom dentro de un rango de fechas específico. Utiliza la API de Zoom para obtener los enlaces de descarga y guarda los archivos en una estructura organizada por fecha.

## 🚀 Instalación y Configuración

### 1️⃣ Clonar el repositorio
```sh
git clone https://github.com/tuusuario/zoom-downloader.git
cd zoom-downloader
```

### 2️⃣ Crear un entorno virtual (opcional pero recomendado)
```sh
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3️⃣ Instalar dependencias
```sh
pip install -r requirements.txt
```

### 4️⃣ Configurar la API de Zoom
Para usar este script, necesitas crear una aplicación en el Marketplace de Zoom y obtener las credenciales necesarias.

1. Accede a [Zoom App Marketplace](https://marketplace.zoom.us/).
2. Inicia sesión con tu cuenta de Zoom.
3. Crea una nueva aplicación con el tipo **"Server-to-Server OAuth"**.
4. En la pestaña **"App Credentials"**, copia los valores de `Client ID`, `Client Secret` y `Account ID`.
5. En la pestaña **"Scopes"**, añade los siguientes permisos:
   - `recording:read:admin` (Para leer grabaciones)
   - `report:read:admin` (Para acceder a los reportes de reuniones)
   - `meeting:read:admin` (Para obtener detalles de las reuniones)
6. Guarda los cambios y activa la aplicación.

### 5️⃣ Configurar credenciales

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```ini
CLIENT_ID=tu_client_id
CLIENT_SECRET=tu_client_secret
ACCOUNT_ID=tu_account_id
```

Asegúrate de reemplazar `tu_client_id`, `tu_client_secret` y `tu_account_id` con las credenciales reales de la API de Zoom.

### 6️⃣ Configurar fechas de descarga
Edita el archivo `Zoom_Downloader_v2.py` y cambia los valores de `start_date` y `end_date` en la función `main()`:

```python
start_date = "2025-01-01"  # Fecha de inicio
end_date = "2025-12-31"    # Fecha de fin
```

## 📥 Uso
Ejecuta el script con el siguiente comando:
```sh
python Zoom_Downloader_v2.py
```

El script descargará todas las grabaciones disponibles en el período especificado y las almacenará en `zoom_recordings/` organizadas por año y mes.

## 🛠️ Solución de Problemas
- **Error 400 (Bad Request)**: Verifica que la API de Zoom está activada y que las credenciales son correctas.
- **Rate Limit Exceeded**: Si la API de Zoom limita la cantidad de solicitudes, el script esperará automáticamente antes de reintentar.
- **Faltan grabaciones**: Asegúrate de que la cuenta tiene permisos suficientes para acceder a todas las grabaciones.

## 📜 Licencia
Este proyecto está bajo la licencia MIT. Puedes modificar y distribuir libremente el código.

---
**¡Listo! Ahora puedes descargar tus grabaciones de Zoom automáticamente! 🚀**

