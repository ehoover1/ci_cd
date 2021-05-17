from gapminder import gapminder
from matplotlib import pyplot as plt

gapminder = gapminder[ gapminder.year == 1952]

plt.bar(gapminder.continent, gapminder.gdpPercap)
plt.xlabel("country")
plt.ylabel("gdpPercap")
plt.style.use("fivethirtyeight")

plt.show()

