from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        """Тест добавления новых книг"""
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_max_length(self):
        """Тест максимальной длины строки"""
        collector = BooksCollector()

        collector.add_new_book('A' * 41)

        assert 'A' * 41 not in collector.get_books_genre()

    def test_add_new_book_duplicate(self):
        """Тест дубликатов книг"""
        collector = BooksCollector()

        collector.add_new_book('Book1')
        collector.add_new_book('Book1')

        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_valid(self):
        """Тест установки жанра"""
        collector = BooksCollector()

        collector.add_new_book('Book1')
        collector.set_book_genre('Book1', 'Фантастика')

        assert collector.get_books_genre()['Book1'] == 'Фантастика'

    def test_set_book_genre_invalid_book(self):
        """Тест установки жанра несуществующей книге"""
        collector = BooksCollector()

        collector.set_book_genre('Book2', 'Фантастика')

        assert 'Book2' not in collector.get_books_genre()

    def test_set_book_genre_invalid_genre(self):
        """Тест установки несуществующего жанра"""
        collector = BooksCollector()

        collector.add_new_book('Book1')
        collector.set_book_genre('Book1', 'Несуществующий жанр')

        assert collector.get_books_genre()['Book1'] == ''

    def test_get_book_genre_valid(self):
        """Тест получения жанра по книге"""
        collector = BooksCollector()

        collector.add_new_book('Book1')
        collector.set_book_genre('Book1', 'Фантастика')

        assert collector.get_book_genre('Book1') == 'Фантастика'

    def test_get_book_genre_invalid(self):
        """Тест получения жанра по несуществующей книге"""
        collector = BooksCollector()

        assert collector.get_book_genre('Book2') is None

    def test_get_books_with_specific_genre_valid(self):
        """Тест получения книг по указанному жанру"""
        collector = BooksCollector()

        collector.add_new_book('Book1')
        collector.add_new_book('Book2')
        collector.set_book_genre('Book1', 'Фантастика')
        collector.set_book_genre('Book2', 'Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Book1', 'Book2']

    def test_get_books_with_specific_genre_invalid(self):
        """Тест получения книг по несуществующему жанру"""
        collector = BooksCollector()

        assert collector.get_books_with_specific_genre('Несуществующий жанр') == []

    def test_get_books_genre(self):
        """Тест получения коллекции книг"""
        collector = BooksCollector()

        collector.add_new_book('Book1')
        collector.set_book_genre('Book1', 'Фантастика')

        assert collector.get_books_genre() == {'Book1': 'Фантастика'}

    def test_get_books_for_children(self):
        """Тест получения книг для детей"""
        collector = BooksCollector()

        collector.add_new_book('Book1')
        collector.add_new_book('Book2')
        collector.set_book_genre('Book1', 'Фантастика')
        collector.set_book_genre('Book2', 'Ужасы')

        assert collector.get_books_for_children() == ['Book1']

    def test_add_book_in_favorites_valid(self):
        """Тест добавления книг в избранное"""
        collector = BooksCollector()

        collector.add_new_book('Book1')
        collector.add_book_in_favorites('Book1')

        assert 'Book1' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate(self):
        """Тест добавления дубликатов в избранное"""
        collector = BooksCollector()

        collector.add_new_book('Book1')
        collector.add_book_in_favorites('Book1')
        collector.add_book_in_favorites('Book1')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_invalid(self):
        """Добавление несущуствующей книги в избранное"""
        collector = BooksCollector()

        collector.add_book_in_favorites('Book2')

        assert 'Book2' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_valid(self):
        """Тест удаления книги из избранного"""
        collector = BooksCollector()

        collector.add_new_book('Book1')
        collector.add_book_in_favorites('Book1')
        collector.delete_book_from_favorites('Book1')

        assert 'Book1' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_invalid(self):
        """Тест удаления несуществующей книги из избранного"""
        collector = BooksCollector()

        collector.delete_book_from_favorites('Book2')

        assert 'Book2' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        """Тест получения списка избранных книг"""
        collector = BooksCollector()

        collector.add_new_book('Book1')
        collector.add_book_in_favorites('Book1')

        assert collector.get_list_of_favorites_books() == ['Book1']
