import Tkinter
import generator_defines
import tkFileDialog

class password_gui(Tkinter.Tk):
    
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def initialize(self):
        self.grid()
        
        ## validate command
        self.valid_command = (self.register(self.validate), '%d', '%i', '%P', \
                         '%s', '%S', '%v', '%V', '%W')
        
        ## entry field 1
        self.entry_1 = self.entry_field('2')
        self.entry_1.grid(row = 0, column = 1)
        
        ## entry field 2
        self.entry_2 = self.entry_field('2')
        self.entry_2.grid(row = 1, column = 1)
        
        ## entry field 3
        self.entry_3 = self.entry_field('2')
        self.entry_3.grid(row = 2, column = 1)
        
        ## entry field 4
        self.entry_4 = self.entry_field('2')
        self.entry_4.grid(row = 3, column = 1)
        
        ## entry field 5
        self.entry_5 = self.entry_field('8')
        self.entry_5.grid(row = 4, column = 1)
        
        ## entry field 6
        self.entry_6 = self.entry_field('10')
        self.entry_6.grid(row = 5, column = 1)
        
        
        ## check button 1
        self.checked_1 = Tkinter.IntVar()
        self.check_button_1 = Tkinter.Checkbutton(text = "Lowercase", variable = self.checked_1, onvalue = 1, \
                                                  offvalue = 0, command = lambda e = self.entry_1, \
                                                  v = self.checked_1: self.entry_check(e,v))
        self.check_button_1.grid(row = 0, column = 0, sticky = 'W')
        
        ## check button 2
        self.checked_2 = Tkinter.IntVar()                                          
        self.check_button_2 = Tkinter.Checkbutton(text = "Uppercase", variable = self.checked_2, onvalue = 1, \
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
        
        ## hash button 
        self.hash_button = Tkinter.Button(text = 'Hash It', command = self.print_hash)
        self.hash_button.grid(row = 6, column = 0, sticky = 'EW')
        
        ## don't allow resizing 
        self.resizable(False, False)
        
        # create a Menu object 
        self.menu_bar = Tkinter.Menu(self) 
        self['menu'] = self.menu_bar 
        self.file_menu = Tkinter.Menu(self.menu_bar)  
        self.menu_bar.add_cascade(label = 'File', menu=self.file_menu)
        self.file_menu.add_command(label = 'Open', command = self.open_file)
        self.file_menu.add_command(label = 'Save as...', command = self.save_as)
        
    ## build default entry field with variable
    def entry_field(self, default):
        entry_variable = Tkinter.IntVar()
        entry_variable.set(u'%s' % default)
        return Tkinter.Entry(self, textvariable = entry_variable, \
                                     validate = 'key', vcmd = self.valid_command, \
                                     state = 'disabled')

    def print_hash(self):
        self.generate_variable.set(self.sha_hash)
        
    ## is the check box checked or not?
    def entry_check(self, entry, checked):
        if checked.get() == 0:
            entry.configure(state = 'disabled')
        else:
            entry.configure(state = 'normal')
            
    ## use generator_defines to build a Password object
    def generate(self):
        
        ## instantiate the object
        password_obj = generator_defines.Password(self.entry_1.get(), self.entry_2.get(), \
                                                                self.entry_3.get(), self.entry_4.get(), \
                                                                self.entry_5.get(), self.entry_6.get())
        
        ## build a string using the functions provided
        ## in generator_defines 
        new_password = password_obj.gen_lowercase() + password_obj.gen_uppercase() + \
                            password_obj.gen_special() + password_obj.gen_numbers()
        
        ## shuffle the string 
        new_password = password_obj.mix_em_up(new_password)
        
        ## produce the sha1 hash to be used later
        self.sha_hash = password_obj.hash_it(new_password)
        
        ## print the password
        self.generate_variable.set(new_password)

    ## sanity check on user input
    ## only allows integers and limits
    ## input to 2 digits
    def validate(self, action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):
        if text in '0123456789' and len(value_if_allowed) < 3:
            return True
        else:
            return False
        
    def save_as(self):
        file_name = tkFileDialog.asksaveasfilename(parent = self, title = 'Save the file as...')
        if len(file_name) > 0:
            saved_file = open('%s' % file_name, 'w')
            file.write(self.generate_variable.get())
            saved_file.close()
        
    def open_file(self):
        file_name = tkFileDialog.askopenfilename(parent = self, title = 'Open file...')
        opened_file = open('%s' % file_name, 'r')
        line = opened_file.readline()
        if len(line) == 40:
            self.generate_variable.set(line)
        
if __name__ == '__main__':
    app = password_gui(None)
    app.title('Generator')
    app.mainloop()
