# Expense Tracker CLI

Este proyecto es una herramienta de línea de comandos para rastrear tus gastos. Permite agregar, listar, resumir y eliminar gastos de un archivo JSON.

## Requisitos

- Python 3.x
- Módulos: `argparse`, `os`, `json`, `datetime`

## Instalación

1. Clona el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
```

2. Asegúrate de tener Python instalado. Puedes verificarlo con:

```bash
python --version
```

## Uso

El programa se ejecuta desde la línea de comandos. Aquí están los comandos disponibles:

### 1. Agregar un gasto

```bash
python expense-tracker.py add --description "Descripción del gasto" --amount 100.50
```

### 2. Listar gastos

```bash
python expense-tracker.py list
```

### 3. Resumir gastos

Para obtener un resumen de todos los gastos:

```bash
python expense-tracker.py summary
```
Para obtener un resumen de los gastos de un mes específico (por ejemplo, octubre):

```bash
python expense-tracker.py summary --month 10
```

### 4. Eliminar un gasto

```bash
python expense-tracker.py delete --id 1
```

## Notas

- El archivo de gastos se guarda en `expenses.json`. Si no existe, se creará automáticamente.
- Asegúrate de proporcionar los argumentos requeridos al usar los comandos.

## Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o enviar un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.
