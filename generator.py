'''
Created on 2013-04-09

@author: ben
'''
import Tkinter
import generator_defines

class password_gui(Tkinter.Tk):
    
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def initialize(self):
        self.grid()
        
        ## validate command
        valid_command = (self.register(self.validate), '%d', '%i', '%P', \
                         '%s', '%S', '%v', '%V', '%W')
        
        ## entry field and variable 1
        self.entry_variable_1 = Tkinter.IntVar()
        self.entry_variable_1.set(u'2')
        self.entry_1 = Tkinter.Entry(self, textvariable = self.entry_variable_1, \
                                     validate = 'key', vcmd = valid_command, \
                                     state = 'disabled')
        self.entry_1.grid(row = 0, column = 1)
        
        ## entry field and variable 2
        self.entry_variable_2 = Tkinter.IntVar()
        self.entry_variable_2.set(u'2')
        self.entry_2 = Tkinter.Entry(self, textvariable = self.entry_variable_2,  \
                                     validate = 'key', vcmd = valid_command, \
                                     state = 'disabled')
        self.entry_2.grid(row = 1, column = 1)
        
        ## entry field and variable 3
        self.entry_variable_3 = Tkinter.IntVar()
        self.entry_variable_3.set(u'2')
        self.entry_3 = Tkinter.Entry(self, textvariable = self.entry_variable_3, \
                                     validate = 'key', vcmd = valid_command, \
                                     state = 'disabled')
        self.entry_3.grid(row = 2, column = 1)
        
        ## entry field and variable 4
        self.entry_variable_4 = Tkinter.IntVar()
        self.entry_variable_4.set(u'2')
        self.entry_4 = Tkinter.Entry(self, textvariable = self.entry_variable_4, \
                                     validate = 'key', vcmd = valid_command, \
                                     state = 'disabled')
        self.entry_4.grid(row = 3, column = 1)
        
        ## entry field and variable 5
        self.entry_variable_5 = Tkinter.IntVar()
        self.entry_variable_5.set(u'8')
        self.entry_5 = Tkinter.Entry(self, textvariable = self.entry_variable_5, \
                                     validate = 'key', vcmd = valid_command, \
                                     state = 'disabled')
        self.entry_5.grid(row = 4, column = 1)
        
        ## entry field and variable 6
        self.entry_variable_6 = Tkinter.IntVar()
        self.entry_variable_6.set(u'8')
        self.entry_6 = Tkinter.Entry(self, textvariable = self.entry_variable_6, \
                                     validate = 'key', vcmd = valid_command, \
                                     state = 'disabled')
        self.entry_6.grid(row = 5, column = 1)
        
        
        ## check button 1
        self.checked_1 = Tkinter.IntVar()
        self.check_button_1 = Tkinter.Checkbutton(text = "Uppercase", variable = self.checked_1, onvalue = 1, \
                                                  offvalue = 0, command = lambda e = self.entry_1, \
                                                  v = self.checked_1: self.entry_check(e,v))
        self.check_button_1.grid(row = 0, column = 0, sticky = 'W')
        
        ## check button 2
        self.checked_2 = Tkinter.IntVar()                                          
        self.check_button_2 = Tkinter.Checkbutton(text = "Lowercase", variable = self.checked_2, onvalue = 1, \
                                                  offvalue = 0, command = lambda e = self.entry_2, \
                                                  v = self.checked_2: self.entry_check(e, v))
        self.check_button_2.grid(row = 1, column = 0, sticky = 'W')
        
        ## check button 3
        self.checked_3 = Tkinter.IntVar()
        self.check_button_3 = Tkinter.Checkbutton(text = "Special Characters", variable = self.checked_3, onvalue = 1, \
                                                  offvalue = 0, command = lambda e = self.entry_3, \
                                                  v = self.checked_3: self.entry_check(e, v))
        self.check_button_3.grid(row = 2, column = 0, sticky = 'W')
        
        ## check button 4
        self.checked_4 = Tkinter.IntVar()
        self.check_button_4 = Tkinter.Checkbutton(text = "Numbers", variable = self.checked_4, onvalue = 1, \
                                                  offvalue = 0, command = lambda e = self.entry_4, \
                                                  v = self.checked_4: self.entry_check(e, v))
        self.check_button_4.grid(row = 3, column = 0, sticky = 'W')
        
        ## check button 5
        self.checked_5 = Tkinter.IntVar()
        self.check_button_5 = Tkinter.Checkbutton(text = "Minimum Length", variable = self.checked_5, onvalue = 1, \
                                                  offvalue = 0, command = lambda e = self.entry_5, \
                                                  v = self.checked_5: self.entry_check(e, v))
        self.check_button_5.grid(row = 4, column = 0, sticky = 'W')
        
        ## check button 6
        self.checked_6 = Tkinter.IntVar()
        self.check_button_6 = Tkinter.Checkbutton(text = "Maximum Length", variable = self.checked_6, onvalue = 1, \
                                                  offvalue = 0, command = lambda e = self.entry_6, \
                                                  v = self.checked_6: self.entry_check(e, v))
        self.check_button_6.grid(row = 5, column = 0, sticky = 'W')
        
        ## generate button
        self.generate_button = Tkinter.Button(text = 'Generate', command = self.generate)
        self.generate_button.grid(row = 6, column = 1, sticky = 'EW')
        
        ## generate entry field and variable
        self.generate_variable = Tkinter.StringVar()
        self.generate_entry = Tkinter.Entry(self, textvariable = self.generate_variable, width = 40, justify = 'center')
        self.generate_entry.grid(row = 7, columnspan = 2, sticky = 'EW')
        
        ## help button 
        self.hash_button = Tkinter.Button(text = 'Hash It', command = self.print_hash)
        self.hash_button.grid(row = 6, column = 0, sticky = 'EW')
        
        ## don't allow resizing 
        self.resizable(False, False)
        

    def print_hash(self):
        self.generate_variable.set(self.sha_hash)
        
    def entry_check(self, entry, checked):
        if checked.get() == 0:
            entry.configure(state = 'disabled')
        else:
            entry.configure(state = 'normal')
            
    def generate(self):
        
        self.password_obj = generator_defines.Password(self.entry_1.get(), self.entry_2.get(), \
                                                                self.entry_3.get(), self.entry_4.get(), \
                                                                self.entry_5.get(), self.entry_6.get())
            
        self.new_password = self.password_obj.gen_lowercase() + self.password_obj.gen_uppercase() + \
                            self.password_obj.gen_special() + self.password_obj.gen_numbers()
        
        self.new_password = self.password_obj.mix_em_up(self.new_password)
        
        self.sha_hash = self.password_obj.hash_it(self.new_password)
        
        self.generate_variable.set(self.new_password)

        
    def validate(self, action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):
        if text in '0123456789' and len(value_if_allowed) < 3:
            return True
        else:
            return False
        
if __name__ == '__main__':
    app = password_gui(None)
    app.title('Generator')
    app.mainloop()
        
        