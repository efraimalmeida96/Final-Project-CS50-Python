# EFRAIM ALMEIDA 
# CURITIBA, BRAZIL JUNE 10th 2025
# CALCULUS CALCULATOR 
# ACELERATION, VELOCITY, POSITION 

import sympy

def main():
    display()
    
    while True:

        movement = input('What movement do you have? ')
        new_movement = input('What movement do you want to know? ')

        while True:

            func_input = input('Type the Function: ')
            if func_input == '0':
                print('Zero is not accepted, Type again.')
                continue

            try:
                func = sympy.sympify(func_input)
                break
            except (sympy.SympifyError, ValueError): # 5*? MISSING VARIABLE
                print('Invalid function syntax. Type again.')

        print()
        option_of_movement(movement, new_movement, func_input)

        if exit_program() == True:
            continue
        else:
            print('EXITING...')
            break
 
    #aaaaaaaaaa
def display():

    print('-=' * 15)
    print(f'{'CALCULUS CALCULATOR':^30}')
    print('-=' * 15)

    movement_display = {
        1: 'Acceleration',
        2: 'Velocity',
        3: 'Position',
    }

    for k, v in movement_display.items():
        print(f'{v:.<25}. [{k}]')
    print('Choose the movement by typing the number.')
    print('The constant in an integral function must be typed with a capital "C".')

def option_of_movement(mvt, new_mvt, fnc_inpt):

    if mvt == '1' and new_mvt == '2': # ACCELERATION TO VELOCITY
        m = Movement(fnc_inpt)
        result = m.integral()
        print(f'The INTEGRAL of [ {fnc_inpt} ] is:')
        print(f'{result}')

    if mvt == '1' and new_mvt == '3':# ACCELERATON TO POSITION
        m = Movement(fnc_inpt)
        first = m.integral()
        m_2 = Movement(first)
        second = m_2.integral()
        print(f'The 2nd INTEGRAL of [ {fnc_inpt} ] is:')
        print(f'{second}')

    if mvt == '2' and new_mvt == '1': # VELOCITY TO ACCELERATION
        m = Movement(fnc_inpt)
        result = m.difference()
        print(f'The DIFFERENCE of [ {fnc_inpt} ] is:')
        print(f'{result}')

    if mvt == '2' and new_mvt == '3': # VELOCITY TO POSITION 
        m = Movement(fnc_inpt)
        result = m.integral()
        print(f'The INTEGRAL of [ {fnc_inpt} ] is:')
        print(f'{result}')

    if mvt == '3' and new_mvt == '2': # POSITION TO VELOCITY
        m = Movement(fnc_inpt)
        result = m.difference()
        print(f'The DIFFERENCE of [ {fnc_inpt} ] is:')
        print(result)

    if mvt == '3' and new_mvt == '1': # POSITION TO ACCELERATION
        m = Movement(fnc_inpt)
        first = m.difference()
        m_2 = Movement(first)
        second = m_2.difference()
        print(f'The 2nd DIFFERENCE of [ {fnc_inpt} ] is:')
        print(second)


def exit_program():

    quit = input('Do you want to calculate another function? [Y / N]: ')
    print()
    
    if quit in 'yYYESyesYes':
        return True
    else:
        return False

class Movement:

    def __init__(self, func):
        self.func = sympy.sympify(func)
        self.x = sympy.symbols('x')
        self.y = sympy.symbols('y')
        self.z = sympy.symbols('z')
        self.t = sympy.symbols('t')
        self.c = sympy.symbols('C')
        self.order_term = {}
    
      
    def difference(self):
        dif = sympy.diff(self.func, self.check_letter())
        return self.reverse_term_order_diff(dif)
    
    def integral(self):
        if not self.func.free_symbols:
            term = self.func * self.x
            return self.reverse_term_order_integral(term, self.c)
            
        else:
            inte = sympy.integrate(self.func, self.check_letter())
            return self.reverse_term_order_integral(inte, self.c)
        
    def reverse_term_order_diff(self, expr):

        final_str = ''
        exprs_str = str(expr)

        if exprs_str.startswith("C"): # FIRST DIFF
            remove_spaces = exprs_str.replace(" ", "")
            index = remove_spaces.index("+")
            final_str = f'{remove_spaces[index + 1:]} + {remove_spaces[:index]}'
            return final_str
        
        return exprs_str

        
    def reverse_term_order_integral(self, expr, ex_c): # STRING MANIPULATION

        as_orded_term = expr.as_ordered_terms()
        if len(as_orded_term) == 1:
            order_print = ''
            order_print += f'{as_orded_term[0]} + {ex_c}'
            return  order_print
        
        else:
            order_print2 = ''
            for order in as_orded_term:
                self.order_term[order] = self.power_of(order)

            order_dict = dict(sorted(self.order_term.items(), key=lambda item: item[1]))
            reverse_dict = reversed(list(order_dict.keys()))

            for term in reverse_dict:

                new_term = str(term)
                if new_term.startswith("C"):
                    term = f' + {term}'

                order_print2 += f'{term}'

            order_print2 += f' + {ex_c}'
            return order_print2

    def power_of(self, variable_str):

        variable_str = str(variable_str)
        if '*cos' in variable_str or '*sin' in variable_str:
            return int(len(self.order_term) + 1)
        if '**' in variable_str:
            return int(variable_str.split("**")[1][0])
        elif '*' in variable_str:
            return 1
        else:
            return 0


    def check_letter(self): # VERIFY ALL THE PRESENT SYMBOLS IN THE EXPRESSION 
        if self.x in self.func.free_symbols:
            return self.x
        if self.y in self.func.free_symbols:
            return self.y
        if self.z in self.func.free_symbols:
            return self.z
        if self.t in self.func.free_symbols:
            return self.t
        if self.c in self.func.free_symbols:
            return self.c

    def __str__(self):
        return f'{self.integral()}'

    def __str__(self):
        return f'{self.difference()}'

if __name__ == "__main__":
    main()