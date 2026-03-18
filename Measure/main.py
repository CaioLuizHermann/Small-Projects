import convert
import input_utils
end = False
while end == False:
    try:
        first_measure_system = input_utils.input_first_measure_system()
        if first_measure_system == 4:
            print("Exiting Program...")
            end = True
            continue
        m1 = input_utils.input_quantity()
        meters = convert.convert_to_meters()
        second_measure_system = input_utils.input_second_measure_system()
        result = convert.convert_from_meters()
        print("The result is...", result)
    except ValueError:
        print("Erro 0: Valor inválido")
        continue    