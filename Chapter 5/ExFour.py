import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Thanh_pho': ['Los Angeles', 'San Diego', 'California City', 'San Jose',
                  'Bakersfield', 'Fresno', 'Palmdale', 'Sacramento', 'Lancaster', 'Oceanside'],
    'area_total_km2': [1302, 964, 527, 466, 385, 296, 275, 259, 243, 107]
}
df = pd.DataFrame(data)

df_sorted = df.sort_values(by='area_total_km2', ascending=True)
plt.barh(df_sorted['Thanh_pho'], df_sorted['area_total_km2'], color='lightgreen')
plt.xlabel('Diện tích (km2)')
plt.ylabel('Thành phố')
plt.title('Top 10 thành phố lớn nhất ở California theo diện tích')

plt.show()