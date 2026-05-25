import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

  from load_data import load_nba_data


@pytest.fixture(scope="session")
  def nba_df():
    """Fixture que carga el dataset NBA una sola vez para toda la sesion."""
      df = load_nba_data()
    assert not df.empty, "El DataFrame no debe estar vacio"
    return df


@pytest.fixture(scope="session")
def guards_df(nba_df):
    """Fixture: jugadores en posicion Guard (G)."""
      return nba_df[nba_df["position"].str.contains("G", na=False)]


  @pytest.fixture(scope="session")
  def centers_df(nba_df):
    """Fixture: jugadores en posicion Center (C)."""
      return nba_df[nba_df["position"].str.contains("C", na=False)]
