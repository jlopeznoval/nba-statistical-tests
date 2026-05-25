"""
test_hipotesis.py
-----------------
Tests de hipotesis: comparacion de grupos por posicion (Guard vs Center).
Utiliza Mann-Whitney U, t-test de Student y prueba de Levene (igualdad de varianzas).
"""
import pytest
from scipy import stats
import numpy as np

ALPHA = 0.05


class TestPuntosGuardsVsCenters:
      """Hipotesis: los Guards anotan mas puntos que los Centers."""

    def test_mann_whitney_pts_guards_vs_centers(self, guards_df, centers_df):
              """Mann-Whitney U: distribucion de puntos Guards vs Centers."""
              pts_guards = guards_df["pts"].dropna()
              pts_centers = centers_df["pts"].dropna()

        stat, p_value = stats.mannwhitneyu(pts_guards, pts_centers, alternative="two-sided")
        print(f"\nMann-Whitney pts: U={stat:.2f}, p={p_value:.6f}")
        print(f"Media Guards: {pts_guards.mean():.2f} | Media Centers: {pts_centers.mean():.2f}")

        assert p_value < ALPHA, (
                      f"Se esperaba diferencia significativa en puntos (p={p_value:.4f} >= {ALPHA})"
        )

    def test_ttest_pts_guards_vs_centers(self, guards_df, centers_df):
              """t-test de Welch: medias de puntos Guards vs Centers."""
              pts_guards = guards_df["pts"].dropna()
              pts_centers = centers_df["pts"].dropna()

        stat, p_value = stats.ttest_ind(pts_guards, pts_centers, equal_var=False)
        print(f"\nt-test pts: t={stat:.4f}, p={p_value:.6f}")

        assert isinstance(p_value, float)
        assert 0 <= p_value <= 1

    def test_levene_varianza_pts(self, guards_df, centers_df):
              """Levene: igualdad de varianzas de puntos entre Guards y Centers."""
              pts_guards = guards_df["pts"].dropna()
              pts_centers = centers_df["pts"].dropna()

        stat, p_value = stats.levene(pts_guards, pts_centers)
        print(f"\nLevene pts: W={stat:.4f}, p={p_value:.6f}")
        assert isinstance(p_value, float)


class TestAlturaGuardsVsCenters:
      """Hipotesis: los Centers son significativamente mas altos que los Guards."""

    def test_mann_whitney_altura(self, guards_df, centers_df):
              """Mann-Whitney U: los Centers deben ser mas altos que los Guards."""
              altura_guards = guards_df["player_height"].dropna()
              altura_centers = centers_df["player_height"].dropna()

        stat, p_value = stats.mannwhitneyu(
                      altura_centers, altura_guards, alternative="greater"
        )
        print(f"\nMann-Whitney altura (Centers > Guards): U={stat:.2f}, p={p_value:.6f}")
        print(f"Media Guards: {altura_guards.mean():.1f} cm | Media Centers: {altura_centers.mean():.1f} cm")

        assert p_value < ALPHA, "Los Centers deben ser significativamente mas altos"

    def test_diferencia_media_altura(self, guards_df, centers_df):
              """La diferencia de altura media debe ser de al menos 10 cm."""
              diff = centers_df["player_height"].mean() - guards_df["player_height"].mean()
              print(f"\nDiferencia de altura media: {diff:.2f} cm")
              assert diff >= 10, f"Se esperaba una diferencia >= 10 cm, obtenida: {diff:.2f} cm"


class TestRebotesGuardsVsCenters:
      """Hipotesis: los Centers capturan mas rebotes que los Guards."""

    def test_mann_whitney_rebotes(self, guards_df, centers_df):
              """Mann-Whitney U: rebotes Centers vs Guards."""
              reb_guards = guards_df["reb"].dropna()
              reb_centers = centers_df["reb"].dropna()

        stat, p_value = stats.mannwhitneyu(
                      reb_centers, reb_guards, alternative="greater"
        )
        print(f"\nMann-Whitney rebotes (Centers > Guards): U={stat:.2f}, p={p_value:.6f}")
        assert p_value < ALPHA, "Los Centers deben tener mas rebotes que los Guards"
