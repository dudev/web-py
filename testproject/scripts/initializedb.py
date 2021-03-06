# -*- coding: utf-8 -*-
import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models import (
    DBSession,
    Post,
    Category,
    Page,
    Comment,
    Base
    )





def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        cat1 = Category(id=1, name='Мысли вслух')
        cat2 = Category(id=2, name='Взгляд изнутри')
        cat3 = Category(id=3, name='Стихи')
        cat4 = Category(id=4, name='Программирование')
        page1 = Page(
            nick='about-me',
            title='Обо мне',
            content='''<p>Меня зовут Русанов (в прошлом Дударев) Евгений; на просторах интернета - dudev и rusevg. Занимаюсь созданием сайтов и программированием более 5 лет, организовываю концерты и прочие ивенты. Из увлечений могу отметить спорт.</p><p>В сайтостроении и программировании хорошо знаю:</p><ul>
<li>PHP 5</li><li>HTML 5</li><li>CSS 3</li><li>JavaScript</li><li>jQuery</li><li>SQL (MySQL, PostreSQL)</li><li>MongoDB</li><li>Yii 1.1, 2.0</li><li>Haskell</li></ul><p>На среднем и ниже средного уровне:</p><ul>
<li>Assembler</li><li>C++</li><li>C#</li><li>Java</li><li>Python</li></ul><p>Разбираюсь в построении высоконагруженных систем.&nbsp;Имею понятие о многих других технологиях и языках.</p><p>Мои работы можно посмотреть в записях относящихся к разделу <a href="/blog/cat/5">Портфолио</a>.</p>'''
        )
        page2 = Page(
            nick='offers',
            title='Услуги',
            content='''<p>Предоставлю Вам следующие услуги:</p><ul>
<li>вёрстка шаблонов для сайта;</li><li>создание сайта под ключ;</li><li>продвижение сайта;</li><li>написание Standalone-приложений;</li><li>и др.</li></ul><p>Мои контакты можно узнать <a href="/contacts.html">здесь</a>.</p>'''
        )
        page3 = Page(
            nick='contacts',
            title='Контакты',
            content='''<p>
	Связаться со мной можно только по электронной почте:&nbsp;<a href="mailto:admin@dudev.ru">admin@dudev.ru</a>. Прошу не пытаться искать другие средства связи и писать туда.
</p>'''
        )
        post1 = Post(
            id = 1,
            title = 'Лето',
            content = '''<p>Лето - такое кроткое, маленькое, беспомощное слово, но, заглянув глубоко внутрь его, найдём глубокий смысл.</p><p>Для каждого человека самое солнечное и тёплое время года ассоциируется совершенно по-разному, но у всех слово "лето" ассоциируется с радостью, зеленью и теплом. Летом одни едут отдыхать на море, вторые едут в гости к родным, друзьям, третьи "сидят дома". Во многом это завис от "толщины" кошелька, но не будем о грустном. И всё-таки, почему люди настолько по-разному проводят "зелёное" время года, почему самое яркое время года настолько по-разному ассоциируется у людей? Главная причина кроется в индивидуальных потребностях и мыслях каждого человека. Например, для веб-мастеров, веб-дизайнеров, веб-программистов (особенно для фрилансеров) лето - "горячая" пора.</p><p>Конечно, тему лета можно раскрывать не одним десятком строк, потому что одни летом едут на море, вторые идут в поход, в экспедицию, третьи едут на дачу, а четвёртые сидят дома и потому что для каждого человека лето значит разное... И этими строками я завершу свою заметку о лете.</p>''',
            category_id = 1
        )
        post2 = Post(
            id = 2,
            title = 'Вперёд Россия',
            content = '''<p>13 мая в моей школе прошёл Праздник Чести Школы. Праздник, на котором чествуют и ещё раз поздравляют всех тех, кто отличился в течение учебного года.</p><p>Очень радует то, что победителей олимпиад разных уровней (вплоть до европейских) среди учеников моей школы с каждым годом всё больше и больше. Особенно порадовал четвёртый класс: все первые места во всех олимпиадах города.</p><p>Жаль, что есть и другие ребята, о них в статье <a href="/blog/4">Взрослые подростки</a>.</p>''',
            category_id = 1
        )
        post3 = Post(
            id = 3,
            title = 'Взгляд изнутри №1',
            content = '''<p>Компьютерные технологии развивались и развиваются очень стремительно. Мы мало что знаем об истории компьютерной техники, о его внутреннем устройстве, о том, как он работает.</p><h2>История развития</h2><p>Попытки облегчить жизнь людей начались очень давно и были успешны. Например, 3000 лет до н. э. в Древнем Вавилоне были изобретены первые счёты. Этот момент можно считать началом истории вычислительной техники.</p><h2>Дальше, больше</h2><p>В 87 год до н. э. в Греции был изготовлен «антикитерский механизм» &mdash; механическое устройство на базе зубчатых передач. Этот механизм использовался для астрономических вычислений. Через довольно большой промежуток времени в 1492 году Леонардо да Винчи в своём дневнике сделал чертёж 13-разрядного суммирующего устройства с десятизубцовыми кольцами. Впервые вычислительную машину, обладающую всеми свойствами современного компьютера, изобрёл в 1941 году Конрад Цузе. И буквально за 70 лет компьютерные технологии сделали колоссальное продвижение вперёд. От ламповых гигантов до многоядерных миниатюрных агрегатов.</p><h2>Взгляд изнутри</h2><p>Устройство компьютера тоже постоянно меняется, появляются новые приспособления и стандарты, совершенствуются существующие. Перечислим некоторые из последних стандартов: USB 3.0, SATA, DVI, PCI-Express.</p><p>Постоянно совершенствуются и устройства для компьютера: флешки (до 128 ГБ), жёсткие диски (до 3 ТБ), лазерные диски (CD, DVD, HD DVD, Blu-Ray [до 128 ГБ], Ultra Density Optical (UDO)[до 500 ГБ], HD VMD (High Density - Versatile Multilayer Disc) [до 100 ГБ], Holographic Versatile Disc [до 3,9 ТБ]), проекторы, мониторы, процессоры и многое другое.</p><h2>Инструмент для всех</h2><p>Сейчас компьютером можно использовать вместо самой сложной техники, например:</p><ul> <li>вместо груды музыкального оборудования (технические эквалайзеры и др.);</li><li>для обработки видео и монтажа фильмов;</li><li>для проведения онлайн встреч и конференций.</li></ul><h2>Сети связи</h2><p>Сейчас мы уже не представляем себе жизни без высокоскоростного интернета, а ведь ещё недавно скорость 64 Kbps считалась очень высокой. А представьте, что вместо нескольких мегабит в секунду у Вас 64 Kbps. Представили? Сложно? Конечно, как качать игры, фильмы на такой скорости? Как просматривать страницы сайтов, если каждая из них сейчас весит более 100 КБ?</p><h2>Как работает?</h2><p>Конечно, ни один компьютер не работает без программной части. Операционная система (например, Windows XP/Vista/7, Linux, UNIX, Ubuntu и др.) – основная программа компьютера. Чтобы выполнять сложные задачи, заменять собой сложную аппаратную технику необходимы сложные программы (например, программа для обработки звука Audacity). Чтобы Вы могли комфортно пользоваться интернетом, необходим хороший браузер, например, Опера, но этого оказывается недостаточно. Чтобы Вы вообще могли посещать сайты, необходимы серверные программы (Apache), базы данных (MySQL, SQLite, Oracle DataBase и др.), веб-языки программирования (PHP, Perl, .NET, Python и др.) и многое другое. Большинство программ написано на языке высокого уровня C++. Есть и другие языки программирования, например:</p><ul> <li>C</li><li>C#</li><li>Pascal</li><li>Basic</li><li>и др.</li></ul>''',
            category_id = 2
        )
        post4 = Post(
            id = 4,
            title = 'Взрослые подростки',
            content = '''<p>К сожалению, многие подростки считают себя очень взрослыми. У некоторых это выражается в хороших поступках, больших достижения, а у кого-то в курении, алкоголизме, наркомании.</p><p>Каждый день я хожу в школу, гулять и думаю: «Куда мы катимся?»</p><p>Дети ругаются матом почти с рождения, курят с начальных классов, а пьют с 10-12 лет, конечно, есть и другие дети, которые не ругаются матом, не курят и не употребляют спиртные напитки, но таких, увы, чрезвычайно мало. К сожалению, зачастую родители не знают о пристрастиях своих чад, а классные руководители и школьные учителя, зная о пагубных привычках ребёнка, родителям ничего не сообщают. По-моему, это не правильно, ведь только родители могут повлиять на ребёнка.</p><p>Очень часто, разговаривая друг с другом напрямую, по телефону, через интернет, люди используют ненормативную лексику. Даже в детских садах, секциях и кружках воспитатели, тренеры зачастую матерятся при детях, а родители потом ещё и удивляются. Ведь дети, особенно маленькие, хорошо запоминают и усваивают всё, что слышат, видят, а потом воспроизводят. И не стоит в будущем удивляться тому, что, однажды, Вы услышите, как Ваш ребёнок матерится.</p><p>Вы хотите, чтобы от курения табака Ваш ребёнок умер на 10-20 лет раньше прикованным к постели из-за тяжелейших болезней. Ведь в табачном дыме содержится более 2000 вредных соединений, в том числе самые опасные вещества: аммиак, ацетон, бензол, метанол, никотин, угарный газ, пестициды, полоний, сероводород, синильная кислота, канцерогенные смолы, радиоактивные изотопы и многие другие. Можно сказать, что, затянувшись, Вы приложились подышать к трубе химического завода. Так почему же большинство подростков начинает курить табак? Во-первых, курильщики в основном пессимисты, а счастливые лица на рекламных щитах продавцов дыма выглядят как насмешка над здравым смыслом. Во-вторых, широкая реклама через СМИ показывает нам «престижность» образа курильщика, а также в фильмах почти всегда богатые и знаменитые изображаются курящими. Есть многие другие причины: расслабиться, собрать мысли, лекарство от стрессов или «за компанию». Кстати, в конце 80-х годов Всемирная Организация Здравоохранения никотин причислен к мягким, но наркотикам! Но не стоит забывать, что никотин не самое ядовитое вещество в табачном дыме, поэтому замена сигарет с большим количеством никотина на сигареты с меньшим его содержанием вреда практически не уменьшает.</p><p>Что же касается алкоголя, то он причиняет не меньший урон организму. Алкоголь, к сожалению, легализированный наркотик, впрочем, так же, как табак. Алкоголь в «чистом» виде, такой как этанол, при попадании в организм любым путем, при достижении некоторой концентрации, вызывает тяжелое отравление организма и, как правило, смерть. У алкоголя имеется множество альтернативных названий, что ещё раз доказывает его популярность. Теперь рассмотрим причины того, почему подростки начинают употреблять спиртное. Опять же первые места занимают вполне банальные причины: «за компанию», расслабиться. А также опять разочаровывает то, что в фильмах, как бы это прискорбно не звучало, богатые и знаменитые не прочь выпить стакан другой, а то и больше, чего-нибудь алкогольного. Опять возникает престижный образ пьющего человека. А если разобраться, то этот образ исчезает, а остаётся только образ неудачника.</p><p>Конечно, к счастью, не все ребята имеют пагубные пристрастия (о них в статье <a href="/blog/2">Вперёд Россия!</a>). Большинство из них обладают, как мне кажется, развитым навыком самовоспитания, а также они чаще всего не идут за большинством и не подражают ему, потому что это личности!</p>''',
            category_id = 1
        )
        post5 = Post(
            id = 5,
            title = 'Год назад',
            content = '''<p>
	Быть может, целый год я шлялся где-то
<br>
	Мечтая встретиться с тобой
<br>
	Быть может, обнимался с кем-то
<br>
	Мечтая обниматься с той
<br>
	Которая 4 сотни дней назад
<br>
	В любви призналась мне
<br>
	Быть может я какой-то гад
<br>
	Но снова вижу я тебя во сне
<br>
	И в этот чудный день влюблённых
<br>
	Спешу тебе большую горку преподнести я
<br>
	Грёз огромных, прекрасным светом озарённых
<br>
	И подарить стишок, тебя любя&hellip;&nbsp;</p>''',
            category_id = 3
        )
        post6 = Post(
            id = 6,
            title = 'Жизнь...',
            content = '''<p>
	А жизнь это полностью классно
<br>
	Валяться у моря, где ветры солёные
<br>
	Глядеть высоко в небеса голубые
<br>
	Где каждое облако будет ценно
<br>
	А осенью слышать, как падает лист
<br>
	С едва пожелтевшей берёзы
<br>
	В саду срезать виноградные лозы
<br>
	Под занавес осени, бежавшей как будто артист
<br>
	Зимой в Новый год подольше стоять у окна
<br>
	Смотря, как летают цветные салюты
<br>
	И ждать до боя курантов минуты
<br>
	Под него вспоминаю родных имена
<br>
	А весна? Зеленеет трава, и журчат ручейки
<br>
	И пойди-ка, найди, кто не пускал корабли
<br>
	Кто не смотрел на цветы, что белеют вдали
<br>
	И кто не видел, как ночью горят фонари
<br>
	В общем, жизнь это круто
<br>
	Есть любовь и улыбки, радость и смех,
<br>
	Есть безумство и ненависть, власть ну и грех.
<br>
	Ты живи, как живёшь. Ведь живёшь ты, а не кто-то&nbsp;
</p>''',
            category_id = 3
        )
        post7 = Post(
            id = 7,
            title = 'Горжусь, дед!',
            content = '''<p>
	Цените тишину всех шумных городов
<br>
	Где вы свободны от военных оков
<br>
	Там где не падают ракеты,
<br>
	И не взрываются снаряды
</p>
<p>
	Где не летают дуры-пули,
<br>
	И не плачут дети от войны
<br>
	И где враги не посягнули
<br>
	На территорию родной моей страны
</p>
<p>
	А дед живёт в гнилой однушке
<br>
	Как будто в старом брошенном леске
<br>
	Лишь изредка приходят к нему внуки
<br>
	А ты взгляни на его сморщенные руки
</p>
<p>
	Которыми себе готовит завтрак он.
<br>
	Ему не нужен миллион
<br>
	Ему достаточно внимания
<br>
	Когда к нему приходят дети всей компанией
</p>
<p>
	Я помню, я горжусь, дед
<br>
	Прости за пафос этот, дед
<br>
	Прости за мат тебе в ответ.
<br>
	Ты помни: я горжусь, дед.
</p>''',
            category_id = 3
        )
        post8 = Post(
            id = 8,
            title = 'О пользе кофе',
            content = '''<p>В популярности кофе не может быть сомнений. Отмечено, что многие предпочитают начинать свой день именно с чашечки ароматного кофе. Его ошеломляющий успех вызван богатством выбора вкусовых вариаций, манящим ароматом и идеальным качеством. Кофе пробуждает от сна и стимулирует к работе, не повышая при этом кровяное давление, данное мнение ошибочно. Одна или две чашечки кофе в день позволят вам чувствовать себя более бодрым в течение всего дня, и всё благодаря содержащимся в его составе кофеину и таурину.</p><p>Согласно данным исследования кофе является незаменимым составляющим рациона женщины, умеренное употребление этого напитка снижает риск болезни сердца и кровеносной системы. Отмечено, что кофе благотворно влияет на организм человека, нормализует работу сердца, улучшает кроветворение, способствует нормальной работе печени.</p><h2>Несколько фактов о пользе кофе.</h2><ol> <li>Кофе считается профилактическим средством в борьбе с желчекаменной болезнью. Данное утверждение верное, мы проверили это, согласно исследованию, проведенном в Гарварде у женщин и мужчин, выпивающих около трёх чашек кофе в день, на 25 % снижается риск заболеть вышеуказанным недугом.</li><li>Кофе является профилактическим средством в борьбе со стрессом и депрессиями. У женщин и мужчин, выпивающих около двух чашек кофе на протяжении всего дня риск к развитию депрессии уменьшается на 15 %, у людей, которые злоупотребляют этим напитком, отмечается повышенная нервная возбудимость и склонность к депрессии увеличивается на 20 %.</li><li>Кофе увеличивает способность к запоминанию информации. Скорость реакции и память улучшается, если пить напиток умеренными дозами.</li><li>Кофе снижает риск возникновения сахарного диабета. Согласно данных исследования люди, выпивающие по 2 чашки кофе в день в 50 % процентах случаях не столкнуться с сахарным диабетом. В данном случае вещества, входящие в состав кофе, а именно hIAPP - полипептид разрушающе воздействует на белковые волокна, что не позволяет развиться недугу.</li><li>Кофе является профилактикой возникновения рака. На сегодняшний день нам стало известно, что люди, пьющие кофе менее подвержены такому заболеванию как: рак молочной железы и рак простаты.</li><li>Кофе способно нормализовать обмен веществ. Отметим, что этот напиток не поможет вернуть прежний вес, кофеину свойственно помогать работе организма и улучшать процесс переваривания и выведения пищи, хлорогеновая кислота уменьшает всасывание глюкозы.</li><li>Нельзя и не отметить прекрасных антиоксидантных свойств кофе.</li><li>Стимуляция и повышение работоспособности. Каждому данный факт известен, что от кофе человек быстрее просыпается и готов к вершению дел, выносливость повышается, сосредоточенность улучшается, реакция на происходящее отличная.</li></ol><p>Выбирайте подходящий вам аромат и пейте кофе в своё удовольствие!</p>''',
            category_id = 1
        )
        post9 = Post(
            id = 9,
            title = 'Подсветка синтаксиса с highlight.js',
            content = '''<p>
	Сегодня установил на свой блог Highlight.js. Эта довольно удобная фишка нужна для удобства восприятия исходных годов (на данный момент 54 языков), как вы уже, думаю, догадались она подсвечинает синтаксис исходников. По утверждению разработчиков highlight.js сам находит куски кода для подсветки, определяет язык и подсвечивает.
	<br>
	Также разработчики предосталяют выбор стиля отображения из 26 (!) вариантв.
</p>
<p>
	Пример работы можно увидеть ниже на примере функции пирамидальной сортировки на C:
</p>
<pre>
<code>#include 
using namespace std;
extern bool DEBUG;
int * heap( int * arr ) {
	int i;
	//строим пирамиду, начиная с листьев постепенно добавляя головы
	for( i = size_of_arr / 2 - 1; i &gt;= 0; i-- ) arr = downHeap( arr, i, size_of_arr - 1 );
	for( i = size_of_arr - 1; i &gt; 0; i--) {
		//меняем первый с последним, т.к. 1 элем. - голова =&gt; наибольший элемент
		swap( arr[ 0 ], arr[ i ] );
		//нормализация пирамиды
		arr = downHeap( arr, 0, i - 1 ); 
	}
	cout &lt;&lt; "Heap sort:" &lt;&lt; endl;
	print_arr( arr );
	if ( DEBUG ) check( arr );
	return arr;
}</code>
</pre>
<p>
	Подключается эта библиотека очень просто:
</p>
<pre><code>
&lt;script src="http://yandex.st/highlightjs/7.3/highlight.min.js" type="text/javascript"&gt;&lt;/script&gt;
&lt;link href="http://yandex.st/highlightjs/7.3/styles/googlecode.min.css" rel="stylesheet" type="text/css"&gt;
&lt;script type="text/javascript"&gt;hljs.initHighlightingOnLoad();&lt;/script&gt;</code>
</pre>
<p>
	Радует, что highlight.js размещен на 
	<a href="http://api.yandex.ru/jslibs/libs.xml#highlightjs" target="_blank">хостинге JS-библиотек Яндекса</a> (там же есть и стилевые файлы).
</p>
<p>
	Ссылки на сайт разработчика: 
	<a href="http://softwaremaniacs.org/soft/highlight/" target="_blank">Описание</a> <a href="http://softwaremaniacs.org/media/soft/highlight/test.html" target="_blank">Демо</a>
</p>''',
            category_id = 4
        )
        post10 = Post(
            id = 13,
            title = 'Взгляд изнутри №2. Что такое видеокарта',
            content = '''<p>Видеокарта – это устройство, обеспечивающее обработку графической информации с последующим выводом ее на дисплей. Она включает в себя следующие элементы: видеопамять, видеопроцессор, цифро-аналоговый преобразователь и систему охлаждения. Видеопамять хранит данные и передает их из видеопроцессора и процессора компьютера. Видеопроцессор является «ядром» видеокарты. Цифро-аналоговый преобразователь выводит цифровую информацию на аналоговый монитор.</p><p>Система охлаждения поддерживает температурный режим видеопамяти и видеопроцессора в допустимых диапазонах.</p><p>Графические карты бывают двух видов: интегрированные (установленные на системной плате) и дискретные (установленные через порт PCI-E или AGP). Последние обладают большей производительностью, такие карты очень хорошо подходят для компьютерных игр.</p>''',
            category_id = 2
        )
        post11 = Post(
            id = 15,
            title = 'В виртуальном плену',
            content = '''<p>Хотелось бы разобраться в причинах появления компьютерной зависимости. Возможно, главная из них - это отсутствие у подростка серьезных увлечений или хобби, которые явно сократили бы пребывание за компьютером и подняли бы уровень его физического развития и здоровья. Спорт в данном случае - одно из лучших лекарств от аддикции. Но есть и другая причина, приклеивающая ребенка к монитору. Это интернет-общение, которое, как мне кажется, постепенно вытесняет реальное взаимодействие подростков. Тысячи онлайн-сообщений, отправленных за день, превышают количество сказанных друг другу слов. Общительные и активные дети, которые довольно легко могут налаживать контакты со сверстниками, точно так же, как и «геймеры до мозга костей» приклеены к монитору, к примеру, просиживая сутками на сайте гениального Павла Дурова, который внес неоценимый вклад в развитие нашего общества. Приведем наглядный пример, Пятнадцатилетняя девочка выходит из метро. Достигнув уже последней ступеньки, которая отделяет подземный мир от заснеженной улицы, она спотыкается, и из ее рук выпадает айфон, выполняющий подключение к сети Internet. Чертыхаясь, школьница немедленно поднимает свою дорогую игрушку и быстро осматривает свое запястье, которое приняло на себя последствия падения и теперь слегка кровоточит. Наскоро натянув на поврежденную руку перчатку, она быстрым шагом направляется к дому, не выпуская из второй ладони электронную причину падения. И вот она поднимается по лестнице, поворачивает ключ в замке и вбегает в квартиру. Сняв курточку и сапожки, замирает на несколько секунд в коридоре, затем осматривает руку и входит в свою комнату. «Привет, мой хороший», - произносит она. Вы, наверное, подумали, что она поздоровалась с любимым щеночком и сейчас сидит на корточках и чешет его за ушком. Вы ошиблись. Слова были адресованы серебристому ноутбуку, который она включила, нежно проведя рукой, как будто бы она гладит любимого питомца. К счастью, на загрузку компьютера требуется время, поэтому наша героиня отправляется в ванную, чтобы разобраться с поврежденной рукой. В итоге, как ни прискорбно, но её дальнейшие действия на этот день очевидны.</p><p>Компьютерная ролевая игра позволяет ребенку моделировать такие жизненные ситуации, с которыми он никогда не столкнется в реальности. Например, вряд ли какой-либо пятиклассник будет спасать мир, прыгая по крышам и борясь с огнедышащим драконом. Основная особенность ролевых компьютерных игр - наибольшее влияние на психику играющего, а также мотивация игровой деятельности, которая строится из потребности принятия роли и ухода из реальности. Механизм формирования психологической аддикции основан на естественном стремлении человека избавиться от разного рода проблем и неприятностей, связанных с повседневной жизнью. Больше всего удивляет тот факт, что люди сами смеются над гуляющими в сети цитатами о современных геймерах или над ставшими в последнее время популярными картинками-демотиваторами, высмеивающими «прилипших к экрану». Говорят, что умение смеяться над собой - это искусство. Так в этом «искусстве» нам нет равных...</p><p>Рассуждать над причинами можно бесконечно, гораздо важнее попробовать выявить способы излечения детей от компьютерной аддикции. Уверяю, что такие радикальные меры, как лишение ребенка любимой игрушки, не вполне подойдут. На самом деле компьютеры в наши дни стали помощниками в образовании: большинство заданий в школах и вузах невозможно выполнить без компьютера. В каждом учебном заведении имеются медиа - залы, которые оснащены всей необходимой аппаратурой и, конечно же, подключены к Интернету.</p><p>Бесспорно, нет ничего плохого в том, что компьютер позволяет детям «открывать мир», находить друзей, сопутствует в осуществлении познавательной деятельности. Мо мы ведем речь о компьютерной зависимости, которая наступает, когда при наличии у ребенка широкого круга альтернатив обучения, общения, проведения досуга он отвергает все новые возможности и использует компьютер, как единственное средство получения удовольствия. В таком случае он не приносит ребенку никакой пользы и рассматривается как предмет патологического влечения.</p><p>Чтобы сократить пребывание подростка за компьютером, необходимо помочь ему правильно организовать свой досуг, используя максимум возможностей, предоставляемых в нашем обществе. Даже поход по магазинам в воскресенье поможет отклеить ребенка от монитора. Если же оставить без внимания компьютерную зависимость, то это может привести к очень плачевным последствиям: «...Тринадцатилетний подросток ограбил родных бабушку с дедушкой, чтобы разжиться стольником для похода в интернет-кафе. Одиннадцатилетний паренек умер от сердечного приступа прямо над клавиатурой. Выяснилось - он просидел в Сети почти тридцать часов безвылазно». И подобных примеров в архивах по делам несовершеннолетних предостаточно.</p><p>И я вовсе не хочу вас напугать, просто привожу примеры последствий компьютерной зависимости. Геймеры, к примеру, обычно ведут себя нервно и раздражительно, отстранены от прелестей реальной жизни. Иногда они проецируют свои успехи в виртуальных мирах на свою настоящую «оффлайновскую» жизнь, чем нередко раздражают окружающих или вызывают у них недоумение. «Не могу тебя встретить &mdash; у нас конференция клана. Купи по дороге «Ред. Булла», я деньги потом отдам». Подобное сообщения вряд ли бы порадовало девушку.</p><p>К сожалению, большинство людей смиренно терпят эту болезнь у своих близких и не предпринимают никаких попыток ее излечения. Но всё возможно, ведь есть вещи, на которые компьютер просто не способен! Он не приготовит вам завтрак, не погуляет с собачкой, не почистит ковер. Он не сможет подать вам руку помощи в сложной ситуации, выслушать вас и прижать к плечу. Цените окружающих вас людей, а не виртуальные успехи! Это лишь иллюзия успехов, общения, дружбы. И вы в нее наивно верите...</p><p>Мир так многообразен и замечателен! Так зачем же сковывать себя рамками холодного виртуального пространства! Чашка горячего кофе, теплый плед, камин, хорошая книга... или беседа по душам с лучшим другом в осеннем парке на скамейке. Неужели глобальная паутина способна заменить такие приятные, простые и необходимые вещи? Я думаю, что нет. А вы хотели бы поспорить?</p>''',
            category_id = 1
        )
        post12 = Post(
            id = 20,
            title = 'Постинг на стену вконтакте',
            content = '''<p>
	Недавно в одном из моих проектов возникла необходимость публиковать информацию о добавляемых товарах на стену в группу ВКонтакте. Пошарив в инете, понял, что ничего подходящего под мою задачу нет. Изучив документацию api нашел еще одну трудность: работать со стеной могут только standalone-приложения. Но хитрый русский мозг сразу придумал как это можно обойти.
</p>
<h2>Создание приложения</h2>
<p>
	Сперва нужно создать приложение. Сделать это можно здесь
	<a href="http://vk.com/editapp?act=create">http://vk.com/editapp?act=create</a>. Выбираете standalone-приложение. После создания вашему приложению присвоится ID.
</p>
<h2>Получение токена</h2>
<p>
	Токен для работы приложения с api получить несложно, достаточно в браузере открыть ссылку:
</p>
<pre><code>https://oauth.vk.com/authorize?client_id=[ID приложения]&amp;scope=[запрашиваемые права]&amp;display=page&amp;response_type=token&amp;redirect_uri=https://oauth.vk.com/blank.html</code></pre>
<p>
	ID приложения мы получили в предыдущем шаге.
</p>
<p>
	Для работы моего класса необходимо запросить следующие права: offline,group,photos,wall. Весь список возможных прав можно найти в документации к api.
</p>
<h2>Класс</h2>
<p>
	Сам класс выполнен на языке PHP. Собственно вот он:
</p>
<pre><code>class vk {
	private $token;
	private $app_id;
	//ID группы или страницы пользователя
	private $group_id;
	//вероятность публикации поста на стену
	private $delta;
	public function __construct( $token, $delta, $app_id, $group_id ) {
		$this-&gt;token = $token;
		$this-&gt;delta = $delta;
		$this-&gt;app_id = $app_id;
		$this-&gt;group_id = $group_id;
	}
	//постинг на стену
	public function post( $desc, $photo, $link ) {
		if( rand( 0, 99 ) &lt; $this-&gt;delta ) {
			$data = json_decode(
						$this-&gt;execute(
							'wall.post',
							array(
								'owner_id' =&gt; -$this-&gt;group_id,
								'from_group' =&gt; 1,
								'message' =&gt; $desc,
								'attachments' =&gt; 'photo-' . $this-&gt;group_id . '_' . $photo . ',' . $link
							)
						)
					);
			if( isset( $data-&gt;error ) ) {
				return $this-&gt;error( $data );
			}
			return $data-&gt;response-&gt;post_id;
		}
		return 0;
	}
	//создание альбома
	public function create_album( $name, $desc ) {
		$data = json_decode(
					$this-&gt;execute(
						'photos.createAlbum',
						array(
							'title' =&gt; $name,
							'gid' =&gt; $this-&gt;group_id,
							'description' =&gt; $desc,
							'comment_privacy' =&gt; 1,
							'privacy' =&gt; 1
						)
					)
				);
		if( isset( $data-&gt;error ) ) {
			return $this-&gt;error( $data );
		}
		return $data-&gt;response-&gt;aid;
	}
	//получение кол-ва фотографий в альбоме
	public function get_album_size( $id ) {
		$data = json_decode(
					$this-&gt;execute(
						'photos.getAlbums',
						array(
							'oid' =&gt; -$this-&gt;group_id,
							'aids' =&gt; $id
						)
					)
				);
		if( isset( $data-&gt;error ) ) {
			return $this-&gt;error( $data );
		}
		return $data-&gt;response['0']-&gt;size;
	}
	//загрузка фотографии
	public function upload_photo( $file, $album_id, $desc ) {
		$data = json_decode(
					$this-&gt;execute(
						'photos.getUploadServer',
						array(
							'aid' =&gt; $album_id,
							'gid' =&gt; $this-&gt;group_id,
							'save_big' =&gt; 1
						)
					)
				);
		if( isset( $data-&gt;error ) ) {
			return $this-&gt;error( $data );
		}
		$ch = curl_init( $data-&gt;response-&gt;upload_url );
		curl_setopt ( $ch, CURLOPT_HEADER, false );
		curl_setopt ( $ch, CURLOPT_RETURNTRANSFER, true );
		curl_setopt ( $ch, CURLOPT_SSL_VERIFYPEER, false );
		curl_setopt ( $ch, CURLOPT_POST, true );
		curl_setopt ( $ch, CURLOPT_POSTFIELDS, array( 'file1' =&gt; '@' . $file ) );
		$data = curl_exec($ch);
		curl_close($ch);
		$data = json_decode( $data );
		if( isset( $data-&gt;error ) ) {
			return $this-&gt;error( $data );
		}
		$data = json_decode(
					$this-&gt;execute(
						'photos.save',
						array(
							'aid' =&gt; $album_id,
							'gid' =&gt; $this-&gt;group_id,
							'server' =&gt; $data-&gt;server,
							'photos_list' =&gt; $data-&gt;photos_list,
							'hash' =&gt; $data-&gt;hash,
							'caption' =&gt; $desc
						)
					)
				);
		if( isset( $data-&gt;error ) ) {
			return $this-&gt;error( $data );
		}
		return $data-&gt;response['0']-&gt;pid;
	}
	private function execute( $method, $params ) {
		$ch = curl_init( 'https://api.vk.com/method/' . $method . '?access_token=' . $this-&gt;token );
		curl_setopt ( $ch, CURLOPT_HEADER, false );
		curl_setopt ( $ch, CURLOPT_RETURNTRANSFER, true );
		curl_setopt ( $ch, CURLOPT_SSL_VERIFYPEER, false );
		curl_setopt ( $ch, CURLOPT_POST, true );
		curl_setopt ( $ch, CURLOPT_POSTFIELDS, $params );
		$data = curl_exec($ch);
		curl_close($ch);
		return $data;
	}
	private function error( $data ) {
		//обработка ошибок
		return false;
	}
}</code></pre>
<h2>Описание работы класса</h2>
<p>
	При создании экземпляра класса указываем токен, вероятность публикации поста на стену (т.к. был прецедент заморозки страницы, я ввел такой параметр; также для меня важнее добавление фотографии в альбом), id приложения, id группы или страницы.
</p>
<h3>Открытые функции</h3>
<p>
	Функция create_album создает альбом в группе, паблике или на странице пользователя. На входе у нее $name - название, $desc - описание. На выходе - id созданного альбома
</p>
<p>
	Функция get_album_size возвращает количество фотографий в альбоме (это необходимо, т.к. размер альбома ограничен 500 фотографиями). На входе: $id - id альбома. На выходе - количество фотографий.
</p>
<p>
	Функция upload_photo загружает фотографию в альбом. На входе: $file - путь до картинки на сервере, $album_id - id альбома, $desc - описание фотки (ограничено примерно 240-250 символами).
</p>
<p>
	Функция post отправляет сообщение на стену. На входе: $desc - текст, $photo - id фотографии в альбомах группы, паблика или пользователя, $link - привязываемая к посту ссылка.
</p>
<h3>Служебные функции</h3>
<p>
	Функция execute выполняет запрос к api.
</p>
<p>
	Функция error обрабатывает ошибки.
</p>
<h2>Заключение</h2>
<p>
	Думаю знающие смогут изменить класс по свои нужды в случае необходимости. На все ваши вопросы отвечу в комментариях.
</p>
<h2>Приложения</h2>
<p>
	<a href="/files/user_file/post/content/vk.class.php" target="_new">vk.class.php</a>
</p>
<p>
	<a href="http://dudev.ru/blog/57_Primyer-ispolzovaniya-klassa-avtopublikacii-postov-vkontaktye.html">Пример использования</a>
</p>''',
            category_id = 4
        )
        comment1 = Comment(
            content = '''В переменной $photo путь к фотографии содержится?''',
            email = 'fastyrus@mail.ru',
            author = 'Руслан',
            post_id = 20
        )
        comment2 = Comment(
            content = '''Добрый день, Руслан.<br>
<br>
Если вы про параметр метода <i>post</i>, то нет. Там содержится <b>ID</b> фотографии. <b>ID</b> фотографии возвращает метод загрузки фотографии в альбом <i>upload_photo</i>.''',
            email = 'admin@dudev.ru',
            author = 'Евгений',
            post_id = 20
        )
        comment3 = Comment(
            content = '''Спасибо. У вас фотография сначала загружается в специальный альбом методом upload_photo, который и возвращает id фотографии и путь до нее. А если нужно только фотографию кидать на стену к добавляемой записи, тогда в альбом же ее грузить не нужно?''',
            email = 'fastyrus@mail.ru',
            author = 'Руслан',
            post_id = 20
        )
        comment4 = Comment(
            content = '''При публикации вручную фотографии прямо на стену, она сохраняется в специальный альбом. Можно ли туда загружать фотографии через API не знаю. Надо пробовать.<br>
Но если туда не получится загрузить, то почему бы не создать для этих целей отдельный альбом?''',
            email = 'admin@dudev.ru',
            author = 'Евгений',
            post_id = 20
        )


	
	
        DBSession.add(cat1)
        DBSession.add(cat2)
        DBSession.add(cat3)
        DBSession.add(cat4)
        DBSession.add(page1)
        DBSession.add(page2)
        DBSession.add(page3)
        DBSession.add(post1)
        DBSession.add(post2)
        DBSession.add(post3)
        DBSession.add(post4)
        DBSession.add(post5)
        DBSession.add(post6)
        DBSession.add(post7)
        DBSession.add(post8)
        DBSession.add(post9)
        DBSession.add(post10)
        DBSession.add(post11)
        DBSession.add(post12)
        DBSession.add(comment1)
        DBSession.add(comment2)
        DBSession.add(comment3)
        DBSession.add(comment4)

