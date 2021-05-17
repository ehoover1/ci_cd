def main():

    from gapminder import gapminder
    
    gapminder = gapminder[ gapminder.year == 1952]
    return gapminder
    
main()