import pytest


@pytest.yield_fixture(scope="session")
def test_domain_project(test_admin_client):
    domain = test_admin_client.Domain()
    domain.slug = "test-project"
    domain.name = "Test Domain"
    domain.description = "Test" * 10
    domain.save()
    yield domain


@pytest.yield_fixture(scope="session")
def test_domain(test_admin_client):
    domain = test_admin_client.Domain()
    domain.slug = "test"
    domain.name = "Test Domain"
    domain.description = "Test" * 10
    domain.save()
    yield domain


@pytest.yield_fixture(scope="session")
def test_role(test_admin_client):
    role = test_admin_client.UserRole()
    role.slug = "test"

    role.save()

    yield role



@pytest.yield_fixture(scope="session")
def test_permission(test_admin_client):
    permission = test_admin_client.Permission()
    permission.slug = "test"

    permission.save()

    yield permission



@pytest.yield_fixture(scope="session")
def test_user(test_admin_client, test_domain, test_role):
    user = test_admin_client.User()
    role = test_role
    domain = test_domain

    user.first_name = "123"
    user.last_name = "123"
    user.patronymic = "123"

    user.birthday = "2019-10-29"

    user.username = "test"

    user.domain_id = domain.id
    user.role_id = role.id

    user.save()
    user.change_password("123")

    yield user


@pytest.yield_fixture(scope="session")
def test_project(test_admin_client, test_domain):
    project = test_admin_client.Project()
    project.slug = "test"
    project.name = "Test"
    project.description = project.name * 10

    project.domain_id = test_domain.id

    project.save()

    yield project


@pytest.yield_fixture(scope="session")
def test_user_permission_link(test_admin_client, test_project, test_permission, test_user):
    link = test_admin_client.UserPermissionLink()
    link.permission_id = test_permission.id
    link.user_id = test_user.id
    link.project_id = test_project.id

    link.save()

    yield link

