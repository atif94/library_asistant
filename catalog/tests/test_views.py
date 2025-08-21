from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_login_required_redirects_my_books(client):
    url = reverse("my_books")
    res = client.get(url)
    # should redirect to login with next param
    assert res.status_code == 302
    assert reverse("login") in res["Location"]


@pytest.mark.django_db
def test_my_books_shows_only_current_user_holdings(client, user, holdings):
    # login as alice
    assert client.login(username="alice", password="Secret123!")
    res = client.get(reverse("my_books"))
    assert res.status_code == 200
    html = res.content.decode()

    # Alice's books present
    assert "Book 1" in html
    assert "Book 2" in html
    # Bob's book absent
    assert "Book 3" not in html


@pytest.mark.django_db
def test_book_detail_and_author_books_render(client, user, books):
    assert client.login(username="alice", password="Secret123!")

    # book detail
    res_detail = client.get(reverse("book_detail", args=[books[0].id]))
    assert res_detail.status_code == 200
    assert books[0].title in res_detail.content.decode()

    # author books (pagination page 1 has 10 items)
    res_author_page1 = client.get(reverse("author_books", args=[books[0].author.id]))
    assert res_author_page1.status_code == 200
    html1 = res_author_page1.content.decode()
    assert "Book 1" in html1 and "Book 10" in html1
    assert "Book 11" not in html1  # should be on page 2

    # page 2
    res_author_page2 = client.get(reverse("author_books", args=[books[0].author.id]) + "?page=2")
    assert res_author_page2.status_code == 200
    html2 = res_author_page2.content.decode()
    assert "Book 11" in html2 and "Book 12" in html2
