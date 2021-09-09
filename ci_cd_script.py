def main():

    from gapminder import gapminder
    
    filler = 'evan'
    gapminder = gapminder[ gapminder.year == 1952]
    return gapminder
    
main()
