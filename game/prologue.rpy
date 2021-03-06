# - пролог -
label prologue:

    jump prologue_chaos

return

# - самое начало -
label prologue_chaos:
    scene bg eyes_closed
    play music another_wind fadein 1

    '''
    {p}
    {cps=20}Тихо...
    {w}и холодно...

    {cps=20}Настолько холодно, что будто мои внутренности переплетаются с этим...

    {cps=20}Холод?
    {w}Уверен ли я, что "это" холод...
    {w}И как "тут" может быть холод...

    {cps=20}И где это "тут"?
    {w}Да и что все же "тут" может то быть?

    {cps=20}А если все не может...

    {cps=20}Что бы там ни было - был я точно не в этом месте.

    {cps=20}Впраду, где я?

    {cps=20}Да и имеет ли это сейчас значение...

    {cps=20}Главное...
    {p}Почему же холод...
    {w}и только внутри...

    {cps=20}Но, может это не холод..?
    {w}А что же это тогда?

    {cps=20}Во всем этом точно нет смысла...

    {cps=20}Может боль?
    {w}Но что значит "боль"?
    {p}Чтобы это ни было - оно только внутри меня...

    {cps=20}Странная тогда эта боль...
    {p}Болит так, словно потерял что-то дорогое...
    {w}или быть может я узнал грустную правду?

    {cps=20}Правду?

    {cps=20}Надо открыть глаза и все пройдет.
    {p}
    '''
    scene bg eyes_opened
    with wipeup
    pause(.5)
    '''
    {cps=20}Слишком темно...
    {p}Тяжело...
    {p}Все так же холодно...

    {cps=20}Идти.
    {w}Нужно срочно встать и идти, но...
    {w}мое тело...

    {cps=20}Не чувствую...
    {w}Не чувствую ни одну конечность...
    {w}Но, как я иду..?
    {w}И можно ли "это" назвать "иду"..?
    {p}Слишком много я задаю себе вопросов сегодня, обещал же так не делать...
    {w}Иду и это сейчас главное.

    {cps=20}Тут только свет, к нему и стоит стремиться, ведь так?
    {w}Все же стоять ли в этом месте точно не имеет значения,
    {w}оно само меня тянет.

    {cps=20}Тянет?

    {cps=20}Я что-то вижу...
    {w}Или мне кажется...
    '''
    scene bg house
    pause(.5)
    '''
    {cps=20}Нет, я определенно слабо, но вижу.
    {p}Поместье?
    {w}Заброшка?
    {w}Может храм?

    {cps=20}Не знаю...

    {cps=20}Это место, оно само тянет меня к этому зданию.
    {w}Может поэтому я себя не чувствую?
    {w}Я определенно иду, но чем...

    {cps=20}Может хватит? Это место не дает мне подчинить тело, значит надо слушаться и не думать.
    {w}Но кого..?

    {cps=20}Запах...
    {w}Дивный, сильно вызывающий отвращение запах, который даже повсеместный холод не может перебить.
    {w}Холод, который даже изъедает меня, не способен перебить этот шлейф гнили и сырости.

    {cps=20}Смешно.
    {w}И я бы не против выдавить такую же гнилую улыбку, но кроме мыслей я ни на что не способен...

    {cps=20}А был ли когда-то вообще?
    '''
    window hide
    scene bg door with Dissolve(.5)

    pause
    window show
    pause(.5)
    '''
    {cps=20}Приближаясь к зданию размытость не спадала, но все же отчетливо виднелась старая дверь.

    {cps=20}Эта дверь похоже еще с тех старых времен, о которых не принято говорить.
    {w}Почему? Почему мне так кажется?
    {w}Никогда я такого не видел вживую...

    {cps=20}Эх, может мне и вправду все это кажется.
    {w}Довольно странно, что я еще имею хоть какое-то удивление.

    {cps=20}Удивление?

    {cps=20}Чем ближе я, сюда приближаюсь, тем больше сила в мое тело возвращается...
    {w}И я иду. Несомненно именно то, что я иду!
    {w}Но похоже это здание само выбрало мне путь сюда.

    {cps=20}Я тут. У этой невиданой ранее мне двери. Важно ли это сейчас?

    {cps=20}Каким бы полумраком все это не было - понятно, что над дверью есть некое светило,
    что освещает вход.

    {cps=20}Свет.
    {w}Очень странный и до абсурдности холодный свет. Сложно, но мнимо видно
    как кружась, падают у подножья входа снежинки.
    {w}Что скрывает этот вход помимо давно покрытого слоя снега...

    {cps=20}Как бы я видно не хотел, или хотел, но я тут...

    {cps=20}Тут?

    {cps=20}Эта дверь...
    {w}Уверен ли я, что надо заходить?
    {w}Да и уверен ли, что не стоит?
    {w}Не думаю, если еще способен, о том, что надо быть уверенным.

    {cps=20}Захожу...
    '''
    scene bg window_open with Dissolve(.5)
    pause(.5)

    play sound old_door fadein 1 fadeout 1

    '''
    {p}
    {cps=20}Здание... Наполненое мрачной пустотой здание.
    {w}Стени, жестокие своим величием стены...
    {w}и коридор..?

    {cps=20}Мрак.
    {w}Ужасная темнота заполняет это место. И еще больший холод наполняет меня из нутри.

    {cps=20}Почему?

    {cps=20}Единственное, что пропускает свет в лихое место это окно.
    {w}Дряхлое, чуть ли не полностью прогнившее окно, которое еще и открыто...

    {cps=20}Лучше... я чувстую свое тело лучше, да и частично вижу...

    {cps=20}Стоит ли пытатся закрыть его? Не станет ли хуже?
    '''

    menu:
        "{cps=20}Да и хватит ли мне сил..?"

        "Попытатся закрыть окно":

            "{cps=20}Стоит попробовать, я смогу, я не настолько немощен."
            $ IsWindowClosed = True

            scene bg window_closed with Dissolve(.5)
            pause(.5)

            play sound c_window fadeout 1
            stop music fadeout 1

        "Не закрывать":
            "{cps=20}Нет, я все так же слаб и не котролирую себя, да и если что пойдет не так..."
            "{p}"

label prologue_chaos_p2:

    "{cps=20}Стою. А что еще остается делать в холодном месте..."
    play sound c_step
    ""
    '''
    {cps=20}Стоп...
    {w}Я слышу звуки...
    {w}Очень странные звуки, особенно если учесть отсутствие чего-то кроме ветра...

    {cps=20}Плохо вижу, но может взглянуть в эту темную чуждую даль..?
    '''

    play sound c_step
    ""
    "{cps=20}Огромный черный силуэт стал вырисовываться в конце того коридора."
    play sound c_step
    ""
    "{cps=20}Оно идет... ко мне?"
    play sound palpitation
    ""

    '''
    {cps=20}Сердце бьется так сильно, словно я вот-вот умру.
    {w}Снова... снова мать его чувство, что я не могу пошевелиться...
    {w}А эти звуки, они всюду...

    {cps=20}Может это смерть..?
    '''

    play sound c_step
    ""
    '''
    {cps=20}Он все ближе и ближе.
    {w}Полы его одежды собирают мусор и пыль... а его лицо...
    {w}Почему я не могу видеть его лицо?
    '''

    play sound c_step
    ""
    '''
    {cps=20}Это какая-то маска?
    {w}Он совсем близко.
    {w}Запах воска и старой бумаги ударили в нос.

    {cps=20}Что за...
    '''
    show chaos calm with Dissolve(.5)
    '''
    {cps=20}Не осознавая всего происходящего я просто вскликнул это,
    даже не понимая, что способен открыть рот.

    {cps=20}Существо протянуло руку к моему лицу.
    {w}Почему я не могу пошевелиться?
    {w}Мое тело словно замерзло...
    '''

    Hero "{cps=20}Что ты такое..?"

    '''
    {cps=20}Снова не осознавая возможности говорить прохрепел я тихо.

    {cps=20}Он слегка сжал мое щеку своими костлявыми лапами и вздохнул.
    '''

    Hero "{cps=20}Ты... {w}Бог?"

    Chaos "{cps=20}Я?"

    "{cps=20}Существо со странным смехом ответило"

    Chaos "{cps=20}Милое дитя, Я нечто выше вашего Бога."

    '''
    {cps=20}Он продолжал хохотать, пока я не мог взять себя в руки.
    Мое тело онемело. Кто передо мной? Что это за тварь.
    '''

    Chaos "{cps=20}Мы с тобой еще увидимся. Реальность более безобразна, чем ты привык ее видеть..."
    play sound c_step
    ""
    hide chaos calm with Dissolve(.5)
    '''
    {cps=20}Он стал уходить в сторону того коридора, из которого пришел.

    {cps=20}Я не могу осознать, что это...
    {w}Голова, она кружится? Спать... Так резко хочется спать...
    '''

    hide window_close
    with fade
    hide window_opened
    with fade

    play sound school_bell fadein 1
    ""
    stop music fadeout 1
    if IsWindowClosed:
        scene bg classroom_wincl with Dissolve(.5)
        window hide
        pause
    else:
        scene bg classroom_winop with Dissolve(.5)
        window hide
        pause

    window show
    ""


    jump prologue_school
return
