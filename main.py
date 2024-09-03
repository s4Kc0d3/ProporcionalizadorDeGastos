import pandas as pd
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

def calcular_aportes():
	"""
	Calcula la contribución de cada usuario a los gastos mensuales de la casa
	en función de sus ingresos.
	"""
	# Solicitar el número de personas con ingresos
	num_usuarios = int(input("¿Cuántas personas tienen ingresos en casa? "))

	# Inicializar listas para los nombres de los usuarios y sus ingresos
	nombres = []
	ingresos = []

	# Recoger los ingresos de cada usuario
	for i in range(num_usuarios):
		nombre = input(f"Ingrese el nombre del usuario {i + 1}: ")
		ingreso = float(input(f"Ingrese el ingreso mensual de {nombre}: "))
		nombres.append(nombre)
		ingresos.append(ingreso)

	# Crear un DataFrame con los datos de ingresos
	df = pd.DataFrame({'Nombre': nombres, 'Ingreso': ingresos})

	# Solicitar el gasto mensual total
	gasto_mensual = float(input("Ingrese el gasto mensual total: "))

	# Calcular el ingreso total
	ingreso_total = df['Ingreso'].sum()

	# Calcular el porcentaje de contribución de cada usuario
	df['Porcentaje_Contribucion'] = df['Ingreso'] / ingreso_total

	# Calcular cuánto debe pagar cada usuario y redondear a dos decimales
	df['Pago'] = (df['Porcentaje_Contribucion'] * gasto_mensual).round(2)

	# Mostrar el DataFrame con los resultados
	print(f"\n{Fore.CYAN}Distribución de pagos:")
	for index, row in df.iterrows():
		print(
			f"{Fore.YELLOW}Nombre: {row['Nombre']} "
			f"{Fore.GREEN}| Ingreso: {row['Ingreso']} € "
			f"{Fore.MAGENTA}| Porcentaje de Contribución: {row['Porcentaje_Contribucion']:.2%} "
			f"{Fore.RED}| Pago: {row['Pago']} €"
		)

	# Mostrar los totales
	print(f"\n{Style.BRIGHT}{Fore.CYAN}Gasto mensual total: {Fore.GREEN}{gasto_mensual} €")
	print(f"{Style.BRIGHT}{Fore.CYAN}Ingreso total de todos los usuarios: {Fore.GREEN}{ingreso_total} €")


def main():
	"""
	Función principal que ejecuta el cálculo de los aportes.
	"""
	calcular_aportes()


if __name__ == "__main__":
	main()
