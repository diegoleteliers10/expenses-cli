import argparse
import os
import json

# Verificar si el archivo JSON existe, si no, crearlo
json_file = 'expenses.json'
if not os.path.exists(json_file):
    with open(json_file, 'w') as f:
        json.dump([], f)  # Inicializa con una lista vacía
        


parser = argparse.ArgumentParser(
    prog='Expense Tracker',
    description='Track your expenses')

parser.add_argument('command', choices=[
                    'add', 'list', 'summary', 'delete'], help=['Comando para añadir un gasto', 'Comando para enlistar los gastos', 'Comando para resumir el total los gastos', 'Comando para borrar un gasto'])
parser.add_argument('--description', type=str,
                    help='Descripción del gasto')
parser.add_argument('--amount', type=float,
                    help='Monto del gasto')
parser.add_argument('--month', type=float,
                    help='Mes del gasto')
parser.add_argument('--id', type=float,
                    help='Borrar un gasto especifico')

args = parser.parse_args()
print(args.command)

if args.command == 'add':
    if not args.description or not args.amount:
        print('Por favor, introduce la descripción con --description y el monto del gasto con --amount')
        exit()
        
    if args.amount < 0:
      print('Por favor, introduce un --amount mayor a 0')
      exit()
      
    # Cargar gastos existentes
    with open(json_file, 'r') as f:
        expenses = json.load(f)
        
    from datetime import datetime
    # Añadir nuevo gasto
    if(len(expenses) ==0):
      expenses.append({'id': len(expenses) + 1, 'date': datetime.now().strftime("%Y-%m-%d"), 'description': args.description, 'amount': args.amount})
    else:
      expenses.append({'id': expenses[-1]['id'] + 1, 'date': datetime.now().strftime("%Y-%m-%d"), 'description': args.description, 'amount': args.amount})

    # Guardar gastos actualizados
    with open(json_file, 'w') as f:
        json.dump(expenses, f)
    print(f"Expense added successfully(ID: {expenses[-1]['id']})")
        
if args.command == 'list':
    # Cargar gastos existentes
    with open(json_file, 'r') as f:
        expenses = json.load(f)
    print("ID \t Date \t Descripción \t Monto")
    # Imprimir gastos
    for expense in expenses:
        print(f"{expense['id']} \t {expense['date']} \t {expense['description']} \t {expense['amount']}")
        
if args.command == 'summary':
    # Cargar gastos existentes
    with open(json_file, 'r') as f:
        expenses = json.load(f)
        
    Months = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
    total = 0
    
    if args.month:
      for expense in expenses:
        if args.month >= 10 and args.month <= 12:
          if int(expense['date'].split('-')[1]) == args.month:
              total += expense['amount']
        if int(expense['date'].split('-')[1][1]) == args.month:
              total += expense['amount']
      print(f"Total expenses in {Months[args.month]}: {total}")

    # Resumir gastos
    if not args.month:
      for expense in expenses:
          total += expense['amount']
      print(f"Total expenses: {total}")
      
if args.command == 'delete':
    # Cargar gastos existentes
    with open(json_file, 'r') as f:
        expenses = json.load(f)
        
    if not args.id:
      print('Por favor, introduce el ID del gasto a borrar con --id')
      exit()
      
    for expense in expenses:
      if expense['id'] == args.id:
        expenses.remove(expense)
        break
    # Guardar gastos actualizados
    with open(json_file, 'w') as f:
        json.dump(expenses, f)
    print(f"Expense deleted successfully")

