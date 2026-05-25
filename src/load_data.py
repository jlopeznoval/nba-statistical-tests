import pandas as pd
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "all_seasons.csv")


def load_nba_data(path: str = DATA_PATH) -> pd.DataFrame:
      """Carga el dataset NBA Players y realiza limpieza basica."""
      df = pd.read_csv(path, index_col=0)
      df.columns = df.columns.str.strip()
      df = df.dropna(subset=["pts", "reb", "ast", "player_height", "player_weight"])
      return df


def get_numeric_columns(df: pd.DataFrame) -> list:
      """Retorna las columnas numericas del DataFrame."""
      return df.select_dtypes(include=["number"]).columns.tolist()


def get_players_by_position(df: pd.DataFrame, position: str) -> pd.DataFrame:
      """Filtra jugadores por posicion."""
      return df[df["position"] == position].copy()


if __name__ == "__main__":
      df = load_nba_data()
      print(f"Dataset cargado: {df.shape[0]} filas x {df.shape[1]} columnas")
      print(df.head())
