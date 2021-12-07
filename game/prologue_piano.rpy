label prologue_piano:

    Hero "{cps=20}Хочу услышать твою игру на синтезаторе."

    Alice "{cps=20}Хорошо, дай мне минутку."
    "{cps=20}Она отошла к инструменту и начала что-то наигрывать."
    hide alice calm with Dissolve(.5)

    "{cps=20}Смотря на нее, я понимал, что она давно не играла на этом инструменте, потому что иногда, как мне слышалось, она не туда попадала."
    "{cps=20}Или мой слух все так же подводил меня, и я ничего не понимаю."

    Alice "{cps=20}Все, я готова, прости за ожидание, давно не игра."
    "{cps=20}Сказала она, и не сказав ни слова больше начала играть."

    show bg alice_piano with Dissolve(.5)
    play music alice_p fadein 1
    window hide
    pause

    '''
    {cps=20}В моей голове синтезатор, это же по факту пианино, для чего-то классического, для того, что не должно тебя грузить и вызывать только позитивные эмоции.
    {w}Но как только она начала – я понял, как я ошибался.

    {cps=20}Я ожидал позитивных эмоций, может что-то полу ритмичное, но – после первых пяти секунд мои уши начали доносить в мозг мелодию, от которой мне ставало грустно.

    {cps=20}Сильная странная боль – вот что пронзало мое тело.

    {cps=20}Это чувство тревоги, тревожности... Как через обычные клавиши можно такое передать?

    {cps=20}И главное то, что чувство это я где-то ощущал.

    {cps=20}Я его помню, как сегодня.
    {w}Может оно и было сегодня?
    {w}Может, оно и было сейчас?

    {cps=20}Сейчас?

    {cps=20}Мелодия?

    {cps=20}Что я черт слышу...
    {w}Чувствую...

    {cps=20}Уверен я только в одном – в этой мелодии заложена вся ее грусть, {w}боль, {w}может страдания?

    {cps=20}Может она, как и я?
    {w}А может ее мир просто сломал?
    {w}Не знаю...

    {cps=20}Ее пальцы – они скользят по клавишам, как коньки по льду.
    {w}Ни одной фальшивой ноты, ни одной запинки.

    {cps=20}Может то, что она «фальшивила» был только блеф, чтоб удивить меня?

    {cps=20}Зачем гадать, хочется только слушать и слушать, слушать и слушать, и прочувствовать эту боль вместе с ней.

    {cps=20}Взглянув ей в лицо, я увидел – она даже не сморит на клавиши...

    {cps=20}Как...

    {cps=20}Она гений?

    {cps=20}Перерождение великих композиторов?

    {cps=20}Эх, не хочу, не хочу забивать себя лишним, пока играет музыка...
    '''

    stop music fadeout 1
    scene bg musician_class with Dissolve(.5)
    "{cps=20}Она закончила. Без слов она просто поставила синтезатор и подошла ко мне."
    show alice calm with Dissolve(.5)

    Hero "{cps=20}Это"
    Alice "{cps=20}Я знаю, увидела."
    "{cps=20}Перебив меня, с первой увиденной мною улыбкой на ее лице, она вышла из класса."

    jump prologue_way
return