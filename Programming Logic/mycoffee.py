def make_coffee(*option):
    """makes coffee"""
    ingredients = ['coffee', 'hot water']
    if option:
        for op in option:
            ingredients.append(op)
   

    print('Started making coffee...')
    print('Getting cup')
    print('Adding {}'.format(', '.join(ingredients)))
    print('stir the mix for 5 seconds')
    print('Finish making coffee')
    
    if option:     
          
        coffee = 'Tasty Coffee with {}'.format(' '.join(option))
        
    else:               
      
        coffee = 'Tasty coffee'
    return coffee   


def serve_coffee(coffee, Person_name):
    """serves coffee"""
    print("{}--Here's your {}. Enjoy!!--\n".format(Person_name, coffee))


my_coffee = make_coffee('maize flour')
serve_coffee(my_coffee, 'Gibbs')    