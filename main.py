import csv
import matplotlib.pyplot as plt

#----------------------------------------------------------------------------------- 

def generate_population_plots_from_dictionary(population_dictionary):
  """
  Generates a population plot from a dictionary
  Creates one plot per continent
  """
  
  for continent in population_dictionary:
    years = population_dictionary[continent]["years"]
    internet_population = population_dictionary[continent]["population"]
    plt.plot(years, internet_population, label=continent, marker="o", alpha=0.5)

  plt.style.use("Solarize_Light2")

  plt.title("Internet Population per Continent")
  plt.xlabel("Year")
  plt.ylabel("Internet Users (in billion users)")
  plt.grid(True)
  plt.legend()
  plt.tight_layout()

  plt.show()

#-----------------------------------------------------------------------------------

def generate_population_dictionary_from_csv(file_name):
  """
  Use the data within the given csv file to generate a dictionary of internet populations per year for each continent

  Returns a dictionary in this format:
  {
    "Africa": {"population": [100, 200, 300], "years": [1990, 2000, 2010]}
    "Asia": {"population": [100, 200, 300], "years": [1990, 2000, 2010]}
  }
  """
  
  population_per_continent = {}

  with open(file_name, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
      continent = row["continent"]
      year = int(row["year"])
      internet_population = int(row["population"])

      if continent not in population_per_continent:
        population_per_continent[continent] = {"population": [], "years": []}

      population_per_continent[continent]["population"].append(internet_population)
      population_per_continent[continent]["years"].append(year)  

  return population_per_continent
  
#===================================================================================== 

file_name = "data.csv"

# Display plots of internet population per continent
population_per_continent = generate_population_dictionary_from_csv(file_name)
generate_population_plots_from_dictionary(population_per_continent)