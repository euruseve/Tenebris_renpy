label prologue_ukulele:

    Hero "{cps=20}Давай-ка вот эту «укукактотам», только что это?"

    Alice "{cps=20}Укулеле. {w}Это «гавайская гитара», но про первое слово не спрашивай, это просто острова где-то по ту сторону океана."

    hide alice calm with Dissolve(.5)

    '''
    {cps=20}Она сняла со своей спины портфель и достала такую маленькую гитарку, у которой только 4 струны.

    {cps=20}Яркий красный цвет этого инструмента контрастировал с ее темным пальто, но отлично сочеталась с ее портфелем.

    {cps=20}Не думаю, что этот инструмент может выдать что-то стоящее.

    {cps=20}Она села на стул и начала играть.
    '''

    show bg alice_ukulele with Dissolve(.5)
    play music alice_u fadein 1
    window hide
    pause

    '''
    {cps=20}То ли этот инструмент такой звучный, то ли у нее божественный дар к игре на нем.

    {cps=20}Казалось простая мелодия, но очень расслабляющая. {w}Слушая, словно попадаешь в место, где все хорошо, тихо, ты не должен ничего делать.
    '''

    show bg eyes_closed with Dissolve(.5)
    '''
    {cps=20}Закрыв глаза, я почувствовал, словно стою на лужайке посреди лета у речки и сейчас, вместе с утренней росой, подымусь прямо к солнцу...

    {cps=20}Ох это чувство теплого моря, о котором я только читал и никогда думал не прочувствую – кажется это именно оно.
    '''

    show bg alice_ukulele with Dissolve(.5)
    "{cps=20}Открыв глаза, я увидел Алису, расслабленную девченку, которая будто на одной волне со мной прожила все мои чувства."

    stop music fadeout 1
    scene bg musician_class with Dissolve(.5)

    show alice s_smile with Dissolve(.5)

    Hero "{cps=20}Это было так круто... {w}Ты словно вернула меня в детское лето, когда все было так хорошо..."
    "{cps=20}Я на одном дыхании промолвил это, смотря на нее глазами как у младенца, которому купили новую игрушку."

    Alice "{cps=20}Спасибо, я рада что тебе понравилось."
    "{cps=20}Она впервые улыбнулась, и это была слишком искренняя улыбка, которая затмила прошлое ее состояние."
    Hero "{cps=20}Это тебе спасибо, впервые рад что задержался в школе."

    jump prologue_way
return
