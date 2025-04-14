import sqlite3


def init_db():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER NOT NULL,
        description TEXT
    )
    ''')

    books = [
        ('1984', 'George Orwell', 1949, 'A classic dystopian novel about a totalitarian society where the government controls every aspect of citizens\' lives.'),
        ('The Master and Margarita', 'Mikhail Bulgakov', 1967, 'A story about the visit of the Devil to Soviet Russia and the encounter of two worlds — the real and the fantastical.'),
        ('Murder on the Orient Express', 'Agatha Christie', 1934, 'A mystery novel about a murder on board a train, with the famous detective Hercule Poirot investigating.'),
        ('Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 1997, 'The first book in the series about the young wizard Harry Potter and his adventures at Hogwarts School of Witchcraft and Wizardry.'),
        ('War and Peace', 'Leo Tolstoy', 1869, 'An epic novel describing the lives of Russian aristocrats during the Napoleonic Wars, exploring the fates of the main characters against the backdrop of historical events.'),
        ('Crime and Punishment', 'Fyodor Dostoevsky', 1866, 'A psychological novel about the moral downfall and redemption of Raskolnikov, a student who murders a pawnbroker.'),
        ('One Hundred Years of Solitude', 'Gabriel García Márquez', 1967, 'A novel about the Buendía family, their rise and fall, which became a landmark in Latin American literature.'),
        ('The Alchemist', 'Paulo Coelho', 1988, 'A wise and inspiring story about a shepherd who embarks on a journey to fulfill his dream and find treasure.'),
        ('Wuthering Heights', 'Emily Brontë', 1847, 'A melancholic story about the passionate but tragic love between Heathcliff and Catherine Earnshaw.'),
        ('Faust', 'Johann Wolfgang von Goethe', 1808, 'A drama exploring themes of human ambition, knowledge, and redemption, in which Faust sells his soul to the devil.'),
        ('Pride and Prejudice', 'Jane Austen', 1813, 'A novel about the manners and matrimonial machinations among the British landed gentry in the early 19th century.'),
        ('The Catcher in the Rye', 'J.D. Salinger', 1951, 'A story about a troubled teenage boy, Holden Caulfield, who struggles with depression and alienation.'),
        ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'A tragic story about Jay Gatsby, his obsession with Daisy Buchanan, and the American Dream in the Jazz Age.'),
        ('To Kill a Mockingbird', 'Harper Lee', 1960, 'A novel about racial injustice in the American South, told through the eyes of a young girl, Scout Finch.'),
        ('The Hobbit', 'J.R.R. Tolkien', 1937, 'A fantasy adventure novel about Bilbo Baggins, a hobbit who is swept into a quest to reclaim treasure guarded by the dragon Smaug.'),
        ('The Lord of the Rings: The Fellowship of the Ring', 'J.R.R. Tolkien', 1954, 'The first part of Tolkien\'s epic high-fantasy trilogy about the battle between good and evil in Middle-earth.'),
        ('Brave New World', 'Aldous Huxley', 1932, 'A dystopian novel about a highly controlled society where happiness is manufactured and individuality is suppressed.'),
        ('The Chronicles of Narnia: The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 1950, 'A classic fantasy novel where four siblings discover the magical land of Narnia and help defeat an evil White Witch.'),
        ('The Picture of Dorian Gray', 'Oscar Wilde', 1890, 'A novel about a man whose portrait ages and shows the effects of his sinful actions, while he remains youthful and beautiful.'),
        ('Frankenstein', 'Mary Shelley', 1818, 'The story of a scientist, Victor Frankenstein, who creates a monster in his lab, leading to tragic consequences for all involved.'),
        ('Dracula', 'Bram Stoker', 1897, 'A Gothic horror novel about the infamous vampire Count Dracula and his attempt to move from Transylvania to England to spread the undead curse.'),
        ('Jane Eyre', 'Charlotte Brontë', 1847, 'The story of an orphaned girl who becomes a governess and falls in love with her mysterious employer, Mr. Rochester.'),
        ('Les Misérables', 'Victor Hugo', 1862, 'A historical novel that explores the lives of several characters during the French Revolution and their struggles for justice and redemption.'),
        ('The Shining', 'Stephen King', 1977, 'A horror novel about a family staying at an isolated hotel during the winter, where supernatural forces begin to torment them.'),
        ('The Road', 'Cormac McCarthy', 2006, 'A post-apocalyptic novel about a father and his young son journeying through a bleak, desolate landscape.'),
        ('Slaughterhouse-Five', 'Kurt Vonnegut', 1969, 'A satirical novel about a soldier who becomes "unstuck in time" and experiences different moments of his life, including his time as a POW in WWII.'),
        ('The Bell Jar', 'Sylvia Plath', 1963, 'A novel about a young woman’s descent into mental illness and her struggle to overcome it, loosely based on Plath\'s own life.'),
        ('The Godfather', 'Mario Puzo', 1969, 'A crime novel that tells the story of the powerful Corleone Mafia family, their rise to power, and the cost of that power.'),
        ('The Hunger Games', 'Suzanne Collins', 2008, 'A dystopian novel about a televised gladiatorial contest in which young people fight to the death as punishment for a failed rebellion.'),
        ('The Secret Garden', 'Frances Hodgson Burnett', 1911, 'A story about a young girl who discovers a secret, neglected garden and helps bring it back to life, which heals her and those around her.'),
        ('The Outsiders', 'S.E. Hinton', 1967, 'A novel about two rival gangs, the Greasers and the Socs, and the struggles of the protagonist, Ponyboy Curtis, to find his place in the world.'),
        ('The Diary of a Young Girl', 'Anne Frank', 1947, 'The poignant and heartbreaking diary of a Jewish girl, Anne Frank, who hid with her family during the Holocaust in WWII.'),
        ('The Kite Runner', 'Khaled Hosseini', 2003, 'A novel about friendship, betrayal, and redemption, set against the backdrop of Afghanistan\'s tumultuous history.')
    ]

    cursor.executemany('''
    INSERT INTO books (title, author, year, description)
    VALUES (?, ?, ?, ?)
    ''', books)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    init_db()
