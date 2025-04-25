# FSRS Service API

**Descripción del proyecto:**
Este repositorio contiene la API del "FSRS Service" implementada con FastAPI. Su función principal es proporcionar la lógica del algoritmo de repetición espaciada FSRS (utilizando la librería `py_fsrs`) para la aplicación DeCajon. Este servicio se comunica con el backend de Spring Boot para gestionar los datos de las piezas musicales (Cards) y el historial de repasos, permitiendo una programación optimizada de la práctica musical.

## Arquitectura
![Diagrama a bloques de la arquitectura del sistema completo](assets/blockdiagram.png)

Este servicio FastAPI actúa como una capa intermedia entre el backend de Spring Boot (que gestiona la base de datos PostgreSQL y la comunicación con la aplicación React Native) y la lógica del algoritmo FSRS. Spring Boot envía peticiones a esta API para tareas como registrar repasos, obtener recomendaciones, etc., y recibe las respuestas con la información procesada por FSRS.

## Endpoints

A continuación, se describen los endpoints principales de esta API:

* **`POST /fsrs/review_card/{card_id}`:**
    * **Función:** Procesa el resultado de un repaso de una pieza musical (`card_id`).
    * **Entrada (Body):** Espera un JSON con la `rating` dada por el usuario (1-4), la `review_datetime` (en formato ISO), y la información actual de la `Card` desde Spring Boot (`card_data`).
    * **Salida:** Retorna un JSON que representa la `Card` actualizada con la nueva fecha de próximo repaso y otros parámetros modificados por el algoritmo FSRS.

[TBD]

## Requisitos

* Python 3.7+
* FastAPI
* Uvicorn
* `py_fsrs`
* `httpx` (si tu FastAPI se comunica de vuelta con Spring Boot para obtener datos)

Puedes instalar las dependencias usando:

```bash
pip install -r requirements.txt