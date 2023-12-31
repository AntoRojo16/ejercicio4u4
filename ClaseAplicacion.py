from tkinter import *
from tkinter import ttk
from functools import partial

class Aplicacion:
    __ventana=None
    __operador=None
    __panel=None
    __operadorAux=None
    __primerOperando=None
    __segundoOperando=None
    
    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.title("Calculadora")
        self.__ventana.config(cursor='heart')
        
        
        self.__panel = StringVar()
        self.__operador=StringVar()
        self.__operadorAux=None
        operatorEntry=ttk.Entry(self.__ventana, width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=(W,E))
        panelEntry = ttk.Entry(self.__ventana, width=20, textvariable=self.__panel, justify='right',state='disabled')
        panelEntry.grid(column=2, row=1, columnspan=2, sticky=(W, E))
        ttk.Button(self.__ventana, text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3, sticky=W)
        ttk.Button(self.__ventana, text='2', command=partial(self.ponerNUMERO, '2')).grid(column=2, row=3, sticky=W)
        ttk.Button(self.__ventana, text='3', command=partial(self.ponerNUMERO, '3')).grid(column=3, row=3, sticky=W)
        ttk.Button(self.__ventana, text='4', command=partial(self.ponerNUMERO, '4')).grid(column=1, row=4, sticky=W)
        ttk.Button(self.__ventana, text='5', command=partial(self.ponerNUMERO, '5')).grid(column=2, row=4, sticky=W)
        ttk.Button(self.__ventana, text='6', command=partial(self.ponerNUMERO, '6')).grid(column=3, row=4, sticky=W)
        ttk.Button(self.__ventana, text='7', command=partial(self.ponerNUMERO, '7')).grid(column=1, row=5, sticky=W)
        ttk.Button(self.__ventana, text='8', command=partial(self.ponerNUMERO, '8')).grid(column=2, row=5, sticky=W)
        ttk.Button(self.__ventana, text='9', command=partial(self.ponerNUMERO, '9')).grid(column=3, row=5, sticky=W)
        ttk.Button(self.__ventana, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=1, row=6, sticky=W)
        ttk.Button(self.__ventana, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=2, row=6, sticky=W)
        ttk.Button(self.__ventana, text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=3, row=6, sticky=W)
        ttk.Button(self.__ventana, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=1, row=7, sticky=W)
        ttk.Button(self.__ventana, text='/', command=partial(self.ponerOPERADOR, '/')).grid(column=2, row=7, sticky=W)
        ttk.Button(self.__ventana, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=3, row=7, sticky=W)
        



        #self.__panel.set('0')
        panelEntry.focus()
        self.__ventana.mainloop()
    
    def ponerNUMERO(self, numero):
        if self.__operadorAux==None:
            valor = self.__panel.get()
            self.__panel.set(valor+numero)
        else:
            self.__operadorAux=None
            valor=self.__panel.get()
            self.__primerOperando=(valor)
            self.__panel.set(numero)
    
    def borrarPanel(self):
        self.__panel.set('0')
    
    def resolverOperacion(self, operando1, operacion, operando2):
        resultado=0
        if operacion=='+':
            resultado=operando1+operando2
        else:
            if operacion=='-':
                resultado=operando1-operando2
            else:
                if operacion=='*':
                    resultado=operando1*operando2
                else:
                    if operacion=='/':
                        resultado=float(operando1)/float(operando2)
        self.__panel.set(str(resultado))
    
    def ponerOPERADOR(self, op):
        if op=='=':
            operacion=self.__operador.get()
            self.__segundoOperando=(self.__panel.get())
            self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
            self.__operador.set('')
            self.__operadorAux=None
        else:
            if self.__operador.get()=='':
                self.__operador.set(op)
                self.__operadorAux=op
            else:
                operacion=self.__operador.get()
                self.__segundoOperando=(self.__panel.get())
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                self.__operador.set(op)
                self.__operadorAux=op


    