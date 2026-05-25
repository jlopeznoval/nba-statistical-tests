# NBA Statistical Tests

Proyecto de **tests estadisticos** sobre el dataset [NBA Players](https://www.kaggle.com/datasets/justinas/nba-players-data) de Kaggle.
Cubre datos biometricos y estadisticas de juego de jugadores NBA desde 1996 hasta 2022.

## Estructura del proyecto

```
nba-statistical-tests/
├── data/
│   └── all_seasons.csv          # Dataset NBA Players (Kaggle)
├── src/
│   └── load_data.py             # Carga y preprocesamiento del dataset
├── tests/
│   ├── test_normalidad.py       # Shapiro-Wilk, D'Agostino, skewness
│   ├── test_hipotesis.py        # Mann-Whitney U, t-test de Welch, Levene
│   ├── test_correlacion.py      # Pearson, Spearman, Kendall tau
│   └── test_anova.py            # ANOVA de una via, Kruskal-Wallis
├── conftest.py                  # Fixtures globales de pytest
├── requirements.txt             # Dependencias Python
└── README.md
```

## Dataset

| Campo | Descripcion |
|-------|-------------|
| `player_name` | Nombre del jugador |
| `team_abbreviation` | Equipo |
| `age` | Edad |
| `player_height` | Altura (cm) |
| `player_weight` | Peso (kg) |
| `pts` | Puntos por partido |
| `reb` | Rebotes por partido |
| `ast` | Asistencias por partido |
| `net_rating` | Rating neto |
| `position` | Posicion (PG, SG, SF, PF, C) |
| `season` | Temporada |

## Tests estadisticos implementados

### 1. Normalidad (`test_normalidad.py`)
- **Shapiro-Wilk** sobre puntos, altura y peso
- - **D'Agostino-Pearson** sobre puntos
  - - **Skewness y Kurtosis** de la distribucion de puntos
   
    - ### 2. Hipotesis (`test_hipotesis.py`)
    - - **Mann-Whitney U**: Guards vs Centers en puntos, altura y rebotes
      - - **t-test de Welch**: medias de puntos entre posiciones
        - - **Prueba de Levene**: igualdad de varianzas
         
          - ### 3. Correlacion (`test_correlacion.py`)
          - - **Pearson**: altura-rebotes, asistencias-puntos, net_rating-puntos
            - - **Spearman**: altura-rebotes, peso-rebotes
              - - **Kendall tau**: peso-rebotes
               
                - ### 4. ANOVA (`test_anova.py`)
                - - **ANOVA de una via**: puntos y rebotes por posicion (PG/SG/SF/PF/C)
                  - - **Kruskal-Wallis**: alternativa no parametrica al ANOVA
                   
                    - ## Instalacion y uso
                   
                    - ```bash
                      # 1. Clonar el repositorio
                      git clone https://github.com/jlopeznoval/nba-statistical-tests.git
                      cd nba-statistical-tests

                      # 2. Crear entorno virtual
                      python -m venv venv
                      source venv/bin/activate  # Windows: venv\Scripts\activate

                      # 3. Instalar dependencias
                      pip install -r requirements.txt

                      # 4. Colocar el dataset
                      # Descarga all_seasons.csv de Kaggle y coloca en data/all_seasons.csv

                      # 5. Ejecutar todos los tests
                      pytest tests/ -v -s

                      # 6. Generar reporte HTML
                      pytest tests/ -v -s --html=report.html --self-contained-html
                      ```

                      ## Tecnologias

                      - **Python 3.11+**
                      - - **pandas** - Manipulacion de datos
                        - - **scipy** - Tests estadisticos
                          - - **numpy** - Operaciones numericas
                            - - **pytest** - Framework de testing
                              - - **pytest-html** - Reportes HTML
                                - - **seaborn / matplotlib** - Visualizaciones
