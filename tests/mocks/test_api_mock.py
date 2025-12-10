def test_api_mock(mocker):
    mock_fn = mocker.patch("src.auth.login", return_value={"status": "OK"})
    assert mock_fn("x","y")["status"] == "OK"
