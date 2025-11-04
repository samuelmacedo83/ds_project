import dsproject as dsp

#TODO: mostrar pros alunos o que fixture
def test_download_data_columns():
    columns = dsp.download_data().columns.tolist()
    expected = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']

    assert columns == expected

