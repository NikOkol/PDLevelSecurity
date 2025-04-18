# security_measures.py

SECURITY_MEASURES = {
    "I. Идентификация и аутентификация субъектов доступа и объектов доступа (ИАФ)": [
        {"code": "ИАФ.1", "text": "Идентификация и аутентификация пользователей, являющихся работниками оператора, включая назначение уникальных идентификаторов, применение надежных методов аутентификации и контроль за корректностью выполнения этих процессов", "levels": [1, 2, 3, 4]},
        {"code": "ИАФ.2", "text": "Идентификация и аутентификация устройств, в том числе стационарных, мобильных и портативных, для защиты от несанкционированного доступа к информационным системам и обеспечения контроля за используемыми устройствами", "levels": [1, 2]},
        {"code": "ИАФ.3", "text": "Управление идентификаторами, в том числе создание, присвоение, уничтожение идентификаторов для пользователей, устройств и систем, с целью обеспечения конфиденциальности и целостности данных, а также для предотвращения возможных угроз безопасности", "levels": [1, 2, 3, 4]},
        {"code": "ИАФ.4", "text": "Управление средствами аутентификации, в том числе хранение, выдача, инициализация, блокирование средств аутентификации и принятие мер в случае утраты и (или) компрометации средств аутентификации с целью повышения уровня безопасности доступа", "levels": [1, 2, 3, 4]},
        {"code": "ИАФ.5", "text": "Защита обратной связи при вводе аутентификационной информации, чтобы предотвратить утечку данных, улучшить безопасность аутентификации и минимизировать риски утраты или компрометации информации", "levels": [1, 2, 3, 4]},
        {"code": "ИАФ.6", "text": "Идентификация и аутентификация пользователей, не являющихся работниками оператора (внешних пользователей), с целью обеспечения защиты системы от угроз, связанных с несанкционированным доступом со стороны внешних лиц или организаций", "levels": [1, 2, 3, 4]},
    ],

    "II. Управление доступом субъектов доступа к объектам доступа (УПД)": [
        {"code": "УПД.1", "text": "Управление учетными записями пользователей, включая заведение, активацию, блокирование, изменение и уничтожение учетных записей с целью обеспечения безопасности и ограничения доступа в зависимости от ролей и привилегий пользователей", "levels": [1, 2, 3, 4]},
        {"code": "УПД.2", "text": "Реализация методов и правил разграничения доступа, включая использование различных моделей разграничения доступа (дискреционный, мандатный, ролевой и другие), чтобы минимизировать риски несанкционированного доступа к данным и ресурсам системы", "levels": [1, 2, 3, 4]},
        {"code": "УПД.3", "text": "Управление информационными потоками, включая фильтрацию, маршрутизацию, контроль соединений, однонаправленную передачу и другие способы управления потоками информации между устройствами, сегментами системы и внешними сетями для обеспечения безопасности", "levels": [1, 2, 3, 4]},
        {"code": "УПД.4", "text": "Разделение полномочий пользователей, включая определение ролей и уровней доступа для разных категорий пользователей, чтобы предотвратить концентрацию полномочий и уменьшить риски злонамеренных действий", "levels": [1, 2, 3, 4]},
        {"code": "УПД.5", "text": "Назначение минимально необходимых прав и привилегий пользователям, администраторам и лицам, обеспечивающим функционирование системы, чтобы гарантировать, что каждый пользователь имеет доступ только к тем данным и функционалу, которые необходимы для выполнения его задач", "levels": [1, 2, 3, 4]},
        {"code": "УПД.6", "text": "Ограничение неуспешных попыток входа в систему с целью предотвращения атак методом подбора паролей и других форм несанкционированного доступа, что повышает уровень безопасности системы", "levels": [1, 2, 3, 4]},
        {"code": "УПД.10", "text": "Блокирование сеанса доступа в информационную систему после установленного времени бездействия пользователя или по его запросу, чтобы избежать утечек данных или несанкционированного доступа при оставлении устройства без присмотра", "levels": [1, 2, 3]},
        {"code": "УПД.11", "text": "Разрешение или запрет действий пользователей, разрешенных до идентификации и аутентификации, для защиты системы от выполнения действий без предварительной аутентификации, которые могут повлиять на безопасность данных", "levels": [1, 2, 3]},
        {"code": "УПД.13", "text": "Реализация защищенного удаленного доступа субъектов доступа к объектам доступа через внешние информационно-телекоммуникационные сети", "levels": [1, 2, 3, 4]},
        {"code": "УПД.14", "text": "Регламентация и контроль использования в информационной системе технологий беспроводного доступа", "levels": [1, 2, 3, 4]},
        {"code": "УПД.15", "text": "Регламентация и контроль использования в информационной системе мобильных технических средств", "levels": [1, 2, 3, 4]},
        {"code": "УПД.16", "text": "Управление взаимодействием с информационными системами сторонних организаций (внешние информационные системы)", "levels": [1, 2, 3, 4]},
        {"code": "УПД.17", "text": "Обеспечение доверенной загрузки средств вычислительной техники", "levels": [1, 2]},
    ],

    "III. Ограничение программной среды (ОПС)": [
        {"code": "ОПС.2", "text": "Управление установкой (инсталляцией) компонентов программного обеспечения, в том числе определение компонентов, подлежащих установке, настройка параметров установки компонентов, контроль за установкой компонентов программного обеспечения", "levels": [1, 2]},
        {"code": "ОПС.3", "text": "Установка (инсталляция) только разрешенного к использованию программного обеспечения и (или) его компонентов", "levels": [1]},
    ],

    "IV. Защита машинных носителей персональных данных (ЗНИ)": [
        {"code": "ЗНИ.1", "text": "Учет машинных носителей персональных данных", "levels": [1, 2]},
        {"code": "ЗНИ.2", "text": "Управление доступом к машинным носителям персональных данных", "levels": [1, 2]},
        {"code": "ЗНИ.8", "text": "Уничтожение (стирание) или обезличивание персональных данных на машинных носителях при их передаче между пользователями, в сторонние организации для ремонта или утилизации, а также контроль уничтожения (стирания) или обезличивания", "levels": [1, 2, 3]},
    ],

    "V. Регистрация событий безопасности (РСБ)": [
        {"code": "РСБ.1", "text": "Определение событий безопасности, подлежащих регистрации, и сроков их хранения", "levels": [1, 2, 3, 4]},
        {"code": "РСБ.2", "text": "Определение состава и содержания информации о событиях безопасности, подлежащих регистрации", "levels": [1, 2, 3, 4]},
        {"code": "РСБ.3", "text": "Сбор, запись и хранение информации о событиях безопасности в течение установленного времени хранения", "levels": [1, 2, 3, 4]},
        {"code": "РСБ.5", "text": "Мониторинг (просмотр, анализ) результатов регистрации событий безопасности и реагирование на них", "levels": [1, 2]},
        {"code": "РСБ.7", "text": "Защита информации о событиях безопасности", "levels": [1, 2, 3, 4]},
    ],

    "VI. Антивирусная защита (АВЗ)": [
        {"code": "АВЗ.1", "text": "Реализация антивирусной защиты", "levels": [1, 2, 3, 4]},
        {"code": "АВЗ.2", "text": "Обновление базы данных признаков вредоносных компьютерных программ (вирусов)", "levels": [1, 2, 3, 4]},
    ],

    "VII. Обнаружение вторжений (СОВ)": [
        {"code": "СОВ.1", "text": "Обнаружение вторжений", "levels": [1, 2]},
        {"code": "СОВ.2", "text": "Обновление базы решающих правил", "levels": [1, 2]},
    ],

    "VIII. Контроль (анализ) защищенности персональных данных (АНЗ)": [
        {"code": "АНЗ.1", "text": "Выявление, анализ уязвимостей информационной системы и оперативное устранение вновь выявленных уязвимостей", "levels": [1, 2, 3]},
        {"code": "АНЗ.2", "text": "Контроль установки обновлений программного обеспечения, включая обновление программного обеспечения средств защиты информации", "levels": [1, 2, 3, 4]},
        {"code": "АНЗ.3", "text": "Контроль работоспособности, параметров настройки и правильности функционирования программного обеспечения и средств защиты информации", "levels": [1, 2, 3]},
        {"code": "АНЗ.4", "text": "Контроль состава технических средств, программного обеспечения и средств защиты информации", "levels": [1, 2, 3]},
        {"code": "АНЗ.5", "text": "Контроль правил генерации и смены паролей пользователей, заведения и удаления учетных записей пользователей, реализации правил разграничения доступа, полномочий пользователей в информационной системе", "levels": [1, 2]},
    ],

    "IX. Обеспечение целостности информационной системы и персональных данных (ОЦЛ)": [
        {"code": "ОЦЛ.1", "text": "Контроль целостности программного обеспечения, включая программное обеспечение средств защиты информации", "levels": [1, 2]},
        {"code": "ОЦЛ.4", "text": "Обнаружение и реагирование на поступление в информационную систему незапрашиваемых электронных сообщений (писем, документов) и иной информации, не относящихся к функционированию информационной системы (защита от спама)", "levels": [1, 2]},
    ],

    "X. Обеспечение доступности персональных данных (ОДТ)": [
        {"code": "ОДТ.3", "text": "Контроль безотказного функционирования технических средств, обнаружение и локализация отказов функционирования, принятие мер по восстановлению отказавших средств и их тестирование", "levels": [1]},
        {"code": "ОДТ.4", "text": "Периодическое резервное копирование персональных данных на резервные машинные носители персональных данных", "levels": [1, 2]},
        {"code": "ОДТ.5", "text": "Обеспечение возможности восстановления персональных данных с резервных машинных носителей персональных данных (резервных копий) в течение установленного временного интервала", "levels": [1, 2]},
    ],

    "XI. Защита среды виртуализации (ЗСВ)": [
        {"code": "ЗСВ.1",  "text": "Идентификация и аутентификация субъектов доступа и объектов доступа в виртуальной инфраструктуре, в том числе администраторов управления средствами виртуализации",  "levels": [1, 2, 3, 4]},
        {"code": "ЗСВ.2",  "text": "Управление доступом субъектов доступа к объектам доступа в виртуальной инфраструктуре, в том числе внутри виртуальных машин",  "levels": [1, 2, 3, 4]},
        {"code": "ЗСВ.3",  "text": "Регистрация событий безопасности в виртуальной инфраструктуре",  "levels": [1, 2, 3]},
        {"code": "ЗСВ.6",  "text": "Управление перемещением виртуальных машин (контейнеров) и обрабатываемых на них данных",  "levels": [1, 2]},
        {"code": "ЗСВ.7",  "text": "Контроль целостности виртуальной инфраструктуры и ее конфигураций",  "levels": [1, 2]},
        {"code": "ЗСВ.8",  "text": "Резервное копирование данных, резервирование технических средств, программного обеспечения виртуальной инфраструктуры, а также каналов связи внутри виртуальной инфраструктуры",  "levels": [1, 2]},
        {"code": "ЗСВ.9",  "text": "Реализация и управление антивирусной защитой в виртуальной инфраструктуре",  "levels": [1, 2, 3]},
        {"code": "ЗСВ.10", "text": "Разбиение виртуальной инфраструктуры на сегменты (сегментирование виртуальной инфраструктуры) для обработки персональных данных отдельным пользователем и (или) группой пользователей", "levels": [1, 2, 3]},
    ],

    "XII. Защита технических средств (ЗТС)": [
        {"code": "ЗТС.3", "text": "Контроль и управление физическим доступом к техническим средствам, средствам защиты информации, средствам обеспечения функционирования, а также в помещения и сооружения, в которых они установлены, исключающие несанкционированный физический доступ к средствам обработки информации, средствам защиты информации и средствам обеспечения функционирования информационной системы, в помещения и сооружения, в которых они установлены", "levels": [1, 2, 3, 4]},
        {"code": "ЗТС.4", "text": "Размещение устройств вывода (отображения) информации, исключающее ее несанкционированный просмотр", "levels": [1, 2, 3, 4]},
    ],

    "XIII. Защита информационной системы, ее средств, систем связи и передачи данных (ЗИС)": [
        {"code": "ЗИС.1",  "text": "Разделение в информационной системе функций по управлению (администрированию) информационной системой, управлению (администрированию) системой защиты персональных данных, функций по обработке персональных данных и иных функций информационной системы",  "levels": [1]},
        {"code": "ЗИС.3",  "text": "Обеспечение защиты персональных данных от раскрытия, модификации и навязывания (ввода ложной информации) при ее передаче (подготовке к передаче) по каналам связи, имеющим выход за пределы контролируемой зоны, в том числе беспроводным каналам связи",  "levels": [1, 2, 3, 4]},
        {"code": "ЗИС.11", "text": "Обеспечение подлинности сетевых соединений (сеансов взаимодействия), в том числе для защиты от подмены сетевых устройств и сервисов", "levels": [1, 2]},
        {"code": "ЗИС.15", "text": "Защита архивных файлов, параметров настройки средств защиты информации и программного обеспечения и иных данных, не подлежащих изменению в процессе обработки персональных данных", "levels": [1, 2]},
        {"code": "ЗИС.17", "text": "Разбиение информационной системы на сегменты (сегментирование информационной системы) и обеспечение защиты периметров сегментов информационной системы", "levels": [1, 2]},
        {"code": "ЗИС.20", "text": "Защита беспроводных соединений, применяемых в информационной системе", "levels": [1, 2, 3]},
    ],

    "XIV. Выявление инцидентов и реагирование на них (ИНЦ)": [
        {"code": "ИНЦ.1", "text": "Определение лиц, ответственных за выявление инцидентов и реагирование на них", "levels": [1, 2]},
        {"code": "ИНЦ.2", "text": "Обнаружение, идентификация и регистрация инцидентов", "levels": [1, 2]},
        {"code": "ИНЦ.3", "text": "Своевременное информирование лиц, ответственных за выявление инцидентов и реагирование на них, о возникновении инцидентов в информационной системе пользователями и администраторами", "levels": [1, 2]},
        {"code": "ИНЦ.4", "text": "Анализ инцидентов, в том числе определение источников и причин возникновения инцидентов, а также оценка их последствий", "levels": [1, 2]},
        {"code": "ИНЦ.5", "text": "Принятие мер по устранению последствий инцидентов", "levels": [1, 2]},
        {"code": "ИНЦ.6", "text": "Планирование и принятие мер по предотвращению повторного возникновения инцидентов", "levels": [1, 2]},
    ],

    "XV. Управление конфигурацией информационной системы и системы защиты персональных данных (УКФ)": [
        {"code": "УКФ.1", "text": "Определение лиц, которым разрешены действия по внесению изменений в конфигурацию информационной системы и системы защиты персональных данных", "levels": [1, 2, 3]},
        {"code": "УКФ.2", "text": "Управление изменениями конфигурации информационной системы и системы защиты персональных данных", "levels": [1, 2, 3]},
        {"code": "УКФ.3", "text": "Анализ потенциального воздействия планируемых изменений в конфигурации информационной системы и системы защиты персональных данных на обеспечение защиты персональных данных и согласование изменений в конфигурации информационной системы с должностным лицом (работником), ответственным за обеспечение безопасности персональных данных", "levels": [1, 2, 3]},
        {"code": "УКФ.4", "text": "Документирование информации (данных) об изменениях в конфигурации информационной системы и системы защиты персональных данных", "levels": [1, 2, 3]},
    ],
}
