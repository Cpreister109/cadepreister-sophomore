import formulas as form
import sys

def main():

    op_list = sys.argv

    if len(op_list) <= 1:

        sys.exit('Need to provide operator')

    elif len(op_list) <= 3:

        sys.exit('Need to provide at least two values')

    else:

        val_list = [float(i) for i in op_list[2:]]

        if op_list[1] == 'add':

            print(f'{form.add(val_list):.2f}')

        elif op_list[1] == 'subtract':

            print(f'{form.subtract(val_list):.2f}')

        elif op_list[1] == 'multiply':

            print(f'{form.multiply(val_list):.2f}')

        elif op_list[1] == 'divide':

            print(f'{form.divide(val_list):.2f}')

        else:

            print('Valid operator names (add, subtract, multiply, divide)')

if __name__ == "__main__":

    main()