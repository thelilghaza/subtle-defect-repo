from src.pipeline import run_pipeline


def test_pipeline_execution():
    assert run_pipeline() is True
