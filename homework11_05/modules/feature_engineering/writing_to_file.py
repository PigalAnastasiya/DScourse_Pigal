""""
Write elements to the text file
    param: file_name:string,
            atribute:string,
           my_list:list - input value

           """
def file_writting(file_name, atribute, my_list):
     with open(file_name, atribute) as file:
         for dig in my_list:
              file.write("%i\t" % dig)