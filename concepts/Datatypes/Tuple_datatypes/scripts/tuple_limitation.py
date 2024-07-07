'''
Limititaions: 

1: Single valued tuple should ends with "," comma:

- By default all the single values of object is considered as single tuple object by Python virtual machine
- (i.e) consider assigning a integer value 10 

            x=10 is equivaluent to x=(10)
- Due to this above scenario all the single object elements inside tuple is considered to its equivalent datatypes
- To overcome come this scenario we need to tell the PVM that it is tuple varibale/object by adding , after single tuple element

            x=(10,)

'''

#multiple value declaration:

tuple_multiple_variable =(1,2,'viki',[1,2])
print("The type of tuple_multiple_variable is: ",type(tuple_multiple_variable))

# Single value declaration:

tuple_single_variable_int =(1)
print("The type of tuple_single_variable_int is: ",type(tuple_single_variable_int))

tuple_single_variable_str =('viki')
print("The type of tuple_single_variable_str is: ",type(tuple_single_variable_str))

tuple_single_variable_list =([1,2])
print("The type of tuple_single_variable_list is: ",type(tuple_single_variable_list))

tuple_single_variable_bool =(True)
print("The type of tuple_single_variable_bool is: ",type(tuple_single_variable_bool))

# Single value declaration with comma(","):

tuple_single_variable_int =(1,)
print("The type of tuple_single_variable_int with , is: ",type(tuple_single_variable_int))

tuple_single_variable_str =('viki',)
print("The type of tuple_single_variable_str with , is: ",type(tuple_single_variable_str))

tuple_single_variable_list =([1,2],)
print("The type of tuple_single_variable_list with , is: ",type(tuple_single_variable_list))

tuple_single_variable_bool =(True,)
print("The type of tuple_single_variable_bool with , is: ",type(tuple_single_variable_bool))