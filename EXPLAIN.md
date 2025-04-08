# Explicación del Enfoque

## Diseño de la Aplicación

1. **Procesamiento de Datos**:
   - Convertí las columnas de fecha a objetos datetime para facilitar el análisis temporal
   - Extraje año, mes y trimestre como columnas separadas
   - Creé identificadores combinados como "2021 Q3" para mejor visualización

2. **Cálculo de Métricas**:
   - Ventas totales: Agregación simple por período
   - Crecimiento interanual: Función que calcula la diferencia porcentual con el mismo período del año anterior

3. **Interactividad**:
   - Implementé filtros para segmentos y categorías usando dropdowns multi-selección
   - Añadí un selector para cambiar entre vista trimestral y mensual
   - Los gráficos se actualizan automáticamente al cambiar los filtros

4. **Visualizaciones**:
   - Gráfico de barras para ventas totales (fácil comparación entre períodos)
   - Gráfico de líneas para crecimiento interanual (mejor para mostrar tendencias)

## Insights Observados

1. **Patrones Estacionales**:
   - Los datos de ejemplo muestran ventas más altas en el tercer trimestre (Q3)
   - Esto podría indicar patrones estacionales en el comercio electrónico

2. **Crecimiento Interanual**:
   - El cálculo de crecimiento muestra cómo evolucionan las ventas en los mismos períodos año tras año
   - Permite identificar si hay crecimiento positivo o negativo

## Decisiones de Diseño

1. **Prioridad a Funcionalidad sobre Estilo**:
   - Según las instrucciones, me enfoqué en la claridad y corrección más que en el estilo
   - La interfaz es minimalista pero funcional

2. **Organización del Código**:
   - Separé el procesamiento de datos de la lógica de visualización
   - Usé callbacks modularizados para mantener el código limpio

3. **Manejo de Datos**:
   - Todos los cálculos se hacen sobre el dataframe filtrado para garantizar consistencia
   - Las transformaciones son documentadas y eficientes