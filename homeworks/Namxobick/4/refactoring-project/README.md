## Теория

### Полезности

- `datetime`: https://docs.python.org/3/library/datetime.html
- `collections`: https://docs.python.org/3/library/collections.html
- `itertools`: https://docs.python.org/3/library/itertools.html
- `functools`: https://docs.python.org/3/library/functools.html
- `os`: https://docs.python.org/3/library/os.html
- `sys`: https://docs.python.org/3/library/sys.html
- `re`: https://docs.python.org/3/library/re.html
- `argparse`: https://docs.python.org/3/library/argparse.html

### Imports

- modules: https://docs.python.org/3/tutorial/modules.html
- Решаем проблему цикличных импортов: https://stackoverflow.com/questions/5748946/pythonic-way-to-resolve-circular-import-statements
- Откуда можно импортировать: https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH и https://stackoverflow.com/questions/19917492/how-to-use-pythonpath и http://www.johnny-lin.com/cdat_tips/tips_pylang/path.html
- Relative imports vs absolute: https://stackoverflow.com/questions/28400690/python3-correct-way-to-import-relative-or-absolute и http://pulkitgoyal.com/absolute-relative-imports


## Практика

Данное задание будет построено в формате ролевой игры, чтобы показать реальность подобных задач, ситуаций и подходов.

### Легенда

В компании, куда вы пришли работать, есть для вас первая задача.
Все сотрудники пользуются внутренней системой ведения учета задач.
Но вот проблема, в ней есть некоторые моменты, которые нужно улучшить.

Никто точно не помнит, кто написал программу и когда.
К сожаению, спросить, как она работает, некого.
Более того, сами сотрудники не могут посмотреть, что там в коде, потому что они не программисты.
Но они слышали, что там есть сложные части, а есть какие-то простые.
Вроде бы код написан нормально, но документации к нему не сохранилось.
Только инструкция по запуску.

### Технические требования

Менеджер подготовил для вас техническое задание, какие фичи он хотел бы увидеть:

- Необходимо добавить всем задачам визуальный статус готовности. Он должен выглядеть так: `+ ToDo: ...`, где `+` или `-` - статус готовности (`+` - выполнено, `-` - невыполнено), `ToDo` - название типа задачи и `...` - атрибуты задачи
- Необходимо реализовать команду `done`, которая бы отмечала задачи выполнеными (все задачи по-умолчанию невыполнены)
- Необходимо реализовать команду `undone`, которая бы отмечала задачи невыполнеными
- Необходимо добавить новый тип задачи: `ToReadItem`, у которой было бы два поля: `heading` и `url`. Следовательно: что прочитать и где

### Проверка результатов (для продвинуты, необязательно)

Старый разработчик был большим фанатом [TTD](https://en.wikipedia.org/wiki/Test-driven_development), и он успел перед своим уходом написать тесты, как должы работать все те новые требования.
Но закончить проект не успел.

В качестве проверки будем использовать их.
