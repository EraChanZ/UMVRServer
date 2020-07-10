from django.db import models
from account.models import Account

class Court(models.Model):
    metro_stations = list(enumerate(['Бульвар Рокоссовского', 'Черкизовская', 'Преображенская площадь', 'Сокольники', 'Красносельская', 'Комсомольская', 'Красные ворота', 'Чистые пруды', 'Лубянка', 'Охотный ряд', 'Библиотека имени Ленина', 'Кропоткинская', 'Парк культуры', 'Фрунзенская', 'Спортивная', 'Воробьёвы горы', 'Университет', 'Проспект Вернадского', 'Юго-Западная', 'Тропарёво', 'Румянцево', 'Саларьево', 'Филатов Луг', 'Прокшино', 'Ольховая', 'Коммунарка', 'Ховрино', 'Беломорская', 'Речной вокзал', 'Водный стадион', 'Войковская', 'Сокол', 'Аэропорт', 'Динамо', 'Белорусская', 'Маяковская', 'Тверская', 'Театральная', 'Новокузнецкая', 'Павелецкая', 'Автозаводская', 'Технопарк', 'Коломенская', 'Каширская', 'Кантемировская', 'Царицыно', 'Орехово', 'Домодедовская', 'Красногвардейская', 'Алма-Атинская', 'Пятницкое шоссе', 'Митино', 'Волоколамская', 'Мякинино', 'Строгино', 'Крылатское', 'Молодёжная', 'Кунцевская', 'Славянский бульвар', 'Парк Победы', 'Киевская', 'Смоленская', 'Арбатская', 'Площадь Революции', 'Курская', 'Бауманская', 'Электрозаводская', 'Семёновская', 'Партизанская', 'Измайловская', 'Первомайская', 'Щёлковская', 'Кунцевская', 'Пионерская', 'Филёвский парк', 'Багратионовская', 'Фили', 'Кутузовская', 'Студенческая', 'Международная', 'Выставочная', 'Киевская', 'Смоленская', 'Арбатская', 'Александровский сад', 'Киевская', 'Краснопресненская', 'Белорусская', 'Новослободская', 'Проспект Мира', 'Комсомольская', 'Курская', 'Таганская', 'Павелецкая', 'Добрынинская', 'Октябрьская', 'Парк культуры', 'Медведково', 'Бабушкинская', 'Свиблово', 'Ботанический сад', 'ВДНХ', 'Алексеевская', 'Рижская', 'Проспект Мира', 'Сухаревская', 'Тургеневская', 'Китай-город', 'Третьяковская', 'Октябрьская', 'Шаболовская', 'Ленинский проспект', 'Академическая', 'Профсоюзная', 'Новые Черёмушки', 'Калужская', 'Беляево', 'Коньково', 'Тёплый Стан', 'Ясенево', 'Новоясеневская', 'Планерная', 'Сходненская', 'Тушинская', 'Спартак', 'Щукинская', 'Октябрьское поле', 'Полежаевская', 'Беговая', 'Улица 1905 года', 'Баррикадная', 'Пушкинская', 'Кузнецкий мост', 'Китай-город', 'Таганская', 'Пролетарская', 'Волгоградский проспект', 'Текстильщики', 'Кузьминки', 'Рязанский проспект', 'Выхино', 'Лермонтовский проспект', 'Жулебино', 'Котельники', 'Рассказовка', 'Новопеределкино', 'Боровское Шоссе', 'Солнцево', 'Говорово', 'Озёрная', 'Мичуринский Проспект', 'Раменки', 'Ломоносовский проспект', 'Минская', 'Парк Победы', 'Третьяковская', 'Марксистская', 'Площадь Ильича', 'Авиамоторная', 'Шоссе Энтузиастов', 'Перово', 'Новогиреево', 'Новокосино', 'Алтуфьево', 'Бибирево', 'Отрадное', 'Владыкино', 'Петровско-Разумовская', 'Тимирязевская', 'Дмитровская', 'Савёловская', 'Менделеевская', 'Цветной бульвар', 'Чеховская', 'Боровицкая', 'Полянка', 'Серпуховская', 'Тульская', 'Нагатинская', 'Нагорная', 'Нахимовский проспект', 'Севастопольская', 'Чертановская', 'Южная', 'Пражская', 'Улица академика Янгеля', 'Аннино', 'Бульвар Дмитрия Донского', 'Селигерская', 'Верхние Лихоборы', 'Окружная', 'Петровско-Разумовская', 'Фонвизинская', 'Бутырская', 'Марьина Роща', 'Достоевская', 'Трубная', 'Сретенский бульвар', 'Чкаловская', 'Римская', 'Крестьянская застава', 'Дубровка', 'Кожуховская', 'Печатники', 'Волжская', 'Люблино', 'Братиславская', 'Марьино', 'Борисово', 'Шипиловская', 'Зябликово', 'Деловой центр', 'Шелепиха', 'Хорошёвская', 'ЦСКА', 'Петровский парк', 'Савёловская', 'Битцевский парк', 'Лесопарковая', 'Улица Старокачаловская', 'Улица Скобелевская', 'Бульвар Адмирала Ушакова', 'Улица Горчакова', 'Бунинская аллея', 'Тимирязевская', 'Улица Милашенкова', 'Телецентр', 'Улица Академика Королёва', 'Выставочный центр', 'Улица Сергея Эйзенштейна', 'Окружная', 'Владыкино', 'Ботанический сад', 'Ростокино', 'Белокаменная', 'Бульвар Рокоссовского', 'Локомотив', 'Измайлово', 'Соколиная гора', 'Шоссе Энтузиастов', 'Андроновка', 'Нижегородская', 'Новохохловская', 'Угрешская', 'Дубровка', 'Автозаводская', 'ЗИЛ', 'Верхние Котлы', 'Крымская', 'Площадь Гагарина', 'Лужники', 'Кутузовская', 'Деловой центр', 'Шелепиха', 'Хорошёво', 'Зорге', 'Панфиловская', 'Стрешнево', 'Балтийская', 'Коптево', 'Лихоборы', 'Лефортово', 'Авиамоторная', 'Нижегородская', 'Стахановская', 'Окская', 'Юго-Восточная', 'Косино', 'Улица Дмитриевского', 'Лухмановская', 'Некрасовка']))
    landlord                = models.ForeignKey(Account, on_delete=models.CASCADE)
    name                    = models.CharField(max_length=30, unique=True)
    address_row             = models.CharField(max_length=100, unique=False)
    latitude                = models.FloatField()
    longitude               = models.FloatField()
    nearest_metro           = models.IntegerField(max_length=50, choices=metro_stations)
    is_free                 = models.BooleanField()

    def __str__(self):
        return self.name