def test_domain_check(test_permission):
    test_permission = test_permission.refresh()

    assert test_permission.id
    assert test_permission.slug == "test"


def test_permission_update(test_permission):
    test_permission.slug = "test1"

    test_permission.save()

    test_permission = test_permission.refresh()

    assert test_permission.slug == "test1"


def test_permission_destroy(test_permission):
    test_permission.destroy()
