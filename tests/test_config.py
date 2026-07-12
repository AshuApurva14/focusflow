from app.core.config import Settings


def test_settings_builds_database_url_from_components(monkeypatch):
    monkeypatch.setenv("DATABASE_HOST", "localhost")
    monkeypatch.setenv("DATABASE_PORT", "5432")
    monkeypatch.setenv("DATABASE_NAME", "focusflow")
    monkeypatch.setenv("DATABASE_USER", "focusflow")
    monkeypatch.setenv("DATABASE_PASSWORD", "secret")
    monkeypatch.delenv("DATABASE_URL", raising=False)

    settings = Settings(_env_file=None)

    assert settings.DATABASE_URL == "postgresql://focusflow:secret@localhost:5432/focusflow"
