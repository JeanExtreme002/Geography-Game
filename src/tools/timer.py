from tkinter import IntVar


class Timer(object):

    def __init__(self, tk_instance):

        self.__tk_instance = tk_instance


    def __wait_while(self, stop_function):

        """
        Espera enquanto a função de parada retornar False.
        """
        
        if not stop_function(): 
            self.__tk_instance.after(100, lambda: self.__wait_while(stop_function))

        else:
            self.__var.set(1)


    def wait(self, time_ms):

        """
        Espera um tempo em segundos.
        """

        var = IntVar()

        self.__tk_instance.after(time_ms, lambda: var.set(1))
        self.__tk_instance.wait_variable(var)


    def wait_while(self, stop_function):

        """
        Espera até que a chamada da função de parada retorne True.
        """

        self.__var = IntVar()
        self.__wait_while(stop_function)
        self.__tk_instance.wait_variable(self.__var)



