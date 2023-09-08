
def test_import_all():

    # ignore the deprecation warnings of yaql and aoihttp
    import warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    import prairie

    assert True

