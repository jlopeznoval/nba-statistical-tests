"""
test_correlacion.py
-------------------
Tests de correlacion entre variables numericas del dataset NBA Players.
Utiliza Pearson (datos normales) y Spearman (datos no normales o ordinales).
"""
import pytest
from scipy import stats
import numpy as np

ALPHA = 0.05


class TestCorrelacionAlturaRebotes:
      """Hipotesis: existe correlacion positiva entre altura y rebotes."""

    def test_pearson_altura_rebotes(self, nba_df):
              """Pearson: correlacion entre altura y rebotes por partido."""
              df = nba_df[["player_height", "reb"]].dropna()
              r, p_value = stats.pearsonr(df["player_height"], df["reb"])
              print(f"\nPearson altura-rebotes: r={r:.4f}, p={p_value:.6f}")

        assert r > 0, "Se espera correlacion positiva entre altura y rebotes"
        assert p_value < ALPHA, "La correlacion debe ser estadisticamente significativa"

    def test_spearman_altura_rebotes(self, nba_df):
              """Spearman: correlacion monotona entre altura y rebotes."""
              df = nba_df[["player_height", "reb"]].dropna()
              rho, p_value = stats.spearmanr(df["player_height"], df["reb"])
              print(f"\nSpearman altura-rebotes: rho={rho:.4f}, p={p_value:.6f}")

        assert rho > 0.3, f"Se espera correlacion Spearman > 0.3, obtenida: {rho:.4f}"
        assert p_value < ALPHA


class TestCorrelacionPuntosTiempoJuego:
      """Hipotesis: los jugadores con mas minutos anotan mas puntos."""

    def test_pearson_minutos_puntos(self, nba_df):
              """Pearson: correlacion entre net_rating y puntos."""
              df = nba_df[["net_rating", "pts"]].dropna()
              r, p_value = stats.pearsonr(df["net_rating"], df["pts"])
              print(f"\nPearson net_rating-puntos: r={r:.4f}, p={p_value:.6f}")
              assert isinstance(r, float)
              assert -1 <= r <= 1

    def test_pearson_asistencias_puntos(self, nba_df):
              """Pearson: correlacion entre asistencias y puntos."""
              df = nba_df[["ast", "pts"]].dropna()
              r, p_value = stats.pearsonr(df["ast"], df["pts"])
              print(f"\nPearson asistencias-puntos: r={r:.4f}, p={p_value:.6f}")

        assert r > 0, "Jugadores con mas asistencias tienden a anotar mas"
        assert p_value < ALPHA


class TestCorrelacionPesoRebotes:
      """Hipotesis: jugadores mas pesados capturan mas rebotes."""

    def test_spearman_peso_rebotes(self, nba_df):
              """Spearman: correlacion entre peso y rebotes."""
              df = nba_df[["player_weight", "reb"]].dropna()
              rho, p_value = stats.spearmanr(df["player_weight"], df["reb"])
              print(f"\nSpearman peso-rebotes: rho={rho:.4f}, p={p_value:.6f}")

        assert rho > 0, "Se espera correlacion positiva entre peso y rebotes"
        assert p_value < ALPHA

    def test_kendall_peso_rebotes(self, nba_df):
              """Kendall tau: correlacion ordinal entre peso y rebotes."""
              df = nba_df[["player_weight", "reb"]].dropna().sample(1000, random_state=42)
              tau, p_value = stats.kendalltau(df["player_weight"], df["reb"])
              print(f"\nKendall tau peso-rebotes: tau={tau:.4f}, p={p_value:.6f}")

        assert tau > 0, "Kendall tau debe ser positivo"
        assert p_value < ALPHA
