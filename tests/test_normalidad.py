"""
test_normalidad.py
------------------
Tests de normalidad sobre variables clave del dataset NBA Players.
Utiliza Shapiro-Wilk (muestras < 5000) y D'Agostino-Pearson.
"""
import pytest
import numpy as np
from scipy import stats

SAMPLE_SIZE = 500  # Shapiro-Wilk requiere n < 5000
ALPHA = 0.05


class TestNormalidadPuntos:
      """Tests de normalidad sobre puntos por partido (pts)."""

    def test_shapiro_wilk_pts(self, nba_df):
              """Shapiro-Wilk sobre muestra de puntos por partido."""
              sample = nba_df["pts"].dropna().sample(SAMPLE_SIZE, random_state=42)
              stat, p_value = stats.shapiro(sample)
              print(f"\nShapiro-Wilk pts: W={stat:.4f}, p={p_value:.6f}")
              # Documentamos el resultado (NBA pts normalmente NO es normal)
              assert isinstance(p_value, float), "p-value debe ser float"
              assert 0 <= p_value <= 1, "p-value debe estar en [0, 1]"

    def test_dagostino_pts(self, nba_df):
              """D'Agostino-Pearson sobre puntos por partido."""
              sample = nba_df["pts"].dropna()
              stat, p_value = stats.normaltest(sample)
              print(f"\nD'Agostino pts: stat={stat:.4f}, p={p_value:.6f}")
              assert isinstance(p_value, float)

    def test_pts_skewness(self, nba_df):
              """La distribucion de puntos debe ser positivamente sesgada (asimetria > 0)."""
              skewness = stats.skew(nba_df["pts"].dropna())
              print(f"\nSkewness pts: {skewness:.4f}")
              assert skewness > 0, "Se espera sesgo positivo en puntos (muchos jugadores con pocos puntos)"

    def test_pts_kurtosis(self, nba_df):
              """Calcula la curtosis de puntos."""
              kurt = stats.kurtosis(nba_df["pts"].dropna())
              print(f"\nKurtosis pts: {kurt:.4f}")
              assert isinstance(kurt, float)


class TestNormalidadAlturaPeso:
      """Tests de normalidad sobre altura y peso de jugadores."""

    def test_shapiro_altura(self, nba_df):
              """Altura de jugadores (player_height en cm)."""
              sample = nba_df["player_height"].dropna().sample(SAMPLE_SIZE, random_state=42)
              stat, p_value = stats.shapiro(sample)
              print(f"\nShapiro-Wilk altura: W={stat:.4f}, p={p_value:.6f}")
              assert 0 <= p_value <= 1

    def test_shapiro_peso(self, nba_df):
              """Peso de jugadores (player_weight en kg)."""
              sample = nba_df["player_weight"].dropna().sample(SAMPLE_SIZE, random_state=42)
              stat, p_value = stats.shapiro(sample)
              print(f"\nShapiro-Wilk peso: W={stat:.4f}, p={p_value:.6f}")
              assert 0 <= p_value <= 1

    def test_altura_rango_valido(self, nba_df):
              """Altura debe estar entre 150 y 250 cm."""
              assert nba_df["player_height"].min() >= 150, "Altura minima debe ser >= 150 cm"
              assert nba_df["player_height"].max() <= 250, "Altura maxima debe ser <= 250 cm"
