from flask import Flask, request, send_file, jsonify
from docxtpl import DocxTemplate
app = Flask(__name__)
count = 0


@app.route('/test', methods=['GET', 'POST'])
def test():
    global count
    dict_person = {
        "Задача	Приобщить к физической культуре и здоровому образу жизни": "\n- с желанием принимает участие в активных видах досуга,"
                                                                              " в спортивных соревнованиях;"
                                                                              "\n- редко болеет;"
                                                                              "\n- проявляет инициативу в организации активного отдыха",
        "Сформировать стремление к здоровому образу жизни, отвращение к вредным привычкам": "\n- не имеет вредных привычек;"
                                                                                            "\n- соблюдает режим дня;"
                                                                                            "\n- соблюдает гигиену тренировок;"
                                                                                            "\n- предпочитает активный отдых",
        "Способствовать формированию осознанного и бережного отношения к природе": "\n- понимает важность сохранения природы;"
                                                                                   "\n- осознанно относится к природе, зря не вредит"
                                                                                   " растениям, а только в случае крайней необходимости;"
                                                                                   "\n- убирает за собой мусор в условиях природы, похода, улицы;"
                                                                                   "\n- правильно утилизирует мусор в условиях похода;"
                                                                                   "\n- спокойно ведет себя в лесу, старается не навредить его обитателям.",
        "Мотивировать к самостоятельной общественно-значимой деятельности": "\n- старается привести в порядок место стоянки;"
                                                                            "\n- инициирует различные природоохранные мероприятия;"
                                                                            "\n- принимает участие в природоохранных акциях, конкурсах;",
        "Способствовать формированию чувства коллективизма": "\n- имеет представление об уникальности флоры\фауны своего края;"
                                                             "\n- знает историю края, значимых для истории края личностей и их вклад в развитие региона;"
                                                             "\n- уважительно отзывается о том месте, в котором живет;"
                                                             "\n- стремиться внести свой вклад в развитие своего класса, школы, двора, поселка\села;"
                                                             "\n- бережно относится к природным, архитектурным, историческим местам, памятникам;"
                                                             "\n- знает и уважительно относится к символике края."
    }
    dict_params = {
        "tech": "Техническая",
        "sci": "Естественнонаучная",
        "art": "Художественная",
        "adv": "Туристско-краеведческая",
        "baseadv": "Основы туризма",
        "lendadv": "Краеведение",
        "schooldanger": "школа безопасности",
    }
    time_limit_dict = {
        'Изучить историю Хабаровского края': 18,
        'Познакомить с этнографией коренных малых народов севера, проживающих в Хабаровском крае': 18,
        'Познакомить с флорой и фауной Хабаровского края': 18,
        'Изучить географию Хабаровского края': 18,
        'Научить основам туристской подготовки': 18,
        'Научить основам гигиены и первой доврачебной помощи': 18,
        'Научить основам топографии и ориентирования': 18,
        'Научить основам краеведения': 18,
        'Научить основам безопасности жизнедеятельности': 18,
        'Научить правильному поведению в чрезвычайных ситуациях': 18,
        'Сформировать первичные умения по оказанию первой доврачебной помощи': 18,
        'Научить основам пожарно-прикладного и спасательного спорта (ППС)': 18,
        'Сформировать начальные умения в проектной деятельности': 9,
        'Научить основам исследовательской деятельности': 9,
    }
    result_dict = {
        'Изучить историю Хабаровского края':
            "\n- будут знать название края, региона, в котором они проживают,"
            " города и населенные пункты Хабаровского края;"
            "\n- будут знать главные"
            " вехи в истории Хабаровского края, роль его в годы ВОВ;"
            "\n- будут знать и"
            " находить на карте первые поселения на территории своего района."
        ,
        'Познакомить с этнографией коренных малых народов севера, проживающих в Хабаровском крае':
            "\n- будут знать традиционные занятия КМНС, места проживания, особенности быта и"
            " культуры коренных народов Хабаровского края"
        ,
        'Познакомить с флорой и фауной Хабаровского края':
            "\n- будут знать основных представителей флоры и фауны;"
            "\n- будут знать и отличать эндемики и редкие и охраняемые растения и животные ХК"
            "\n- будут знать и соблюдать правила поведения в природе, осуществлять природоохранную деятельность."
        ,
        'Изучить географию Хабаровского края':  "\n- знают размеры Хабаровского края, его природные особенности,"
            " географическое положение. основных представителей флоры и фауны, полезные ископаемые;"
            "\n- Могут показать на карте Хабаровский край, реку Амур, города Хабаровского края,"
            " муниципальные районы и их административные центры. "
        ,
        'Научить основам туристской подготовки':
            "\n- будут уметь использовать личное и групповое туристское снаряжение по назначению, "
            "разводить костер, ставить палатку, готовить на костре;"
            "\n- научатся преодолевать туристские препятствия;"
            "\n- получат опыт участия в походах выходного дня;"
            "\n- будут соблюдать правила поведения и техники безопасности во время занятий,"
            " походов, соревнований; "
        ,
        'Научить основам гигиены и первой доврачебной помощи':
            "\n- будут знать и соблюдать гигиенические требования в полевых условиях;"
            "\n- будут правильно одеваться для занятий в спортзале и на открытом воздухе;"
            "\n- будут соблюдать режим тренировок и отдыха"
            "\n- смогут осуществлять первичный самоконтроль физического состояния"
            "\n- смогут оказать первую помощь при закрытых переломах, ссадинах,"
            " наложить повязку, обработать рану, транспортировать пострадавщего;"
            "\n- будут знать правила сердечно-лёгочной реанимации"
        ,
        'Научить основам топографии и ориентирования':
            "\n- знают назначение спортивных карт и умеют ими пользоваться;"
            "\n- знают значение условных знаков и умеют их читать;"
            "\n- понимают что такое масштаб;"
            "\n- умеют ориентироваться по спортивной карте на местности;"
            "\n- могут составить план местности;"
            "\n- правильно определяют стороны света по компасу;"
        ,
        'Научить основам краеведения':
            "\n- знают историю образования края, его природные особенности, географическое положение."
            " основных представителей флоры и фауны, эндемики Дальнего Востока,"
            " полезные ископаемые;"
            "\n- знают памятники природы и истории Хабаровского края, "
            "могут пользоваться интерактивной картой памятников Хабаровского края."
        ,
        'Научить основам безопасности жизнедеятельности':
            "\n- знает причины пожаров и способы их предотвращения;"
            "\n- знает и соблюдает правила обращения с огнѐм;"
            "\n- знает порядок действий при возникновении загораний и пожара;"
            "\n- знает особенности горения синтетических материалов и способы прекращения горения;"
            "\n- знает и может применять первичные средства пожаротушения;"
            "\n- знает ядовитые растения, опасных животных и насекомых обитающих на территории Дальнего Востока"
            "\n- знает правила безопасного поведения на воде, при грозе."
        ,
        'Научить правильному поведению в чрезвычайных ситуациях':
            "\n- знает правила оптимального поведения при различных видах ЧС;"
            "\n- может обеспечить эвакуацию пострадавших в ЧС;"
            "\n- знает и может применить навыки выживания в ЧС;"
            "\n- знает и может подать сигналы бедствия различным путем."
        ,
        'Сформировать первичные умения по оказанию первой доврачебной помощи':
            "\n- будет знать правила оказания помощи при различных травмах."
            "\n- сможет наложить повязку, шину на перелом, остановить кровотечение;"
            "\n- может изготовить носилки разным способом;"
            "\n- будет знать необходимый минимальный состав аптечки;"
            "\n- будет знать правила применения лекарственных средств первой необходимости."
        ,
        'Научить основам пожарно-прикладного и спасательного спорта (ППС)':
            "\n- частие в конкурсах по по ППС и конкурсу WSR"
        ,
        'Сформировать начальные умения в проектной деятельности':
            "\n- знает, что такое проект, его структурные элементы;"
            "\n- соблюдает план и сроки выполнения проекта;"
            "\n- может сделать 6-8 слайдов к тексту защиты проекта;"
            "\n- может ответить на вопросы по сути созданного им проекта."
        ,
        'Научить основам исследовательской деятельности':
            "\n- знает и умеет применять методы исследования;"
            "\n- может составить диаграмму, график;"
            "\n- может провести эксперимент в рамках своей темы;"
            "\n- может представить результаты исследования."
        ,
        'Научить основам кооперации':
            "\n- умеют слушать и слышать друг друга;"
            "\n- принимает и выполняет возложенные обязанности, поручения при"
            " участии в разных формах групповой работы;"
            "\n- понимает свою ответственность за общий результат;"
            "\n- работает на результат, не смотря на межличностные отношения в группе."
        ,
        'Развить коммуникативные навыки':
            "\n- общается с большинством обучающихся в группе;"
            "\n- проявляет уважение к другим обучающимся, к педагогу;"
            "\n- может вербализовать свои вопросы, пожелания, задает"
            " вопросы и просит помощи в затруднительных ситуциях;"
            "\n- способен делиться (материалами, инструментами, знаниями, и т.д.);"
            "\n- проявляет эмпатию по отношению к другим обучающимся в группе;"
    }
    quest_data_dict = {
        'Изучить историю Хабаровского края': {
            "module_name": "История Хабаровского края",
            "teori": "Первые появления русских землепроходцев."
                     "Экспедиции И.Ю. Москвитина, В.Д. Пояркова, Е.П. Хабарова."
                     " Амурские сплавы. Первые поселения казаков на территории ХК."
                     " Условия жизни казаков и крестьян, основные занятия.\n"
                     "\tХабаровский край в годы ВОВ. Жизнь людей, работа предприятий в годы войны."
                     " Вклад жителей в дело победы. Знакомство с виртуальной картой памятных мест ВОВ. "
                     "Символа хабаровского края. Герб, флаг, гимн края. Значения цветов флага."
                     "  Символизм фигур на гербе.",
            "practic": "Работа с к\к. Отметить пути освоения Приамурья."
                       " Отметить первые русские поселения в вашем районе Разгадывание кроссворда."
                       " Подготовка презентаций по теме «Мой город\поелок\село в годы ВОВ."
                       " Участие в краеведческих конкурсах."
        },
        'Познакомить с этнографией коренных малых народов севера, проживающих в Хабаровском крае': {
            "module_name": "Этнография.",
            "teori": "Коренные народы Хабаровского края – исконные жители Приамурья:"
                     " эвены, эвенки, нанайцы, нивхи, орочи, негидальцы, удыгейцы."
                     " Их расселение и занятия Культура и быт. Легенды, мифы, сказки, народные приметы."
                     " Народные ремесла. Шаманизм коренных народов. Роль шаманов."
                     " Верования, духи, защита от злых  сил.\n\tБыт и культура коренных народов своего района.",
            "practic": "Работа с к\к. Отметить на карте места компактного расселения разных национальностей,"
                       " национальные села вашего района. Разгадывание кроссворда, ребуса."
                       " Изготовление нанайской куклы по образцу из бумаги."
                       " Изготовление поделки «Оберег».\n"
                       " \tЭкскурсия в местный краеведческий музей (виртуальная экскурсия при отсутствии такового)."
        },
        'Познакомить с флорой и фауной Хабаровского края': {
            "module_name": "Флора и фауна Хабаровского края",
            "teori": "Особенности природы, связанные с протяженностью ХК с севера на юг. Разновидности лесов. Тайга."
                     "  Основные виды деревьев и кустарников. Животные, проживающие в Хабаровском крае."
                     " Эндемики ХК. Что такое эндемики?\n\t Красная книга ХК. "
                     "Исчезающие животные, обитающие на территории вашего района."
                     " Что такое заказник, заповедник, памятник природы. Заповедные места ХК.",
            "practic": "Определение по рисунку (гербарию) растений. Экскурсия в лес."
                       "  Игра-лото с названиями животных (10- 15 животных с названием и описанием)."
                       " Изготовление поделки «Лотос» из бумаги. "
                       "Изготовление листовок о защите редких и исчезающих животных и растениях (по выбору)."
                       " Участие в природоохранной акции. Разгадывание кроссворда по теме.\n\t"
                       " Экскурсия в заповедник, заказник, к памятнику природы виртуальная экскурсия."
        },
        'Изучить географию Хабаровского края': {
            "module_name": "География Хабаровского края ",
            "teori": "Хабаровский край, его природные особенности, географическое положение, климат,"
                     " его рельеф, крупнейшие реки, полезные ископаемые. Разнообразие растительного"
                     " и животного мира, обоснованное протяженностью Хабаровского края с севера на юг. "
                     "Административное деление, города и районные центры."
                     " Зависимость социально-экономического развития муниципалитетов от природных условий."
                     " Туристические возможности края (района). ",
            "practic": "Работа с атласом и контурной картой Хабаровского края: обозначение административной"
                       " и государственной границ, граничащих субъектов и государств; река Амур,"
                       " города Хабаровского края, муниципальные районы и их административные центры."
                       " Разработка туристической тропы по территории муниципального района. "
        },
        'Научить основам туристской подготовки': {
            "module_name": "Основы туристской подготовки",
            "teori": "Туристско-краеведческая деятельность учащихся. "
                     "Активные формы туристско-краеведческой деятельности."
                     " Туризм — средство познания своего края, физического и духовного развития,"
                     " оздоровления, воспитания самостоятельности. \n\t"
                     "«Туристские походы. Техника безопасности при проведении туристских походов»."
                     " Определение цели и района похода."
                     " Распределение обязанностей в группе. "
                     "Разработка маршрута, составление плана-графика движения.\n\tОрганизация туристского быта. "
                     "Привалы и ночлеги. Туристский бивак. Виды костров. Выбор места для привала и ночлега (бивака). "
                     "Основные требования к месту привала и бивака.\n\tПонятие о личном и групповом снаряжении. "
                     "Личное снаряжение для походов выходного дня (ПВД) и степенных походов, требования к нему."
                     " Групповое снаряжение, требования к нему."
                     " Типы палаток, их назначение.\n\tОрганизация питания в 2-3-дневном походе. Меню."
                     " Продуктовая раскладка (список продуктов и их количество). Рецепты походных блюд",
            "practic": "Подготовка и проведение похода. Составление плана подготовки похода. "
                       "Изучение маршрута похода. Подбор снаряжения для похода. Составление меню. "
                       "Фасовка, упаковка и переноска продуктов в рюкзаках. Приготовление пищи в полевых условиях."
                       "  Установка палаток различных видов. Разведение костра. Установка тента."
                       "Развёртывание и свёртывание лагеря (бивака)."
        },
        'Научить основам гигиены и первой доврачебной помощи': {
            "module_name": "Основы гигиены и первая доврачебная помощь",
            "teori": "Личная гигиена туриста, профилактика заболеваний."
                     " Применение средств личной гигиены в походах и во время тренировочного процесса."
                     " Подбор одежды и обуви для тренировок и походов, уход за одеждой и обувью. "
                     "Особенности соблюдения гигиенических правил в походных условиях. \n\t"
                     "Основные приёмы оказания первой доврачебной помощи. Походный травматизм. "
                     "Помощь при различных травмах. "
                     "Сердечно-лёгочная реанимация.\n\tВлияние систематических занятий"
                     " физической культурой и спортом на укрепление здоровья, развитие"
                     " физических качеств: силы, быстроты, ловкости, гибкости, выносливости."
                     " Формирование правильной осанки. Гармоническое телосложение как основа долголетия."
                     " Значение и содержание врачебного контроля, и формы работы по врачебному контролю."
                     " Значение и содержание самоконтроля спортсмена.\n\tПоходная медицинская аптечка, "
                     "ее назначение. Состав походной аптечки. Хранение и транспортировка аптечки в походных условиях.",
            "practic": "Наложение жгута, ватно-марлевой повязки, обработка ран. Виды повязок."
                       " Оказание первой помощи условно пострадавшему"
                       " (ссадины, порезы, потёртости, травма головы, перелом предплечья, перелом голени,"
                       " перелом пальца руки). Сердечно-лёгочная реанимация. Транспортировка пострадавшего.\n\t"
                       "Применение методов самоконтроля физического состояния: измерение пульса, частоты дыхания. \n\t"
                       "Сбор походной аптечки. Упаковка, хранение лекарственных средств."
        },
        'Научить основам топографии и ориентирования': {
            "module_name": "Топография и ориентирование",
            "teori": "План и карта. Понятие о топографической карте, спортивной карте."
                     " Условные знаки, их назначение. Масштаб. Виды масштабов.\n\t"
                     " Компас. Типы компасов. Правила обращения с компасом."
                     " Определение сторон горизонта по компасу, ориентирование карты по компасу.",
            "practic": "Составление плана помещения. Изучение условных знаков топографических карт."
                       " Знакомство с различными формами рельефа. Топографические диктанты,"
                       " упражнения на запоминание знаков. «Путешествия» по картам."
                       " Ориентирование карты по компасу."
                       " Практикум по ориентированию на местности в реальных условиях."
                       " Соревнования по ориентированию на местности."
        },
        'Научить основам краеведения': {
            "module_name": "Основы краеведения ",
            "teori": "Хабаровский край, его природные особенности, географическое положение."
                     " Климат, растительность и животный мир Хабаровского края, его рельеф, реки, озёра,"
                     " полезные ископаемые. Памятники истории и культуры."
                     " Малочисленные народы проживающие на территории Хабаровского края – коренные жители края."
                     " Их культура, быт, традиции. История города Хабаровска.\n\tТуристские возможности родного края,"
                     " обзор экскурсионных объектов, музеи. Наиболее интересные места для проведения походов."
                     " Памятники истории и культуры, музеи края.\n\t Общественно-полезная работа в путешествии,"
                     " охрана природы и памятников культуры»",
            "practic": "Экскурсия в краеведческий музей. Виртуальные экскурсии по достопримечательностям "
                       "Хабаровского края. Работа с контурной картой края. "
                       "Проведение уроков краеведения для учащихся школы.\n\tСанитарная уборка биваков"
                       " и троп во время проведения туристских путешествий. "
        },
        'Научить основам безопасности жизнедеятельности': {
            "module_name": "Окружающая среда и опасности повседневной жизни",
            "teori": "Понятия об опасных и вредных факторах окружающей среды. "
                     "Источники опасных и вредных факторов на улице, дома, в природе.\n\t"
                     " Пожары в жилых помещениях, причины их возникновения. Опасные факторы горения."
                     " Особенности горения синтетических материалов."
                     " Способы прекращения горения веществ и материалов. Подручные (первичные)"
                     " средства пожаротушения и порядок их применения."
                     " Правила поведения и действия при возникновении загораний и пожара."
                     " Меры предохранения от получения ожогов, отравлений газом и дымом."
                     " Оказание первой помощи пострадавшим при пожаре."
                     "  Электробезопасность при пользовании электроэнергией в бытовых помещениях."
                     " Средства бытовой химии и меры предосторожности при их использовании."
                     " Правила поведения в общении с природой и животным миром.."
                     " Меры предосторожности во время грозы. Ядовитые растения, опасные животные и насекомые."
                     " Правила безопасного поведения на воде. ",
            "practic": "Применение подручных средств пожаротушения, практика пользования техническими"
                       " средствами пожаротушения, профилактика и оказание помощи при поражении электротоком,"
                       " оказание помощи при отравлениях, оказание первой помощи утопающему"
        },
        'Научить правильному поведению в чрезвычайных ситуациях': {
            "module_name": "Чрезвычайные ситуации природного и техногенного характера.",
            "teori": "Краткая характеристика стихийных бедствий, наиболее опасных для Дальнего Востока,"
                     " их физическая сущность, причины возникновения, характер и стадии развития"
                     " Первичные и вторичные опасные факторы стихийных бедствий."
                     " Способы обеспечения безопасности человека, правила поведения и действия при"
                     " стихийных бедствиях.\n\t Аварии и катастрофы на промышленных предприятиях,"
                     " гидротехнических сооружениях, транспорте и их возможные последствия"
                     " (химическое заражение, затопление, массовые пожары). Потенциальные опасности"
                     " аварий и катастроф местных предприятий и других объектов народного хозяйства.\n\t"
                     " Система международных сигналов бедствия. Знаки-сигналы на местности для воздушных"
                     " поисковых спасательных служб.",
            "practic": "Отработка способов химической защиты. Очистка воды подручными средствами."
                       " Изготовление и применение плавсредств для эвакуации."
                       "  Отработка эвакуации пострадавших с различных видов объектов (многоэтажный дом,"
                       " колодец, машина после ДТП, с дерева и т.п.) "
        },
        'Сформировать первичные умения по оказанию первой доврачебной помощи': {
            "module_name": "Первая доврачебная помощь.",
            "teori": "Оказание первой помощи при кровотечениях, переломах, травмах головы, ушибах. Виды повязок."
                     " Наложение шин. Транспортировка пострадавшего, изготовление носилок из подручных средств."
                     " Транспортировка при травмах головы. Сердечно-легочная реанимация. Непрямой массаж сердца и"
                     " искусственное дыхание. Оказание помощи при: отравлениях и ожогах средствами бытовой химии;"
                     " при отравлении, укусе змеи, насекомого, утоплении, пострадавшему от электрического тока,"
                     " переохлаждении. Аптечка для похода: состав, назначение, применение.",
            "practic": "отработка правильного наложения повязок жгутов, шин;\n"
                       "отработка сердечно-легочной реанимации;\n"
                       "подготовка аптечки для похода;\n"
                       "отработка транспортировки пострадавшего с изготовлением носилок разным способом."
        },
        'Научить основам пожарно-прикладного и спасательного спорта (ППС)': {
            "module_name": "Пожарно-прикладные  и спасательные соревнования и конкурсы. ",
            "teori": "История ППС.  Виды ППС. Классификация по пожарно-прикладным упражнениям,"
                     " утвержденные нагрудные знаки, а также положения о порядке присвоения звания"
                     " «Мастера спорта СССР» и спортивных разрядах."
                     "  Включение пожарно-прикладного спорта в Единую Всесоюзную Спортивную Квалификацию."
                     " Правила проведения соревнований по видам ППС: общие положения, старт,"
                     " бег по дистанции, финиш. Пожарно-техническое вооружение. Виды соревнований."
                     " Последовательность проведения соревнований по видам предусматривается положением"
                     " о соревнованиях или устанавливается на месте судейской коллегией.\n\tСпасательные"
                     " работы, как компетенция конкурсного движения «Молодые профессионалы"
                     " (Ворлдскиллс Россия)» (далее WSR).\n\tСтандарты, которые предъявляются участникам"
                     " для возможности участия в соревнованиях, а также принципы, методы и процедуры,"
                     " которые регулируют соревнования.",
            "practic": "Отработка навыков работы с оборудованием. Подготовка к соревнованиям по ППС и  конкурсу WSR"
        },
        'Сформировать начальные умения в проектной деятельности': {
            "module_name": "Основы проектной деятельности",
            "teori": "Что такое проект, его структурные элементы. Сроки и планирование работы над проектом."
                     " Представление проекта и его результатов."
                     " Интерфейс и правила создания презентации в программе PowerPoint. Защита проекта."
                     " Культура речи при защите проекта.",
            "practic": "Работа над проектом. Подготовка защиты под руководством педагога, составление текста."
                       " Создание презентации в программе PowerPoint для защиты проекта."
        },
        'Научить основам исследовательской деятельности': {
            "module_name": "Основы исследовательской деятельности.",
            "teori": "Исследование и проект, отличия и сходства. Методы исследования. Эксперимент."
                     " Методы описания и представления результатов исследования. Диаграммы. Графики. Анализ результатов",
            "practic": "Исследовательская работа. Составление описания и защиты исследования."
                       " Составление графиков, диаграмм. "
        },
        'Научить основам кооперации': {
            "module_name": "Основы кооперации",
            "teori": "",
            "practic": ""
        },
        'Развить коммуникативные навыки': {
            "module_name": "",
            "teori": "",
            "practic": ""
        }
    }
    dop_list = ['en_form_edu', 'en_subject_taskss', 'en_metasubject_tasks', 'en_personal_tasks', 'en_metasubject_tasks_no']
    data_dict = {}
    for key, item in request.values.lists():
        if key in dop_list:
            data_dict[key] = item
        else:
            data_dict[key] = item[0]
    modules_dict = []
    subj_data_dict = []
    data_dict["cop_meta_result"] = []
    data_dict["cop_sub_result"] = []
    if data_dict["en_training_periodn"] == "36":
        if data_dict["en_duration_lesson_choice"] == "1":
            data_dict["en_duration_lesson"] = "1"
            data_dict["en_number_classes"] = "2"
        if data_dict["en_duration_lesson_choice"] == "2":
            data_dict["en_duration_lesson"] = "2"
            data_dict["en_number_classes"] = "1"
        if data_dict["en_duration_lesson_choice"] == "3":
            data_dict["en_duration_lesson"] = "1"
            data_dict["en_number_classes"] = "1"
    dop_dict = {
        "tech": "Развитие технических способностей ",
        "sci": "Формирование устойчивого интереса к исследовательской деятельности",
        "art": "Развитие творческих способностей",
        "adv": "Духовно-нравственное воспитание средствами туристско-краеведческой деятельности"
    }
    data_dict['cop_meta_result'] = ''
    data_dict['cop_sub_result'] = ''
    data_dict['cop_person_result'] = ''
    data_dict["en_program_objectives"] = dop_dict[data_dict["en_orientation"]]
    all_time = int(data_dict["en_training_periodn"]) * int(data_dict["en_duration_lesson"]) * int(data_dict["en_number_classes"]) // 18
    if len(data_dict['en_subject_taskss']) > 0:
        for item in data_dict['en_subject_taskss']:
            modules_dict.append({"name": item, "time": time_limit_dict[item]})
            subj_data_dict.append(quest_data_dict[item])
            data_dict["cop_meta_result"] += result_dict[item]
    if len(data_dict['en_metasubject_tasks']) > 0:
        for item in data_dict['en_metasubject_tasks']:
            if all_time >= len(data_dict['en_subject_taskss']) + 1:
                modules_dict.append({"name": item, "time": time_limit_dict[item]})
            subj_data_dict.append(quest_data_dict[item])
            data_dict["cop_sub_result"] += result_dict[item]
    if len(data_dict['en_metasubject_tasks_no']) > 0:
        for item in data_dict['en_metasubject_tasks_no']:
            if item in result_dict.keys():
                data_dict["cop_sub_result"] += result_dict[item]
    if len(data_dict['en_personal_tasks']) > 0:
        for item in data_dict['en_personal_tasks']:
            if item in dict_person.keys():
                data_dict['cop_person_result'] += dict_person[item]
    data_dict['modules'] = modules_dict
    data_dict['plan_list'] = subj_data_dict
    data_dict['en_orientation'] = dict_params[data_dict['en_orientation']]
    data_dict['en_type_activity'] = dict_params[data_dict['en_type_activity']]
    name = f"program {count}.docx"
    doc1 = DocxTemplate("5.docx")
    doc1.render(data_dict)
    doc1.save(name)
    count += 1
    return send_file(name)
    # return jsonify({})


if __name__ == '__main__':
    app.run()
