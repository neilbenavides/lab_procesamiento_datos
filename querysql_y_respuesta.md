## Query SQL:
SELECT dd.City, dd.[Total Population], ca.CO, ca.NO2, ca.O3, ca.SO2, ca.[PM2.5], ca.PM10
FROM datos_demografico AS dd
JOIN calidad_aire AS ca
ON dd.City = ca.city
ORDER BY dd.[Total Population] DESC, (ca.CO + ca.NO2 + ca.O3 + ca.SO2 + ca.[PM2.5] + ca.PM10) DESC
LIMIT 10;

##  Interpretación de los resultados:
Según los datos obtenidos, no parece haber una correlación directa entre la población de la ciudad y la calidad del aire. Por ejemplo, Nueva York, que es la ciudad más poblada de la lista, no tiene los niveles más altos de contaminantes. De hecho, Phoenix, que tiene aproximadamente la mitad de la población de Nueva York, muestra la concentración más alta de CO.
Además, San José, que es la ciudad menos poblada de la lista, tiene una de las concentraciones más altas de CO y NO2. Por otro lado, Los Ángeles, que es la segunda ciudad más poblada, tiene niveles relativamente bajos de la mayoría de los contaminantes.
Por lo tanto, basándonos en estos datos, no sería correcto afirmar que las ciudades más pobladas tienen la peor calidad del aire. La calidad del aire puede estar influenciada por muchos otros factores.