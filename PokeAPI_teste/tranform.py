from extract import lista
import pandas as pd

df = pd.DataFrame(data = lista, index = range(1,200), columns = ["order","name", "height", "weight"])
df.head(199)

