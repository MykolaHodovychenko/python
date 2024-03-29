# Основы Python

Чтобы успешно использовать любой язык программирования, нам необходимо освоить два навыка:

- прежде всего, вам необходимо изучить язык программирования - вам необходимо изучать словарь и грамматику. После этого, необходимо научиться правильно произносить слова на новом языке и знать, как строить грамотные "предложения" на этом языке;
- после этого, вам необходимо "рассказать историю". При написании истории, вы комбинируете слова и предложения, чтобы донести до читателя некоторые идеи. В программировании, наша программа будет "историей", а задача, которую нужно решить будет "идеей".

Как только вы изучите Python, вы обнаружите, что изучить другие языки будет гораздо легче. Новый язык программирования будет иметь другой словарь и грамматику, но навыки решения поставленных задач пригодятся вам вне зависимости от используемого языка программирования.

Вы быстро выучите "словарь" и научитесь составлять "предложения" на языке Python. Для получения навыка написания грамотных программ понадобится гораздо больше времени. Изучение программирования похоже на изучения письма. Мы начнем с чтения и объяснения программ, потом мы попытаемся писать простые программы, потом мы начнем писать все более сложные программы. 

В какой-то момент мы увидите шаблоны и приемы для создания программ, после чего вы сможете самостоятельно решать поставленные перед вами задачи путем написания программ на языке программирования. Как только вы научитесь решать поставленные задачи, программирования превратится в очень занимательный и творческий процесс.

Мы начнем изучать Python со словаря и базовой структуры программы. Будьте терпеливы, так как простые примеры будут напоминать вам о тех временах, когда вы только учились читать.

## Ключевые слова Python

В отличие от человеческого языка, словарь Python очень мал. 

В языках программирования словарь называют **"зарезервированными словами"** или **"ключевыми словами"** (**reserved words** или **keywords**). Когда Python видит эти слова, для него они имеют только одно значение. 

Позже, когда вы будете писать программы, вы будете создавать свои слова, которые будут называться **переменными** (**variables**).Правильно подобрать название переменной - не такая простая задача как кажется, но вы не сможете использовать зарезервированные слова в качестве названия переменных.

Список зарезервированных слов в Python выглядит следующим образом:

| Keyword    | Keyword |Keyword | Keyword|
|-----------|------------|----|----|
​False|class|from|or|
​None|continue|global|pass|
True|def|if|raise
and|del|import|return|
as|elif|in|try
assert|else|is|while|
async|except|lambda|with|
await|finally|nonlocalyield|
break|for|not
​
Мы постепенно будем изучать, что значат те или иные слова, но сейчас мы сосредоточимся на возможности "разговаривать"

```python
print("Hello, world!")
```

Итак, мы написали наше первое корректное предложение на языке Python. Наше предложение начинается со слова `print()`, после которого идет строка текста в кавычках, заключенная в скобки.

## Значения и типы

**Значения** (**values**) являются одними из базовых вещей, с которыми работает программа. Значения - это данные, которыми оперирует программа. Например, это цифры 1, 2 или текстовая строка `"Hello, world!"`.
Значения принадлежат к разным типам данных (data type): 2 - это **целое число** (**integer**), `"Hello, world!"` это **строка** (**string**). Python понимает что это текстовая строка, потому что она заключена в кавычки.

Python может выполнить команду `print` и с целым числом

```python
>>> print (5)
5
```

Если вы не уверены, какой тип имеет значение, вы можете вызвать команду `type`, чтобы Python вам подсказал

```python
>>> type("Hello")
<type 'str'>

>>> type(17)
<type 'int'>

>>> type(5.0)
<type 'float'>
```

Мы уже знакомы с типом `string` и с типом `integer`, но новым типом для нас является тип `float` - сокращение от `floating point` (`число с плавающей точкой`).

А что, если мы попробуем узнать тип следующих значений `"17"` или `"3.2"`?

```python
>>> type("17")
<type 'str'>

>>> type("3.2")
<type 'str'>
```

Они являются строками, так как заключены в кавычки.

## Переменные

Одной из самых мощных "фишек" языков программирования является возможность манипулировать переменными (variable). Переменная ссылается на определенное значение в памяти.

Когда вы только начинаете изучать программирование, думайте о переменной как о контейнере. Переменная хранит значения, чтобы вы потом могли их повторно использовать в программе. Это сокращает избыточность, улучшает производительность и делает код более читабельным.

Для того, чтобы использовать переменную, вы сначала должны **присвоить значение переменной**. Позже, вы можете получить доступ к значению через переменную. Вы можете присваивать переменным другие значения.

Для задания переменной значения используется **инструкция присвоения** = (**assignment statement**). Используем инструкцию присвоения для создания новой переменной и присвоения ей значения

```python
>>> message = "Hello"
>>> n = 924
>>> pi = 3.14159
```

При попытке создать переменную с именем `class`, Python выдаст ошибку

```python
>>> class = "Hi!"
  File "<stdin>", line 1
    class = "Hi!"
          ^
SyntaxError: invalid syntax
```

Мы попытались использовать зарезервированное слово `class` для имени переменной, чего делать нельзя - когда Python видит слово `class` - он ожидает определенный код и, не находя его, выдает ошибку синтаксиса.

Мы можем вывести на экран значения созданных нами переменных с помощью функции `print()`

```python
>>> print (n)
924

>>> print (pi)
3.14159

>>> print (message)
Hello
```

С помощью команды `type` мы можем вывести на экран тип переменной. В Python тип переменной зависит от того, на данные какого типа переменная ссылается.

```python
>>> type(message)
<type 'str'>

>>> type(pi)
<type 'float'>

>>> type(n)
<type 'int'>
```

### Имена переменных

Как правило, программисты выбирают осмысленные имена переменных. Хорошее название переменной должно "документировать себя" - отражать содержимое и назначение переменной.

Имя переменной может быть сколь угодно длинным, оно может содержать буквы и цифры, но оно не может начинаться с цифры. Вы можете использовать заглавные буквы для имен переменных, но это является плохой практикой в Python и желательно избегать этого.

Если переменная состоит из нескольких слов, в Python принято каждое слово отделять нижним подчеркиванием (`_`), например: `max_speed` или `word_length`. Имена переменной может начинаться с нижнего подчеркивания, но такие переменные имеют специальное предназначение и мы рассмотрим это позже

```python
>>> 4dudes = 500
  File "<stdin>", line 1
    4dudes = 500
         ^
SyntaxError: invalid syntax

>>> var@ = 10000
  File "<stdin>", line 1
    var@ = 10000
       ^
SyntaxError: invalid syntax
```

Из примера мы видим, что переменная `4dudes` является некорректной, так как она начинается с цифры, переменная `var@` также является некорректной, так как содержит символ `@`, который не является символом алфавита или цифрой.

## Statements (инструкции)

**Инструкция** (**statement**) - это часть кода, которую Python может выполнить. Код на Python представляет из себя последовательность инструкций.

Python выполняет программу путем выполнения инструкций друг за другом, пока все инструкции не будут выполнены. В общем случае, Python выполняет инструкции сверху вниз.

Python выполняет инструкции путем вычисления выражений одно за одним, после чего Python применяет операции к этим выражениям.

> Присвоение значения переменной является инструкцией!

## Выражения

**Выражение** (**expression**) - это комбинация из значений, переменных и операторов.

> В языках программирования, значение само по себе является выражением, поэтому нижеприведенные примеры являются корректными выражениями

```python
>>> x = 20 # Это statement

>>> 17 # Это выражение
17

>>> x # Это тоже выражение
20

>>> x + 17 # Вычисляется значение выражения
37
```

Если вы напечатаете выражения в интерактивном режиме, Python вычислит значение выражения и выведет значение в качестве результата. Однако, в коде программы выражение само по себе ничего не делает.

Python вычисляет значение выражения путем вычисления значений под-выражений, а потом применяет операции к этим под-выражениям.

> Вызов функции в Python является выражением.

## Операторы и операнды

**Операторы** (**operator**) - специальные символы, которые выполняют вычисления, например, сложение или умножение. Значения, к которым применяется оператор называются операндами.

Давайте рассмотрим арифметические операторы в Python и какие вычисления они выполняют

|Оператор|Значение|
|---|--|
|`+`|сложение|
|`-`|вычитание|
|`*`|умножение|
|`/`|деление|
|`//`|целочисленное деление|
|`**`|возведение в степень|
|`%`|деление по модулю (взятие остатка от деления)|

Нам следует остановиться на операциях деления и целочисленного деления. Зачем нужны две операции деления?

Дело в том, что в различных языках программирования операция деления может вести себя по-разному. Например, в языке программирования **C** результатом деления целого числа на целое число будет целое число. Если при делении возникнет остаток, он будет отброшен - число округлится до ближайшего меньшего целого. Например

```c++
int main(void) {
  printf("%d\n", 3/6);
  return 0;
}
```

Выдаст результат равный `0`. Из общего понимания математики мы ожидали увидеть ответ равным `0.5`, но это дробное число - тип `float`. Так как в языке **C** деление целого числа на целое число даст целое число, дробная часть будет отброшена и в результате мы получим `0`.

Если мы хотим получить корректный ответ, мы должны один из операндов сделать числом с плавающей точкой. Тогда, по правилам языка **C**, если один из операндов будет `float`, то результат операции также будет `float`. Код

```c++
int main(void) {
  printf("%f\n", 3/6.0);
  return 0;
}
```

даст нам результат `0.5`.

В языке Python дело обстоит иначе - при использовании обычного деления Python правильно поймет наши намерения и результатом деления целого числа на целое число будет число с плавающей точкой.

```python
>>> 3/6
0.5
```

Если же мы хотим, чтобы Python повел себя как язык C, мы можем воспользоваться оператором целочисленного деления. Тогда результатом деления одного целого числа на второе целое число будет целое число.

```python
>>> 3//6
0
```

### Порядок операций в выражении

Когда в выражении присутствуете более одного оператора, порядок вычисления зависит от приоритета операции. Для арифметических операторов, Python соблюдает общепринятую математическую конвенцию. Для того, чтобы запомнить приоритет операторов, запомните акроним **PEMDAS**:

- **P**arentheses (скобки) имеют наивысший приоритет, с помощью скобок вы можете точно выстроить нужный порядок вычисления выражений;
- **E**xponentiation (возведение в степень) имеет следующий по приоритету порядок. Например, выражение `2**1+1` будет равно `3`, а не `4`;
- **M**ultiplication (умножение) и **D**ivision (деление) имеют одинаковый приоритет. Такой же приоритет имеет операция деления по модулю (*Modulo*);
- наименьший приоритет имеют **A**ddition (сложение) и **S**ubtraction (вычитание);
- операторы с одинаковым приоритетом выполняются слева направо.

#### Оператор деления по модулю (Modulo)

Оператор деления по модулю используются с двумя целочисленными операндами и возвращает остаток от деления первого операнда на второй.

Оператор деления по модулю бывает очень полезен в некоторых ситуациях. Например, вы можете узнать - делится ли одно число нацело на второе (остаток от деления будет `0`) или получить крайне правые цифры в числе (например, выражение `x % 10` вернет единицы, выражение `x % 100` вернет две правые цифры числа).

### Арифметические операции со строками

Выражение и его результат зависит не только от операторов, но и от типа данных, к которым применяется тот или иной оператор. Применительно ко строкам можно применить некоторые арифметические операторы, но результат выражений будет совершенно иным

|Оператор|Значение|
|---|--|
|`+`|конкатенация (сложение) строк. Оба операнда должны быть строками|
|`*`|повторение строк. Первый операнд - строка, второй операнд - целое число|
|`%`|форматирование строк (будет рассмотрено в отдельной теме)|

Операция конкатенации используется для "склеивания" строк. Оба операнда выражения должны быть строкой, в противном случае Python выдаст ошибку

```python
>>> "Hello," + " world!"
'Hello, world!'

>>> "hello" + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

Операция повторения позволяет создать новую строку, которая будет повторенной несколько раз исходной строкой

```python
>>> "abc" * 2
'abcabc'

>>> "aabb" * 5
'aabbaabbaabbaabbaabb'

>>> "aa " * 5
'aa aa aa aa aa '

>>> "aa" * 2.0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cant multiply sequence by non-int of type 'float'
```

## Консольный ввод в Python

Так как программа без данных не имеет смысла, мы так или иначе будем сталкиваться с необходимостью ввести данные в программу.
Существует много способов получения данных: чтение из файла, получение данных по сети, загрузка данных из базы данных, пользовательский ввод (с клавиатуры, мыши, других устройств) и так далее.
В рамках данного курса мы рассмотрим несколько способов получения входных данных, но пока остановимся на самом простом для реализации способе - пользовательский ввод из консоли.
Python предоставляет встроенную функцию (потом мы разберем, что это такое) под названием `input()`. После выполнения statement, который содержит функцию `input()`, Python приостанавливает выполнение программы и ждет ввода пользователя с клавиатуры. Когда пользователь введет нужные данные и нажмет Enter, программа продолжит свою работу

<p align="center">
    <img src = "https://files.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LnmXmI-D1suCZkVT17D%2F-MH_lPqwG54ZnNOTmvo4%2F-MH_mEC1aragqfLneuFN%2Fpython%20-%20%20Anaconda%20Prompt%20(anaconda3)%20-%20python%20(2)%20(1).gif?alt=media&token=702064a5-4e73-4086-8d80-455c6d3b2362"/>
</p>

Обратите внимание, что после названия функции `input()` мы указываем пустые скобки - это синтаксис вызова функции.

Функции в Python возвращают значение. Функция `input()` возвращает строку с тем, что ввел пользователь. На видео выше мы видим, что мы ввели текст `user input`, после чего функция `input()` вернула `user input`, но это просто выражение в виде строки `user input`, которое просто выводится на экран, так как мы находимся в интерактивном режиме. Если мы напишем программу и запустим ее в среде разработки, ничего не произойдет.

<p align="center">
    <img src = "https://files.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LnmXmI-D1suCZkVT17D%2F-MH_dVt-hpQQzWkbSl7f%2F-MH_fAtgUXeScklzFKl4%2FSpyder%20(Python%203.8)%20-%20%20Spyder%20(Python%203.8).gif?alt=media&token=31c5e811-e0d2-42d0-96de-5f9207792f63"/>
</p>

Чтобы работать со входными данными, мы должны сохранить наш ввод. Это мы можем сделать с помощью переменной - мы сохраним пользовательский ввод как значение переменной.

```python
my_input = input()
print("Вы ввели " + my_input)
```

Работа программы будет выглядеть следующим образом

<p align="center">
    <img src = "https://files.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LnmXmI-D1suCZkVT17D%2F-MH_dVt-hpQQzWkbSl7f%2F-MH_ibKDSF5OP5O8cBnX%2FSpyder%20(Python%203.8)%20-%20%20Spyder%20(Python%203.8)%20(1)%20(2).gif?alt=media&token=d0dfbc06-c39d-4fba-aa13-4eac255c4ba8"/>
</p>

Давайте внимательно разберем statement

```python
my_input = input()
```

1. Вызывается функция `input()`;
2. Приложение приостанавливается и ждет, пока пользователь введет текст;
3. Функция `input()` возвращает значение - пользовательский текст в виде строки;
4. Создается переменная `my_input`;
5. Выполняется оператор присвоения;
6. Переменная `my_input` теперь имеет тип строка.

Таким образом, мы создали переменную `my_input`, которая хранит результат пользовательского ввода и мы можем дальше с ним работать в нашей программе.

Разберем вызов функции `print()`

```python
print ("Вы ввели " + my_input)
```

Вычисляется выражение "Вы ввели" + `my_input`. Мы уже знаем, что это операция конкатенации строк. Вычисленное выражение передается функции `print()`, которая выводит в консоль склеенную строку.
