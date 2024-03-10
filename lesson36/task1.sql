create table lessons(
    number INTEGER NOT NULL ,
    topic VARCHAR(64) NOT NULL,
    date DATE NOT NULL ,
    homework_done_status BOOLEAN NOT NULL
);

insert into lessons(number, topic, date, homework_done_status)
values
    (30, 'Основи мережевого програмування', '2024-2-24', true),
    (31, 'Вступ до HTTP, створення HTTP-запитів', '2024-2-26', true),
    (32, 'Потоки', '2024-2-28', false),
    (33, 'Мультипроцесорність', '2024-3-02', false),
    (34, 'Asyncio', '2024-3-04', false);

delete from lessons
        where homework_done_status = true;

update lessons
set homework_done_status = true
where number in (32, 33);

-- ще раз написав код знизу щоб було видно хід роботи
delete from lessons
        where homework_done_status = true;
