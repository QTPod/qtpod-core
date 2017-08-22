
import requests


# Punctuator API endpoint
PUNCTUATE_API = "http://bark.phon.ioc.ee/punctuator"

# threshold between timestamps to add a break
TSTAMP_THRESH = 0.35


def _punctuate_tstamp(tscript, tstamps):

    text = ""

    for n in range(len(tscript) - 1):
        diff = tstamps[n+1] - tstamps[n]
        text += tscript[n]
        text += ".\n" if diff > 0.35 else " "

    return text


def _punctuate_api(tscript):

    text = " ".join(tscript)

    # call the API endpoint
    resp = requests.post(PUNCTUATE_API, data={"text": text})
    resp.raise_for_status()
    resp.close()

    return resp.text


def punctuate(tscript, tstamps, method="api"):

    if method == "api":
        return _punctuate_api(tscript)
    elif method == "tstamp":
        return _punctuate_tstamp(tscript, tstamps)
    else:
        raise ValueError("unknown punctuate method")


if __name__ == "__main__":

    # test text
    test_text = """
        support for climate money and the following message come from powered
        cloud based software that makes it easy for businesses to track share
        signed policies and procedures and short employees no what it takes to
        your business safe and successful learn more and power the m. s. dot
        quick warning today's show contains profanity and offensive racial
        something strange has happened to the passage of time and i don't know
        you've noticed this but it's just this happens to me every week it
        like friday and you're like oh it is tuesday afternoon here's how this
        time more is affecting all of us here at planet money now every year
        may know this right at the end of the year we do a special pod cast
        tradition and then there's probably kept we look back at the long
        behind us and we update all the stories will tell you what happens to
        after we turned the microphones off we call it the rest of the story
        after the immortal words uh broadcaster paul harvey debate together you
        i are going to learn [noise] the rest of the story but things in this
        are now changing so quickly this year this year we're going to do the
        where we're doing a year's worth of updates now in july we're doing
        involved with the money i'm robert smith today on the show we will tell
        about a supreme court case unleashed cultural team and we're going to
        back in on the robot was supposed to make us rich by now and it's
        new tactic in a war that we covered extensively eagles versus <unk> mm
        mm mm support for planet money and the following message come from the
        platinum card from american express take your business forward with the
        and know out of the business platinum card backed by the service end
        of american express news world is crazy now in fact we're gonna have to
        the show super quick to update so quickly before we have to update the
        for the rest of the story has its own rest of the story with me in
        is also chang hey robert good to have your here also did an amazing pod
        back in may [noise] about a rock band a rock band with and offensive
        the name was the slams offensive maybe to some people <unk> this land
        asian american rock band and they were in a battle with the federal
        over registering their name as each mark because the federal government
        not want to put it sort of official feel it's official like our with a
        on a registered trademark seal on a name which they felt was
        to asian americans that's right now simon tend the founder of the rock
        he thought that's not fair that's that's a violation of my first
        rights so he took his case all the way to the supreme court and that is
        we ended the pot cast but in the last few months a lot it's happened
        up right so the court agreed with simon tan and this land they said yes
        is a violation of the first amendment the u._s. government cannot be in
        business deciding what trademarks our disparaging which ones are not
        banning only the ones that are disparaging so i'm into a store near you
        tee shirts hats all money goes to the band exactly but people have been
        with sort of a larger question because of the supreme court decision
        that is have the floodgates opened does this mean that a bunch of
        offensive massaging his homophobic hateful phrases earn now going to be
        is trademarks you're about to hear some of these words just another
        too i called up i tried my lawyer <unk> lake and he's been tracking all
        trademark applications coming through the door since the supreme court
        and hear some of the names of people want to trade mart gutter slopes
        damn begins mega mega mega mega and make a demus wow wait how many
        did you just they're they're ah at least five here and there probably
        since then so at least five trademark applications for an i. g. g. a.
        <unk> since the supreme court decision yes uh a couple of on the day of
        supreme court decision it was actually three and i was curious you know
        where these people behind these applications to register and i. g. g.
        on the same day that the supreme court decision came down because
        they were they must be pretty determine people people who want to own
        word for commercial purposes and of course the fear is that this would
        someone who has racist intentions of l._a. potentially so i try this
        guy in mississippi who was behind two of she applications to register
        i._g._a. on the same day as the supreme court decision and his name is
        sporting events and i asked him why he want to register this word so
        i thought that i had a duty you know what i'm saying in a
        to to protect that word to secure that word you know what i'm saying
        to make sure that he's used in a way that i think would not disparities
        get you're wondering curtis is african american and he is now in this
        against the races because if he can trademark the word than he can keep
        people from making products with a bad people from making products okay
        what curtis wants to do is basically brand tee shirts with and i. g. g.
        and m. believes in on the front of the t. shirt will be seems like
        or brother had so people will associate those good positive ideas with
        brand <unk> i mean he no he says this is a way of reclaiming the word
        is exactly what simon tam said about the name of the ban the slips and
        was especially grateful that he pounds so quickly that he moved in
        on the same day is the supreme court opinion because when he noticed
        another guy wanted to register and i. g. g. a. as a trademark and gave
        really funny feeling about the whole thing a bad feeling was that
        guy also wanted to register the swap <unk> as a trademark so curtis
        there thinking this can't be good one guy wants to register and i. g.
        a. and just wants to go so i called him up [noise] his name is steve
        why slapstick is because uh the term has an incendiary meaning behind
        yeah and it's and it's currently used as a symbol of hate and if we can
        around we won't be able to control the sale of the brand in the use of
        brand as well oh so you're you're trying to basically grab the <unk> so
        actual racist and heaters can't grab the slapstick i as a harasser
        correct so this guy see meaner is actually trying to do the exact same
        that curtis border neat is trying to do some very good people buying
        bad words exactly but there is a catch in order to register the swat
        as a trademark you have to sell a swap stick a product so meaner has
        out a solution to this problem he is going to sell blankets do they
        socks apparel with the <unk> all over it but he's going to totally
        them i i have reservations about this [laughter] first of all do they
        just wants to cause should not exist in the world but also it's just
        a loaded emotional offensive symbol that even if you're doing it for
        even if you're putting on something even if no one buys it the very
        of its existence seems wrong and you just put your finger on a
        problem with steve mannered strategy so under trademark law the
        will only approve your trademark application if consumers connect your
        with the product that you are selling uh but the slapstick <unk> it's
        well known there's so much terrible history behind it the nazis adolf
        the holocaust then it's unlikely anyone would connect that simple to
        random blinking so maybe we'll probably never get to <unk> but then
        neither well anyone else nothing changed so much you <unk> [noise]
        to be honest with you all [noise] we are plenty of money we're not
        to be here this week doing the show 'cause we plan to money we're
        to be rich i don't know if you remember the episode we did back in
        but planet money developed a a stock trading <unk> uh a little program
        that reads twitter and trade stocks based on sweets from the president
        the united states donald trump <unk> mark let our development team what
        what happened yes we called it boating spot of the united states being
        after president of the united states it watches donald trump's twitter
        and if the president mentions accompany by name buddhist will buy or
        stock of that company depending on if the <unk> is positive or negative
        allergy pass the hat we all put money into it so that we have a
        dollars in an online stock brokerage account that is all connected up
        buddhist and it's ready to invest and make money doubling doubling
        again but what happened <unk> has not made a trade yet it has not sold
        bought a single share of stock [noise] now what are we developed as it
        like such a great idea because donald trump was reading about these
        you toss often and insult or an add a boy and we're more attacks or
        the texas and the market would immediately move up or down and that
        we would be um on the right side of that trade but i mean at least i've
        dumped trump is not reading about companies <unk> he is still treating
        companies but he's doing it very early in the morning and yes he is at
        a._m. demon that seems to hit it right his films go as the sun is
        and you know what is not going on at that time stock trading stock
        the shock market does not open until nine thirty a._m. i ran the
        and i checked and only about fifteen percent of president <unk>
        while the stock market is open at least since bonus has been watching
        probably good for the stock market but bad for our trading at least
        fun so i want more action and so do all of the people following bonus
        it or they haven't been sending us a ton of different ideas for
        up the computer code and making prayed more so i called up money
        of the head of investments at trade works he is one of the people who
        us build <unk> and i went over some of the ideas with him i wouldn't
        want to do this um well i want to get a chance to trade that is fair i
        but at the trade it too um but the reason we have noticed and we don't
        a person doing this is because um one of the big advantage is is that
        know <unk> can be patient um disciplined this whole experiment was
        to teach us about outdoor ethnic trading so letting my dumb human
        <unk> getting the way just completely defeats the purpose so literally
        spot is keeping people like us from like getting emotional and just
        like i want to make money on what <unk> what that is one of the
        of having a <unk> but i still had to ideas for how to do it and i
        to do it so one we can trade in what it's called after hours training
        you hear about this all the time right there is the u._s. stock markets
        basically open from nine thirty to for but you know if there's somebody
        another place in the world they decide they really need some cash in
        middle of the night uh there are places where you can trade stocks
        hours money said letting buddhist trade and the after hours markets it
        work technically like he could make the buck do that but it would
        backfire because there are so few people trading after hours that it
        costs more to trade and it's it's just a really risky place for a
        <unk> so like on a scale of one to ten how good of an idea is is it's
        bad [laughter] okay this is my money so i agree with him what else he
        [noise] my next idea was um what if voters reads donald trumps early
        to eat and then it waits until the market opens and then <unk>
        right then well it's not a good idea let's call it a bad idea um
        a bad idea but uh with uh less potential to be a disaster because the
        logic of buddhist was that when trumped weeds he moved to stock price
        away so we would buy right away and then get out thirty minutes later
        that we minimize that risk but if we wait hours after the to eat then
        kinds of other things could move their stock price in between <unk> and
        the stock market open so we lose our advantage because something
        in the world to move stocks and our bought didn't detect that 'cause it
        detects donald trump is right there could have been a big thing the
        before that's ready to burst onto the scene when the market opens it is
        a bad idea to change your trading strategy in the middle of your
        but you know what we should do it anyway going to do it i wouldn't do
        anyway yeah ah <unk> is going to change [noise] starting right now if
        trumped <unk> about a company before the market opens buddhist will see
        make a decision to buy or sell the stock and then jump into action
        when the market opens and get out thirty minutes later i don't know if
        should have told all together stock traders are our strategy at this
        and oldest will be looking to make a deal at nine thirty in the morning
        we're we're suckers on this one vet your alley robert oh well my thing
        you want to follow the trades you can follow boating onto it or <unk>
        <unk> and stay with us because coming up after the break we have an
        on the terminal struggle between our national bird and our national
        bird the eagles versus chickens a new technology has shifted the
        stay with us yoyo everybody stretch armstrong my name is buffy the
        k. cool bob loves if you love this <unk> listening to you should check
        a new show what's good with stretch and bobby so this is not your
        if you show we're going to be telling stories that you're not going to
        anywhere else <unk> poor however you find your pockets fits what's good
        smith i'm here for the summer rest of the story jacob gold speaking of
        of the many many many many find stories you've told what is the most
        thing you have to tell us right now i got an update on eagles versus
        i'm in so okay as you recall early this year i went down to georgia
        i met wheel harris he's up a farmer who raises you know free range all
        chickens he took me out into one of his fields and he showed me his one
        problem bald eagles keep killing his chickens so this so this what
        looking at here is basically the back half of a chicken right there's
        and legs but at the top half of the central heat legal oh here's <unk>
        the body cavity 'cause you seen that that happening what you're saying
        <unk> body cavity now the problem as a remember from the pie test was
        can't kill the eagles this is a national civil yes he did have this
        you got the special permit that lets them harassed them and he showed
        all these things he tried he tried nets and noise canons any special
        that shoots firecrackers in the air none of it worked and that's how we
        up <unk> that's how we ended up <unk> he was he was losing two beagles
        our listeners god love them felt like this was an opportunity for them
        solve so many people wrote to us and i found out row two will dozens of
        with all these suggestions you know one person was like i was hiking in
        and the chickens have had little red keeps tight around their necks and
        else was like i work in this book chemical garden and we had bagpipe
        at a wedding and that made the eagles this incredible array of of
        actually called up one of the people who heard the story and wanted to
        uh he's a mechanic from southern california named brian holly and when
        heard the story he immediately thought of this this really astonishing
        that happened to him twenty years ago he was working at a landfill and
        lentil was just infested with sea gulls and if you know seagulls you
        like this is a problem if you're working on the equipment <unk> get
        [laughter] covered with tropics covered with dropping machine anything
        until you see in a single shit [noise] so gratuitous and and the people
        the landfill like wheel back in georgia had tried all these different
        to try and get rid of the birds in fact they tried those same guns that
        fireworks and none of it worked until somebody and they should [noise]
        okay just string fishing between the two we want so okay so so one line
        so sure so they actually try it and all it's doing what they did they
        up to twenty foot poles right up into the sky one on each side of the
        where they were working at the landfill and then they strong a single
        piece of fishing line you know modeled filament line between the polls
        twenty feet in the sky and then the seagulls stopped flying over the
        area where they had strung up the line and then the seagulls they just
        round in a circle outside where holly and the other guys were working
        was really weird because you know standing around looking at you and
        just think okay offered hitchcock amazing yeah and a month later the
        just left do we know why this word no it's so it's something something
        a mystery we actually even called the few scientists it's not clear
        somehow the line confuses the birds like maybe they see the light <unk>
        it but but in some way they feel like they cannot land in the area
        the line nobody really knows it just works at least it worked in
        with the sea gulls and then went highly hurt our show he thought well
        it'll work in georgia with the eagles and he really really wanted to
        this message to two will to the chicken farmer you reached out to us he
        one of his sons go on line and figure out the phone number for will be
        the farms you got voicemail accurate for going on in in georgia finally
        gets on the phone with somebody at the farm tells them about the
        wire and we'll harris who runs the farm things what do i got to lose
        right everything i may as well try the fishing wire so few days ago i
        down to georgia to see how it's going this is the first one and we've
        that we feel good and it appears to this one what possible i know i i
        now to be clear will says he's not ready to declare victory yet those
        his words uh there's a few like big cats one is so they've stronger
        up over two of their sort of groups of chickens and he goes just went
        the other chickens on the farm the other big thing will as worried
        is this is the low season for eagles they're only a few eagles that
        for the summer the big influx comes in the winter when eagle migration
        they're real test is going to be in a few months when they got all the
        and place i went all the migrate towards eagles come in so i told well
        great i will check back with you in a few months we never solved
        that plane might have to know what's the poor <unk> just blows my mind
        i'm super shocked and i think so either will in fact he asked me to
        a message to do i listen to brian how you don't just give him or die
        express martin buying rather be at least i will do that i would be
        happy to do that okay thanks a lot we'll keep in touch but holly hadn't
        from the guys on the farm for a while he didn't know how grateful will
        he didn't know that the experiment so far anyway is a success so i told
        god shoo [laughter] [laughter] [noise] [laughter] me too like this this
        a beautiful story like chicken necks [noise] can you would like to hear
        original shows we talked about today and you really should uh the show
        simon ham and the slant is called unspeakable trademark this episode
        seven four modus episode is episodes seven three and he goes versus
        episodes seven too and we love to hear from you or their mother stories
        you want to hear <unk> you could say this email split up money and
        that more before they show was produced by the editor and brian first
        one less thing went up money will be live on stage this september to
        york city now here this pod cast festival go to now here this best dot
        to learn more and get your ticket and her offer <unk> money and check
        to see [noise] i'm jackie and i'm robert how are you know the rest of
        story [noise] summer so far [noise]
    """

    punctuate(test_text, None)
