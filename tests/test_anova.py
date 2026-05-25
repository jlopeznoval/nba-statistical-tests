"""
test_anova.py
-------------
Tests ANOVA de una via y Kruskal-Wallis para comparar multiples grupos
en el dataset NBA Players (por posicion o era).
"""
import pytest
from scipy import stats
import numpy as np

ALPHA = 0.05
POSICIONES = ["PG", "SG", "SF", "PF", "C"]


@pytest.fixture(scope="module")
def grupos_por_posicion(nba_df):
      """Retorna un dict {posicion: serie_de_puntos} para las 5 posiciones."""
      grupos = {}
      for pos in POSICIONES:
                pts = nba_df[nba_df["position"] == pos]["pts"].dropna()
                if len(pts) >= 30:
                              grupos[pos] = pts
                      return grupos


class TestAnovaPuntosPorPosicion:
      """ANOVA de una via: los puntos difieren segun la posicion."""

    def test_anova_una_via_puntos(self, grupos_por_posicion):
              """One-way ANOVA: al menos una posicion difiere en puntos."""
              grupos = list(grupos_por_posicion.values())
              assert len(grupos) >= 3, "Se necesitan al menos 3 grupos para ANOVA"

        f_stat, p_value = stats.f_oneway(*grupos)
        print(f"\nANOVA puntos por posicion: F={f_stat:.4f}, p={p_value:.6f}")

        assert p_value < ALPHA, (
                      f"ANOVA no significativo (p={p_value:.4f}): las posiciones no difieren en puntos"
        )

    def test_kruskal_wallis_puntos(self, grupos_por_posicion):
              """Kruskal-Wallis (no parametrico): alternativa a ANOVA si no hay normalidad."""
              grupos = list(grupos_por_posicion.values())
              assert len(grupos) >= 3

        h_stat, p_value = stats.kruskal(*grupos)
        print(f"\nKruskal-Wallis puntos: H={h_stat:.4f}, p={p_value:.6f}")

        assert p_value < ALPHA, "Kruskal-Wallis no significativo"

    def test_medias_por_posicion(self, grupos_por_posicion):
              """Documenta las medias de puntos por posicion."""
              for pos, pts in grupos_por_posicion.items():
                            print(f"  {pos}: media={pts.mean():.2f}, std={pts.std():.2f}, n={len(pts)}")
                            assert pts.mean() > 0, f"La media de puntos de {pos} debe ser positiva"


class TestAnovaRebotesPorPosicion:
      """ANOVA de una via: los rebotes difieren segun la posicion."""

    def test_anova_rebotes(self, nba_df):
              """One-way ANOVA sobre rebotes."""
              grupos = []
              for pos in POSICIONES:
                            reb = nba_df[nba_df["position"] == pos]["reb"].dropna()
                            if len(reb) >= 30:
                                              grupos.append(reb)

                        assert len(grupos) >= 3
        f_stat, p_value = stats.f_oneway(*grupos)
        print(f"\nANOVA rebotes por posicion: F={f_stat:.4f}, p={p_value:.6f}")

        assert p_value < ALPHA

    def test_kruskal_wallis_rebotes(self, nba_df):
              """Kruskal-Wallis sobre rebotes."""
        grupos = []
        for pos in POSICIONES:
                      reb = nba_df[nba_df["position"] == pos]["reb"].dropna()
                      if len(reb) >= 30:
                                        grupos.append(reb)

                  assert len(grupos) >= 3
        h_stat, p_value = stats.kruskal(*grupos)
        print(f"\nKruskal-Wallis rebotes: H={h_stat:.4f}, p={p_value:.6f}")
        assert p_value < ALPHA
