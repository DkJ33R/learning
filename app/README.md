# Learning

Proyecto de aprendizaje en Node.js/Express para practicar JavaScript y desarrollo backend.

---

## 1. Instalar Git (macOS y Windows)

1. Ve a la página oficial de descargas de Git:  
   [https://git-scm.com/downloads](https://git-scm.com/downloads)
2. Elige tu sistema operativo (**macOS** o **Windows**).
3. Descarga el instalador y sigue las instrucciones:
   - **Windows:** Ejecuta el archivo `.exe` descargado y sigue el asistente.
   - **macOS:** Abre el archivo `.dmg` y sigue los pasos de instalación.
4. Verifica la instalación abriendo una terminal y ejecutando:
   ```sh
   git --version
   ```

---

## 2. Instalar Node.js

1. Ve a [https://nodejs.org/](https://nodejs.org/) y descarga la versión LTS para tu sistema operativo.
2. Instala siguiendo las instrucciones del instalador.
3. Verifica la instalación en la terminal:
   ```sh
   node --version
   npm --version
   ```

---

## 3. Clonar y lanzar la aplicación

1. Clona el repositorio:
   ```sh
   git clone https://github.com/DkJ33R/learning.git
   cd learning/learning/app
   ```
2. Instala las dependencias:
   ```sh
   npm install
   ```
3. Lanza la aplicación:
   ```sh
   npm start
   ```
   El servidor se iniciará en [http://localhost:3000](http://localhost:3000)

---

## 4. Ejecutar archivos dentro de `study` con Node.js

Dentro de la carpeta `learning/learning/app/study` hay varios archivos JavaScript para practicar conceptos.

Para ejecutar cualquiera de estos archivos, usa el siguiente comando desde la carpeta `study`:

```sh
cd learning/learning/app/study
node nombre_del_archivo.js
```
Por ejemplo:
```sh
node condicional.js
```

---

## 5. Endpoints principales de la app

- **Raíz:**  
  [http://localhost:3000/](http://localhost:3000/)  
  Devuelve: `Hello World Juan Esteban!`

- **Operaciones matemáticas:**  
  [http://localhost:3000/math?value1=2&value2=3&operation=suma](http://localhost:3000/math?value1=2&value2=3&operation=suma)  
  Operaciones soportadas: `suma` (suma), `resta` (resta)

---

## 6. Recursos útiles

- [Descargar Git](https://git-scm.com/downloads)
- [Descargar Node.js](https://nodejs.org/)
- [Repositorio del proyecto](https://github.com/DkJ33R/learning)

---

¡Feliz aprendizaje!

