def make_coffee():
    """makes coffee"""
    ingredients = ['coffee', 'hot water']
    print('Started making coffee...\nGetting cup')    
    print('Adding {}'.format(', '.join(ingredients)))
    print('stir the mix for 5 seconds\nFinish making coffee')   
    coffee = 'Tasty coffee'
    return coffee

def serve_coffee(coffee, Person_name):
    """serves coffee"""
    print("--Here's your {} {}. Enjoy!!--\n".format(coffee,Person_name))


my_coffee = make_coffee()
serve_coffee(my_coffee, 'Gibbs')    